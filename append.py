import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/ec2-user/dsdemo.json'

import apache_beam as beam
import argparse
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText

class AppendDoFn(beam.DoFn):
    def process(self, element):
        return element + " - Hello World!"
    
parser = argparse.ArgumentParser()
parser.add_argument('--input', dest='input',
                   default='gs://dataflow-samples/shakespeare/kinglear.txt')
parser.add_argument('--output', dest='output',
                   default='gs://dsp_model_store_famenor/shakespeare/kinglear.txt')

known_args, pipeline_args = parser.parse_known_args(None)
pipeline_options = PipelineOptions(pipeline_args)

p = beam.Pipeline(options=pipeline_options)
lines = p | 'read' >> ReadFromText(known_args.input)
appended = lines | 'append' >> beam.ParDo(AppendDoFn())
appended | 'write' >> WriteToText(known_args.output)

result = p.run()
result.wait_until_finish()