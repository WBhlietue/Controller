using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using Unity.Mathematics;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.EventSystems;
public class JoyStick : MonoBehaviour, IPointerDownHandler, IPointerUpHandler, IDragHandler
{
    public float maxDistance;
    public Transform handle;
    public List<DirSet> dirSet = new List<DirSet>();
    string previous = "";

    public void CheckDirection(float angle)
    {
        for (int i = 0; i < dirSet.Count; i++)
        {
            if (dirSet[i].Chekc(angle))
            {
                if (dirSet[i].key != previous)
                {
                    if(previous.Length > 0){
                        MainManager.instance.SendData(previous, 0);
                    }
                    previous = dirSet[i].key;
                    MainManager.instance.SendData(dirSet[i].key, 1);
                }

            }
        }
    }
    public void OnDrag(PointerEventData eventData)
    {
        Vector2 dis = eventData.position - (Vector2)transform.position;
        if (dis.magnitude > maxDistance)
        {
            dis = dis.normalized * maxDistance;
        }
        handle.position = (Vector2)(transform.position) + dis;
        Calculate();
    }

    public void OnPointerDown(PointerEventData eventData)
    {
        handle.position = eventData.position;
        Calculate();
    }

    void Calculate()
    {
        float angle = Vector2.Angle(handle.localPosition, Vector2.up) * (handle.localPosition.x > 0 ? 1 : -1);
        CheckDirection(angle);
    }

    public void OnPointerUp(PointerEventData eventData)
    {
        handle.localPosition = Vector3.zero;
    }
}

[System.Serializable]
public class DirSet
{
    public float lesser;
    public float upper;
    public string key;
    public bool useOR = false;
    public bool Chekc(float angle)
    {
        if (useOR)
        {
            if (angle < lesser || angle > upper)
            {
                return true;
            }
        }
        else
        {
            if (angle < lesser && angle > upper)
            {
                return true;
            }
        }
        return false;
    }
}
