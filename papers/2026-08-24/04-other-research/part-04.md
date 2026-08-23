# 📦 其他研究 | 2026年08月24日

> 本类共 **155** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-155**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-155**

---

### 151. [DreamHand: Repurposing Video Diffusion Models for Occlusion-Robust Egocentric 3D Hand Motion Recovery](https://arxiv.org/abs/2608.20308)

**<font color=#1a73e8>作者：</font>** Yufei Liu, Xixi Wang, Hao Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric video offers scalable manipulation data for embodied AI, yet recovering metric 3D hand trajectories remains challenging due to severe object occlusion and frequent out-of-sight gaps. Existing single-frame and windowed temporal regressors fail when hand shortly leaves the frame, while recent video diffusion models (VDMs) rely on heavy, stochastic multi-step sampling as pixel-space renderers. We instead repurpose VDM into a deterministic geometry encoder. A single forward pass over the clean latent exposes scene content beyond current observations, including occluded and out-of-sight hands. We introduce DreamHand, an offline clip-level framework that extracts features via a Deterministic Clean-Latent Encoder and decodes them with a Bidirectional Spatiotemporal Decoder. DreamHand recovers continuous bimanual trajectories with metric placement and no external detector, while a Ray-Based Camera Solver supports a second configuration that needs no test-time camera intrinsics. Across five egocentric benchmarks, DreamHand sets a new state of the art, cutting MPJPE-p by 30% on occlusion-heavy ARCTIC and 40% on HOT3D. These gains reach 46%-61% once out-of-sight hands are included in the evaluation, offering a scalable path from everyday human video to robot manipulation data.

---


### 152. [Inter-X++: A Comprehensive Benchmark for Multimodal Human-Human Interaction Analysis](https://arxiv.org/abs/2608.20312)

**<font color=#1a73e8>作者：</font>** Liang Xu, Chengqun Yang, Zili Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The capability to perceive and synthesize human-human interactions is fundamental to developing intelligent digital human systems. However, existing datasets and modeling approaches are fundamentally constrained by low-fidelity kinematics, the omission of dexterous hand gestures and a severe lack of rich multimodal annotations. Furthermore, fragmented interaction representations and inconsistent evaluation protocols also impede fair and rigorous benchmarking. To systematically address these bottlenecks, we present Inter-X++, a comprehensive and large-scale benchmark designed to empower versatile HHI analysis. Captured via a novel hybrid motion capture system, Inter-X++ provides 11,388 high-fidelity interaction sequences and over 8.1M frames, featuring precise whole-body movements and detailed finger articulations. Meanwhile, we enrich the data foundation with multifaceted annotations, including hierarchical fine-grained textual descriptions, interaction categories, causal interaction orders, the relationship and personality of the subjects, as well as vertex-level contact maps and physically regularized constraints. Leveraging these elaborate annotations, we formulate a unified testing ground comprising four categories of downstream tasks that symmetrically span both generative and perceptive paradigms. To eliminate benchmarking ambiguities, we systematically standardize the interaction representations and evaluation protocols. Finally, we go beyond dataset construction to propose OpenHHI, a single and unified HHI representation and modeling framework that jointly optimizes interaction reconstruction and semantic understanding. Extensive experiments reveal that OpenHHI achieves state-of-the-art performance on both generation and perception tasks. This definitively proves that our unified representation successfully bridges interaction understanding and generation simultaneously.

---


### 153. [A comparison between ceiling-mounted FMCW, IR-UWB and Wi-Fi radar for in-bedroom human activity monitoring and sleep interruption detection](https://arxiv.org/abs/2608.20322)

**<font color=#1a73e8>作者：</font>** Anton Lambrecht, Reda El Hail, Xianjun Jiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite their growing importance for contact-free radio frequency (RF) based healthcare monitoring, different radio technologies such as frequency-modulated continuous wave (FMCW) radar, impulse radio ultra-wideband (IR-UWB), and Wi-Fi sensing are rarely compared under identical deployment conditions, as existing studies typically differ in hardware, datasets, and evaluation methodologies. In addition, the performance of ceiling-mounted radars, despite their practical deployment and cost advantages in healthcare environments, remain underexplored. Therefore, this paper presents a controlled comparison and analysis of ceiling-mounted FMCW, IR-UWB, and Wi-Fi sensing using synchronized recordings from 20 participants across six room layouts. All technologies are evaluated with the same convolutional neural network (CNN) on both a fine-grained 10-class human activity recognition (HAR) task and a coarse 4-class sleep monitoring task. IR-UWB achieves the highest cross-subject activity recognition performance (89.0% macro F1), while FMCW generalizes best to unseen room layouts (83.8% macro F1). For sleep monitoring, all technologies exceed 92% macro F1 in unseen environments. The results reveal a fundamental trade-off between recognition performance and environmental robustness, which can be explained through differences in range resolution, antenna diversity, Doppler resolution, and spatial information retention. These findings provide practical guidelines for the design of healthcare-oriented RF sensing systems.

---


### 154. [G-CARL: Grounded Checklist-Aligned Reward Learning for Patient-Oriented Medical Report Interpretation](https://arxiv.org/abs/2608.20331)

**<font color=#1a73e8>作者：</font>** Shiao Xie, Siyu Chen, Jianwei Lv 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalized interpretation of medical reports has emerged as an increasingly important need among patients. Addressing this need requires both evidence-grounded medical factuality and context-dependent patient communication, yet existing medical vision-language tasks do not adequately capture these dual requirements. To bridge this gap, we introduce Patient-oriented Medical Report Interpretation (PMRI), a novel open-ended multimodal generation task that requires models to explain medical reports in accurate and accessible language based on a user's query and dialogue history. These two objectives differ fundamentally in their verifiability, yet remain tightly coupled, making them difficult to optimize jointly under conventional supervised fine-tuning and holistic reinforcement learning paradigms. To address this challenge, we propose G-CARL, a grounded, checklist-aligned reinforcement learning framework that combines multi-source retrieval for atomic claim verification with context-aware, instance-specific weighted checklists for response coverage, providing structured supervision for factuality, user-demand satisfaction, and expression quality without constraining response diversity. We further construct MMedReport, a real-world PMRI benchmark, along with a clinician-designed three-dimensional evaluation protocol. Extensive experiments demonstrate that G-CARL consistently outperforms existing post-training baselines in overall quality, claim-level precision, and checklist recall. Pairwise preference evaluation by clinicians further confirms that G-CARL produces interpretations that are more accurate and better aligned with patient needs.

---


### 155. [4DAnyone: Create Anyone in 4D from a Casual Monocular Video](https://arxiv.org/abs/2608.20335)

**<font color=#1a73e8>作者：</font>** Yudong Jin, Tao Xie, Qihang Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present 4DAnyone, a framework for reconstructing 4D humans from an uncalibrated monocular video by generating reconstruction-grade multiview-consistent videos and lifting them into 4D Gaussian Splatting (4DGS). Existing camera-controlled video diffusion models synthesize plausible novel-view videos but fail to maintain consistency when scaled to the tens of target views required for 4DGS reconstruction. We identify this failure as a bounded-attention-context problem: when target views exceed the capacity of a single DiT forward pass, they must be split into groups, exposing two coupled bottlenecks. On the reference-context side, conditioning on all previously generated views grows as $O(N)$, weakening cross-view appearance guidance. On the target-context side, disjoint groups cannot directly exchange information, causing global structural drift. 4DAnyone addresses both bottlenecks with two complementary designs: Reference Context Packing (RCP) compresses growing reference views into a fixed-length mixed-resolution context with $O(1)$ reference-context complexity, while Target Context Routing (TCR) rotates target-view groupings during denoising to share context across groups at high-noise steps and stabilize details at low-noise steps. We further build the MVGameHuman dataset using our in-house game engine and combine it with light-stage and in-the-wild video datasets for training. Experiments on DNA-Rendering and DyMVHumans show that 4DAnyone outperforms prior methods in both novel-view video quality and downstream 4DGS reconstruction, with robust in-the-wild generalization. See our project page for video results and source code: this https URL.

---


> [!TIP]
> 当前位于：**151-155**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-155**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
