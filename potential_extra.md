https://huggingface.co/datasets/gretelai/synthetic_text_to_sql
https://huggingface.co/datasets/philschmid/sql-create-context-copy
https://huggingface.co/datasets/mdowling/sql_with_index
https://huggingface.co/datasets/AayushShah/SQL_Merged_IDs_and_Text
https://huggingface.co/datasets/AayushShah/Univeral_SQL_Three_Datasets_Combined_WithText_IDs
https://huggingface.co/datasets/higgsfield/question_to_sql need to split using re in order to create context col


General Idea for unified schema
| NLQ | Context | SQL Response | Input_ids | Attention_mask | Labels |
|-----|---------|--------------|-----------|----------------|--------|
|     |         |              |           |                |        |
|     |         |              |           |                |        |
|     |         |              |           |                |        |