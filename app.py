import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# API key for validation
API_KEY = "AKIRU"

# API URL for player information
PLAYER_INFO_URL = "https://freefireinfoapiv2lk-team.vercel.app/api/playerstats"
WISHLIST_API_URL = "https://ariflex-labs-wishlist-api.vercel.app/items_info"

# Function to fetch player info
def get_player_info(uid, region):
    api_key = "PRINCE-PERM-KEY"
    url = f"{PLAYER_INFO_URL}?uid={uid}&region={region}&api_key={api_key}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch player information."}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Function to fetch wishlist info
def get_wishlist(uid, region):
    url = f"{WISHLIST_API_URL}?uid={uid}&region={region}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch wishlist information."}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Combined API endpoint
@app.route('/AKIRU-INFO-API', methods=['GET'])
def akiru_info_api():
    # Extracting parameters from the request URL
    uid = request.args.get('UID')
    region = request.args.get('REGION')
    key = request.args.get('key')

    # Validate API key
    if key != API_KEY:
        return jsonify({"error": "Invalid API key."}), 403

    # Fetch player info
    player_info = get_player_info(uid, region)
    
    # Fetch wishlist info
    wishlist_info = get_wishlist(uid, region)

    # Assuming player_info and wishlist_info are structured as per the requested response
    account_info = player_info.get("AccountInfo", {})
    captain_info = player_info.get("captainBasicInfo", {})
    guild_info = player_info.get("GuildInfo", {})
    social_info = player_info.get("socialinfo", {})
    pet_info = player_info.get("petInfo", {})
    wishlist_items = wishlist_info.get("items", [])

    response_data = {
        "AccountInfo": {
            "AccountAvatarId": account_info.get("AccountAvatarId", ""),
            "AccountBPBadges": account_info.get("AccountBPBadges", ""),
            "AccountBPID": account_info.get("AccountBPID", ""),
            "AccountBannerId": account_info.get("AccountBannerId", ""),
            "AccountCreateTime": account_info.get("AccountCreateTime", ""),
            "AccountEXP": account_info.get("AccountEXP", ""),
            "AccountLastLogin": account_info.get("AccountLastLogin", ""),
            "AccountLevel": account_info.get("AccountLevel", ""),
            "AccountLikes": account_info.get("AccountLikes", ""),
            "AccountName": account_info.get("AccountName", ""),
            "AccountRegion": account_info.get("AccountRegion", ""),
            "AccountSeasonId": account_info.get("AccountSeasonId", ""),
            "AccountType": account_info.get("AccountType", ""),
            "BrMaxRank": account_info.get("BrMaxRank", ""),
            "BrRankPoint": account_info.get("BrRankPoint", ""),
            "CsMaxRank": account_info.get("CsMaxRank", ""),
            "CsRankPoint": account_info.get("CsRankPoint", ""),
            "EquippedWeapon": account_info.get("EquippedWeapon", []),
            "EquippedWeaponImages": [f"https://ff-community-api.vercel.app/icons?id={weapon_id}" for weapon_id in account_info.get("EquippedWeapon", [])],
            "ReleaseVersion": account_info.get("ReleaseVersion", ""),
            "Role": account_info.get("Role", ""),
            "ShowBrRank": account_info.get("ShowBrRank", ""),
            "ShowCsRank": account_info.get("ShowCsRank", ""),
            "Title": account_info.get("Title", ""),
            "hasElitePass": account_info.get("hasElitePass", False)
        },
        "AccountProfileInfo": {
            "EquippedOutfit": account_info.get("EquippedOutfit", []),
            "EquippedOutfitImages": [f"https://ff-community-api.vercel.app/icons?id={outfit_id}" for outfit_id in account_info.get("EquippedOutfit", [])],
            "EquippedSkills": account_info.get("EquippedSkills", []),
            "EquippedSkillsImages": account_info.get("EquippedSkillsImages", [])
        },
        "GuildInfo": {
            "GuildCapacity": guild_info.get("GuildCapacity", ""),
            "GuildID": guild_info.get("GuildID", ""),
            "GuildLevel": guild_info.get("GuildLevel", ""),
            "GuildMember": guild_info.get("GuildMember", ""),
            "GuildName": guild_info.get("GuildName", ""),
            "GuildOwner": guild_info.get("GuildOwner", "")
        },
        "OXX3JMXgOb": captain_info.get("nickname", ""),
        "captainBasicInfo": {
            "AvatarImage": f"https://ff-community-api.vercel.app/icons?id={captain_info.get('AvatarImage', '')}",
            "BannerImage": f"https://ff-community-api.vercel.app/icons?id={captain_info.get('BannerImage', '')}",
            "EquippedWeapon": captain_info.get("EquippedWeapon", []),
            "accountId": captain_info.get("accountId", ""),
            "accountType": captain_info.get("accountType", ""),
            "badgeCnt": captain_info.get("badgeCnt", ""),
            "badgeId": captain_info.get("badgeId", ""),
            "bannerId": captain_info.get("bannerId", ""),
            "createAt": captain_info.get("createAt", ""),
            "csMaxRank": captain_info.get("csMaxRank", ""),
            "csRank": captain_info.get("csRank", ""),
            "csRankingPoints": captain_info.get("csRankingPoints", ""),
            "exp": captain_info.get("exp", ""),
            "headPic": captain_info.get("headPic", ""),
            "lastLoginAt": captain_info.get("lastLoginAt", ""),
            "level": captain_info.get("level", ""),
            "liked": captain_info.get("liked", ""),
            "maxRank": captain_info.get("maxRank", ""),
            "nickname": captain_info.get("nickname", ""),
            "pinId": captain_info.get("pinId", ""),
            "rank": captain_info.get("rank", ""),
            "rankingPoints": captain_info.get("rankingPoints", ""),
            "region": captain_info.get("region", ""),
            "releaseVersion": captain_info.get("releaseVersion", ""),
            "seasonId": captain_info.get("seasonId", ""),
            "showBrRank": captain_info.get("showBrRank", ""),
            "showCsRank": captain_info.get("showCsRank", ""),
            "title": captain_info.get("title", "")
        },
        "creditScoreInfo": {
            "creditScore": captain_info.get("creditScore", ""),
            "periodicSummaryEndTime": captain_info.get("periodicSummaryEndTime", ""),
            "periodicSummaryStartTime": captain_info.get("periodicSummaryStartTime", ""),
            "rewardState": captain_info.get("rewardState", "")
        },
        "petInfo": pet_info,
        "socialinfo": social_info,
        "Wishlist_items": wishlist_items
    }
    
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)
