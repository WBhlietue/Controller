using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.SceneManagement;

public class MainManager : MonoBehaviour
{
    public static MainManager instance;
    private void Awake()
    {
        instance = this;
        Debug.Log(CheckIP.serverIP);
        if (CheckIP.serverIP.Length == 0)
        {
            SceneManager.LoadScene("CheckIP");
        }
    }
    public void Back(){
        SceneManager.LoadScene("CheckIP");
    }

    public void SendData(string btnName, int status, Vector2 chig, float length = 0)
    {
        PostData data = new PostData()
        {
            keyName = btnName,
            status = status,
            x = chig.x,
            y = chig.y,
            length = length
        };
        CheckIP.ws.Send(JsonUtility.ToJson(data));
        // StartCoroutine(PostRequest(btnName, status));
    }
    // IEnumerator PostRequest(string btnName, int status)
    // {
    //     PostData data = new PostData()
    //     {
    //         keyName = btnName,
    //         status = status
    //     };

    //     UnityWebRequest www = UnityWebRequest.PostWwwForm(CheckIP.serverIP+"/key", JsonUtility.ToJson(data));
    //     www.SetRequestHeader("Content-Type", "application/json");
    //     yield return www.SendWebRequest();

    //     if (www.result == UnityWebRequest.Result.Success)
    //     {

    //     }
    //     else
    //     {

    //     }
    //     www.Dispose();

    // }

}
