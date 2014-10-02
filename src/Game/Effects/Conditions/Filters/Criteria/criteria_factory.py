from fixed_criteria import FixedCriteria
from source_criteria import SourceCriteria

from kao_factory.factory import Factory
from kao_factory.typed_factory import TypedFactory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter

CriteriaFactory = TypedFactory('type', {"FIXED":Factory(FixedCriteria, [PrimitiveParameter("field"), PrimitiveParameter("value"), PrimitiveParameter("operation")]),
                                        "SOURCE":Factory(SourceCriteria, [PrimitiveParameter("field"), PrimitiveParameter("source")])})