from queue import Queue
from threading import Thread
from readers.MAXCSVReader import MAXCSVReader
from Results import ResultCouple, FileCmpResult
from datetime import datetime

__author__ = 'saflores'


class AsyncFileComparator(Thread):
    def __init__(self, file_test, file_ref, q: Queue):
        super().__init__()
        self.file_test = file_test
        self.file_ref = file_ref
        self.queue = q
        self.result_couple_l = []

        #TODO: decide what type of file this is
        ###############################################################
        # for now we only have one kind of reader so create two of them
        self.record_test = MAXCSVReader(file_test)
        self.record_ref = MAXCSVReader(file_ref)

        ###############################################################
        # check that the records are actually equivalent:
        if len(self.record_test.variables) != len(self.record_ref.variables):
            raise NotImplementedError('Files must have the same number of variables')

        if len(self.record_test.times) != len(self.record_ref.times):
            raise NotImplementedError('files do not have the same number of samples')

    def run(self):
        self.queue.put(self.__compare())

    def __compare(self):
        all_variables_pass = True

        ###############################################################
        # some output to the user
        print('Comparing ' + str(len(self.record_test.variables)) + ' variables')

        ###############################################################
        # iterate over the test's variables and compare it with it's
        # reference counterpart
        for v_test in self.record_test.variables:

            v_ref = self.record_ref.get_variable(v_test.fullname)
            vars_match, error = v_test.compare_to(v_ref)

            r = ResultCouple(v_test, v_ref, vars_match, error)
            self.result_couple_l.append(r)
            print(r)

            all_variables_pass = (r.status == 'matched' or r.status == 'passed') and all_variables_pass

        ###############################################################
        # Pack everything in an object and return

        file_cmp_result = FileCmpResult(self.file_test,
                                        self.file_ref,
                                        all_variables_pass,
                                        self.result_couple_l,
                                        datetime.now())

        return file_cmp_result
