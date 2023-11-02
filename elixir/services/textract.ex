defmodule Elixir.Textract do
  @moduledoc """
  A sample code example in Elixir.
  """

  @doc """
  Analyze document.
  > Copy this function into your Elixir project and copy the `deps/0` in `mix_sample.exs` into your `mix.exs`.

  ## Examples
      # Run this to try out `analyze_document/3`/`analyze_document/4`
      YourProject.Textract.analyze_document("access_key", "secret_key", "region", "path")

  > More explanations here: https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html

  Example provided by @enkr1 | enkr99@gmail.com

  """
  def analyze_document(access_key, secret_key, region, png_path \\ "/path/to/png") do
    case AWS.Client.create(access_key, secret_key, region)
         |> AWS.Textract.analyze_document(%{
           "Document" => %{"Bytes" => png_path |> File.read!() |> Base.encode64()},
           "FeatureTypes" => ["TABLES", "FORMS"]
         }) do
      {
        :ok,
        %{
          "AnalyzeDocumentModelVersion" => _,
          "Blocks" => blocks,
          "DocumentMetadata" => _
        } = _result_map,
        response = _map_with_encoded_body_str
      } ->
        # ...
        response |> IO.inspect(label: "response")

      {:error, {_key, %{body: reason}} = reason_tupple} ->
        # ...
        reason_tupple |> IO.inspect(label: "reason_tupple")
        {:error, reason}

      edge_case ->
        edge_case |> IO.inspect(label: "edge_case")
        {:error, "Something went wrong when extracting the file ..."}
    end
  end
end
