async function getAISuggestion() {
  const title = document.getElementById("title").value.trim();
  if (!title) {
    alert("Please enter a project title to get AI suggestions.");
    return;
  }

  try {
    const res = await fetch("http://127.0.0.1:5000/suggest", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title })
    });

    const data = await res.json();

    if (data.suggestion) {
      document.getElementById("description").value = data.suggestion;
    } else {
      alert("No suggestion received. Check the server logs.");
      console.error("Response data:", data);
    }

  } catch (error) {
    alert("Error getting AI suggestion. Make sure your Flask server is running.");
    console.error(error);
  }
}