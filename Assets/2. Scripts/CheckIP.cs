using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using UnityEngine.Networking;
using UnityEngine.SceneManagement;
using WebSocketSharp;
// using System.Net.WebSockets;
// using System;
// using System.Threading;
// using System.Text;

class PostData
{
    public string keyName;
    public int status;
    public float x;
    public float y;
}

public class CheckIP : MonoBehaviour
{
    public TMP_InputField input;
    public TextMeshProUGUI btnText;
    bool checking = false;
    public static string serverIP = "";
    public static bool vibrate = false;
    public Toggle toggle;
    public static WebSocket ws;
    private void Start() {
        input.text = PlayerPrefs.GetString("ip", "127.0.0.1");
    }
    public void Check()
    {
        if (!checking)
        {
            vibrate = toggle.isOn;
            checking = true;
            btnText.text = "wait";

            // Connect();

            ws = new WebSocket("ws://" + input.text + ":8000/websocket");
            ws.OnOpen += (s, e) =>
            {
                serverIP = "ws://" + input.text + ":8000/websocket";
                PlayerPrefs.SetString("ip", input.text);
                SceneManager.LoadScene("controller");
            };
            ws.OnError += (s, e) =>
            {
                btnText.text = "Error";
            };
            ws.OnMessage += (s, e) =>
            {
                Debug.Log(e.Data);
            };
            ws.Connect();


            // StartCoroutine(PostRequest());
        }
    }

    // async void Connect(){
    //     ClientWebSocket ws =new ClientWebSocket();
    //     CancellationToken ct = new CancellationToken();
    //     Uri uri = new Uri("ws://127.0.0.1:8000/websocket");
    //     await ws.ConnectAsync(uri, ct);
    //     Debug.Log("Asd");
    //     await ws.SendAsync(new ArraySegment<byte>(Encoding.UTF8.GetBytes("hi")), WebSocketMessageType.Binary, true, ct);
    // }

    // IEnumerator PostRequest()
    // {
    //     string ip = "http://" + input.text + ":8000/checkConnect";
    //     Debug.Log(ip);
    //     PostData data = new PostData()
    //     {
    //         keyName = "test",

    //     };
    //     Debug.Log(JsonUtility.ToJson(data));
    //     UnityWebRequest www = UnityWebRequest.PostWwwForm(ip, JsonUtility.ToJson(data));
    //     www.SetRequestHeader("Content-Type", "application/json");

    //     yield return www.SendWebRequest();
    //     checking = false;
    //     Debug.Log(www.result);
    //     if (www.result == UnityWebRequest.Result.Success)
    //     {
    //         Debug.Log("Response: " + www.downloadHandler.text);
    //         www.Dispose();

    //         btnText.text = "connected";
            
    //         serverIP = "http://" + input.text + ":8000";
    //         SceneManager.LoadScene("controller");

    //     }
    //     else
    //     {
    //         Debug.LogError(www.error);
    //         btnText.text = www.result.ToString();
    //     }
    //     www.Dispose();

    // }
}
