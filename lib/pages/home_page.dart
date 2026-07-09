import 'package:flutter/material.dart';
import '../wigets/side_bar.dart';
import '../wigets/search_section.dart';

class Homepage extends StatelessWidget {
  const Homepage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Row(
        children: [
          SideBar(),
          Column(
            children: [
              SearchSection(), // search section
              // footer
            ],
          ),
        ],
      ),
    );
  }
}
