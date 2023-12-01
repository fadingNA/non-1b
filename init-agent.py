

user_proxy = UserProxyAgent(name="user_proxy",
                            is_termination_msg=lambda msg: "Terminate" in msg["content"],
                            human_input_mode="ALWAYS",
                            max_consecutive_auto_reply=1)

researcher = GPTAssistantAgent(name="researcher",
                               llm_config={
                                   "config_list": config_list,
                                   "assistant_id": "asst_31CUYLlH6hCsvkN87p7jSBzg",
                               })

researcher.register_function(
    function_map={
        "web_scraping": web_scraping,
        "web_search": web_search
    }
)

research_manager = GPTAssistantAgent(name="research_manager",
                                     llm_config={
                                         "config_list": config_list,
                                         "assistant_id": "asst_xLx5q2KxPnOkXhS0ChVPMrsG",
                                     })


research_director = GPTAssistantAgent(name="research_director",
                                      llm_config={
                                          "config_list": config_list,
                                          "assistant_id": "asst_GrQIIfBToByaL7IOeYcQMwib",
                                      })
research_director.register_function(
    function_map={
        "get_airtable_records": get_airtable_records,
        "update_single_airtable_record": update_single_airtable_record,
    }
)

group_chat = autogen.GroupChat(agents=[user_proxy, researcher, research_manager, research_director],
                               messages=[], max_round=10)
group_chat_manager = autogen.GroupChatManager(group_chat=group_chat,
                                              llm_config={"config_list": config_list})


message = """
Research the api weather data which one is forecast or historical data
provide. focus on the hourly data.
list: https://airtable.com/appqSQcliGnkSLbaa/tbl74uZ3blk6CEwAE/viwivoHsMjvlq0AB8?blocks=hide
"""
user_proxy.initiate_chat(group_chat_manager, message=message)