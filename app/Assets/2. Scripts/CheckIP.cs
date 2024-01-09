using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using UnityEngine.Networking;
using UnityEngine.SceneManagement;

class PostData
{
    public string keyName;
    public int status;
}

public class CheckIP : MonoBehaviour
{
    public TMP_InputField input;
    public TextMeshProUGUI btnText;
    bool checking = false;
    public static string serverIP = "";
    public static bool vibrate = false;
    public Toggle toggle;
    public void Check()
    {
        if (!checking)
        {
            vibrate = toggle.isOn;
            checking = true;
            btnText.text = "wait";
            StartCoroutine(PostRequest());
        }
    }
    IEnumerator PostRequest()
    {
        string ip = "http://" + input.text + ":8000/checkConnect";
        Debug.Log(ip);
        PostData data = new PostData()
        {
            keyName = "test",

        };
        Debug.Log(JsonUtility.ToJson(data));
        UnityWebRequest www = UnityWebRequest.PostWwwForm(ip, JsonUtility.ToJson(data));
        www.SetRequestHeader("Content-Type", "application/json");

        yield return www.SendWebRequest();
        checking = false;
        Debug.Log(www.result);
        if (www.result == UnityWebRequest.Result.Success)
        {
            Debug.Log("Response: " + www.downloadHandler.text);
            www.Dispose();

            btnText.text = "connected";
            serverIP = "http://" + input.text + ":8000";
            SceneManager.LoadScene("controller");

        }
        else
        {
            Debug.LogError(www.error);
            btnText.text = www.result.ToString();
        }
        www.Dispose();

    }
}
