using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;
using TMPro;

public class ClickBtn : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler, IPointerDownHandler
{
    public string btnName;
    public bool isWork = true;
    bool isEnter = false;

    private void Start()
    {
        TextMeshProUGUI text = GetComponentInChildren<TextMeshProUGUI>();
        var keymaps = CheckIP.keyMap.Split(", ");
        foreach (var item in keymaps)
        {
            var sets = item.Split(": ");
            var name = sets[0].Substring(1, sets[0].Length - 2);
                Debug.Log(btnName + ", " + name + ", " + btnName.Equals(name));
            if (btnName == name)
            {
                text.text = sets[1].Substring(1, sets[1].Length - 2);
                break;
            }
        }
    }



    public void OnPointerEnter(PointerEventData eventData)
    {
        // SendInfo(1);
        // Vibrate();
    }

    public void OnPointerExit(PointerEventData eventData)
    {
        SendInfo(0);
    }
    public void SendInfo(int status)
    {
        if (!isWork)
        {
            return;
        }
        MainManager.instance.SendData(btnName, status, Vector2.zero);
    }

    void Vibrate()
    {
        if (!isWork)
        {
            return;
        }
        if (CheckIP.vibrate)
        {
            Handheld.Vibrate();
        }
    }

    public void OnPointerDown(PointerEventData eventData)
    {
        SendInfo(1);
        Vibrate();
    }
}
