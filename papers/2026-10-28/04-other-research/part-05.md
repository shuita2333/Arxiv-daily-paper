# 📦 其他研究 | 2026年10月28日

> 本类共 **446** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-446](./part-09.md)

---

### 201. [BoundedGS: Memory-Efficient High-Resolution Training for 3D Gaussian Splatting](https://arxiv.org/abs/2610.34233)

**<font color=#1a73e8>作者：</font>** Xiaobin Deng, Changyu Diao, Min Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution 3D Gaussian Splatting training increases pixel and Gaussian-tile intersection counts, expanding rasterization caches that coexist with projection and gradient state at peak memory. A complete-view update aggregates gradients across the view; each region's forward and backward caches can be released after its contribution is collected. BoundedGS separates rasterization and projection backward passes and bounds the active local rasterization working set according to its measured load. Candidate-indexed projection and compact gradient storage address the view-level peaks exposed by this change, while CPU-assisted structure rebuilding and bounded image supply manage resources outside rendering. In a resolution sweep at a fixed count of about 6M Gaussians, the measured rendering working set stays within 1.073-1.077 GiB from 1K to 16K; at 11K, a warm pass takes 19.79 seconds versus 21.76 for full-frame execution. Across five native 5K outdoor scenes, full training reduces the mean rendering working set from 9.97 to 1.76 GiB (82.3%), retains similar reconstruction quality, and shortens training time from 36.7 to 33.9 minutes.
Project page: this https URL

---


### 202. [ParetoGS: High-Quality Continuous-Budget 3D Gaussian Splatting with Sparse Adapted Anchors](https://arxiv.org/abs/2610.34235)

**<font color=#1a73e8>作者：</font>** Xiaobin Deng, Changyu Diao, Min Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scalable 3D Gaussian Splatting allows one scene representation to serve different Gaussian-count budgets, yet its quality-budget curve may lag behind models optimized separately for each budget. Reducing the number of Gaussians changes both the selected members and the reconstruction tasks carried by the survivors; parameters inherited from a high-budget model may fit a low-budget representation poorly. We propose ParetoGS, which describes member changes and parameter evolution with a small set of adapted budget anchors and decodes intermediate budgets without separate optimization at every requested count. ParetoGS alternates pruning and fixed-member adaptation to build nested anchors with persistent identities, and encodes their parameter changes relative to the full model in a compact residual atlas. At decoding, it interpolates the states of shared members and gradually introduces the rendering contributions of new members, connecting sparse anchors into a continuous-budget representation. Across 13 scenes, ParetoGS attains better average PSNR, SSIM, and LPIPS with fewer Gaussians than the compared prefix methods at 10% of each method's own full model. From a shared full model, it also outperforms FlexGS-imp at its trained 1%, 5%, and 10% budgets and NanoGS-imp at the 1% and 0.1% budgets. On Garden, its non-anchor quality approaches an empirical reference from independently optimized GNS models at higher retention ratios and exceeds it at some lower-budget points. Across 13 scenes, encoding reduces mean additional state from 390.0 to 85.7 MB with an average PSNR change of 0.01 dB.
Project page: this https URL

---


### 203. [$Δτ$-Bench: Pushing Agents Toward a Moving Capability](https://arxiv.org/abs/2610.34238)

**<font color=#1a73e8>作者：</font>** Shuofei Qiao, Xuanguang Pan, Yijun Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce $\Delta\tau$-Bench, an executable agent benchmark that models the structural evolution of large tool ecosystems. In $\Delta\tau$-Bench, independently evolving services continually reshape how tasks can be accomplished: familiar tools may disappear or be replaced, while more efficient alternatives emerge amid overlapping functionality and noisy documentation. Against this moving capability frontier, we evaluate whether agents can proactively discover efficient tool-use paths and promptly revise their accumulated procedural knowledge, bringing together demands that existing benchmarks fail to examine. $\Delta\tau$-Bench comprises 1,588 validated multi-turn tasks across 42 domains and six successive ecosystem states generated through capability-preserving transformations. Our evaluation shows that even the strongest evaluated model or harness achieves only 42.3% task success, while initial gains from existing skill-learning methods can not consistently translate into better adaptation as the ecosystem evolves. These findings motivate Steward, an ecosystem manager that jointly manages tools and procedural knowledge through incremental skill maintenance and dynamic provisioning during task execution. Experiments show that Steward sustains higher task success across ecosystem changes with lower skill-maintenance overhead, while improving both recovery from disrupted workflows and adoption of more efficient alternatives.

---


### 204. [Alignment via Generalization](https://arxiv.org/abs/2610.34242)

**<font color=#1a73e8>作者：</font>** Shai Shalev-Shwartz, Amnon Shashua  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI systems can become better at achieving the goals we give them without becoming better at doing what we actually want. Studying this alignment problem rigorously requires a framework connecting measurable performance to intended behavior. We propose Aligned-PAC learning, whose central idea is to reduce alignment to generalization: does success on the requirements used for training extend to requirements the system has not encountered? Rather than express our entire intention through a single training objective, we represent its different aspects through a collection of specific requirements. This perspective already yields strong theoretical results. We show how independent evaluation can provide rigorous evidence of alignment across the represented requirements, and establish how much evaluation is needed. We also develop an optimization method that, under explicit assumptions, combines learned models to satisfy the training requirements. The framework does not solve alignment in full: choosing requirements that faithfully capture our intentions, and understanding when learning will generalize to unseen requirements, remain open challenges. It provides a foundation for making these questions precise and studying them with the tools of learning theory.

---


### 205. [RacerGS: Residual-Autoregressive Context for 3D Gaussian Splatting Compression](https://arxiv.org/abs/2610.34263)

**<font color=#1a73e8>作者：</font>** Wenqing Wang, Huimin Zeng, Yun Fu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has emerged as a promising approach for fast, high-quality novel-view rendering. However, its large parameter size remains a bottleneck for storage and transmission. We propose RacerGS, a compact 3DGS compression framework that achieves scene reconstruction at significantly reduced storage sizes with preserved fidelity. To obtain compact and spatially coherent features, we design a hash projection model that projects the anchor hash encodings into compact context features. Additionally, we introduce a FiLM-modulated autoregressive GRU context model that utilizes causal dependencies among anchor feature groups and uses recurrent hidden states to refine entropy-model parameters, improving bitrate efficiency. Furthermore, we adaptively entropy-code quantized anchor-attribute residuals relative to their context-predicted means, leveraging spatial consistency to reduce symbol entropy. Overall, RacerGS achieves more than 150x compression over vanilla 3DGS and 28x over Scaffold-GS, while providing comparable rendering quality. Extensive experiments across five datasets demonstrate that RacerGS outperforms prior 3DGS compression methods in both storage reduction and rate-distortion performance.

---


### 206. [Robust Single-Parameter Point Cloud Registration using Truncated Lp Functions](https://arxiv.org/abs/2610.34271)

**<font color=#1a73e8>作者：</font>** Seong Hun Lee, Patrick Vandewalle, Javier Civera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a novel method for robust point cloud registration with only one tunable parameter. Our method, dubbed TLP, uses truncated $L_p$ functions with different values of $p$ to assign priority scores to correspondences, select the hypothesis, and refine the final model. By leveraging the robustness of truncated functions, TLP effectively handles the high outlier rates commonly encountered in real-world 3D feature matching. We also exploit GPU parallelization to evaluate hypotheses efficiently, enabling registration from thousands of correspondences in under a second on average. With only one tunable parameter, our method offers greater practicality than multi-parameter methods that require dataset-specific tuning of several parameters. Evaluations on public benchmark datasets demonstrate that TLP achieves higher accuracy than state-of-the-art single-parameter methods. Furthermore, it outperforms two widely used multi-parameter methods on three of the four evaluated datasets while maintaining competitive runtime.

---


### 207. [EditDistill: Is It Possible to Guide Video Editing with Image Editing?](https://arxiv.org/abs/2610.34303)

**<font color=#1a73e8>作者：</font>** Guojun Lei, Hong Li, Hongbing Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in image editing have enabled fine-grained and highly controllable visual modifications. However, achieving similar levels of controllability in video editing remains an open challenge, particularly for precise local edits, dynamic temporal effects, and consistent lighting across this http URL this paper, we propose EditDistill, a framework that distills image-level visual transformations from edits to guide video this http URL, given a source video and an edit prompt, we first generate an edited version of the initial video frame using an off-the-shelf image editing model. We then distill the visual transformation of this original-edited image pair into a compact representation termed an edit this http URL descriptor is injected into a video diffusion model through our lightweight fusion module, which steers the denoising process toward the desired edit. To align the video trajectory with the demonstrated image edit while preserving motion and layout, we train with edit-descriptor alignment and DINO structural consistency losses, and derive an equivalent inference-time guidance formulation under flow this http URL experiments demonstrate that our method achieves strong performance on standard benchmarks and produces high-quality video editing results across diverse scenarios. For more details and videos, please refer to the anonymous webpage: this https URL.

---


### 208. [Real-Time Conveyor Belt Defect Detection via Edge TPU-Accelerated YOLOv11 on Raspberry Pi 5](https://arxiv.org/abs/2610.34304)

**<font color=#1a73e8>作者：</font>** Muhammad Nur Bijak Bestari, Mulki Indana Zulfa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conveyor belts are vital arteries in continuous bulk material handling, particularly in heavy process industries such as cement manufacturing. Undetected structural anomalies (longitudinal tears, holes, degraded patch repairs, and impact punctures) cause catastrophic belt snapping, costly downtime, and severe safety hazards. While deep learning offers high accuracy, existing models rely on power-hungry workstation GPUs, hindering practical deployment at remote industrial edge points. In this paper, we propose, implement, and validate an end-to-end, low-power edge AI vision system for real-time conveyor belt defect detection deployed on a Raspberry Pi 5 accelerated by a Google Coral Edge TPU coprocessor. The system leverages an optimized YOLOv11 nano (YOLOv11n) architecture trained on a multi-source industrial corpus exceeding 3,000 augmented samples from an operational cement plant in West Java, open-source datasets, and automated captures. The model undergoes post-training full integer quantization (INT8) compiled for systolic tensor execution. Experimental results demonstrate robust detection capability, achieving precision of 0.742, recall of 0.730, and mAP@0.5 of 0.764 across four defect classes. Deployed on-site in an IP-rated enclosure interfaced with an RTSP PoE industrial camera, the system achieves stable throughput of 30-40 FPS at 320x320 resolution with an end-to-end latency of 70-90 ms. Operational profiling under harsh clinker dust confirms thermal equilibrium at 55 +/- 5 deg C on the host CPU and ~65 deg C on the Edge TPU with zero frame loss. This demonstrates that edge AI bridges the gap between high-accuracy computer vision and cost-effective predictive maintenance in continuous manufacturing.

---


### 209. [Learning Discriminative Prototypes via Boundary Repulsion MixUp for Object Re-Identification](https://arxiv.org/abs/2610.34305)

**<font color=#1a73e8>作者：</font>** Athena Psalta, Vasileios Tsironis, Konstantinos Karantzalos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object re-identification requires embeddings that are robust to intra-class variation in viewpoint, illumination, and occlusion, yet preserve sharp separation between visually similar identities. The hardest errors arise precisely where confusable identities meet, a region that pairwise losses shape only implicitly. We present PBR-ReID, a prototype-based framework that makes this inter-class geometry an explicit learning target. Each identity is represented by a learnable prototype jointly optimized with a DiNOv3 backbone and the resulting prototype similarity matrix reveals, at every training step, which identities are most confusable. On this signal we build Boundary Repulsion MixUp (BRM), a geometry-aware regularizer that converts standard MixUp's weakness into a discriminative signal. Rather than interpolating samples across confusable identities, which blurs the boundaries that matter most, BRM constructs an explicit boundary proxy between each confusable pair and repels their features away from it, converting boundary ambiguity into a discriminative signal. We adopt a two-stage training protocol consisting of a prototype warmup phase followed by EMA-stabilized joint fine-tuning. Extensive experiments on person and vehicle ReID benchmarks demonstrate strong performance, with thorough ablations confirming each component's contribution. Code is available at this https URL.

---


### 210. [Birth, Death and Diff: Insertion-Based Sequence Generation with Corrections](https://arxiv.org/abs/2610.34310)

**<font color=#1a73e8>作者：</font>** Durga Prasad Maram, Dhruvesh Patel, Tahira Naseem 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Insertion-based masked diffusion models enable flexible-length, parallel generation by interleaving mask insertion with token unmasking. However, because their generation decisions are irreversible, aggressive parallel decoding can introduce errors that subsequent steps cannot correct, necessitating conservative decoding with more forward passes (NFEs). Moreover, they exhibit higher entropy than standard MDMs because they marginalize over multiple alignments during training and therefore require even more conservative decoding in the absence of a correction mechanism. To address this limitation, we introduce ${\delta}$MDM, which makes intermediate generations revisable by equipping an insertion-based model with substitution and deletion operations. During training, we expose the model to errors caused by aggressive unmasking and insertion, teaching it to correct its own mistakes. At inference time, we interleave insertion and unmasking with correction steps that can revise previously unmasked tokens and remove unnecessary masks. This mechanism makes aggressive decoding practical, improving both generation speed and quality. ${\delta}$MDM Pareto-dominates FlexMDM, a vanilla insertion-based MDM, on the speed--quality trade-off. On high-diversity unconditional text generation on OpenWebText, it halves the generative perplexity relative to FlexMDM at the highest inference budget. It also achieves lower generative perplexity at all inference budgets compared to MDM trained from scratch with variable-length padded sequences. On low-diversity conditional text generation on TinyGSM, it matches FlexMDM accuracy with half as many NFEs.

---


### 211. [TopX: Text-to-Motion for Unseen Skeletons from the Skeleton File Alone](https://arxiv.org/abs/2610.34321)

**<font color=#1a73e8>作者：</font>** Tengjiao Sun, Pengcheng Fang, Xiaoyu Zhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-motion models generate for the skeletons they were trained on, while a new character arrives as a skeleton file and nothing else. We study text-to-motion for skeletons that no training clip has used, with no clips of the character, no template, no retargeting and no fine-tuning. We present TopX, a 73M-parameter flow-matching transformer that generates joint rotations and a root trajectory for any kinematic tree from its tree, rest pose and joint names. Motion is normalised by the rest pose and the size of the skeleton, and the rest pose enters as a world-frame descriptor that does not depend on how the rig's author oriented each joint, with rest conventions randomised in training. Attention is factorised over the joints and the frames of a motion and carries a spatial--temporal encoding designed for skeleton graphs of any topology: queries and keys are rotated across joints by a heat-kernel coordinate of the skeleton graph, which is defined for every tree and does not change with the order of its joints or the eigenbasis of its Laplacian, and across frames by a rotary encoding of frame order. To measure what this buys, we build SkelShift: four motion corpora under one codec, 143,334 captioned clips on skeletons of 4 to 142 joints, from which 4,232 clips on 2,043 skeletons are held out by clip, rig, tree class or species and organised along topology, joint count, body plan, species and rig source, and scored by motion quality: Fréchet distances on public kinetic features and on kinematic descriptors, foot skating and ground contact. Against UniMate trained on the same clips, on test rigs without a training clip, TopX lowers the descriptor FID from 5.73 to 4.58 when UniMate's guidance is tuned for the kinetic FID, and the kinetic FID from 1.48 to 0.55 when it is tuned for the descriptor FID, also on motions no training skeleton performs; fewer of its frames sink below the ground.

---


### 212. [Xing USP: A Cross-Family Semantic Contract for Information Extraction and Intent-Slot Parsing](https://arxiv.org/abs/2610.34343)

**<font color=#1a73e8>作者：</font>** Zhongqiu Li, Boyang Wang, Ruiyu Fang 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured semantic parsing is typically judged by whether the correct category is assigned, which leaves value recovery and instance-level associations unexamined: a system may recognize an event yet bind an argument to the wrong instance, or identify an intent yet supply an incorrect slot value. We present USP, a cross-family semantic contract that represents categories, fields, values, and instance associations through a common interface for named-entity recognition, relation extraction, event extraction, and intent-slot parsing. The contract is paired with five diagnostic matching views---category agreement, field recognition, field-value pairing, instance-bound assignment, and complete-instance recovery---that ask distinct questions about the same output. Using this contract, we normalize 61 datasets into a unified corpus with shared schemas, prompts, and matching rules, and compare six models on a fixed test subset. Our fine-tuned Xing4.0-29B-Intent attains 57.70 task-balanced Field-Value Micro-F1 (equally weighted across the four task families) and ranks first in every family and on all five views; its margin over the strongest alternative widens from 2.93 points for category matching to 20.73 points for complete-instance matching. This widening gap shows that category agreement alone understates structural deficits. USP thus offers the community a shared representation, a normalized 61-dataset corpus, and a diagnostic evaluation protocol that make structural agreement measurable and comparable across extraction and intent-slot tasks.

---


### 213. [Birth-Death Structural Learning for 3D Gaussian Splatting](https://arxiv.org/abs/2610.34344)

**<font color=#1a73e8>作者：</font>** Quan Tran Hong, Long Nguyen-Chi, Binh T. Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has become a standard representation for real-time novel-view synthesis. Yet, its quality-efficiency trade-off still relies heavily on adaptive density control. Existing cloning, splitting, and pruning rules use proxy signals, such as position gradients, opacity, and image-space error. Although effective in practice, these signals do not directly answer the structural question behind density control: where should new Gaussians be allocated to reduce the multi-view reconstruction loss, and which existing primitives can be pruned with minimal penalty. To address this, we propose first-variation birth-death control for 3DGS, a principled approach that replaces heuristic structural decisions with a variational score derived from the reconstruction loss. At each structural update, we freeze the current Gaussian population, attach auxiliary mass coordinates to each primitive, and differentiate the multiview loss with respect to these coordinates. We demonstrate that this score is a coordinate of the first variation of the Splat Regression Model, giving a rigorous local descent surrogate for birth-death moves: high-score Gaussians are selected as birth sites, while low-score, low-opacity Gaussians are selected for removal. Across standard 3DGS benchmarks, integrating this score into 3DGS-MCMC yields state-of-the-art reconstruction quality and outperforms existing methods, delivering the most significant gains under tight Gaussian budgets. Ultimately, our work provides compelling evidence that gradient-based variational metrics offer a principled alternative to proxy heuristics in 3DGS.

---


### 214. [Spatially-Aware Self-Organizing Graph Autoencoders via Localized Hebbian Learning](https://arxiv.org/abs/2610.34346)

**<font color=#1a73e8>作者：</font>** Robin Koç, Hazal Moğultay Özcan, Fatoş T. Yarman Vural  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional autoencoders rely on static network architectures to learn latent representations. Recently we suggested a dynamic architecture inspired by Hebbian plasticity, enabling topological self-organization among convolutional feature maps (R. Koç et al., Proceedings of the SIU, 2026). Early implementations of this paradigm infer relationships among feature maps using global average pooling and model their interactions through scalar-valued connections. This approach falls short to fully exploit the underlying spatial information, embedded in input images. Furthermore, abrupt transitions between different loss functions and training dynamics can introduce representation shocks, leading to unstable feature learning. In this paper, we introduce a Spatially-Aware Self-Organizing Graph Autoencoder (S-LooM) to address these structural bottlenecks. By using spatial cross-correlation, and spatial kernels, S-LooM establishes dynamic connections among feature maps. We replace static scalar message passing of autoencoders with learnable spatial kernels and eliminate high-frequency deconvolutional artifacts observed in decoders using nearest-neighbor upsampling. Via a soft-blending training curriculum, the latent topology aligns smoothly during training. Our experiments show that S-LooM yields a more stable topology, compared to the state of the art dynamic architectures. Meaning, the graph structure that emerge has more resistance to feature entanglement and noise. It forms functional communities responsible for visual attributes, such as illumination, shape and texture even under high connection densities.

---


### 215. [A Computationally Efficient Non-Interpolation Virtual Trellis Approach for Mammogram Gradient-based Patterns Analysis](https://arxiv.org/abs/2610.34352)

**<font color=#1a73e8>作者：</font>** Shahid Rasheed, Muhammad Rashid, Seifedine Kadry 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feature analysis is a crucial step in medical image analysis, particularly in breast cancer classification. Traditional image analysis methods often struggle with optimal patterns along the diagonal axis, computational efficiency and feature buffer storage. Different classical operators require high-efficiency hardware for the complex operations, such as image convolution and gradient analysis, which are used for processing complex machine learning models for training and test operations. Here, in this research, we introduce a non-interpolation virtual trellis-based (NVHT) operator that utilizes a filter kernel over the same square image without transformation to a hexagonal trellis. This proposed method is very efficient in reducing computational and storage costs. The proposed operator is used for improved feature extraction efficiency and accuracy in disease classification. This method outperforms conventional approaches by leveraging a hexagonal pixel representation while maintaining high sensitivity in different directions with less storage.

---


### 216. [SEEK: Skill Extraction with Evolving Knowledge against Frontier Science Agents](https://arxiv.org/abs/2610.34365)

**<font color=#1a73e8>作者：</font>** Cheng Gui, Xiang Zheng, Xingjun Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Science agents increasingly package domain expertise as reusable skills that plan analyses, select tools, and execute workflows. This modularity creates a confidentiality risk: the interactions that deliver a skill's capability can also reveal the skill itself. We build an extensible benchmark of 40 protected skills across eight open- and closed-source science-agent platforms, comparing direct, fixed-strategy, and bandit-guided iterative probing under reference-based and reference-free evaluation. Leakage is pervasive: all eight platforms (100%) leak at least one protected skill, and four reach 100% attack success under a single direct request. To stress-test platforms that resist simple probing, we propose SEEK (Skill Extraction with Evolving Knowledge), a black-box, self-evolving red-teaming agent that consolidates response-derived evidence in persistent memory and evolves reusable attack skills, using only user-visible responses. On 12 skills from SpatialAgent and Biomni, SEEK achieves 100% attack success while reducing the mean first-success round by 31.8% and 38.2% relative to bandit-guided probing. Against a confidentiality policy that blocks all three benchmark protocols, SEEK still extracts one of six protected skills. These findings show that current science agents do not reliably protect their skills and that defenses must be evaluated against adaptive, multi-turn attackers.

---


### 217. [Whether or Where? Tail Calibration Signals Finite-Budget Reward Hacking in Best-of-N Selection](https://arxiv.org/abs/2610.34375)

**<font color=#1a73e8>作者：</font>** Cheng Gui, Yihua Shao, Lei Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Best-of-N (BoN) inference returns the candidate with the highest proxy reward, so a larger $N$ tests the proxy's extreme tail more than its average ranking quality. We show that the exact BoN value is a Beta-weighted integral of conditional true reward over within-prompt score quantiles. It follows that BoN depends on scores only through their ranks. It also follows that BoN can decline only if the calibration curve in the tail turns downward, and the budget where the decline appears depends on where that turn lies. Under a bounded additive model, the error tail sets the limit: Gaussian errors keep improving, Laplace errors reach a plateau, and heavy-tailed errors return to the prior mean. When error variance is largest at low true reward, even Gaussian noise can push BoN below random selection. Synthetic phase maps agree with this taxonomy. On real candidate pools spanning several verifiable domains, base policies, and learned reward models, tail failures are rare and all occur in code generation. A held-out tail calibration statistic reliably predicts where a cross-fitted budget cap helps. It does about as well as rank accuracy, and the cap is competitive with a Soft-BoN baseline. Tail calibration therefore does not replace ranking metrics. It is an audit that is unchanged by any monotone rescaling of the reward scores and shows which budgets are at risk.

---


### 218. [AndroidFlux: Evaluating and Reward Modeling Failure Recovery Capabilities in Mobile Use Multimodal Agents](https://arxiv.org/abs/2610.34384)

**<font color=#1a73e8>作者：</font>** Gyubeum Lim, Yemo Koo, Ghunwoo Jang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mobile-use multimodal agents are typically evaluated by task success from a clean initial state, which does not isolate their ability to recover from intermediate errors. Because mobile environments change dynamically, a general mobile-use agent must complete tasks robustly even from unexpected states and in unseen environments. This requires knowing when and where an agent makes errors, and whether it can recover from errors and subsequent states. To evaluate this capability, we introduce AndroidFlux, a failure-recovery benchmark built on AndroidWorld. AndroidFlux restores recorded trajectories to controlled checkpoints before, at, and after the first recoverable error, so that different agents continue from the same device state and history. On these checkpoints, a complementary reward-modeling benchmark evaluates recovery-action preferences using downstream rollout outcomes. We further release an offline reinforcement learning (RL) dataset that improves both error recovery and overall task success. Our evaluations show that recovery performance only partially correlates with clean-start success, and that explicit reasoning helps only models trained with GUI-domain specific RL.

---


### 219. [Outcome-Aware Agents: When Does Causal Structure Help a Forward Model Foresee the Consequences of Actions?](https://arxiv.org/abs/2610.34385)

**<font color=#1a73e8>作者：</font>** Mallesh Madapathi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agents that act on real systems should predict what their actions will cause before acting. We study when causal structure helps a learned forward model do this, using a planner that rejects candidate actions whose simulated multi-step outcome is unsafe, in synthetic structural causal models where the true consequences are known. We compare the Action-Conditioned Latent Structural Causal Model (AC-LSCM: per-factor mechanisms over a learned sparse graph, actions as do-interventions) with three unstructured forward models on seven random graphs with 10 or 20 variables, a task configured by a fixed rule, and two controls: a do-wrapper that gives every model the same action semantics, and counterfactual data given to all models or to none. When its factors are the observed variables, AC-LSCM recovers the true graph exactly on every 10-variable graph and has lower three-step prediction error than every baseline in all 396 paired comparisons. Its excess safety violations over an oracle are 0.25 of the no-model level on 10-variable graphs (best baseline 0.31) and 0.41 on 20-variable graphs (0.53), and its margin is largest for two-variable actions never seen in training (0.18 versus 0.28). With learned latent factors the same model is worse than the baselines; the choice of factors matters more than the explicit do-operator or counterfactual data, and every planner stays far from the oracle. This version corrects an earlier one, whose model learned an empty graph and whose headline 36x safety improvement came from a task that tested only extrapolation of action values; we withdraw that claim. Code and all per-seed results are released.

---


### 220. [No Cones, No Duals: A Fast and Scalable Solver for NRSfM](https://arxiv.org/abs/2610.34403)

**<font color=#1a73e8>作者：</font>** Suryansh Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-rigid structure from motion (NRSfM) aims to recover camera motion and time-varying 3D shape from tracked 2D image measurements. Recent high-performing methods show that shape-space factorization remains highly effective for this task. These methods often use costly solvers for two key steps. First, a semidefinite programming (SDP) cone solver to perform Euclidean correction. Next, an alternating direction method of multipliers (ADMM) solver to recover the low-rank shape. These steps often scale poorly to long sequences and dense point tracks. We propose a fast, scalable NRSfM solver that avoids these costly steps. For rotation estimation, we introduce a differentiable Euclidean correction that directly optimizes small factors for each sequence. A row-polar projection then maps each estimated camera block to the closest row-orthonormal matrix. For shape estimation, we introduce an unrolled spectral-proximal solver. It combines reprojection-gradient steps with weighted singular-value shrinkage in the reshuffled shape domain. This solver further uses FISTA-style restart and continuation. The spectral shrinkage operator itself is classical, but we embed it in a fixed differentiable solver, while preserving NRSfM's geometric constraints. The proposed approach is category-agnostic, requires no external training data, and maps naturally to modern accelerator-friendly linear algebra primitives. Across sparse, dense, noisy, missing-data, and long-sequence benchmarks, our solver achieves substantial speedups with competitive reconstruction accuracy, including 7x-1000x runtime improvements on dense sequences with 28,887 tracked points.

---


### 221. [Maximum-Likelihood Decoding of Gabidulin Codes Is NP-Hard Even in Dimension One](https://arxiv.org/abs/2610.34404)

**<font color=#1a73e8>作者：</font>** Philippe Gaborit  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fix a prime power q. We prove that deciding whether a received word y in Fnqm lies at rank distance at most n-2 from the one-dimensional Gabidulin code {{\lambda.g : {\lambda} in Fqm } is NP-complete. Thus maximum-likelihood decoding of Gabidulin codes is NP-hard even for k = 1, an analogue of the Guruswami-Vardy theorem for Reed-Solomon codes. In the Hamming metric, by contrast, hardness at this radius requires the dimension to grow with the length, as in the Guruswami-Vardy theorem. The reduction is deterministic; consequently Rank Syndrome Decoding (RSD) and Rank Minimum Distance (RMD) for Fqm -linear codes are NP-complete under deterministic polynomial reductions, whereas the previously known reduction was randomized. The proof goes through a pivot problem that we introduce, Twisted Square Membership (TSM): given Fq-subspaces U, W in FqN , decide whether some non-zero a in U satisfies a^(q+1) in W . Quadratic systems in d unknowns are encoded into TSM, then TSM into Gabidulin decoding. The last step views the received word as an Fq-linear map and decoding at radius n - 2 as the search for an Fq-plane on which it acts as a scalar. With support U + {\tau} W in a cubic extension and map a + {\tau} b to a^(q^2) + {\tau} bq^q , two Frobenius twists force solution planes to encode the relation a^(q+1) in W . All constructions are explicit and polynomial, with N = O(qd^2 ), n less than N + d, and m = 3N .

---


### 222. [On Detection Reliability for Small Object Segmentation](https://arxiv.org/abs/2610.34432)

**<font color=#1a73e8>作者：</font>** Olivier Rukundo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study investigates whether predicted bounding boxes are reliable for determining where small-object segmentation should be performed without risking false negatives outside those boxes. The investigation leverages adenovirus particles as small objects, YOLO26x for detection, YO-LO26x-Sem for segmentation, and Mask R-CNN for both detection and segmentation. Segmenta-tion-model predictions were matched to ground-truth adenovirus masks or reference objects using their centroids, with ground-truth mask centroids preferred over ground-truth bounding-box centroids as references for matching. Matched predicted-mask centroids were considered as inside at least one detector-predicted bounding box or outside all such boxes, while ground-truth masks without matched predictions were recorded as having no matched segmentation. For the YOLO26 models, 34 reference objects (47.89%) had matched segmentation centroids inside at least one pre-dicted box, 8 (11.27%) had centroids outside all predicted boxes, and 29 (40.85%) had no matched predicted segmentation. For the Mask R-CNN model, the corresponding counts were 69 (97.18%), 0 (0.00%), and 2 (2.82%). These preliminary experiments demonstrated that restricting segmentation to detector-predicted bounding boxes risks excluding matched segmentation predictions outside those boxes, potentially introducing false negatives.

---


### 223. [Perceived Acceptability of Sensory Augmentation](https://arxiv.org/abs/2610.34451)

**<font color=#1a73e8>作者：</font>** Michel Witter, Alwin de Rooij, Michel van Dartel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Sensory augmentation (SA) can extend how people perceive and engage with public environments through the body, offering opportunities to support shared multimodal experiences between deaf and hearing visitors. Designing such systems requires understanding which combinations of tactile stimuli and body locations users perceive as acceptable. We examined the perceived acceptability of fictitious yet feasible SA configurations in a museum use-case. Using a modified technology acceptance model, we surveyed 307 deaf and hearing participants about tactile stimulus types and body locations. The results showed significant effects of stimulus type and body location on acceptance, but no interactions with hearing status. Participants generally preferred temperature-based stimuli, subtle movement, texture, and tickling over vibration, and distal over proximal body locations. These findings suggest that tactile SA design should be guided primarily by embodied and contextual factors rather than hearing status, informing future systems for shared multimodal experience in public cultural settings.

---


### 224. [Toward Neuroadaptive Communication Interfaces: A Framework for Personalized Speech and Language Support](https://arxiv.org/abs/2610.34457)

**<font color=#1a73e8>作者：</font>** Carlos Bruno, Luis Ricardo Santos  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Speech and language technologies have expanded access to communication, but the support they provide is often fixed. The same linguistic or visual aid may help one user and hinder another, or become less useful as task demands change. This project proposes a framework for adapting language presentation to individual abilities and ongoing interaction. It separates access to a message from the estimation of user needs and from the selection of support, including sentence segmentation, pictograms, and optional spoken output. Behavioral feedback provides the primary evidence for adaptation; electroencephalography is considered an additional, uncertainty-aware source of information rather than a direct measure of comprehension. We specify a staged evaluation comparing fixed, behavior-adaptive, and neuroadaptive interfaces. The central question is whether neural information improves comprehension and communication efficiency beyond a strong behavioral baseline.

---


### 225. [From Explaining to Enabling: Actionable Transparency in Algorithmic Insurance Pricing](https://arxiv.org/abs/2610.34459)

**<font color=#1a73e8>作者：</font>** Agathe Fernandes Machado, Fei Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) systems increasingly make consequential decisions about individuals, including credit, hiring, and insurance. Research on ML-driven insurance pricing has asked how the pricing mechanism itself can be made accountable. Yet it remains unclear how an individual policyholder's algorithmically determined premium should be explained to them. We argue that a useful explanation must be valid, actionable, and reliable. A valid recommendation lowers the premium according to the model. An actionable recommendation changes only characteristics the policyholder can control. A reliable recommendation has an actual outcome that is likely to meet the target, even in sparsely observed regions of the feature space where the model is uncertain. We formalize these three requirements as axioms and develop a method that turns an algorithmic premium into recommendations that meet them. The method meets the third requirement with a Conformal Prediction constraint, which screens out recommendations that the model is too uncertain about and thereby bounds the rate of unreliable recommendations. We apply four Counterfactual Explanation techniques to 57,832 real Florida flood-insurance claims and 98,058 synthetic driver-telematics policies. We adapt these techniques for insurance applications, so that their recommendations change only controllable characteristics and resemble policyholders observed in the data. In our illustrations, the constrained recommendations for high-risk policyholders are both more reliable and associated with larger predicted risk reductions than the unconstrained ones. These results suggest that insurers can give policyholders explanations that are both actionable and trustworthy. The work contributes to research on algorithmic accountability and offers implications for insurers and regulators.

---


### 226. [Task Relevance-Driven Prompt Expansion for Federated Continual Learning](https://arxiv.org/abs/2610.34461)

**<font color=#1a73e8>作者：</font>** Jiahua Dong, Wenqi Liang, Yang Cong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated continual learning (FCL) has attracted considerable interest by enabling local clients to continually acquire knowledge from new tasks. However, most FCL methods assume that the global server has prior knowledge of the arrival times and number of categories for new tasks, which is unrealistic in the real world. Furthermore, they neglect the importance of positive inter-task semantic relationships when learning new tasks and are significantly affected by irrelevant relationships from old tasks, thereby exacerbating catastrophic forgetting. To resolve the above challenges, we develop a novel Task Relevance-driven Prompt Expansion (TRPE) model. Specifically, to eliminate the reliance on prior knowledge of new tasks, we propose an out-of-distribution detector to identify the arrival of new tasks within local clients, along with a radius-adaptive DBSCAN to infer the quantity of categories in new tasks on the proxy server. Moreover, to explore positive inter-task relationships, we calculate the affinity between the original gradient for learning new task and its gradient orthogonal to the feature space of old tasks to evaluate semantic relevance between old and new tasks from a global perspective. Then, we use this global task relevance to determine the key-prompt pair for new tasks and identify highly related old tasks. After concatenating their prompts for training, we can leverage such positive inter-task relations to improve the continual learning of newly arriving tasks. To balance the learning of new tasks and the forgetting of old ones, a soft orthogonality constraint is applied to the local key and prompt gradients. Experiments spanning diverse datasets and backbones confirm the efficacy of our TRPE model.

---


### 227. [Finite-Sample Sensitivity of Kernel Metrics for Generative Evaluation](https://arxiv.org/abs/2610.34477)

**<font color=#1a73e8>作者：</font>** Tomasz Radzikowski, Mateusz Modrzejewski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kernel distances such as the Kernel Inception Distance (KID) and the Kernel Audio Distance (KAD) compare generated and reference samples in an embedding space, and model comparisons rest on their values. Each ships with one fixed kernel, and a reported value does not say which changes that kernel detects at the sample size used. We run each default as a permutation two-sample test on real embeddings of symbolic music, audio and images, comparing a sample with an independent sample changed by a mean shift, an isotropic contraction, or a rotation that keeps the mean and the covariance trace and is matched to the shift in transport distance. At 780 samples per side, both defaults rarely detect the rotations in five evaluation spaces, while they detect the shifts in every run. The median-bandwidth Gaussian kernel of KAD detects the contraction and regains power against rotations on image embeddings with an order of magnitude more samples. The cubic kernel of KID contains second- and third-moment information but misses the contraction in most runs, and our experiments do not establish a high-power rotation regime for it over the tested sample sizes. Narrower Gaussian bandwidths restore sensitivity in music and audio, an $\ell_1$ Laplace kernel does so for images, and aggregated tests combine both at nominal level. We recommend that a reported kernel distance state its sample budget and the changes its configuration detects at that budget.

---


### 228. [From Outranking Flow Scores to Linear Programs: Group Decision Making in PROMETHEE II](https://arxiv.org/abs/2610.34481)

**<font color=#1a73e8>作者：</font>** Alexandre Flachs, Yves De Smet  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study inverse and consensus analysis for PROMETHEE II ranking problems when the performance table is fixed. Existing approaches in PROMETHEE-based sensitivity and consensus analysis usually focus on deviations of criteria weights while treating preference functions as fixed. Nevertheless both sets of parameters jointly determine the outranking flow scores. We introduce a linear reparametrization of the PROMETHEE II net flow scores based on weighted preference increments over the observed differences of performances. This representation yields a linear expression of the net flows and clarifies how weights and preference functions interact. Building on this result, we derive linear optimization models for three settings: minimizing weight deviations while allowing preference functions to vary; minimizing deviations over the full set of preference parameters; and multiple decision-maker consensus analysis (with objectives based either on total deviation or on the maximal individual deviation to promote fairness). An illustrative example shows that allowing preference functions to vary can dramatically change the inverse-analysis conclusions obtained from weight-only models, and that the proposed group formulations distinguish efficient consensuses from fairer ones.

---


### 229. [Models Verify Sufficiency, Not Validity: Usable Falsehoods Evade the Checks that Gaps Trigger](https://arxiv.org/abs/2610.34488)

**<font color=#1a73e8>作者：</font>** Naveen Madiraju  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ask a model "how many settlements did the Normans control?" and it answers that the passage does not say. Tell it "given that the Normans controlled 12 settlements of 400 inhabitants, what is the total?" and it computes 4,800. Nothing was added to the passage; the unsupported fact merely became usable. Benchmarks for unanswerable questions are built almost entirely by omission, deleting the fact a question needs and scoring refusal, so they never probe this. Holding source support fixed and varying only whether an unsupported premise is usable, flagging drops 8-30 points and commitment to an answer rises 1.5-2.3x on GSM8K across four models spanning two families and 2B-26B; all 16 paired contrasts remain significant after Holm correction. Two further manipulations reproduce it, one also on SQuAD: a fact asserted rather than asked about, and a corrupted intermediate value rather than a removed one. Models articulate the exact gap they then ignore, stating that "there is no financial information provided" for an inert premise and silently adopting a fabricated price for the same item. We read these as one behaviour: whether a model checks depends substantially on whether usable material is present, even when source support is held fixed. Because the main design never instructs models to reject premises introduced in the question, adopting such a premise can also be read as conditional reasoning, and we delimit what the design does and does not show. In the judging seat the pattern differs: asked whether the answer follows, judges pass solutions with a required step deleted 78-99% of the time at every scale tested. A natural prompt-level mitigation lowers accuracy by 22 points without improving detection.

---


### 230. [Efficient Proof Generation for Lean Statements with Multiple Candidate Answers](https://arxiv.org/abs/2610.34490)

**<font color=#1a73e8>作者：</font>** Pengzhen Lin, Ke Zhang, Maziar Raissi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In formal systems such as Lean 4, efficiently finding answers to mathematical problems and generating verifiable proofs is an important task in automated mathematical reasoning. In the traditional way where an upstream solver provides multiple candidate answers, the common workflow requires searching for proofs for each candidate separately, incurring redundant computational cost. To this end, we propose a joint proof framework that integrates candidate answer selection, answer supplementation, and formal proof generation into a unified reasoning process. At its core is a trained prover that selects given or proposes new answers and generates a proof for at least one answer in a single call. Joint proof can also reuse generated proofs to check for faithfulness errors. For problems with a unique answer, if two distinct answers both obtain verifiable proofs under the same formal statement, this confirms the statement does not faithfully preserve the original problem semantics. On MATH-500, AMC 2023, and AIME 2024/2025/2026, our framework achieves the same formal proof success rate as per-candidate proof generation with about one sixth of the token cost, and identifies at least 6.1% of the formalized statements as unfaithful without requiring additional judges. Our model and code are available at this https URL.

---


### 231. [Approximate Unlearning in Prototype-based-classifiers](https://arxiv.org/abs/2610.34495)

**<font color=#1a73e8>作者：</font>** Sreejita Ghosh, Mohammad Mohammadi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The recent data and AI regulations and governance needs have highlighted the need for removing specific data even from models trained on or with them. While retraining the entire model is a theoretically trivial solution, it is computationally expensive, thereby motivating research in Machine Unlearning. This paper introduces a robust approximate unlearning technique for the family of prototype-based classifiers called Generalized Learning Vector Quantization, aimed at removal of effects of specified samples, either due to deletion request or due to them being identified as noisy or corrupt. We first show the impact of the different sizes of the forget set, as well as the characteristics of the data in this set, on the unlearned model. To address the sources of instabilities detected in this unlearning method we propose an adapted version of this technique, such that the unlearning is robust to the characteristics of the forget set. Thereafter using the intrinsic interpretability property of GLVQ and appropriate metrics defined in unlearning literature, we show the efficacy (approximately 0 deviation of parameters and performance of unlearned model relative to retrained model) and efficiency (6X for smallest dataset to 10^(5)X in the largest dataset) of the proposed unlearning techniques compared to naive retrained, on six benchmark datasets for tabular data recommended by literature. Although in this work we investigated only binary class problems, the proposed robust unlearning strategy can be readily applied for removing sample effects from any trained GLVQ model, i.e., it does not require any modification in the training scheme of GLVQ.

---


### 232. [Does the Voynich Manuscript Mean Anything? Calibrated Tests Find Little Trace of Language](https://arxiv.org/abs/2610.34499)

**<font color=#1a73e8>作者：</font>** Xin Zhang, Victor S. Sheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Voynich manuscript is a fifteenth-century book in a script that no one can read. One account holds that its text means nothing and that a scribe made it by copying his own words and changing them a little. The other holds that a real language lies hidden behind a cipher. We write each account as a program that fills the pages of the manuscript, fit every program with the same budget, and check it on statistics the fit never saw. The copying process of Timm and Schinner predicts these statistics far better than any cipher with one key. But ciphers that switch keys between the manuscript's two dialects, or that encode only the word classes of a real text, predict them equally well. Word statistics alone cannot decide. We look for a trace of language that needs no decipherment. In 28 texts in 16 languages the same word pairs keep sharing a line. The manuscript shows this pattern at half the strength of the weakest of these texts. A word code keeps the pattern above the manuscript unless its plaintext has a weak pattern or many words are miscopied. Solvers that decipher control texts find no readable text in the manuscript under a letter cipher, a word code or 28 codes with one letter, letter pair or syllable per word. Word codes of abbreviated Latin, the plaintext their fits prefer, show which word follows which more clearly than the manuscript unless two words in five are miscopied. One cipher remains possible, a nomenclator with a second key whose scribe miscopies more than half of the words, and our solvers cannot exclude it in 9 of 16 languages. Most of the structure a solver finds comes from how the end of one word shapes the start of the next, which reflects how tightly glyphs are bound to each other. Planted messages are found reliably only when they are long, each letter always becomes the same word and these words are adjacent, so other messages could hide.

---


### 233. [Best Policy Tracking in Reinforcement Learning](https://arxiv.org/abs/2610.34501)

**<font color=#1a73e8>作者：</font>** Judith Echevarrieta, Etor Arza, Aritz Pérez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning commonly exhibits non-monotonic performance dynamics in single-task settings. During learning, a sequence of policies is generated whose true performance is unknown and may oscillate significantly across iterations. Despite this well-known phenomenon, standard experimental practice typically reports either the final visited policy or the best among periodically evaluated ones, implicitly assuming that these selection criteria reliably approximate the best-performing policy visited throughout the entire sequence.
In this work, we present an empirical study on the implications of non-monotonicity for policy selection in single-task policy-based reinforcement learning. We introduce post-hoc diagnostic metrics to characterize performance degradation and assess the accuracy and efficiency of different selection criteria. These metrics allow us to evaluate commonly used selection strategies across standard continuous-control benchmarks using a well-established on-policy actor-critic method. Our results show that, in this representative experimental setting, widely adopted selection practices can deviate considerably from the best policy encountered during learning, leading to underperforming estimates and suboptimal use of computational resources. As an alternative, we recommend a validation-based policy selection strategy constrained by computational cost, which provides a more consistent and accurate approximation of the best visited policy while improving selection efficiency. Overall, our findings highlight policy selection as an underexplored factor in the evaluation protocols of reinforcement learning and motivate further study on explicit and standardized validation-based selection procedures.

---


### 234. [Ambiguous Fits: The Rashomon Effect and Challenges in Scaling Law Estimation](https://arxiv.org/abs/2610.34514)

**<font color=#1a73e8>作者：</font>** Bruno Mlodozeniec, Spencer Frei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating neural scaling laws involves an end-to-end pipeline: designing a scaling recipe, training models across scales, evaluating models on a target metric, and deploying an algorithm to fit a scaling law to the resulting data. This final fitting stage is often treated as routine: standard procedures minimize a non-convex fitting loss using local optimization from a grid of initializations, and return the best solution found. Yet such heuristic searches can fail in two distinct ways: they offer no guarantee of returning a nearly optimal solution, and they obscure whether fundamentally different parameter choices fit the data nearly as well. Indeed, we show that standard scaling law fitting is subject to a Rashomon effect (Breiman, 2001): the sublevel sets of near-minimizers correspond to broad parameter regions whose extrapolations diverge substantially at scale. We resolve these issues with a deterministic branch-and-bound algorithm that guarantees nearly optimal fitting loss and exhaustively maps the near-minimizers to the implied range of scaling curves.

---


### 235. [How Much Information Can We Fit inside a Transformer?](https://arxiv.org/abs/2610.34553)

**<font color=#1a73e8>作者：</font>** Amirhossein Basareh, Rishabh Sanjay, Daniel de Mello 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How efficiently can transformers store factual knowledge? The answer to this question has implications for both model design and understanding the limits of transformer-based systems. Prior studies observe a linear relationship between the number of facts memorized and the number of model parameters required, substantially worse than what theoretical analyses predict is achievable. We re-examine empirical scaling: through rigorous and systematic experiments, including extensive hyperparameter search via Bayesian optimization, we determine the smallest model that can perfectly memorize a given set of facts, and measure how this minimum size scales with the number of facts. On synthetic datasets of random, independent (subject, relation, object) triples---e.g., (Paris, capital_of, France) ---drawn at random with no exploitable structure, we find that memorization capacity, the size of the largest dataset that a model memorizes completely, grows exponentially with the transformer dimension. Equivalently, the minimum transformer dimension $d_{\min}$ required to memorize $N$ facts grows logarithmically in $N$. Across 11 dataset sizes spanning $N = 45$ to $49{,}920$, a lack-of-fit F-test does not reject the logarithmic fit (with an offset), but it does reject all other tested alternatives including power-law. Along the depth axis, however, at fixed width, the maximum memorizable dataset size grows sublinearly with the number of layers over the measured range. We further extend our exploration to structured data containing symmetric relations or two-hop composition. In this setting, we find that transformers exploit these regularities to further improve capacity. All code to reproduce our results is available at this https URL.

---


### 236. [CVM-Store: A Secure Storage System for Confidential Virtual Machines](https://arxiv.org/abs/2610.34560)

**<font color=#1a73e8>作者：</font>** Thore Sommer, Masanori Misono, Dimitrios Stavrakakis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Stateful cloud workloads require high-performance persistent storage when running on untrusted cloud infrastructure. Confidential Virtual Machines (CVMs) promise to protect these workloads through hardware-enforced memory encryption and isolation without requiring application changes. However, they protect only data in use; persistent storage lies outside the CVM trust boundary, exposing all stateful data to the cloud provider.
Extending the trust boundary to persistent storage presents inherent challenges. High-bandwidth workloads require near-raw NVMe throughput, yet the default kernel CVM I/O stacks are inadequate, and userspace I/O libraries are not designed with CVM use cases in mind. Access patterns and storage semantics vary between workloads, necessitating access-pattern-aware security abstractions rather than uniform block-level encryption. In order to mitigate against rollback, freshness is needed, but CVMs lack hardware primitives for this purpose, requiring alternative solutions.
We present CVM-Store, a storage system that co-designs a high-throughput userspace I/O engine with CIF (confidentiality, integrity, freshness) data protection. The key insight is that neither authenticated encryption nor I/O is a bottleneck by itself, but their naive combination is. CVM-Store exploits this by interleaving them, eliminating redundant copies and OS/hypervisor mediation. CIF guarantees are provided as composable primitives that adapt protection to workload access patterns, from which we derive three concrete authenticated abstractions: a KVS, a log, and a filesystem. An asynchronous trusted counter service provides freshness guarantees with epoch-based batching, which enables rollback protection without dedicated hardware support. CVM-Store delivers full CIF guarantees within $\approx$1% (write) and 1-19% (read) of raw NVMe bandwidth for large objects.

---


### 237. [FlockWorld: Toward Population-Scale Multi-Agent Video World Models through Artificial Life Simulation](https://arxiv.org/abs/2610.34564)

**<font color=#1a73e8>作者：</font>** Meryem Koksal, Yunzhe Wang, Volkan Ustun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most action-conditioned video world models remain limited to a single player, while existing multiplayer models support only small, fixed groups of agents. We introduce FlockWorld, an artificial-life environment built on Reynolds's Boids algorithm for studying population-scale multi-agent video world models. Specifically, FlockWorld renders synchronized egocentric crops, assigns distinct colors to preserve camera-agent identity across views, exposes rule-derived accelerations as actions, and lets the number of camera agents be configured independently of the size of the surrounding population. We further introduce FlockDiT, an action-conditioned latent diffusion transformer trained with flow matching on FlockWorld data to jointly generate synchronized egocentric videos for multiple agents. Our results suggest that joint generation benefits agent detection at density-matched settings and that diffusion forcing improves rollout fidelity. Together, FlockWorld and FlockDiT provide a controlled testbed for multi-agent video generation.

---


### 238. [Agentic AI Orchestration Framework for Spatial Intelligence: Supply Chain Deployment](https://arxiv.org/abs/2610.34569)

**<font color=#1a73e8>作者：</font>** Constantinos Papantoniou, Brian Hilton  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial spatial decisions are assembled across systems that share neither a reference frame nor an owner, and analysts spend substantial effort reconciling those systems rather than reasoning about space. This paper presents ANASSA, a reference architecture integrating structured reasoning, multi-agent workflow orchestration, authoritative spatial grounding, and feedback-driven execution, and reports its instantiation in an operating supply-chain deployment. The architecture places typed data contracts at agent boundaries, validates spatial claims against a certified authoritative foundation, and enforces two blocking human-in-the-loop approvals inside a six-step cognitive loop. The deployment covers multi-hazard risk assessment on an ocean-and-inland freight lane, including cold-chain excursion detection over container telemetry. Across a three-month proof of concept (POC) with three implementation iterations, three deployment outcomes are reported: 25% improvement in data quality, 50% reduction in spatial workflow runtime, and 60% lower decision latency relative to the preceding manual workflow. Absolute deployment-scale quantities and baseline counts are confidential; reported percentages are observed relative changes. These are uncontrolled deployment observations, not controlled experiments. We therefore specify instrumentation and ablation protocols for mechanism-level evaluation.

---


### 239. [RefinedGAW: A Refined German Academic Web Dataset](https://arxiv.org/abs/2610.34572)

**<font color=#1a73e8>作者：</font>** Maximilian Idahl, Oleh Astappiev, Benedikt Droste 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The largest open German text datasets are built from broad web crawls, which provide scale but limited coverage of specific domains. We introduce RefinedGAW, a processed and annotated resource derived from 26 semi-annual crawls of the German Academic Web, totaling 122 million documents and 314 billion tokens, with full crawl and capture history of every text. Documents labeled as academic research account for 84% of German RefinedGAW tokens across HTML and PDF. At 87.6 billion tokens, this exceeds the 64.9 billion tokens in the German subsets of FineWeb2 and FinePDFs, despite their almost five-times-larger combined size. RefinedGAW also contains substantial amounts of educational, math-heavy, and expert-oriented content with minimal commercial bias. Across HTML and PDF, 88% of German RefinedGAW documents have no near-duplicate candidate match in the three evaluated reference datasets, supporting complementary coverage. We release a queryable metadata index for fine-grained data selection and a rehydration tool for retrieving and processing source documents.

---


### 240. [Conditional Diffusion Generation of DVL and Inertial Signals for Underwater Navigation](https://arxiv.org/abs/2610.34574)

**<font color=#1a73e8>作者：</font>** Michal Levin, Itzik Klein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous underwater vehicles (AUVs) navigate without satellite positioning and rely on Doppler velocity log (DVL) and inertial sensors for motion estimation. Deep learning methods for processing these sensors require training data covering the motion the AUV encounters, commonly obtained through costly sea trials. To overcome this limitation, we present a conditional diffusion framework that generates synthetic DVL and inertial signals to replace real recordings in training. The generator employs an Elucidated diffusion model conditioned on three per-channel motion descriptors. Three configurations are evaluated: DVL beams alone, inertial channels alone, and all channels jointly from one model. Across thirteen trajectories of the real dataset, the generated signals followed the requested conditions with Pearson correlations between 0.72 and 0.997, transferred to trajectories withheld from generator training, and did not replicate any training window. A BeamsNet velocity estimator trained on generated signals alone, with no real recording retained, matched the velocity error obtained with the full real training set. Replacing up to all real windows with generated ones caused no measurable loss. Thus, this approach reduces the dependence of learned AUV navigation on sea-trial data, enables training when recordings are scarce, and facilitates developing and evaluating deep learning methods for underwater navigation.

---


### 241. [Cumulative Marginal Matching for One-Step Diffusion](https://arxiv.org/abs/2610.34575)

**<font color=#1a73e8>作者：</font>** Paribesh Regmi, Rui Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The sampling procedures of diffusion and flow-matching models involve hundreds of denoising steps incurring substantial inference time, which has motivated a growing body of work on training schemes for few-step and one-step generation. Existing approaches primarily seek to align the generation trajectory of few-step and base models, yet their training objectives only involve discrepancies at a single point in the trajectory, encouraging only local \emph{point-level} alignment. While recent methods such as \emph{Shortcut-CSL} introduce cumulative objective that enforce alignment over the entire trajectory, this is suboptimal as they do not directly enforce alignment between the distributions induced by the two models throughout the generation process. We propose \emph{Cumulative Marginal Matching} (CMM), a principled objective for few-step generation: by viewing flow-matching as a sequence of intermediate marginal distributions connecting the prior and data distributions, CMM directly optimizes the cumulative discrepancy between the base and few-step marginal distributions over the entire sequence. Specifically, we formulate this discrepancy using the Wasserstein-2 distance. By exploiting the pushforward representation of flow-matching, we transform an intractable cumulative Wasserstein objective into a tractable surrogate that can be optimized using samples from the intermediate marginal, which are readily generated through the conditional interpolation process of flow-matching. Furthermore, we show that the existing \emph{Shortcut-CSL} objective arises as a first-order approximation of that of the CMM, establishing a theoretical connection between the two objectives. Experiments on standard benchmarks demonstrate improvement in generation quality over \emph{Shortcut-CSL} and other state-of-the-art one- and few-step baselines under identical training budgets.

---


### 242. [Sparse Sum-of-Squares Layers for Certified Learning](https://arxiv.org/abs/2610.34590)

**<font color=#1a73e8>作者：</font>** Ege Gursoy, Nicolas Mansard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central limitation of modern machine learning systems is the lack of formal certificates guaranteeing their behavior beyond empirical, sample-based evaluation. Sum-of-squares (SOS) methods provide such guarantees by certifying polynomial inequalities over continuous domains via semidefinite programming (SDP). While prior work has introduced SDP layers as differentiable components in neural networks, repeated learning calls can lose the computational benefit of the forward program's sparse representation. We propose Sparse SOS Layers, differentiable value layers whose backward passes reuse the local coordinates of the forward solve. Under a fixed template and learned objective coefficients, each layer avoids building dense certificates and reuses its sparse structure across training steps. Compared with existing methods, our approach achieves up to 2.7 times speedup in total warm-call time, with nearly 100 times lower memory usage (1.7 vs. 160 GiB) for relatively large problem sizes for the tested dense parameterization. Experiments cover sparse polynomial certification, pendulum control, combinatorial relaxations, robotics projection, oscillator chains, and pose graph synchronization. A design study achieves zero certified violations across unseen problem instances and sizes, while requiring roughly 7 times fewer optimization solves than estimating gradients by perturbing the objective coefficients and re-solving the problem (finite differences). These results show that sparse certificate values can be effectively integrated into learning pipelines when the backward pass respects the verifier's structure.

---


### 243. [Finetuning Prompt-Based Image Editor for Geometry-Consistent Room Defurnishing](https://arxiv.org/abs/2610.34597)

**<font color=#1a73e8>作者：</font>** Prakhar Kulshreshtha, Brian Pugh, Zachary Nussdorfer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Erasing all furniture from a single room image to generate its empty counterpart is valuable for XR applications such as diminished reality and virtual staging. The challenge is twofold: inpainting the furniture regions with realistic content, and doing so without distorting the room's 3D geometry. Prompt-driven image editors, such as FLUX.2, handle realism impressively, but their structural faithfulness is inferior to explicit layout conditioned inpainting. To improve geometric consistency, we propose a training recipe for finetuning a LoRA on 2,500 furnished-empty room pairs. FLUX.2 with our LoRA adaptor significantly improves geometric consistency while retaining the high texture fidelity. This single-photo inpainter can be an effective building block for depth-aware and 3D-consistent XR pipelines.

---


### 244. [FlexiMIND: Combined Pretrained Vision Features and Local Structure for Training-Free Deformable Medical Image Registration](https://arxiv.org/abs/2610.34600)

**<font color=#1a73e8>作者：</font>** Mojtaba Safari, Mingzhe Hu, Shansong Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective. Deformable image registration remains challenging because corresponding anatomy may exhibit different intensity relationships. Hand-crafted modality-robust descriptors such as Modality-Independent Neighborhood Descriptor with Self-Similarity Context (MIND-SSC) and features from pretrained vision encoders provide distinct representations for correspondence estimation, but how they should be combined remains unclear. We investigate whether tighter integration improves registration over a sequential, scale-separated design. Approach. We introduce FlexiMIND, a training-free and label-free two-stage framework in which frozen FlexiCT-2D encoder features establish contextual correspondence and MIND-SSC refines the deformation within ConvexAdam. Five alternative feature-coupling strategies were evaluated under a protocol across CT-CT (DIR-Lab 4DCT 4DCT, 10 cases), MR-MR (ACDC, 50 patients), and MR-CT (Learn2Reg Abdomen MR-CT, 8 pairs) registration. Performance was assessed using target registration error (TRE), Dice similarity coefficient (Dice), SDlogJ, and local folding. Main results. FlexiMIND achieved a TRE of 1.27 mm on DIR-Lab 4DCT, a DSC of 0.807 on ACDC, and an organ-averaged DSC of 0.825 on Abdomen MR-CT. Across 15 coupling-strategy dataset comparisons, only four outperformed the reference method, with a maximum absolute improvement of 0.0043 in Dice, whereas degradation reached 20.6 % in TRE and 37.9 % in Dice. Changes in registration accuracy were closely associated with changes in deformation-field regularity, and strategies that better preserved regularity generally remained closest to the reference performance. Landmark-level analysis showed that the pretrained encoder stage primarily reduced large correspondence errors rather than uniformly improving local precision. Code is available upon acceptance at this https URL.

---


### 245. [Do Words Matter? What Text Contributes to Few and Full-Shot Vision-Language Anomaly Detection](https://arxiv.org/abs/2610.34610)

**<font color=#1a73e8>作者：</font>** Arda Baris Basaran, Mesut Ceylan, Elgar Fleisch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language anomaly detectors describe normal and abnormal appearance with text, and their gains are commonly credited to the semantic content of these descriptions. This attribution is plausible in the zero-shot setting, but few- and full-shot detectors interpose a trained visual adapter, and in that setting it has not been isolated. Changing a description changes both its meaning and its geometry, so accuracy comparisons cannot separate the two. We ask what a fixed pair of text embeddings, or anchors, contributes to such a detector: semantic content, effective scale, or joint anchor geometry. For a single anchor pair, the answer is effective scale alone. The score reads the anchors only through their difference, and a trained adapter can rotate to follow any replacement direction, leaving that direction, and with it the linguistic content, unidentifiable. We prove that replacement anchors with the same difference-vector length permit exactly the same probability maps and attainable losses. Across seven medical datasets, three vision backbones, both supervision regimes, and three adapter families, scale-matched random and orthogonal anchors track correct prompts; breaking the scale match opens a gap that restoring it closes without text. The same pattern holds in MVFA and when MadCLIP's learned prompts are replaced by a text-free learned scale. When one adapter serves many categories, the answer expands to their joint arrangement. Rotating all category axes together changes nothing, as predicted. For the tested CLIP prompts, these axes are nearly collinear, and meaning-free rotations that spread them apart improve performance on both industrial benchmarks. Even under frozen zero-shot transfer, a random anchor frame transfers as well as the prompt frame: coordinate consistency, not meaning. What these detectors read from their prompts is scale and arrangement, not semantic content.

---


### 246. [A Battery for AI Propensity Measurement: Rubrics, Synthetic Item Banks, and Annotations](https://arxiv.org/abs/2610.34614)

**<font color=#1a73e8>作者：</font>** Peter Romero, Haotian Li, Hugo Save 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We release a battery of 28 propensities for AI research, with expert-written rubrics, synthetic datasets, and annotated demand intervals, built with the method of Romero-Alvarado et al. (2026). We selected a wide collection of generic propensities that may influence the behavior of AI systems and humans. They are inspired by psychometric, psychological, and behavioral research, so that experimental results can be understood in the context of familiar constructs previously used also for human behavior research. The rubrics are useful for annotating existing benchmarks whose items may be relevant or not for one or more propensities. For easier profiling, however, the synthetic datasets are defined in such a way that they should be sensitive to one propensity only, allowing for a quick prototyping of propensity profiles using the battery of datasets. We also outline directions for future propensity research.

---


### 247. [CSI-TextBench: A Dataset and Benchmark for Language-Grounded Ambient Sensing Perception](https://arxiv.org/abs/2610.34616)

**<font color=#1a73e8>作者：</font>** Guozhen Zhu, Yuqian Hu, Sakila S Jayaweera 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Indoor context deciphered by ambient sensing underpins many applications, from assisted living to smart buildings, yet remains weakly connected to the language-aligned paradigm of modern multimodal systems. Through billions of IoT devices, ambient WiFi Channel State Information (CSI) captures the indoor context of human activity and environmental dynamics passively via ubiquitous, always-on infrastructure. However, unlike vision or audio, CSI lacks naturally paired text like captions or transcripts, limiting its integration with language-driven AI systems.
We present CSI-TextBench, a large-scale dataset and benchmark for aligning CSI data with natural language, unifying 3 sensing benchmarks into 285,790 samples across 7 tasks and pairing them with 2,291 hierarchically structured, label-derived descriptions via many-to-many assignment to construct 2.0 million CSI-text training tuples. Benchmarking 5 alignment methods from 4 paradigm families, we show that contrastive CSI-text alignment matches supervised classifiers without class labels, adapts to unseen classes with few samples, and responds to open-vocabulary natural-language prompts. A single unified model supports compositional scene understanding, answering joint queries over activity, proximity, and identity, achieving 86.9% top-1 accuracy on 140 composite scenes, outperforming task-specific classifier ensembles. CSI-TextBench enables ubiquitous ambient sensing as a language-indexed perception layer, enabling indoor contextual awareness in language-driven AI systems.

---


### 248. [Valid Early Detection of Memorization in Diffusion Models](https://arxiv.org/abs/2610.34617)

**<font color=#1a73e8>作者：</font>** Yixiao Jing, Chia-Yu Hsu, Milad Hoseinpour 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models can sometimes reproduce examples from their training data, a phenomenon known as memorization. Existing memorization detection methods for unconditional diffusion models typically operate at a pre-selected timestep and therefore cannot adapt the detection time to the evolving denoising trajectory. Sequential monitoring enables adaptive detection but repeated testing across timesteps complicates trajectory-level false-alarm control. We study two ways of combining split conformal calibration with sequential monitoring for prompt-free memorization detection: per-step Bonferroni calibration and direct trajectory-level calibration of the maximum memorization score. The former controls repeated testing by splitting the false-alarm budget across timesteps, whereas the latter calibrates the event of ever crossing a threshold directly through the trajectory-level maximum. We evaluate this formulation on an unconditional CIFAR-10 EDM using two complementary per-step statistics based on geometry and representation spikiness. Experiments show that sequential monitoring improves the power-timing tradeoff over fixed-time detection. Compared with Bonferroni calibration, trajectory-level calibration achieves comparable detection power while using the false-alarm budget less conservatively and enabling earlier detection at higher noise levels.

---


### 249. [P2P-Former: Bridging the Supervision Gap Between Point and Proposal in Temporal Action Localization](https://arxiv.org/abs/2610.34618)

**<font color=#1a73e8>作者：</font>** Yunchuan Ma, Laiyun Qing, Sai Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, point-supervised temporal action localization has attracted increasing attention due to its low annotation cost (only one frame per action instance) and competitive detection performance. However, since point annotations are less complete than proposal annotations, existing methods mainly rely on multiple instance learning for snippet-level classification, which leads to a performance gap compared to fully supervised models. To bridge this gap, we propose P2P-Former, a novel point-to-proposal Transformer-based framework that effectively connects point-level supervision with proposal-level learning for temporal action localization. In this work, we identify two key challenges in transitioning from point-level supervision to full supervision: (1) how to generate reliable proposals as pseudo ground-truth, and (2) how to effectively integrate point-level cues into the fully supervised paradigm. To address the first challenge, we propose a Point-aware Proposal Generation (PPG) strategy that refines the confidence of proposals produced by a base locator using a point-aware importance estimation function, and then performs optimal matching between point annotations and candidate proposals to select reliable proposals as pseudo ground-truth. To tackle the second challenge, we introduce a Point-guided Semantic Enhancement (PSE) module that aggregates prototypes from point-annotated features and injects them into snippet features through Transformer-based interactions. Moreover, we design a Point-to-Proposal Constraint Loss (PPCL) that enforces each predicted proposal to include the annotated point, thereby encouraging more accurate localization. Extensive experiments on the THUMOS14 and ActivityNet-1.3 datasets demonstrate that our method outperforms several existing state-of-the-art approaches.

---


### 250. [RIDE-Splat: Reflection Removal for In-the-Wild Driving Environments](https://arxiv.org/abs/2610.34632)

**<font color=#1a73e8>作者：</font>** Kevin David Hayes, Alex Hanson, Allen Tu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driving video captured through a windshield violates the world-space consistency assumed by 3D Gaussian Splatting (3DGS): the road scene exhibits parallax while cabin reflections remain attached to the camera, causing standard 3DGS to embed reflected content into the reconstructed scene. We introduce RIDE-Splat, a pipeline for reflection-free 3D reconstruction from posed driving video without clean images, reflection masks, or pretrained networks. RIDE-Splat assigns world-consistent transmission through the windshield to a 3DGS scene and the dominant camera-attached reflection to one shared, signed RGB image. It builds the clean reconstruction in two passes. First, it learns the 3D geometry and the signed reflection image, representing both added radiance and transmission attenuation. Then, it uses the reflection-removed training images to fit a clean 3DGS model. At inference, the reflection image is discarded, preserving the standard 3DGS rendering path. We also introduce the RIDE-Splat Dataset, the first 3D reconstruction benchmark for reflection removal from driving video -- with real driving scenes, physical windshield reflections in training views, and separately captured non-reflective evaluation images. Across the RIDE-Splat Dataset, XLD, and Wayve, RIDE-Splat outperforms 3DGS, DC-Gaussian, and RobustSplat on all nine aggregate metrics, improving PSNR by up to 3.59 dB and reducing LPIPS by up to 0.0876. We achieve the highest metrics in 38 out of 42 per-scene comparisons and removes windshield reflections that remain visible in the baselines while preserving the transmitted scene.

---


> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-446](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
