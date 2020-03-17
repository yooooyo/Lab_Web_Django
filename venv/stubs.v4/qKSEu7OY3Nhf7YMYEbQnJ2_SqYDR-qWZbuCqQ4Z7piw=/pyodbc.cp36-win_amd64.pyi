import builtins as _mod_builtins
import datetime as _mod_datetime

class NullParam(_mod_builtins.object):
    __class__ = NullParam
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

BINARY = _mod_builtins.bytearray
Binary = _mod_builtins.bytearray
BinaryNull = NullParam()
class Connection(_mod_builtins.object):
    'Connection objects manage connections to the database.\n\nEach manages a single ODBC HDBC.'
    __class__ = Connection
    def __enter__(self):
        '__enter__() -> self.'
        return self
    
    def __exit__(self, *excinfo):
        '__exit__(*excinfo) -> None.  Commits the connection if necessary.'
        pass
    
    def __init__(self, *args, **kwargs):
        'Connection objects manage connections to the database.\n\nEach manages a single ODBC HDBC.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def add_output_converter(self, sqltype, func):
        'add_output_converter(sqltype, func) --> None\n\nRegister an output converter function that will be called whenever a value with\nthe given SQL type is read from the database.\n\nsqltype\n  The integer SQL type value to convert, which can be one of the defined\n  standard constants (e.g. pyodbc.SQL_VARCHAR) or a database-specific value\n  (e.g. -151 for the SQL Server 2008 geometry data type).\n\nfunc\n  The converter function which will be called with a single parameter, the\n  value, and should return the converted value.  If the value is NULL, the\n  parameter will be None.  Otherwise it will be a bytes object.\n\nIf func is None, any existing converter is removed.'
        pass
    
    @property
    def autocommit(self):
        'Returns True if the connection is in autocommit mode; False otherwise.'
        pass
    
    def clear_output_converters(self):
        'clear_output_converters() --> None\n\nRemove all output converter functions.'
        pass
    
    def close(self):
        'Close the connection now (rather than whenever __del__ is called).\n\nThe connection will be unusable from this point forward and a ProgrammingError\nwill be raised if any operation is attempted with the connection.  The same\napplies to all cursor objects trying to use the connection.\n\nNote that closing a connection without committing the changes first will cause\nan implicit rollback to be performed.'
        pass
    
    def commit(self):
        'Commit any pending transaction to the database.'
        pass
    
    def cursor(self):
        'Return a new Cursor object using the connection.'
        pass
    
    def execute(self, sql, params=None):
        'execute(sql, [params]) --> Cursor\n\nCreate a new Cursor object, call its execute method, and return it.  See\nCursor.execute for more details.\n\nThis is a convenience method that is not part of the DB API.  Since a new\nCursor is allocated by each call, this should not be used if more than one SQL\nstatement needs to be executed.'
        pass
    
    def get_output_converter(self, sqltype):
        "get_output_converter(sqltype) --> <class 'function'>\n\nGet the output converter function that was registered with\nadd_output_converter.  It is safe to call if no converter is\nregistered for the type (returns None).\n\nsqltype\n  The integer SQL type value being converted, which can be one of the defined\n  standard constants (e.g. pyodbc.SQL_VARCHAR) or a database-specific value\n  (e.g. -151 for the SQL Server 2008 geometry data type).\n"
        pass
    
    def getinfo(self, type):
        'getinfo(type) --> str | int | bool\n\nCalls SQLGetInfo, passing `type`, and returns the result formatted as a Python object.'
        return ''
    
    @property
    def maxwrite(self):
        'The maximum bytes to write before using SQLPutData.'
        pass
    
    def remove_output_converter(self, sqltype):
        'remove_output_converter(sqltype) --> None\n\nRemove an output converter function that was registered with\nadd_output_converter.  It is safe to call if no converter is\nregistered for the type.\n\nsqltype\n  The integer SQL type value being converted, which can be one of the defined\n  standard constants (e.g. pyodbc.SQL_VARCHAR) or a database-specific value\n  (e.g. -151 for the SQL Server 2008 geometry data type).\n'
        pass
    
    def rollback(self):
        'Causes the the database to roll back to the start of any pending transaction.'
        pass
    
    @property
    def searchescape(self):
        'The ODBC search pattern escape character, as returned by\nSQLGetInfo(SQL_SEARCH_PATTERN_ESCAPE).  These are driver specific.'
        pass
    
    def set_attr(self, attr_id, value):
        'set_attr(attr_id, value) -> None\n\nCalls SQLSetConnectAttr with the given values.\n\nattr_id\n  The attribute id (integer) to set.  These are ODBC or driver constants.\n\nvalue\n  An integer value.\n\nAt this time, only integer values are supported and are always passed as SQLUINTEGER.'
        pass
    
    def setdecoding(self, sqltype, encoding=None, ctype=None):
        'setdecoding(sqltype, encoding=None, ctype=None) --> None\n\nConfigures how text of type `ctype` (SQL_CHAR or SQL_WCHAR) is decoded\nwhen read from the database.\n\nWhen reading, the database will assign one of the sqltypes to text columns.\npyodbc uses this lookup the decoding information set by this function.\nsqltype: pyodbc.SQL_CHAR or pyodbc.SQL_WCHAR\n\nencoding: A registered Python encoding such as "utf-8".\n\nctype: The C data type should be requested.  Set this to SQL_CHAR for\n  single-byte encodings like UTF-8 and to SQL_WCHAR for two-byte encodings\n  like UTF-16.'
        pass
    
    def setencoding(self):
        pass
    
    @property
    def timeout(self):
        'The timeout in seconds, zero means no timeout.'
        pass
    

class Cursor(_mod_builtins.object):
    'Cursor objects represent a database cursor, which is used to manage the context\nof a fetch operation.  Cursors created from the same connection are not\nisolated, i.e., any changes done to the database by a cursor are immediately\nvisible by the other cursors.  Cursors created from different connections are\nisolated.\n\nCursors implement the iterator protocol, so results can be iterated:\n\n  cursor.execute(sql)\n  for row in cursor:\n     print row[0]'
    __class__ = Cursor
    def __enter__(self):
        '__enter__() -> self.'
        return self
    
    def __exit__(self, *excinfo):
        '__exit__(*excinfo) -> None.  Commits the connection if necessary..'
        pass
    
    def __init__(self, *args, **kwargs):
        'Cursor objects represent a database cursor, which is used to manage the context\nof a fetch operation.  Cursors created from the same connection are not\nisolated, i.e., any changes done to the database by a cursor are immediately\nvisible by the other cursors.  Cursors created from different connections are\nisolated.\n\nCursors implement the iterator protocol, so results can be iterated:\n\n  cursor.execute(sql)\n  for row in cursor:\n     print row[0]'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return Cursor()
    
    def __next__(self):
        'Implement next(self).'
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def arraysize(self):
        'This read/write attribute specifies the number of rows to fetch at a time with\nfetchmany(). It defaults to 1 meaning to fetch a single row at a time.'
        pass
    
    def cancel(self):
        'Cursor.cancel() -> None\nCancels the processing of the current statement.\n\nCancels the processing of the current statement.\n\nThis calls SQLCancel and is designed to be called from another thread tostop processing of an ongoing query.'
        pass
    
    def close(self):
        'Close the cursor now (rather than whenever __del__ is called).  The cursor will\nbe unusable from this point forward; a ProgrammingError exception will be\nraised if any operation is attempted with the cursor.'
        pass
    
    def columns(self):
        'C.columns(table=None, catalog=None, schema=None, column=None)\n\nCreates a results set of column names in specified tables by executing the ODBC SQLColumns function.\nEach row fetched has the following columns:\n  0) table_cat\n  1) table_schem\n  2) table_name\n  3) column_name\n  4) data_type\n  5) type_name\n  6) column_size\n  7) buffer_length\n  8) decimal_digits\n  9) num_prec_radix\n 10) nullable\n 11) remarks\n 12) column_def\n 13) sql_data_type\n 14) sql_datetime_sub\n 15) char_octet_length\n 16) ordinal_position\n 17) is_nullable'
        pass
    
    def commit(self):
        'Commits any pending transaction to the database on the current connection,\nincluding those from other cursors.\n'
        pass
    
    @property
    def connection(self):
        'This read-only attribute return a reference to the Connection object on which\nthe cursor was created.\n\nThe attribute simplifies writing polymorph code in multi-connection\nenvironments.'
        pass
    
    @property
    def description(self):
        'This read-only attribute is a sequence of 7-item sequences.  Each of these\nsequences contains information describing one result column: (name, type_code,\ndisplay_size, internal_size, precision, scale, null_ok).  All values except\nname, type_code, and internal_size are None.  The type_code entry will be the\ntype object used to create values for that column (e.g. `str` or\n`datetime.datetime`).\n\nThis attribute will be None for operations that do not return rows or if the\ncursor has not had an operation invoked via the execute() method yet.\n\nThe type_code can be interpreted by comparing it to the Type Objects defined in\nthe DB API and defined the pyodbc module: Date, Time, Timestamp, Binary,\nSTRING, BINARY, NUMBER, and DATETIME.'
        pass
    
    def execute(self):
        'C.execute(sql, [params]) --> Cursor\n\nPrepare and execute a database query or command.\n\nParameters may be provided as a sequence (as specified by the DB API) or\nsimply passed in one after another (non-standard):\n\n  cursor.execute(sql, (param1, param2))\n\n    or\n\n  cursor.execute(sql, param1, param2)\n'
        pass
    
    def executemany(self, sql, seq_of_params):
        'executemany(sql, seq_of_params) --> Cursor | count | None\n\nPrepare a database query or command and then execute it against all parameter\nsequences  found in the sequence seq_of_params.\n\nOnly the result of the final execution is returned.  See `execute` for a\ndescription of parameter passing the return value.'
        pass
    
    @property
    def fast_executemany(self):
        'This read/write attribute specifies whether to use a faster executemany() which\nuses parameter arrays. Not all drivers may work with this implementation.'
        pass
    
    def fetchall(self):
        'fetchall() --> list of Rows\n\nFetch all remaining rows of a query result, returning them as a list of Rows.\nAn empty list is returned if there are no more rows.\n\nA ProgrammingError exception is raised if the previous call to execute() did\nnot produce any result set or no call was issued yet.'
        return list()
    
    def fetchmany(self, size=cursor.arraysize):
        "fetchmany(size=cursor.arraysize) --> list of Rows\n\nFetch the next set of rows of a query result, returning a list of Row\ninstances. An empty list is returned when no more rows are available.\n\nThe number of rows to fetch per call is specified by the parameter.  If it is\nnot given, the cursor's arraysize determines the number of rows to be\nfetched. The method should try to fetch as many rows as indicated by the size\nparameter. If this is not possible due to the specified number of rows not\nbeing available, fewer rows may be returned.\n\nA ProgrammingError exception is raised if the previous call to execute() did\nnot produce any result set or no call was issued yet."
        return list()
    
    def fetchone(self):
        'fetchone() --> Row | None\n\nFetch the next row of a query result set, returning a single Row instance, or\nNone when no more data is available.\n\nA ProgrammingError exception is raised if the previous call to execute() did\nnot produce any result set or no call was issued yet.'
        pass
    
    def fetchval(self):
        'fetchval() --> value | None\n\nReturns the first column of the next row in the result set or None\nif there are no more rows.'
        pass
    
    def foreignKeys(self):
        'C.foreignKeys(table=None, catalog=None, schema=None,\n            foreignTable=None, foreignCatalog=None, foreignSchema=None) --> self\n\nExecutes the SQLForeignKeys function and creates a results set of column names\nthat are foreign keys in the specified table (columns in the specified table\nthat refer to primary keys in other tables) or foreign keys in other tables\nthat refer to the primary key in the specified table.\n\nEach row fetched has the following columns:\n  0) pktable_cat\n  1) pktable_schem\n  2) pktable_name\n  3) pkcolumn_name\n  4) fktable_cat\n  5) fktable_schem\n  6) fktable_name\n  7) fkcolumn_name\n  8) key_seq\n  9) update_rule\n 10) delete_rule\n 11) fk_name\n 12) pk_name\n 13) deferrability'
        pass
    
    def getTypeInfo(self):
        'C.getTypeInfo(sqlType=None) --> self\n\nExecutes SQLGetTypeInfo a creates a result set with information about the\nspecified data type or all data types supported by the ODBC driver if not\nspecified.\n\nEach row fetched has the following columns:\n 0) type_name\n 1) data_type\n 2) column_size\n 3) literal_prefix\n 4) literal_suffix\n 5) create_params\n 6) nullable\n 7) case_sensitive\n 8) searchable\n 9) unsigned_attribute\n10) fixed_prec_scale\n11) auto_unique_value\n12) local_type_name\n13) minimum_scale\n14) maximum_scale\n15) sql_data_type\n16) sql_datetime_sub\n17) num_prec_radix\n18) interval_precision'
        pass
    
    def nextset(self):
        'nextset() --> True | None\n\nJumps to the next resultset if the last sql has multiple resultset.Returns True if there is a next resultset otherwise None.'
        pass
    
    @property
    def noscan(self):
        'NOSCAN statement attr'
        pass
    
    def primaryKeys(self):
        'C.primaryKeys(table, catalog=None, schema=None) --> self\n\nCreates a results set of column names that make up the primary key for a table\nby executing the SQLPrimaryKeys function.\nEach row fetched has the following columns:\n 0) table_cat\n 1) table_schem\n 2) table_name\n 3) column_name\n 4) key_seq\n 5) pk_name'
        pass
    
    def procedureColumns(self):
        'C.procedureColumns(procedure=None, catalog=None, schema=None) --> self\n\nExecutes SQLProcedureColumns and creates a result set of information\nabout stored procedure columns and results.\n  0) procedure_cat\n  1) procedure_schem\n  2) procedure_name\n  3) column_name\n  4) column_type\n  5) data_type\n  6) type_name\n  7) column_size\n  8) buffer_length\n  9) decimal_digits\n 10) num_prec_radix\n 11) nullable\n 12) remarks\n 13) column_def\n 14) sql_data_type\n 15) sql_datetime_sub\n 16) char_octet_length\n 17) ordinal_position\n 18) is_nullable'
        pass
    
    def procedures(self):
        'C.procedures(procedure=None, catalog=None, schema=None) --> self\n\nExecutes SQLProcedures and creates a result set of information about the\nprocedures in the data source.\nEach row fetched has the following columns:\n 0) procedure_cat\n 1) procedure_schem\n 2) procedure_name\n 3) num_input_params\n 4) num_output_params\n 5) num_result_sets\n 6) remarks\n 7) procedure_type'
        pass
    
    def rollback(self):
        'Rolls back any pending transaction to the database on the current connection,\nincluding those from other cursors.\n'
        pass
    
    def rowIdColumns(self):
        'C.rowIdColumns(table, catalog=None, schema=None, nullable=True) -->\n\nExecutes SQLSpecialColumns with SQL_BEST_ROWID which creates a result set of columns that\nuniquely identify a row\n\nEach row fetched has the following columns:\n 0) scope\n 1) column_name\n 2) data_type\n 3) type_name\n 4) column_size\n 5) buffer_length\n 6) decimal_digits\n 7) pseudo_column'
        pass
    
    def rowVerColumns(self):
        'C.rowIdColumns(table, catalog=None, schema=None, nullable=True) --> self\n\nExecutes SQLSpecialColumns with SQL_ROWVER which creates a result set of columns that\nare automatically updated when any value in the row is updated.\n\nEach row fetched has the following columns:\n 0) scope\n 1) column_name\n 2) data_type\n 3) type_name\n 4) column_size\n 5) buffer_length\n 6) decimal_digits\n 7) pseudo_column'
        pass
    
    @property
    def rowcount(self):
        'This read-only attribute specifies the number of rows the last DML statement\n (INSERT, UPDATE, DELETE) affected.  This is set to -1 for SELECT statements.'
        pass
    
    def setinputsizes(self, sizes):
        'setinputsizes(sizes) -> None\n\nSets the type information to be used when binding parameters.\nsizes must be a sequence of values, one for each input parameter.\nEach value may be an integer to override the column size when binding character\ndata, a Type Object to override the SQL type, or a sequence of integers to specify\n(SQL type, column size, decimal digits) where any may be none to use the default.\n\nParameters beyond the length of the sequence will be bound with the defaults.\nSetting sizes to None reverts all parameters to the defaults.'
        pass
    
    def setoutputsize(self):
        'Ignored.'
        pass
    
    def skip(self, count):
        'skip(count) --> None\n\nSkips the next `count` records by calling SQLFetchScroll with SQL_FETCH_NEXT.\nFor convenience, skip(0) is accepted and will do nothing.'
        pass
    
    def statistics(self):
        'C.statistics(catalog=None, schema=None, unique=False, quick=True) --> self\n\nCreates a results set of statistics about a single table and the indexes associated with \nthe table by executing SQLStatistics.\nunique\n  If True, only unique indexes are retured.  Otherwise all indexes are returned.\nquick\n  If True, CARDINALITY and PAGES are returned  only if they are readily available\n  from the server\n\nEach row fetched has the following columns:\n\n  0) table_cat\n  1) table_schem\n  2) table_name\n  3) non_unique\n  4) index_qualifier\n  5) index_name\n  6) type\n  7) ordinal_position\n  8) column_name\n  9) asc_or_desc\n 10) cardinality\n 11) pages\n 12) filter_condition'
        pass
    
    def tables(self):
        "C.tables(table=None, catalog=None, schema=None, tableType=None) --> self\n\nExecutes SQLTables and creates a results set of tables defined in the data\nsource.\n\nThe table, catalog, and schema interpret the '_' and '%' characters as\nwildcards.  The escape character is driver specific, so use\n`Connection.searchescape`.\n\nEach row fetched has the following columns:\n 0) table_cat: The catalog name.\n 1) table_schem: The schema name.\n 2) table_name: The table name.\n 3) table_type: One of 'TABLE', 'VIEW', SYSTEM TABLE', 'GLOBAL TEMPORARY'\n    'LOCAL TEMPORARY', 'ALIAS', 'SYNONYM', or a data source-specific type name."
        pass
    

DATETIME = _mod_datetime.datetime
class DataError(DatabaseError):
    'Exception raised for errors that are due to problems with the processed data\nlike division by zero, numeric value out of range, etc.'
    __class__ = DataError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Exception raised for errors that are due to problems with the processed data\nlike division by zero, numeric value out of range, etc.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pyodbc'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class DatabaseError(Error):
    'Exception raised for errors that are related to the database.'
    __class__ = DatabaseError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Exception raised for errors that are related to the database.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pyodbc'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

Date = _mod_datetime.date
def DateFromTicks(ticks):
    'DateFromTicks(ticks) --> datetime.date\n\nReturns a date object initialized from the given ticks value (number of seconds\nsince the epoch; see the documentation of the standard Python time module for\ndetails).'
    pass

class Error(_mod_builtins.Exception):
    "Exception that is the base class of all other error exceptions. You can use\nthis to catch all errors with one single 'except' statement."
    __class__ = Error
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        "Exception that is the base class of all other error exceptions. You can use\nthis to catch all errors with one single 'except' statement."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pyodbc'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class IntegrityError(DatabaseError):
    'Exception raised when the relational integrity of the database is affected,\ne.g. a foreign key check fails.'
    __class__ = IntegrityError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Exception raised when the relational integrity of the database is affected,\ne.g. a foreign key check fails.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pyodbc'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class InterfaceError(Error):
    'Exception raised for errors that are related to the database interface rather\nthan the database itself.'
    __class__ = InterfaceError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Exception raised for errors that are related to the database interface rather\nthan the database itself.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pyodbc'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class InternalError(DatabaseError):
    'Exception raised when the database encounters an internal error, e.g. the\ncursor is not valid anymore, the transaction is out of sync, etc.'
    __class__ = InternalError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Exception raised when the database encounters an internal error, e.g. the\ncursor is not valid anymore, the transaction is out of sync, etc.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pyodbc'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

NUMBER = _mod_builtins.float
class NotSupportedError(DatabaseError):
    'Exception raised in case a method or database API was used which is not\nsupported by the database, e.g. requesting a .rollback() on a connection that\ndoes not support transaction or has transactions turned off.'
    __class__ = NotSupportedError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Exception raised in case a method or database API was used which is not\nsupported by the database, e.g. requesting a .rollback() on a connection that\ndoes not support transaction or has transactions turned off.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pyodbc'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class OperationalError(DatabaseError):
    "Exception raised for errors that are related to the database's operation and\nnot necessarily under the control of the programmer, e.g. an unexpected\ndisconnect occurs, the data source name is not found, a transaction could not\nbe processed, a memory allocation error occurred during processing, etc."
    __class__ = OperationalError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        "Exception raised for errors that are related to the database's operation and\nnot necessarily under the control of the programmer, e.g. an unexpected\ndisconnect occurs, the data source name is not found, a transaction could not\nbe processed, a memory allocation error occurred during processing, etc."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pyodbc'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class ProgrammingError(DatabaseError):
    'Exception raised for programming errors, e.g. table not found or already\nexists, syntax error in the SQL statement, wrong number of parameters\nspecified, etc.'
    __class__ = ProgrammingError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Exception raised for programming errors, e.g. table not found or already\nexists, syntax error in the SQL statement, wrong number of parameters\nspecified, etc.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pyodbc'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

ROWID = _mod_builtins.int
class Row(_mod_builtins.object):
    'Row objects are sequence objects that hold query results.\n\nThey are similar to tuples in that they cannot be resized and new attributes\ncannot be added, but individual elements can be replaced.  This allows data to\nbe "fixed up" after being fetched.  (For example, datetimes may be replaced by\nthose with time zones attached.)\n\n  row[0] = row[0].replace(tzinfo=timezone)\n  print row[0]\n\nAdditionally, individual values can be optionally be accessed or replaced by\nname.  Non-alphanumeric characters are replaced with an underscore.\n\n  cursor.execute("select customer_id, [Name With Spaces] from tmp")\n  row = cursor.fetchone()\n  print row.customer_id, row.Name_With_Spaces\n\nIf using this non-standard feature, it is often convenient to specifiy the name\nusing the SQL \'as\' keyword:\n\n  cursor.execute("select count(*) as total from tmp")\n  row = cursor.fetchone()\n  print row.total'
    __class__ = Row
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, *args, **kwargs):
        'Row objects are sequence objects that hold query results.\n\nThey are similar to tuples in that they cannot be resized and new attributes\ncannot be added, but individual elements can be replaced.  This allows data to\nbe "fixed up" after being fetched.  (For example, datetimes may be replaced by\nthose with time zones attached.)\n\n  row[0] = row[0].replace(tzinfo=timezone)\n  print row[0]\n\nAdditionally, individual values can be optionally be accessed or replaced by\nname.  Non-alphanumeric characters are replaced with an underscore.\n\n  cursor.execute("select customer_id, [Name With Spaces] from tmp")\n  row = cursor.fetchone()\n  print row.customer_id, row.Name_With_Spaces\n\nIf using this non-standard feature, it is often convenient to specifiy the name\nusing the SQL \'as\' keyword:\n\n  cursor.execute("select count(*) as total from tmp")\n  row = cursor.fetchone()\n  print row.total'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def cursor_description(self):
        'The Cursor.description sequence from the Cursor that created this row.'
        pass
    

SQLWCHAR_SIZE = 2
SQL_ACCESSIBLE_PROCEDURES = 20
SQL_ACCESSIBLE_TABLES = 19
SQL_ACCESS_MODE = 101
SQL_ACTIVE_ENVIRONMENTS = 116
SQL_AGGREGATE_FUNCTIONS = 169
SQL_ALTER_DOMAIN = 117
SQL_ALTER_TABLE = 86
SQL_ASYNC_MODE = 10021
SQL_ATTR_ACCESS_MODE = 101
SQL_ATTR_ANSI_APP = 115
SQL_ATTR_AUTOCOMMIT = 102
SQL_ATTR_CURRENT_CATALOG = 109
SQL_ATTR_LOGIN_TIMEOUT = 103
SQL_ATTR_ODBC_CURSORS = 110
SQL_ATTR_QUIET_MODE = 111
SQL_ATTR_TRACE = 104
SQL_ATTR_TRACEFILE = 105
SQL_ATTR_TRANSLATE_LIB = 106
SQL_ATTR_TRANSLATE_OPTION = 107
SQL_ATTR_TXN_ISOLATION = 108
SQL_AUTOCOMMIT = 102
SQL_BATCH_ROW_COUNT = 120
SQL_BATCH_SUPPORT = 121
SQL_BIGINT = -5
SQL_BINARY = -2
SQL_BIT = -7
SQL_BOOKMARK_PERSISTENCE = 82
SQL_CATALOG_LOCATION = 114
SQL_CATALOG_NAME = 10003
SQL_CATALOG_NAME_SEPARATOR = 41
SQL_CATALOG_TERM = 42
SQL_CATALOG_USAGE = 92
SQL_CHAR = 1
SQL_COLLATION_SEQ = 10004
SQL_COLUMN_ALIAS = 87
SQL_CONCAT_NULL_BEHAVIOR = 22
SQL_CONVERT_BIGINT = 53
SQL_CONVERT_BINARY = 54
SQL_CONVERT_BIT = 55
SQL_CONVERT_CHAR = 56
SQL_CONVERT_DATE = 57
SQL_CONVERT_DECIMAL = 58
SQL_CONVERT_DOUBLE = 59
SQL_CONVERT_FLOAT = 60
SQL_CONVERT_FUNCTIONS = 48
SQL_CONVERT_GUID = 173
SQL_CONVERT_INTEGER = 61
SQL_CONVERT_INTERVAL_DAY_TIME = 123
SQL_CONVERT_INTERVAL_YEAR_MONTH = 124
SQL_CONVERT_LONGVARBINARY = 71
SQL_CONVERT_LONGVARCHAR = 62
SQL_CONVERT_NUMERIC = 63
SQL_CONVERT_REAL = 64
SQL_CONVERT_SMALLINT = 65
SQL_CONVERT_TIME = 66
SQL_CONVERT_TIMESTAMP = 67
SQL_CONVERT_TINYINT = 68
SQL_CONVERT_VARBINARY = 69
SQL_CONVERT_VARCHAR = 70
SQL_CONVERT_WCHAR = 122
SQL_CONVERT_WLONGVARCHAR = 125
SQL_CONVERT_WVARCHAR = 126
SQL_CORRELATION_NAME = 74
SQL_CREATE_ASSERTION = 127
SQL_CREATE_CHARACTER_SET = 128
SQL_CREATE_COLLATION = 129
SQL_CREATE_DOMAIN = 130
SQL_CREATE_SCHEMA = 131
SQL_CREATE_TABLE = 132
SQL_CREATE_TRANSLATION = 133
SQL_CREATE_VIEW = 134
SQL_CURRENT_QUALIFIER = 109
SQL_CURSOR_COMMIT_BEHAVIOR = 23
SQL_CURSOR_ROLLBACK_BEHAVIOR = 24
SQL_DATABASE_NAME = 16
SQL_DATA_SOURCE_NAME = 2
SQL_DATA_SOURCE_READ_ONLY = 25
SQL_DATETIME_LITERALS = 119
SQL_DBMS_NAME = 17
SQL_DBMS_VER = 18
SQL_DDL_INDEX = 170
SQL_DECIMAL = 3
SQL_DEFAULT_TXN_ISOLATION = 26
SQL_DESCRIBE_PARAMETER = 10002
SQL_DM_VER = 171
SQL_DOUBLE = 8
SQL_DRIVER_HDESC = 135
SQL_DRIVER_HENV = 4
SQL_DRIVER_HLIB = 76
SQL_DRIVER_HSTMT = 5
SQL_DRIVER_NAME = 6
SQL_DRIVER_ODBC_VER = 77
SQL_DRIVER_VER = 7
SQL_DROP_ASSERTION = 136
SQL_DROP_CHARACTER_SET = 137
SQL_DROP_COLLATION = 138
SQL_DROP_DOMAIN = 139
SQL_DROP_SCHEMA = 140
SQL_DROP_TABLE = 141
SQL_DROP_TRANSLATION = 142
SQL_DROP_VIEW = 143
SQL_DYNAMIC_CURSOR_ATTRIBUTES1 = 144
SQL_DYNAMIC_CURSOR_ATTRIBUTES2 = 145
SQL_EXPRESSIONS_IN_ORDERBY = 27
SQL_FILE_USAGE = 84
SQL_FLOAT = 6
SQL_FORWARD_ONLY_CURSOR_ATTRIBUTES1 = 146
SQL_FORWARD_ONLY_CURSOR_ATTRIBUTES2 = 147
SQL_GETDATA_EXTENSIONS = 81
SQL_GROUP_BY = 88
SQL_GUID = -11
SQL_IDENTIFIER_CASE = 28
SQL_IDENTIFIER_QUOTE_CHAR = 29
SQL_INDEX_KEYWORDS = 148
SQL_INFO_SCHEMA_VIEWS = 149
SQL_INSERT_STATEMENT = 172
SQL_INTEGER = 4
SQL_INTEGRITY = 73
SQL_INTERVAL_DAY = 103
SQL_INTERVAL_DAY_TO_HOUR = 108
SQL_INTERVAL_DAY_TO_MINUTE = 109
SQL_INTERVAL_DAY_TO_SECOND = 110
SQL_INTERVAL_HOUR = 104
SQL_INTERVAL_HOUR_TO_MINUTE = 111
SQL_INTERVAL_HOUR_TO_SECOND = 112
SQL_INTERVAL_MINUTE = 105
SQL_INTERVAL_MINUTE_TO_SECOND = 113
SQL_INTERVAL_MONTH = 102
SQL_INTERVAL_SECOND = 106
SQL_INTERVAL_YEAR = 101
SQL_INTERVAL_YEAR_TO_MONTH = 107
SQL_KEYSET_CURSOR_ATTRIBUTES1 = 150
SQL_KEYSET_CURSOR_ATTRIBUTES2 = 151
SQL_KEYWORDS = 89
SQL_LIKE_ESCAPE_CLAUSE = 113
SQL_LOGIN_TIMEOUT = 103
SQL_LONGVARBINARY = -4
SQL_LONGVARCHAR = -1
SQL_MAX_ASYNC_CONCURRENT_STATEMENTS = 10022
SQL_MAX_BINARY_LITERAL_LEN = 112
SQL_MAX_CATALOG_NAME_LEN = 34
SQL_MAX_CHAR_LITERAL_LEN = 108
SQL_MAX_COLUMNS_IN_GROUP_BY = 97
SQL_MAX_COLUMNS_IN_INDEX = 98
SQL_MAX_COLUMNS_IN_ORDER_BY = 99
SQL_MAX_COLUMNS_IN_SELECT = 100
SQL_MAX_COLUMNS_IN_TABLE = 101
SQL_MAX_COLUMN_NAME_LEN = 30
SQL_MAX_CONCURRENT_ACTIVITIES = 1
SQL_MAX_CURSOR_NAME_LEN = 31
SQL_MAX_DRIVER_CONNECTIONS = 0
SQL_MAX_IDENTIFIER_LEN = 10005
SQL_MAX_INDEX_SIZE = 102
SQL_MAX_PROCEDURE_NAME_LEN = 33
SQL_MAX_ROW_SIZE = 104
SQL_MAX_ROW_SIZE_INCLUDES_LONG = 103
SQL_MAX_SCHEMA_NAME_LEN = 32
SQL_MAX_STATEMENT_LEN = 105
SQL_MAX_TABLES_IN_SELECT = 106
SQL_MAX_TABLE_NAME_LEN = 35
SQL_MAX_USER_NAME_LEN = 107
SQL_MULTIPLE_ACTIVE_TXN = 37
SQL_MULT_RESULT_SETS = 36
SQL_NEED_LONG_DATA_LEN = 111
SQL_NON_NULLABLE_COLUMNS = 75
SQL_NO_NULLS = 0
SQL_NULLABLE = 1
SQL_NULLABLE_UNKNOWN = 2
SQL_NULL_COLLATION = 85
SQL_NUMERIC = 2
SQL_NUMERIC_FUNCTIONS = 49
SQL_ODBC_CURSORS = 110
SQL_ODBC_INTERFACE_CONFORMANCE = 152
SQL_ODBC_VER = 10
SQL_OJ_ALL_COMPARISON_OPS = 64
SQL_OJ_CAPABILITIES = 115
SQL_OJ_FULL = 4
SQL_OJ_INNER = 32
SQL_OJ_LEFT = 1
SQL_OJ_NESTED = 8
SQL_OJ_NOT_ORDERED = 16
SQL_OJ_RIGHT = 2
SQL_OPT_TRACE = 104
SQL_OPT_TRACEFILE = 105
SQL_ORDER_BY_COLUMNS_IN_SELECT = 90
SQL_PACKET_SIZE = 112
SQL_PARAM_ARRAY_ROW_COUNTS = 153
SQL_PARAM_ARRAY_SELECTS = 154
SQL_PARAM_INPUT = 1
SQL_PARAM_INPUT_OUTPUT = 2
SQL_PARAM_OUTPUT = 4
SQL_PARAM_TYPE_UNKNOWN = 0
SQL_PC_NOT_PSEUDO = 1
SQL_PC_PSEUDO = 2
SQL_PC_UNKNOWN = 0
SQL_PROCEDURES = 21
SQL_PROCEDURE_TERM = 40
SQL_QUIET_MODE = 111
SQL_QUOTED_IDENTIFIER_CASE = 93
SQL_REAL = 7
SQL_RESULT_COL = 3
SQL_RETURN_VALUE = 5
SQL_ROW_UPDATES = 11
SQL_SCHEMA_TERM = 39
SQL_SCHEMA_USAGE = 91
SQL_SCOPE_CURROW = 0
SQL_SCOPE_SESSION = 2
SQL_SCOPE_TRANSACTION = 1
SQL_SCROLL_OPTIONS = 44
SQL_SEARCH_PATTERN_ESCAPE = 14
SQL_SERVER_NAME = 13
SQL_SMALLINT = 5
SQL_SPECIAL_CHARACTERS = 94
SQL_SQL92_DATETIME_FUNCTIONS = 155
SQL_SQL92_FOREIGN_KEY_DELETE_RULE = 156
SQL_SQL92_FOREIGN_KEY_UPDATE_RULE = 157
SQL_SQL92_GRANT = 158
SQL_SQL92_NUMERIC_VALUE_FUNCTIONS = 159
SQL_SQL92_PREDICATES = 160
SQL_SQL92_RELATIONAL_JOIN_OPERATORS = 161
SQL_SQL92_REVOKE = 162
SQL_SQL92_ROW_VALUE_CONSTRUCTOR = 163
SQL_SQL92_STRING_FUNCTIONS = 164
SQL_SQL92_VALUE_EXPRESSIONS = 165
SQL_SQL_CONFORMANCE = 118
SQL_SS_TIME2 = -154
SQL_SS_XML = -152
SQL_STANDARD_CLI_CONFORMANCE = 166
SQL_STATIC_CURSOR_ATTRIBUTES1 = 167
SQL_STATIC_CURSOR_ATTRIBUTES2 = 168
SQL_STRING_FUNCTIONS = 50
SQL_SUBQUERIES = 95
SQL_SYSTEM_FUNCTIONS = 51
SQL_TABLE_TERM = 45
SQL_TIMEDATE_ADD_INTERVALS = 109
SQL_TIMEDATE_DIFF_INTERVALS = 110
SQL_TIMEDATE_FUNCTIONS = 52
SQL_TINYINT = -6
SQL_TRANSLATE_DLL = 106
SQL_TRANSLATE_OPTION = 107
SQL_TXN_CAPABLE = 46
SQL_TXN_ISOLATION = 108
SQL_TXN_ISOLATION_OPTION = 72
SQL_TXN_READ_COMMITTED = 2
SQL_TXN_READ_UNCOMMITTED = 1
SQL_TXN_REPEATABLE_READ = 4
SQL_TXN_SERIALIZABLE = 8
SQL_TYPE_DATE = 91
SQL_TYPE_TIME = 92
SQL_TYPE_TIMESTAMP = 93
SQL_UNION = 96
SQL_UNKNOWN_TYPE = 0
SQL_USER_NAME = 47
SQL_VARBINARY = -3
SQL_VARCHAR = 12
SQL_WCHAR = -8
SQL_WLONGVARCHAR = -10
SQL_WMETADATA = -888
SQL_WVARCHAR = -9
SQL_XOPEN_CLI_YEAR = 10000
STRING = _mod_builtins.str
Time = _mod_datetime.time
def TimeFromTicks(ticks):
    'TimeFromTicks(ticks) --> datetime.time\n\nReturns a time object initialized from the given ticks value (number of seconds\nsince the epoch; see the documentation of the standard Python time module for\ndetails).'
    pass

Timestamp = _mod_datetime.datetime
def TimestampFromTicks(ticks):
    'TimestampFromTicks(ticks) --> datetime.datetime\n\nReturns a datetime object initialized from the given ticks value (number of\nseconds since the epoch; see the documentation of the standard Python time\nmodule for details'
    pass

UNICODE_SIZE = 2
class Warning(_mod_builtins.Exception):
    'Exception raised for important warnings like data truncations while inserting,\n etc.'
    __class__ = Warning
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Exception raised for important warnings like data truncations while inserting,\n etc.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pyodbc'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

__doc__ = "A database module for accessing databases via ODBC.\n\nThis module conforms to the DB API 2.0 specification while providing\nnon-standard convenience features.  Only standard Python data types are used\nso additional DLLs are not required.\n\nStatic Variables:\n\nversion\n  The module version string.  Official builds will have a version in the format\n  `major.minor.revision`, such as 2.1.7.  Beta versions will have -beta appended,\n  such as 2.1.8-beta03.  (This would be a build before the official 2.1.8 release.)\n  Some special test builds will have a test name (the git branch name) prepended,\n  such as fixissue90-2.1.8-beta03.\n\napilevel\n  The string constant '2.0' indicating this module supports DB API level 2.0.\n\nlowercase\n  A Boolean that controls whether column names in result rows are lowercased.\n  This can be changed any time and affects queries executed after the change.\n  The default is False.  This can be useful when database columns have\n  inconsistent capitalization.\n\npooling\n  A Boolean indicating whether connection pooling is enabled.  This is a\n  global (HENV) setting, so it can only be modified before the first\n  connection is made.  The default is True, which enables ODBC connection\n  pooling.\n\nthreadsafety\n  The integer 1, indicating that threads may share the module but not\n  connections.  Note that connections and cursors may be used by different\n  threads, just not at the same time.\n\nqmark\n  The string constant 'qmark' to indicate parameters are identified using\n  question marks."
__file__ = 'c:\\Users\\ZapMaster PV\\Documents\\Work\\HP_Project\\Lab_Web_Django\\venv\\Lib\\site-packages\\pyodbc.cp36-win_amd64.pyd'
__name__ = 'pyodbc'
__package__ = ''
apilevel = '2.0'
def connect(str, autocommit=False, ansi=False, timeout=0, **kwargs):
    "connect(str, autocommit=False, ansi=False, timeout=0, **kwargs) --> Connection\n\nAccepts an ODBC connection string and returns a new Connection object.\n\nThe connection string will be passed to SQLDriverConnect, so a DSN connection\ncan be created using:\n\n  cnxn = pyodbc.connect('DSN=DataSourceName;UID=user;PWD=password')\n\nTo connect without requiring a DSN, specify the driver and connection\ninformation:\n\n  DRIVER={SQL Server};SERVER=localhost;DATABASE=testdb;UID=user;PWD=password\n\nNote the use of braces when a value contains spaces.  Refer to SQLDriverConnect\ndocumentation or the documentation of your ODBC driver for details.\n\nThe connection string can be passed as the string `str`, as a list of keywords,\nor a combination of the two.  Any keywords except autocommit, ansi, and timeout\n(see below) are simply added to the connection string.\n\n  connect('server=localhost;user=me')\n  connect(server='localhost', user='me')\n  connect('server=localhost', user='me')\n\nThe DB API recommends the keywords 'user', 'password', and 'host', but these\nare not valid ODBC keywords, so these will be converted to 'uid', 'pwd', and\n'server'.\n\nSpecial Keywords\n\nThe following specal keywords are processed by pyodbc and are not added to the\nconnection string.  (If you must use these in your connection string, pass them\nas a string, not as keywords.)\n\n  autocommit\n    If False or zero, the default, transactions are created automatically as\n    defined in the DB API 2.  If True or non-zero, the connection is put into\n    ODBC autocommit mode and statements are committed automatically.\n   \n  ansi\n    By default, pyodbc first attempts to connect using the Unicode version of\n    SQLDriverConnectW.  If the driver returns IM001 indicating it does not\n    support the Unicode version, the ANSI version is tried.  Any other SQLSTATE\n    is turned into an exception.  Setting ansi to true skips the Unicode\n    attempt and only connects using the ANSI version.  This is useful for\n    drivers that return the wrong SQLSTATE (or if pyodbc is out of date and\n    should support other SQLSTATEs).\n   \n  timeout\n    An integer login timeout in seconds, used to set the SQL_ATTR_LOGIN_TIMEOUT\n    attribute of the connection.  The default is 0 which means the database's\n    default timeout, if any, is used.\n"
    pass

def dataSources():
    'dataSources() --> { DSN : Description }\n\nReturns a dictionary mapping available DSNs to their descriptions.'
    pass

def drivers():
    'drivers() --> [ DriverName1, DriverName2 ... DriverNameN ]\n\nReturns a list of installed drivers.'
    pass

def getDecimalSeparator():
    'getDecimalSeparator() -> string\n\nGets the decimal separator character used when parsing NUMERIC from the database.'
    return ''

lowercase = False
native_uuid = False
paramstyle = 'qmark'
pooling = True
def setDecimalSeparator(string):
    'setDecimalSeparator(string) -> None\n\nSets the decimal separator character used when parsing NUMERIC from the database.'
    pass

threadsafety = 1
version = '4.0.30'
