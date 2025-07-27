open System
open System.Text.RegularExpressions

[<EntryPoint>]
let main argv =
    Console.Clear()
    Console.BackgroundColor <- ConsoleColor.Yellow
    Console.ForegroundColor <- ConsoleColor.Black
    Console.WriteLine("\n\n")

    let mutable insideBody = false
    let mutable insideScript = false

    let bodyRegex = Regex(@"<body", RegexOptions.IgnoreCase)
    let scriptStartRegex = Regex(@"<script", RegexOptions.IgnoreCase)
    let scriptEndRegex = Regex(@"</script", RegexOptions.IgnoreCase)
    let breakRegex = Regex(@"<br|<p|</p", RegexOptions.IgnoreCase)
    let hrefRegex = Regex(@"href\s*=\s*""([^""]*)""", RegexOptions.IgnoreCase)
    let tagStripper = Regex(@"<.*?>", RegexOptions.IgnoreCase)

    let rec loop () =
        let line = Console.ReadLine()
        if not (isNull line) then
            if not insideBody then
                if bodyRegex.IsMatch(line) then
                    insideBody <- true

            if insideBody then
                if scriptStartRegex.IsMatch(line) then
                    insideScript <- true
                if scriptEndRegex.IsMatch(line) then
                    insideScript <- false
                    loop()
                elif not insideScript then
                    // Print line breaks
                    if breakRegex.IsMatch(line) then
                        Console.WriteLine()

                    // Print all href URLs
                    for m in hrefRegex.Matches(line) do
                        let href = (m :?> Match).Groups.[1].Value
                        Console.WriteLine(href)

                    // Print visible text
                    let text = tagStripper.Replace(line, "")
                    if not (String.IsNullOrWhiteSpace(text)) then
                        Console.Write(text + " ")

            loop()

    loop()
    0
