class FilterSortDecorator:
    def init(self, db_rep, filter_func=None, sort_func=None):
        self.db_rep = db_rep
        self.filter_func = filter_func
        self.sort_func = sort_func

    def get_k_n_short_list(self, k, n):
        result = self.db_rep.get_k_n_short_list(k, n)
        if self.filter_func:
            result = filter(self.filter_func, result)
        if self.sort_func:
            result = sorted(result, key=self.sort_func)
        return list(result)

    def get_count(self):
        result = self.db_rep.get_count()
        if self.filter_func:
            result = filter(self.filter_func, result)
        return len(list(result))