https://huggingface.co/datasets/gretelai/synthetic_text_to_sql \
https://huggingface.co/datasets/philschmid/sql-create-context-copy \
https://huggingface.co/datasets/mdowling/sql_with_index \
https://huggingface.co/datasets/AayushShah/SQL_Merged_IDs_and_Text \
https://huggingface.co/datasets/AayushShah/Univeral_SQL_Three_Datasets_Combined_WithText_IDs \
https://huggingface.co/datasets/jasmeeetsingh/sql-spider-kaggledbqa-with-context?row=0

Idea for unified schema:

| id        | nlq    | sql_context | sql_response | input_ids | attention_mask | labels    | sql_complexity | complexity_reasoning |
|-----------|--------|-------------|--------------|-----------|----------------|-----------|----------------|----------------------|
| Serial PK | String | String      | String       | List[Int] | List[Int]      | List[int] | String         | String               |
