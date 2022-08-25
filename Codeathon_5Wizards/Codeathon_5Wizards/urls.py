from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('All_Tools.urls')),
    path('frequency_tool', include('Frequency_Tool_5G.urls')),
    path('power_tool', include('Power_Tool_5G.urls')),
    path('re_mapping_tool',include('RE_Mapping_Tool_5G.urls')),
    path('throughput_tool',include('Throughput_Tool_5G.urls')),
    path('du_log_parser_tool', include('Du_Log_Parser_Tool_5G.urls')),
    path('ota_algo_tool',include('OTA_Algo_Tool_5G.urls')),
    path('ptp_timing_delay_tool',include('PTP_Timing_Delay_Parsing_Tool_5G.urls')),
    path('qual_log_parsing_tool',include('Qual_Log_Parsing_Tool_5G.urls')),
    path('link_budget_tool',include('Link_Budget_Tool_5G.urls')),
    path('nr_arfcn_tool',include('NR_ARFCN_GSCN_Tool_5G.urls')),
    path('odu_cpu_utilization_tool',include('ODU_CPU_Utilization_Tool_5G.urls')),
    path('global_result_tool',include('Global_Result_Tool_5G.urls')),

]
