# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkdts.endpoint import endpoint_data

class DescribePreCheckStatusRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'DescribePreCheckStatus','dts')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_StructType(self):
		return self.get_query_params().get('StructType')

	def set_StructType(self,StructType):
		self.add_query_param('StructType',StructType)

	def get_PageNo(self):
		return self.get_query_params().get('PageNo')

	def set_PageNo(self,PageNo):
		self.add_query_param('PageNo',PageNo)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_JobCode(self):
		return self.get_query_params().get('JobCode')

	def set_JobCode(self,JobCode):
		self.add_query_param('JobCode',JobCode)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_DtsJobId(self):
		return self.get_query_params().get('DtsJobId')

	def set_DtsJobId(self,DtsJobId):
		self.add_query_param('DtsJobId',DtsJobId)

	def get_StructPhase(self):
		return self.get_query_params().get('StructPhase')

	def set_StructPhase(self,StructPhase):
		self.add_query_param('StructPhase',StructPhase)