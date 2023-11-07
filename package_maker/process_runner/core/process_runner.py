import importlib
import os

try:
    from importlib import reload
except:
    pass
import sys

import package_maker.process_runner

class ProcessRunner(object):
    def __init__(self, project=None, app=None, processor=None, process=None, kwargs=None, ignore_processes=None):
        super(ProcessRunner, self).__init__()
        if kwargs is None:
            kwargs = dict()
        if ignore_processes is None:
            ignore_processes = list()
        self.project = project.lower()
        if app:
            self.app = app.lower()
        else:
            self.app = None
        self.process = process
        self.processor = processor
        self.kwargs = kwargs
        self.ignore_processes = ignore_processes

    def getModule(self):
        configFile = '{}_config'.format(self.project)
        importedModule = importlib.import_module('package_maker.process_runner.processor.{}.config.{}'.format(
            self.processor, configFile))
        reload(importedModule)
        return importedModule

    def getProcessList(self):
        moduleName = self.getModule()
        os.environ['PROJECT'] = self.project
        os.environ['PROCESS'] = self.process
        try:
            processes = moduleName.__getattribute__(self.process)
        except:
            raise RuntimeError("""
----------------------------------------------------------------------------------
{} processor not implimented for {} project's  {} dept
----------------------------------------------------------------------------------           
""".format(self.processor, self.project, self.process)
                               )
        if isinstance(processes, list):
            return processes
        elif isinstance(processes, dict) and self.app:
            return processes[self.app]
        else:
            raise RuntimeError("""
----------------------------------------------------------------------------------
Can't find process list for {} project's {} dept and {} app 
----------------------------------------------------------------------------------           
""".format(self.processor, self.project, self.process, self.app)
                               )

    def runProcesses(self):
        process_list = self.getProcessList()
        for each_process in process_list:
            process_name = importlib.import_module('package_maker.process_runner.processor.{}.processes.{}'.format(
                self.processor, each_process)
            )
            if each_process in self.ignore_processes:
                continue
            ret_status, ret_data = process_name.run(**self.kwargs)
            self.kwargs.update({each_process: ret_data})
            # print('ret_status:', ret_status)
            # print('process_name:', process_name.__getattribute__('__name'))
            if ret_status:
                raise RuntimeError("""
----------------------------------------------------------------------------------
'Error in process {} : \n{} \n'
----------------------------------------------------------------------------------           
""".format(process_name.__getattribute__('__name'), ret_data)
                                   )


if __name__ == "__main__":
    '''
    data = eval(sys.argv[1])
    project_name = sys.argv[2].upper()
    processor = sys.argv[3]
    process = sys.argv[4]  
    ignore_processes = sys.argv[5]  
    '''
    arg_names = ['temp', 'data', 'project_name', 'processor', 'process', 'app', 'ignore_processes']
    args = dict(zip(arg_names, sys.argv))
    # print(args)

    p = ProcessRunner(
        args.get('project_name'),
        app=args.get('app'),
        processor=args.get('processor'),
        process=args.get('process'),
        kwargs=eval(args.get('data')),
        ignore_processes=args.get('ignore_processes')
    )
    p.runProcesses()
