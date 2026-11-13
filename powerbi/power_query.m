// Power Query M template for importing the cleaned fact table.
let
    Source = Csv.Document(File.Contents("<PROJECT_PATH>\data\processed\sales_clean.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(Headers, {{"order_id", type text}, {"order_date", type date}, {"quantity", Int64.Type}, {"unit_price", Currency.Type}, {"unit_cost", Currency.Type}, {"discount_rate", Percentage.Type}})
in
    Types
