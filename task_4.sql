Select Column_name,
		column_type,
        is_nullable,
        column_key,
        column_default,
        extra
FROM
	Information_schema.columns
WHERE
	table_name='Books'
    AND table_schema= DATABASE()