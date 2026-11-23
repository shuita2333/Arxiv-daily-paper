# 📦 其他研究 | 2026年11月24日

> 本类共 **206** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-206](./part-05.md)

---

### 101. [GAAFormer: Geometry-Anchored Attention Transformer for Joint Point Cloud Denoising and Upsampling](https://arxiv.org/abs/2611.27281)

**<font color=#1a73e8>作者：</font>** Haoxi Tian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point cloud denoising and upsampling require samples that accurately recover the underlying surface from noisy or sparse observations. A central challenge in both tasks is preserving surface coverage while refining point locations. We introduce GAAFormer (Geometry-Anchored Attention Transformer), a unified generative octree transformer that performs both tasks with a shared network. Its decoder anchors attention neighborhoods to geometry, providing spatial context for occupancy prediction and point generation. Fixed voxel windows and alternating shifts preserve the grouping of surviving nodes as the output tree changes. The design retains the encoder, positional encoding, prediction heads, and parameter count of a serialized-attention backbone. We establish a deletion-consistency property of the neighborhood rule and evaluate both tasks using the same model. On PUNet, GAAFormer achieves a mean Chamfer distance (CD) of $6.0643\times10^{-5}$, reducing CD and Hausdorff distance by 3.35% and 19.34%, respectively, relative to the serialized backbone. For upsampling, it achieves CD values of $0.8475$, $1.7057$, and $1.0147$ ($\times10^{-5}$) on PU-GAN, PU1K, and Sketchfab, respectively, with improvements in CD, Hausdorff distance, and point-to-surface distance over the same backbone on PU-GAN and Sketchfab. These results establish a single architecture for point cloud denoising and upsampling. Within the shared encoder-decoder, the same geometry-anchored attention module improves both noise removal and dense point generation without task-specific redesign or additional parameters.

---


### 102. [DermKG: A Concept-Centric Knowledge Graph for Interpretable Skin Disease Diagnosis from Dermatological Morphology](https://arxiv.org/abs/2611.27283)

**<font color=#1a73e8>作者：</font>** Cheng Huang, Yanmei Li, Mao Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dermatologists describe lesions with a standardized morphological lexicon, which makes concept-based models attractive for interpretable skin disease diagnosis. How much diagnostic information these concepts actually carry, however, is rarely quantified. We present DermKG, a concept-centric knowledge graph built on the expert-annotated SkinCon subset of Fitzpatrick17k (3,230 images, 48 concepts, 113 diseases). DermKG has 3,452 nodes of 8 types and 19,365 edges of 11 relation types, and encodes disease concept profiles, concept co-occurrence, a three-level diagnostic hierarchy, and 20 clinical morphology rules, all of which are supported by the training data (15 strong, 5 moderate). An information-ceiling analysis shows that the 3,230 lesions collapse onto only 813 distinct concept vectors, bounding concept-only top-1 accuracy at 38.9\% for diseases and 77.6\% for the nine categories. Within this bound, DermKG-Net, a graph neural network that scores lesions against disease prototypes and aggregates them along the hierarchy, raises category-level balanced accuracy from 0.257 to 0.411 over the strongest of 11 baselines (paired bootstrap difference $+0.150$, 95\% CI $[0.073, 0.231]$) and more than doubles minority-category recall. Ablations show that most of this gain comes from the hierarchical prototype objective, with a smaller contribution from graph structure. DermKG further yields rule-based reasoning chains and concept-level explanations for individual predictions.

---


### 103. [Preserving Pretrained CFG Structure in RL for Diffusion Models with Conditional Contrast Regularization](https://arxiv.org/abs/2611.27288)

**<font color=#1a73e8>作者：</font>** Yunfei Zheng, Xiaolong Wang, Dandan Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has become an important component in the post-training of diffusion models. In practice, however, standard RL often improves the target reward without reliably preserving holistic generation quality, leading to unstable reward-quality trade-offs that we view as a form of reward hacking. Since Classifier-Free Guidance (CFG) is known to improve visual clarity, prompt alignment, and perceptual quality in generation, we investigate whether its underlying structure can serve as a useful prior during RL. We present a unified geometric view that interprets both CFG and RL as correction vectors in a common prediction space, and identify the projection of the RL-induced correction onto the pretrained CFG correction as a useful diagnostic of quality-related structural preservation. Geometric analysis and rotation intervention further show that the pretrained CFG direction carries information useful for generation quality that reward-driven RL updates do not necessarily preserve. Based on this insight, we propose Conditional Contrast Regularization (CCR), which uses the frozen reference model's conditional contrast as a local structural prior during RL. Experiments across multiple reward settings and backbones show that CCR more consistently preserves generation quality while maintaining competitive reward, yielding a better reward-quality trade-off than standard RL and generic regularization methods.

---


### 104. [EgoLAM: Learning Latent Actions from Hand and Head Motion](https://arxiv.org/abs/2611.27290)

**<font color=#1a73e8>作者：</font>** Ziyi Ding, Yiwei Wang, Zhongxing Wei 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent action models let a robot policy learn from video by turning the change between two frames into a training target. In egocentric video, a cup can move across the image because a hand pushes it or because the wearer turns. Both changes help predict the next frame, but only the first describes manipulation. During training, EgoLAM supervises the action code with measured wrist motion and supplies camera motion separately to the forward model. Even when the wearer turns while pushing a cup, the training target still describes how the hand pushed it. The action encoder pools object slots around each hand, and wrist translation and rotation can be decoded from the code in a common reference frame. Extracting a code then requires only two RGB frames. Alongside LARYBench classification and regression, we measure how much wrist motion a frozen code retains and how strongly it responds to a synthetic view or lighting change. EgoLAM has the highest hand-motion decoding score among eight evaluated models. Across three LIBERO suites, policies pretrained on its codes and fine-tuned on expert demonstrations achieve 79.38% mean success, 28.73 points above expert behavior cloning and 9.76 points above the strongest other latent action model in each suite on average.

---


### 105. [A Vision-Based Framework for Manual Assembly Verification and Adaptive Operator Assistance](https://arxiv.org/abs/2611.27293)

**<font color=#1a73e8>作者：</font>** Naveen Joseph Delphin, Leonardo Venturoso, Isabella Soraruf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Manual assembly remains difficult to monitor because operator actions, components, and task progress must be interpreted together. This paper presents a modular framework based on a single overhead red-green-blue (RGB) camera, combining object detection, hand-motion tracking, region-aware interaction detection, finite-state verification, task-specific pose classification, and configurable visual guidance. The system was evaluated during pneumatic-piston assembly and disassembly with eight participants under three assistance conditions: full, mid, and no guidance. Mixed-effects analysis identified an association between assistance condition and a composite measure of motion quality, with lower estimated scores under mid and no guidance relative to full guidance. However, the condition-by-trial interaction was not statistically significant, and the estimated differences in learning trajectories remain descriptive. No condition differences were detected in completion time or failed-stage counts. The study demonstrates the integration of visual perception, procedural verification, and configurable operator feedback in a single-camera workflow. Selecting assistance according to operator expertise remains a design objective for future investigation.

---


### 106. [Observed, Curated, Reused: Observation Bias in Clinical AI Evaluation](https://arxiv.org/abs/2611.27301)

**<font color=#1a73e8>作者：</font>** Md Shamim Ahmed, Lukas Galke Poech, Richard Röttger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical AI evaluations are vulnerable to observation bias embedded in routine medical documentation, which captures only what clinicians notice, test, and record rather than a complete clinical picture. As this evidence travels into publications and reference knowledge graphs, crucial distinctions disappear: unexamined symptoms blur with confirmed negatives, and chronological disease progression is lost. Surviving evidence can also enter both the benchmark query and the reference knowledge base, creating a self-referential loop where a patient is evaluated against clues derived from their own published case report.
To quantify this bias, we tracked 6,503 clinical cases across six historical Human Phenotype Ontology (HPO) releases (October 2021-June 2026) to identify when HPO first cited the publications describing them. This yielded a confirmatory cohort with an observable "source ingestion" event, where HPO cited a case's source publication as target-disease evidence. Diagnostic rankers depended heavily on these source publications: for our primary semantic ranker (Resnik), publication-weighted mean reciprocal rank rose from 0.26 before paper ingestion to 0.84 upon inclusion in HPO, but collapsed to 0.05 when source-linked assertions were counterfactually removed. Two additional rankers (IC-cosine and LIRICAL) reproduced this trajectory, and control experiments confirmed the diagnostic jump was driven by the patient's publication rather than background HPO growth.
Clinical AI systems may therefore score well because their knowledge base contains evidence linked to the test case's source publication, rather than through generalization. Modern knowledge is not the problem; evaluation evidence must match the claim. Trustworthy benchmarks must separate patients, source-linked evidence, and time: historical tests should use only knowledge available at the intended decision time.

---


### 107. [$γ$-Scape: An Agent-Centric World for Mobile Embodied Intelligence](https://arxiv.org/abs/2611.27306)

**<font color=#1a73e8>作者：</font>** Xiaotao Zhang, Lin Qian, Hao Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent embodied agents construct and adapt robot behavior through executable programs, tool use, and interaction feedback. Studying these systems in mobile manipulation calls for physical worlds that connect agent-directed execution with its physical consequences and reusable interaction experience. We introduce $\gamma$-Scape, an agent-centric simulation and benchmark platform for mobile embodied intelligence. Agents compose motion tools and learned skills to carry out complete tasks that combine navigation and manipulation in a persistent physical world. BenchForge grounds structured objectives in physical task instances with instructions, reference programs, and goal evaluators, defining task goals while preserving agents' choice of valid solutions. An agentic collection harness further enables agents to produce demonstrations by carrying out contact-rich interactions through sustained control and physical feedback. Assisted reference execution and human guidance provide complementary experience. The resulting tool traces and aligned observation-action records support program refinement and policy learning, with common task-goal criteria for subsequent evaluation. We benchmark representative agent systems on complete tasks and demonstrate contact collection and trace-informed program revision. Together, these workflows provide infrastructure for research on embodied recursive self-improvement.

---


### 108. [BioCL-POS: Biological Completer-aware Learning with Predictive Observation Selection - A Wild Ginseng Study](https://arxiv.org/abs/2611.27316)

**<font color=#1a73e8>作者：</font>** Yulu Wang, Tingting Yao, Taolue Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Growers and traders rely on root morphology to assess wild ginseng, yet breakage can obscure important structural traits. We study point cloud completion to provide geometric references for morphological analysis. Does providing more observed points always improve 3D completion? We test whether selected subsets improve recovery of the original missing region while keeping the pretrained completer fixed. We introduce BioCL-POS, an external selector that predicts how the completer responds to candidate inputs. For each candidate, we predict the displacement and distance from shared spatial locations to the nearest points in its completion. We use these spatial responses to estimate recovery quality and supervise them with measurements from actual completions. At inference, we select an input from the observed geometry and run the completer once. We evaluate four frozen completers on controlled gaps in ginseng and tree data at 5%,10%, and 20% omission, and examine 30% omission on ginseng. At 5--20% omission, we outperform full-input completion and all five alternative selectors on both datasets with all four completers. We achieve lower mean reconstruction error and higher mean F-score and coverage. We thus show that selecting observations can improve geometric recovery without retraining the completer, providing more accurate geometric references for subsequent morphological analysis.

---


### 109. [GGDriver: Glance at What Is Shared, Gaze at What Differs for Perception-Free Planning](https://arxiv.org/abs/2611.27330)

**<font color=#1a73e8>作者：</font>** Jiawei Sun, Maosen Li, Jiamin Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A planner deciding whether to turn left or continue straight needs to inspect different parts of the scene for each maneuver. Yet many end-to-end driving planners evaluate every candidate trajectory against the same compressed scene representation. We let each candidate select the visual evidence used to refine and score it. A global glance first produces trajectory hypotheses from shared scene features. We then project a corridor around each trajectory into the camera views and use the resulting mask to attend to patch features at the backbone's native resolution. After refinement, the scorer projects each final proposal again and ranks it using evidence along its own path. This geometric selection requires only the predicted trajectory and camera calibration. On three planners with different scene representations (learned registers, a perception-supervised bird's-eye-view grid, and a coarse image-token grid), adding this gaze improves planning scores. In ablations, path-aligned patches outperform both a matched number of randomly selected patches and attention over all patches. Using the gaze for ranking yields larger gains than using it for refinement alone. With a ViT-S backbone and no perception labels, GGDriver achieves a rater feedback score of 8.110 on the WOD-E2E test set, 94.2 PDMS on NAVSIM-v1, 48.6 EPDMS on NAVSIM-v2, and a closed-loop Driving Score of 72.18 on Bench2Drive.

---


### 110. [CoGITAtion: Collaborative Gaze-based Interpretable Task-adaptive Representation for Privacy-sensitive Applications](https://arxiv.org/abs/2611.27340)

**<font color=#1a73e8>作者：</font>** Mayar Elfares, Yasmine Elfares, Andreas Bulling  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaze-based analysis provides rich behavioural information for privacy-sensitive applications, but deployment is challenged by heterogeneous, scarce, and distributed data. We present CoGITAtion (Collaborative Gaze-based Interpretable Task-Adaptive Representation), a framework for privacy-preserving inference over vertically distributed gaze data. CoGITAtion transforms variable-length gaze recordings into compact, interpretable gaze-transition graphs and descriptors computed locally by each data owner. Task-adaptive models accommodate heterogeneous and missing feature blocks through task and availability gating, avoiding unnecessary private computation. Results show that shared components capture patterns that generalise across tasks, while task-specific components provide capacity without increasing model size. Public availability gating further reduces encrypted computation by removing branches determined by publicly known task and owner availability without altering predictions. Overall, CoGITAtion enables gaze model reuse, efficient privacy-preserving deployment, and robust inference under incomplete owner availability while retaining interpretable gaze representations.

---


### 111. [ReSA: Preserving Reference-Specified Foreground in In-Context Segmentation](https://arxiv.org/abs/2611.27341)

**<font color=#1a73e8>作者：</font>** Dezhao Su, Bingxu Hou, Jingdi Lei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-context segmentation uses annotated references to specify the target and its extent in a query image. Accurately transferring this reference-specified foreground requires recovering target regions while suppressing irrelevant predictions. We propose ReSA, a reference-guided framework that unifies query adaptation and mask selection through a shared reference kernel. ReSA leverages foreground and background reference prototypes to constrain prediction changes during adaptation and guide foreground selection through reference-weighted reconstruction. This shared guidance promotes consistent use of reference information across prediction refinement and mask formation. ReSA further selects among adapted predictions and aligns boundary refinement with the selected foreground threshold. We establish a theoretical bound connecting reference-response changes during adaptation and soft reconstruction. With a frozen visual encoder and lightweight test-time adaptation, ReSA requires no offline task training. Ablation studies demonstrate improved foreground retention and effective suppression of false-positive regions, while qualitative results show more complete masks with fewer isolated artifacts. Across ten object, part, and cross-domain segmentation benchmarks, ReSA achieves the highest average mIoU among the evaluated methods, reaching 62.6% in 1-shot and 71.8% in 5-shot.

---


### 112. [Borrow the Style, Follow the Prompt: Progressive Reference-Guided Stylization](https://arxiv.org/abs/2611.27360)

**<font color=#1a73e8>作者：</font>** Yu Lin, Zi-Jun Wang, Zhilin Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-guided text-to-image stylization transfers visual appearance to content specified by text, but the reference subjects and backgrounds can interfere with what the generated image depicts. Suppressing this unwanted information can also discard transferable texture and material cues, creating a tension between content control and faithful preservation of the reference style. Accordingly, we propose ProStyle, which learns a content-suppressed style prior through cross-content supervision on same-style pairs with different subjects and backgrounds and injects it with weak conditioning at auxiliary layers to strengthen style expression. Building on this prior, a complementary pathway learns residual corrections from full reference patch features with the content-suppressed style pathway frozen, before both pathways undergo joint refinement under the same objective. For cross-content learning and evaluation, we introduce ReConStyle, which provides 134K training pairs, two test settings, and object-level measures of target-content fidelity and reference-object overlap alongside style similarity and text alignment. ProStyle outperforms all compared SD1.5-based baselines and achieves the best average rank of 1.86 across four automatic and three human-evaluation criteria on ReConStyle-Full. In the user study, it substantially outperforms the baselines in text alignment and combined suitability, with selection rates of 84.36% and 50.90%, respectively. On the external Style-Rank benchmark, it also achieves the highest CLIP-Text and ImageReward scores.

---


### 113. [Testing for Coordination Failures in Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.27368)

**<font color=#1a73e8>作者：</font>** Dennis Gross, Jørn Eirik Betten, Helge Spieker  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Deep parallel cooperative multi-agent reinforcement learning (CMARL)} trains multiple agents that all act at every time step to optimize a common objective. Like single-agent RL, CMARL can produce unsafe behaviors that violate implicit safety requirements not captured by the reward, and these behaviors are hard to explain. However, testing CMARL policies for safety has received less attention than the safety testing of single-agent RL policies. In this paper, we propose DisQ, a test case selection method that identifies failure-revealing states in value-based CMARL by exploiting a signal specific to trained Q-learning agents. The signal is the Q-value gap, an explainable metric that flags a state when the agents' estimates of the achievable return diverge by more than a calibrated threshold. DisQ selects such states for execution and skips those without a gap. Our experiments in four CMARL benchmark environments show that, in most of the evaluated configurations, DisQ improves failure detection over single-agent RL testing methods applied to CMARL, namely random testing and search-based testing with genetic algorithms. Our main contributions are the Q-value gap, an indicator of potential miscoordination computable from a single state without executing the system, and DisQ, a test case selection method that adapts existing single-agent testing methods to CMARL.

---


### 114. [ReActWAM: Action-Consistent Caching for Efficient World-Action Models](https://arxiv.org/abs/2611.27372)

**<font color=#1a73e8>作者：</font>** Zhaochen Guo, Yunke Wang, Siyu Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World-action models (WAMs) often generate future visual states alongside robot actions, introducing substantial computational overhead during inference. During closed-loop execution, consecutive inference cycles often predict similar action sequences, leading to redundant computation. However, reducing this redundancy requires distinguishing consistent actions from changes that demand fresh computation. To address these challenges, we propose ReActWAM, a training-free framework that combines action-intent-guided prefix skipping with inner-chunk prediction reuse. A coarse-to-fine assessment evaluates motion changes, visual consistency, and action prediction conflicts. For eligible chunks, we draw on first-step differences to adapt the cached latent and network features to the current condition, providing an estimate at a later denoising step that bypasses the redundant prefix. Subsequent inference refines this estimate while reusing stable denoising predictions within the chunk. Experiments across LingBot-VA, FastWAM and the Cosmos family on LIBERO-Long and RoboTwin 2.0 demonstrate $1.41\times$--$5.44\times$ GPU inference speedup, with minimal degradation in task success rates. Real-world experiments on a Franka Research 3 (FR3) robot further achieve $1.46\times$ end-to-end speedup while maintaining success rate.

---


### 115. [Gumbel Substitution: Removing Sampler Drift from RL Without Trusting the Sampler](https://arxiv.org/abs/2611.27375)

**<font color=#1a73e8>作者：</font>** Romain Fanucci, Malik El Hassani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When RL rollouts come from untrusted samplers on arbitrary hardware, precision and checkpoint lag, the sampling distribution $q$ differs from the trainer's policy $p$, and training on the sampler's tokens adds a drift term equal to supervised fine-tuning toward $q$. Published corrections (TIS, MIS, IcePop, score centering, GSPO, CISPO) all need $q(y)$, which a permissionless sampler reports and can misreport. We introduce Gumbel substitution. The coordinator fixes public Gumbel noise for every token position, bit-identical across GPUs, and the sampler draws $y=\arg\max(\ell^q+G)$. The trainer recomputes $v^*=\arg\max(\ell^p+G)$, the token its own policy would have drawn with the same noise, and scores $v^*$ in the sampler's context. For a sampler that follows the protocol, $v^*$ is an exact sample from $p$ given the prefix, so the drift vanishes in expectation for any $q$, without sampler-reported probabilities. We measure the residual left by the deployed heads, bound the one added by admission gates, and state what an adaptive sampler can still do. The same comparison gives a per-token match rate that admits and pays samplers. In the lab, on a 9B model with the same head on both sides, the expected drift of uncorrected training is at least 170 to 4,800 times that of substitution. On a 2B model under strong mismatch, uncorrected training collapses while substitution stays stable, comparable to MIS with score centering given the true $q$. On a permissionless network, a 9B model was trained for 158 optimizer steps on 15.75B tokens from heterogeneous samplers, with no skipped step and 1.21% of tokens substituted; it improved on all eight held-out benchmarks.

---


### 116. [VMSA: Video Memory Skill Agent for Long Video Understanding](https://arxiv.org/abs/2611.27381)

**<font color=#1a73e8>作者：</font>** Changin Choi, Jungwon Park, Jungmin Ko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video question answering requires retrieving and integrating relevant evidence from videos spanning hours or even days. Recent agentic approaches organize video information into external memories and iteratively retrieve evidence to answer questions. However, effective retrieval and reasoning remain challenging, as agents must determine what information to search for, which memory sources to access, and how to connect evidence across distant temporal intervals. To address these challenges, we propose Video Memory Skill Agent (VMSA), a framework that jointly designs structured video memories and memory skills for long-video understanding. VMSA constructs three complementary memory components. Segment Caption Memory and Entity Event Memory serve as searchable evidence sources, while Entity-Aware Episode Memory provides broad yet detailed video context to guide evidence retrieval and reasoning. To further support effective memory utilization, VMSA induces memory skills from successful agent trajectories, incrementally refining or extending a compact skill library to guide iterative evidence retrieval, reasoning, and verification. Across seven long-video question-answering benchmarks, VMSA achieves the highest accuracy on all three week-long egocentric benchmarks, outperforming the strongest baseline by up to 9.4% on Ego-R1 Bench, and the best or competitive performance on four additional benchmarks. Ablation studies further demonstrate the contributions of all three memory components and memory skills, with memory skills also improving temporal evidence localization.

---


### 117. [PanoUAV-Track: Full-Spherical UAV Visual Tracking in the Wild](https://arxiv.org/abs/2611.27383)

**<font color=#1a73e8>作者：</font>** Bingyu Li, Lichang Yang, Zhiyuan Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing UAV tracking benchmarks predominantly rely on perspective cameras with limited fields of view. Omnidirectional cameras enable full-spherical observation, yet tracking from moving UAV platforms remains largely unexplored. Unlike ground-level panoramic tracking, UAV-mounted omnidirectional cameras observe targets across both azimuth and elevation, introducing geometric challenges under equirectangular projection (ERP). To investigate this setting, we capture approximately \textbf{40 hours of real-world 8K panoramic UAV video} and construct \textbf{PanoUAV-Track} through temporal clip extraction, target annotation, and the integration of simulated sequences. The resulting benchmark comprises 1,895 sequences, 507,961 frames, and 2,872 annotated objects, covering real-world daytime and nighttime scenes alongside simulation, and supporting both visual and language-based target specification. Through extensive evaluations, we reveal a clear \textbf{perspective-to-spherical} generalization gap and identify tracking degradation associated with latitude-dependent distortion and ERP seam discontinuity. To address these challenges, we propose \textbf{PanoUAV-Tracker (PUTrack)}, a geometry-aware tracking framework combining latitude-adaptive search and seam-aware periodic sampling. PUTrack improves zero-shot and in-domain tracking, particularly for seam-crossing targets. Code and benchmark resources will be available\footnote{\textcolor{tabpink}{this https URL}}.

---


### 118. [What Stays in the Picture? From Redundant Instructions to Dependency-Aware Image Editing](https://arxiv.org/abs/2611.27388)

**<font color=#1a73e8>作者：</font>** Zi-Jun Wang, Yu Lin, Zhilin Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce complex redundant-instruction image editing, where a single request specifies multiple objects, their attributes, and spatial relations while revising or canceling earlier editing requirements. Direct editing can fail to recover this intent, while splitting the request into successive steps can preserve obsolete edits and visual errors. Our key insight is to resolve the revision history into a final editing target that jointly guides planning and verification, so that obsolete requests do not become visual edits. Based on this insight, CRIE-Agent learns to consolidate revisions into object-level final intent and executes the retained objects in reference-first blocks, establishing referenced objects before their dependents. Verification then guides complete re-execution from the source image, with conditional layout hints, preventing visual errors from failed attempts from being carried into subsequent ones. We also construct CRIE-S, a benchmark containing 10,000 complex and redundant editing instructions with exact final intent annotations. Across five image-editing backends on CRIE-S, CRIE-Agent raises complete editing success from 0% under direct editing to 27.5--50.0%.

---


### 119. [Evidence sufficiency assessment enables cost-effective review allocation in on-premise clinical AI agents](https://arxiv.org/abs/2611.27390)

**<font color=#1a73e8>作者：</font>** Yiwen Qiu, Che Sun, Shu Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-premise clinical AI agents must auto-accept high-confidence diagnoses, deferring others to clinician review, yet token probabilities and self-reported confidence miss errors, while more reliable five-run consistency incurs fivefold compute. We propose training-free decision-point evidence sufficiency assessment and a three-tier sequential triage protocol. Masking reasoning and diagnosis, the same 4B model scores sufficiency from objective evidence via prior-debiased probabilities over five ordered levels. Calibration freezes a nominal top-50% threshold, selecting single-run, five-run consistency, or full-deferral tiers by whether the one-sided 95% Wilson lower confidence bound of pass rate among accepted cases meets the 95% clinical target line. Across 1,605 MIRA-v2, CDM, VivaBench, and in-hospital liver malignancy primary cohort cases, MIRA-v2 single-run top-50% pass rate reached 98.91%, matching five-run consistency, saving ~80% compute; CDM achieved 96.00% test attainment by escalating to the five-run consistency tier; cross-specialty, missing-imaging, and combined enriched cohorts entered the full-deferral tier, capping calibration false-certification rate at 0.00%-3.50%.

---


### 120. [Beyond Linear Decodability: Understanding and Improving Instruction Following in World Action Models](https://arxiv.org/abs/2611.27401)

**<font color=#1a73e8>作者：</font>** Bokai Ji, Jiapeng Chen, Yi Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World action models (WAMs) exhibit strong manipulation capabilities yet often fail to follow test-time language instructions. Prior work shows that non-following (NF) WAMs encode information about the instructed target, but this information does not control their behavior. By comparing NF WAM with its instruction-following (IF) counterpart, we find that target information is substantially more linearly decodable in IF WAMs, despite being encoded in both. Motivated by this observation, we introduce linear decodability supervision (LDS), a simple yet effective auxiliary training objective that promotes the linear decodability of the instructed target information. On LIBERO-CF, InternW0-$\Delta$ with LDS achieves a success rate of 74.6% and a grounding rate of 89.2%, surpassing the strongest baseline by 26.8 and 42.9 percentage points, respectively. The effectiveness of LDS challenges the prevailing interpretation that encoded target information does not contribute to WAMs' behavior. To reconcile this apparent contradiction, we propose a prior-instruction competition mechanism, which explains NF and IF behavior as arising from the dominance of prior and instruction signals, respectively. We provide causal evidence for this mechanism by evaluating two training-free interventions derived from it. We reinterpret LDS through this mechanism, showing that it acts as a form of instruction signal enhancement. Finally, more comprehensive evaluations across diverse manipulation tasks and visual domains demonstrate the consistent effectiveness of LDS.

---


### 121. [BladeR: Scalable, Shape-Guided 3D Reconstruction of Wind Turbine Blades from UAV Imagery](https://arxiv.org/abs/2611.27407)

**<font color=#1a73e8>作者：</font>** Jonathan Sterckx, Michiel Vlaminck, Hiep Luong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The structural integrity of wind turbine blades is critical for safe, efficient energy production. Accurate 3D reconstruction allows precise localization and quantification of wear and early damage detection. While drone-based inspections are standard, their high-resolution imagery poses challenges such as weak texture, lighting variability, and high computational cost. We present BladeR, a scalable pipeline for high-quality 3D reconstruction from inspection imagery. A hierarchical sparse reconstruction strategy leverages GPS/IMU data and blade shape priors to guide advanced keypoint matchers on full-resolution images. For dense reconstruction, a tiled Gaussian Splatting framework processes 45 MP images at native resolution, isolates the blade from background, and adaptively enhances detail recovery along the leading edge. Validation against commercial and open-source baselines shows significant improvements in model completeness and detail.

---


### 122. [Projector Time Map Calibration for Event-based Structured Light](https://arxiv.org/abs/2611.27412)

**<font color=#1a73e8>作者：</font>** Buu-Hoang-Lam Le, Kota Mizutani, Shohei Nobuhara  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing event-based structured light obtains a dense projector-camera correspondence from the timestamp of an event. It assumes that the projector scans a parallel raster and that the sensor timestamps each pixel independently, and we show that neither assumption holds. We obtain the correspondence from a temporal code that identifies the projector pixel directly and therefore needs no prior calibration, we calibrate the projector time map from the same recording, and we recover the geometry of the system and the offsets between its clocks by a spatio-temporal self-calibration in a preamble of a few seconds that needs no reference object and no second camera.

---


### 123. [Pose-based Co-speech Gesture Detection](https://arxiv.org/abs/2611.27415)

**<font color=#1a73e8>作者：</font>** Frances Yung, Ninlawat Phuangschoke  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Co-speech gesture detection identifies the spans in which a speaker gestures (e.g., beat or semantic gestures) in video. As a first step in gesture annotation, it is crucial for studying human communicative behaviour. Despite the availability of automatic tools and models, co-speech gesture detection remains underexplored, and its current state of the art is unclear: existing methods have been evaluated using different datasets, experimental setups, and metrics, making their performance difficult to compare. To address this gap, we benchmark existing detectors using the same cross-validation folds across three datasets (MULTISIMO, GESRes, and CABBS), with evaluation at the frame, gesture-span, and window levels. Our results show that previously reported performance does not consistently transfer to this common evaluation setting. Performance varies substantially across datasets, particularly with gesture frequency, indicating that the task remains far from solved. We further propose a CTR-GCN + BiLSTM model that outperforms the previous best method, MPSL, on CABBS. Our results provide a more consistent basis for comparing existing approaches and highlight key challenges for future research on co-speech gesture detection.

---


### 124. [Learned Network Dynamics for Model Predictive Traffic Signal Control under Incidents](https://arxiv.org/abs/2611.27435)

**<font color=#1a73e8>作者：</font>** Dang Viet Anh Nguyen, Carlos Lima Azevedo, Tomer Toledo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model predictive control (MPC) of urban traffic signals relies on a model of how queues respond to signal decisions, which is hard to specify and calibrate in heterogeneous networks, particularly when incidents change capacities and turning shares. Measurements add a second limitation: the controlled lanes at the stop line are often short, so queues extending upstream of them fall outside lane-level measurements. We propose GNN-MPC, a receding-horizon controller that plans with action-conditioned network dynamics learned by graph neural networks. Phase sequences are coordinated across intersections by approximate best responses, with an acceptance test that keeps the predicted cost no higher than that of the initial plan. In microscopic simulation under non-recurrent incidents, GNN-MPC reduces travel time and increases completed trips relative to all tested controllers, on a homogeneous grid and a heterogeneous 21-intersection network. Controlled comparisons on the heterogeneous network distinguish the roles of observation and prediction. With nearly as many vehicles entering the network, GNN-MPC reduces travel time by 13% relative to MaxPressure with the same upstream measurement, and GNN-MPC without the upstream representation does not reproduce its performance. Under the same traffic measurements, planner and objective, replacing the learned dynamics with calibrated store-and-forward predictors increases travel time by 31-34%. Observing hidden demand and predicting its response to control are thus complementary requirements of network-level predictive control.

---


### 125. [Ego2Ego: Generative Visual Perspective Taking Across Collaborators](https://arxiv.org/abs/2611.27459)

**<font color=#1a73e8>作者：</font>** Chuhan Jiao, John Gideon, Anshul Gupta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual perspective taking, the ability to infer what another person sees from their position, is fundamental to human collaboration. However, prior works reduced perspective taking to state estimation, geometric reconstruction, or discrete question answering, whereas existing cross-view video generation methods either inferred the target view from the input video alone or required an external camera that observes the target person. We introduce generative visual perspective taking: Given an ego person's egocentric video, a scene point cloud, and a collaborator's camera trajectory, the task is to generate the continuous egocentric video from the collaborator's perspective. This task is challenging given extreme viewpoint shifts, dynamic occlusions, and sparse visual overlap. We address these challenges with Ego2Ego -- a set of backbone-agnostic geometric modules that provide a pretrained video diffusion model with the 3D scene geometry shared by both interactants. Ego2Ego renders dense, temporally consistent scene coordinate maps into every view as a shared spatial reference, aligns cross-view tokens in 3D ray space through relative geometric attention, and recovers regions outside the ego person's current view from the ego person's visual memory. Experiments on the CoMind dataset across three video diffusion backbones show that Ego2Ego consistently improves visual quality, Level-2 scene layout accuracy, and collaborator motion, outperforming state-of-the-art cross-view video generation baselines on every backbone. By generating the collaborator's egocentric video more accurately, Ego2Ego brings visual perspective taking to human-robot collaboration, where it can help infer what a human collaborator sees and does, and can turn single-person recordings into synchronised multi-perspective videos for robot learning.

---


### 126. [Supervaluationism about vagueness and indeterminacy: A judgment-aggregation perspective](https://arxiv.org/abs/2611.27463)

**<font color=#1a73e8>作者：</font>** Christian List, Paul Egré, Franz Dietrich  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supervaluationism about vagueness and indeterminacy is based on the idea that some sentences, or predicates within them, have multiple competing interpretations or specifications. A sentence is deemed determinately true if and only if it is true according to all specifications; and determinately false if and only if it is false according to all specifications. In all other cases, the sentence is assigned no determinate truth-value. Supervaluationism, however, is only one way of taking into account the verdicts of different specifications -- in technical terms, "aggregating" those verdicts. In this paper, we introduce insights from the theory of judgment aggregation to study a broad class of different aggregation functions. This allows us to offer an axiomatic characterization of supervaluationism, which, in turn, locates it precisely within a larger logical space of possible approaches to vagueness and indeterminacy. Among other results, we axiomatically compare supervaluationism with subvaluationism, the epistemic theory of vagueness, and Strong Kleene and LP logics.

---


### 127. [Cecilia: Towards Layout-Inclusive Optical Music Recognition](https://arxiv.org/abs/2611.27465)

**<font color=#1a73e8>作者：</font>** Congren Dai, Zhancheng Guo, Xiaobing Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing an editable music score requires musical events, sung text and the instructions that organise them on the page. Existing recognition targets often omit part of this information, while direct MusicXML prediction repeats substantial structural markup. We introduce Cecilia, a compact representation of canonicalised MusicXML that retains musical content, lyric attachments and layout instructions. Cecilia-OMR predicts this representation through metadata and measure-bounded music segments from shared visual memory. A learned count head determines the number of output segments. Across paired complete scores under a common tokeniser, the ratio of mean MusicXML to Cecilia sequence lengths is 27.73. Cecilia-OMR outperforms Legato 2 on Camera String Quartets and both Lieder conditions, with a four-condition OpenScore macro normalised edit distance of 0.2232 against 0.2998. Separate evaluations of lyrics, notation trees and rendered layout reveal complementary aspects of reconstruction and quantify the contribution of layout instructions. Training-stage, reward and candidate-selection studies further examine how recognition changes across model adaptation and decoding.

---


### 128. [Communication-constrained multiagent risk estimation: a simulation benchmark for adult sore throat](https://arxiv.org/abs/2611.27468)

**<font color=#1a73e8>作者：</font>** Anas H. Alzahrani  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Distributed predictive agents may need to approach a shared estimate under limited, unreliable communication. We evaluated classical symmetric pairwise gossip among five agents initialized from frozen calibrated predictions in a synthetic adult sore-throat benchmark. Ninety runs across three fixed generator families supplied 270,000 underlying test encounters, each observed through four missingness views. Complete, ring and star graphs were compared at eight interaction budgets and transaction failure probabilities of 0, 0.2 and 0.5. The coordination extension was designed after inspection of the predictive benchmark and is exploratory. Outcomes were disagreement around the conserved arithmetic mean and its exact decomposition of mean-agent Brier error. In the base view at eight attempted pairs and 0.2 failure, disagreement variance was 0.000109 for the complete graph, 0.000134 for the ring and 0.000175 for the star. The paired complete-minus-ring difference was -0.000024 (95% Monte Carlo interval -0.000030 to -0.000019). The centralized mean had base Brier 0.069781, compared with 0.069368 for Kumo alone. Agreement therefore does not establish superiority to the strongest individual predictor. Code, fixed probability inputs and results support replay without model refitting. The study quantifies finite-budget coordination under specified simulation assumptions; it proposes no new gossip algorithm and establishes no clinical accuracy or utility.

---


### 129. [Cannot Wait to Verify: Parallel Drafting to Eliminate Verifier Idle Time in Speculative Decoding](https://arxiv.org/abs/2611.27477)

**<font color=#1a73e8>作者：</font>** Divya Jyoti Bajpai, Arun Verma, Manjesh Kumar Hanawal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive inference in large transformer models is limited by token-level sequential execution, resulting in high latency and low GPU utilization. Speculative decoding (SD) mitigates this bottleneck by introducing a draft-and-verifier model. However, the drafting stage remains sequential, leaving the verifier idle and underutilizing compute. To address this, we propose a plug-and-play drafting adaptive drafting method that parallelizes inference across transformer layers during draft generation. Starting from a shared hidden state, our approach evaluates multiple layers in parallel and verifies consistency by measuring divergence in hidden-state space. Layer-wise draft states are accepted when deviations are small; otherwise, a correction step is applied. By exploiting redundancy across transformer layers, our method accelerates draft generation and improves hardware utilization without modifying architectures or requiring retraining. Experimental results on NLP tasks show that our method speeds up the drafting stage by up to $1.65\times$ with minimal degradation in accuracy, while maintaining the same performance as SD.

---


### 130. [Verifying and Strengthening Neural Tangent Kernel Theory](https://arxiv.org/abs/2611.27487)

**<font color=#1a73e8>作者：</font>** Hao Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Writing
Neural tangent kernel (NTK) theory explains why very wide neural networks trained by gradient methods converge in the lazy-training regime. Its standard proof combines matrix concentration, random Gram matrices, continuous-time dynamics, spectral perturbation, and a bootstrap argument, but has lacked machine-checked verification. We present a Lean\~4 formalisation for two-layer networks, proving an end-to-end theorem: for a smooth bounded activation (instantiated with $\sigma=\tanh$), frozen biases, paired $\pm 1$ initialisation, and explicit width conditions, gradient flow exists uniquely with probability at least $1-\delta$, and
$$ \|r(t)\|^2 \leq \|y\|^2 e^{-\lambda_0 t/2}. $$
The sole data assumption is population NTK non-degeneracy, $\lambda_0>0$. Initial coercivity, kernel drift, the movement bootstrap, the residual ODE, and flow existence and uniqueness are formally proved.
The formalisation also sharpens the standard analysis in two ways. First, replacing the conventional matrix-Bernstein variance proxy with the classical row-covariance proxy yields estimated concentration-width certificates for $\tanh$ that are $36$--$53\times$ smaller at $(m,d)=(16,8)$ and $94$--$121\times$ smaller at $(32,16)$. Lean certifies the inequality; the ratios are numerical. Second, the network Hessian has operator norm $\Theta(\sqrt{p})$ on the sup-norm parameter ball (a paper calculation), preventing the expected $O(1/\sqrt{p})$ linearisation bound via sup-norm Taylor estimates. An $L^2$ parameter geometry resolves this issue. Required widths remain polynomial but far beyond practical scales, limiting applicability.

---


### 131. [Which Dwarf Is This? Doppeldwarf-306 and Near-Identical Instance Retrieval](https://arxiv.org/abs/2611.27490)

**<font color=#1a73e8>作者：</font>** Turhan Can Kargin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most established instance-retrieval benchmarks emphasise landmarks; small sculptures from visually similar series offer a complementary challenge. We introduce Doppeldwarf-306: 1,691 openly licensed photographs of 306 bronze dwarf statues in Wrocław, Poland, many made in themed series that share one style, with the photographer of each image recorded. With no training, nearest-neighbour search over frozen DINOv2 features names the right statue first for 93.1% of leave-one-out queries, and the best of thirteen backbones from seven pretraining paradigms reaches 94.7%. Accuracy falls slowly as candidates are added: for DINOv2, by about 0.8 points each time their number doubles. A natural design for a phone guide compares a photograph only with statues near the user. In simulation this helps, but less than an equal number of randomly chosen statues does, so random subsampling overstates its value; a permutation test ties the penalty to the real layout (p = 0.005). Used as a weight instead of a filter, location raises DINOv2 from 93.4% to 98.7% for a simulated user 25 m from the statue. With the query's photographer withheld, learned local-feature matching raises DINOv2 accuracy from 81.8% to 85.5% and also improves DINOv3. Comparing the two best candidates cuts DINOv2's false acceptance of unknown statues from 38.3% to 19.6% at 90% known acceptance.

---


### 132. [Learning Unknown Oscillators From Bandit Feedback](https://arxiv.org/abs/2611.27492)

**<font color=#1a73e8>作者：</font>** Priyank Jayraj, Poonam Goyal, Navneet Goyal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study semi-bandits driven by unknown oscillators. Each round, a learner selects two of four reward channels and observes their individual rewards. Frequency errors change future reward rankings and the resulting measurements. We show when committing to one fitted oscillator lets its greedy choices expose prediction errors. Our controller bounds reward loss (regret) over a continuous confidence set and holds the longest block within budget. An online regression policy gathers observations when the check fails. Regret grows at a square-root rate, up to logarithmic factors, across all frequencies and extends to two competing oscillators. On 96 fresh synthetic instances, checked commitment uses 49 fits instead of 1,023, with 1.5% higher mean regret than fitting every round. Matched isolated timings give a 4.69-fold speedup. The confidence sets also certify trajectory regret.

---


### 133. [Turnout: Adaptive Attention Switching for Efficient Reasoning](https://arxiv.org/abs/2611.27500)

**<font color=#1a73e8>作者：</font>** Anna Kuzina, Mart van Baalen, Paul N. Whatmough 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc transformer linearization replaces the key-value cache of full attention, which grows linearly with generation length, with a fixed size state. This change reduces memory consumption but often hurts accuracy. In reasoning tasks, which require long generations, this effect is especially pronounced. In this work we introduce Turnout, a method that mitigates accuracy loss as a result of linearization, while maintaining its memory-reduction benefits. We apply post-hoc linearization to a pretrained full-attention model, training a linear path through distillation while leaving the original full-attention path unchanged. During response generation, the resulting hybrid model retains both paths and uses a learned policy to control when each layer switches from full to linear attention. We train the policy with reinforcement learning using a reward that balances answer correctness and memory use. Empirical evaluation of our method shows that the learned adaptive policy achieves a better accuracy-efficiency Pareto frontier on reasoning tasks compared to fixed switching and static hybrid baselines.

---


### 134. [Solar-Conditioned Flow Matching for Multitemporal Aerial Visible-to-Infrared Image Translation](https://arxiv.org/abs/2611.27501)

**<font color=#1a73e8>作者：</font>** Wenwen Fang, Bingwei Hui, Xin Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial visible-to-infrared (V2IR) image translation provides scalable thermal data across the full diurnal cycle. However, existing methods predominantly learn a static mapping within narrow acquisition windows. As the thermal state evolves throughout the day, a single visible image may correspond to multiple plausible IR appearances, making V2IR translation an inherently multitemporal task. This letter proposes solar-conditioned latent flow matching (Solar-Flow), which upgrades aerial V2IR translation from static mapping to multitemporal generation. First, we design three computable physical factors, namely the solar elevation, the thermal phase clock (TPC), and the flight altitude. The TPC counts the elapsed heating and cooling hours on a continuous 24-hour axis anchored at sunrise, so the thermal state stays well defined even at hours without training samples. Second, we inject the condition into every Transformer block of a pretrained flow matching generator through adaptive layer normalization. This design preserves translation fidelity and enables multitemporal generation. Finally, we construct a paired aerial V2IR dataset covering 14 hour groups. Solar-Flow achieves multitemporal generation on this dataset, where a single visible image is translated into plausible IR images at multiple times of day, even at hours that were never seen in training.

---


### 135. [Self-Supervised Continuous-Time Depth Learning and Ego-Motion Estimation from Asynchronous Events](https://arxiv.org/abs/2611.27509)

**<font color=#1a73e8>作者：</font>** Sadiq O. Macaulay, Dipon Kumar Ghosh, Hadfield Simon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras register brightness changes pixel by pixel with microsecond precision, whereas the dense depth that could supervise them is costly to acquire and exists only at isolated instants. Condensing the stream into frames eases learning, but at the expense of the very timing that sets event sensing apart. We propose a self-supervised approach in which each event is assigned its own depth in continuous time, and the camera motion is recovered from the same observations. Supervision arises from geometry: lifted into 3D by its predicted depth and displaced by the camera motion at the instant it fired, an event should coincide with others produced by the same edge, so any misalignment exposes an error in depth or motion. Differentiable rendering then turns these per-event estimates into dense depth maps at target times within each window, faithful to the events behind them. On MVSEC, the approach outperforms prior event-only self-supervised methods in most sequences and depth ranges, with the widest margins at night, and recovers camera rotation more accurately than an earlier unsupervised event-based method. Ablations isolate the roles of local spatiotemporal context, the temporal backbone, and the alignment objective. These results position motion-compensated event alignment as a principled source of supervision for continuous-time depth and ego-motion estimation.

---


### 136. [Breaking the Barrier of Hard Samples: A Data-Centric Approach to Synthetic Data for Medical Tasks](https://arxiv.org/abs/2611.27511)

**<font color=#1a73e8>作者：</font>** Maynara Donato de Souza, Cleber Zanchettin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data scarcity and quality issues remain significant barriers to developing robust predictive models in medical research. Traditional reliance on real-world data often leads to biased models with poor generalizability across diverse patient populations. Synthetic data generation has emerged as a promising solution, yet challenges related to these samples' representativeness and effective utilization persist. This paper introduces Profile2Gen, a novel data-centric framework designed to guide the generation and refinement of synthetic data, focusing on addressing hard-to-learn samples in regression tasks. We conducted approximately 18,000 experiments to validate its effectiveness across six medical datasets, utilizing seven state-of-the-art generative models. Results demonstrate that refined synthetic samples can reduce predictive errors and enhance model reliability. Additionally, we generalize the DataIQ framework to support regression tasks, enabling its application in broader contexts. Statistical analyses confirm that our approach achieves equal or superior performance compared to models trained exclusively on real data.

---


### 137. [PGS-PCQA: Perceptually Gated Synthetic Supervision for No-Reference Point Cloud Quality Assessment](https://arxiv.org/abs/2611.27512)

**<font color=#1a73e8>作者：</font>** Qinyuan Fan, Meng Zhang, Clemens Gühmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing no-reference point cloud quality assessment (NR-PCQA) methods perform well within individual datasets but generalize poorly across datasets. We identify insufficient distortion coverage in training data as a key cause: on unseen distortion types, models rank severity levels near chance or even in reverse. We propose perceptually gated synthetic supervision for no-reference point cloud quality assessment (PGS-PCQA), an NR-PCQA model trained with synthetic distortion ranking. It builds a synthetic distortion bank from source reference point clouds and uses within-type severity ranking as supervision in addition to the source mean opinion scores (MOS), requiring no subjective scores for the synthetic samples. Since higher severity does not always mean lower perceived quality, a perceptual gate softens the ranking targets of pairs with small perceptual differences in rendered views. The synthetic supervision is used only during training and needs no target-domain data. In a single training run on SJTU-PCQA, PGS-PCQA achieves Spearman rank correlation coefficients (SRCCs) of 0.709 on WPC and 0.751 on BASICS. The corresponding published DSP-PCQA scores are 0.595 and 0.723. Under reference-disjoint cross-validation, PGS-PCQA achieves SRCCs of 0.955 on SJTU-PCQA, 0.934 on WPC, 0.906 on BASICS, and 0.791 on LS-PCQA Part I. In the exclusion experiment, the reported scores for the reduced synthetic bank represent 58-65% of the full-bank SRCC gain relative to training without the bank. Code is available at this https URL.

---


### 138. [PhiJEPA: Denoising Latent Predictions for Visual Representation Learning](https://arxiv.org/abs/2611.27516)

**<font color=#1a73e8>作者：</font>** Makoto Yamada, Yao-Hung Hubert Tsai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can a predictor trained to infer hidden image regions still help a world model plan when part of an object disappears from view and the visible context is blurred? We introduce PhiJEPA, a joint-embedding predictive architecture that adapts PhiNet's two-stage prediction to masked Transformers. From sparse, photometrically corrupted context, a Transformer block predicts hidden tokens of an independently corrupted teacher view. A token-wise MLP then maps these predictions to clean teacher tokens. Controlled ablations show that the combined objective improves dense features over the tested one-stage alternatives. Pre-trained on ImageNet-1K with $5.6\times10^{19}$ training FLOPs, PhiJEPA achieves 69.3 mIoU on linear PASCAL VOC segmentation, exceeding the evaluated I-JEPA and DSeq-JEPA checkpoints in segmentation accuracy, with 25\% fewer training FLOPs than I-JEPA. It also improves hidden-region segmentation over Simple I-JEPA (49.1 vs.\ 44.3 mIoU). As an application, we use the frozen encoder in DINO-WM on PushT, and reuse the pre-training predictor, which JEPAs usually discard, to complete occluded tokens without fine-tuning. In open-loop planning with simultaneous object occlusion and Gaussian blur ($\sigma=2$ pixels), predictor completion raises success from 33\% to 65\%, compared with 25\% for Simple I-JEPA with its predictor and 40\% for iBOT with pixel inpainting. Together, these results support two-stage latent prediction as an efficient approach to learning visual representations that remain useful under photometric degradation and support completion under partial observation.

---


### 139. [On the Limits of Observability for Evaluating Coverage in Machine Unlearning](https://arxiv.org/abs/2611.27543)

**<font color=#1a73e8>作者：</font>** Ziluowen Luo, Jun Yin, Songyang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove the influence of any requested subset of training data while preserving utility on the remaining data. Empirical evaluations measure predictive accuracy and infer training-set membership (MIAs) from model outputs or intermediate activations. However, by focusing on selected forget sets, these evaluations can overlook Coverage, the range of requests a method can fulfill. To assess this coverage, we first conduct a stress test of observability with 502 retrained models, finding that hidden embeddings reveal known deletions missed in predictions. To characterize capacity limits on coverage, we show that distinguishing all $n$ singleton deletions with linear scores can require a shared representation of rank $\Omega(\log n)$. We further extend the bound to arbitrary subsets and show when partial deletion can appear complete. Building on this analysis, we propose CEO, a framework for evaluating unlearning coverage under limited observability. Its compositional color-shape benchmark makes forgetting and retained utility measurable from the full output distribution and provides a leave-one-out retraining oracle for each target. From a fixed number of oracle observables, we estimate empirical target coverage, the fraction of targets reliably flagged when deleted and rarely flagged under any other deletions. To recover missed deletions, CEO further expands each observable representation into high-dimensional activation space with the frozen encoder of a SAE trained on the original model. Extensive experiments of 20 baselines shows that even on this simple synthetic task, only retraining from scratch covers all deletion targets.

---


### 140. [Alliance Rupture and Repair in Simulating Cognitive Behavioral Therapy Dialogues](https://arxiv.org/abs/2611.27544)

**<font color=#1a73e8>作者：</font>** Jian Chai, Yitian Yang, Siqi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In cognitive behavioral therapy (CBT), routine work can strain the client-counselor working alliance, and the counselor must then notice the rupture, repair it, and adapt the work that follows. Existing CBT simulators model client resistance and follow structured treatment plans, but rarely track alliance state or allow counselors to repair ruptures over multiple turns and revise their plans accordingly. We present ALLY, a simulation framework that brings alliance rupture, repair, and replanning into ongoing CBT dialogue. Each client has a hidden alliance state that governs how openly the client engages. Like a real counselor, the counselor agent sees only the dialogue. It must notice when the client pulls back or pushes against the work, repair the rupture, and replan the rest of the session around what it has learned. Automatic evaluation shows that ALLY's counselors are closer to real CBT counselors than those of existing public synthetic datasets in strategy flow and emotional dynamics, and that ALLY is rated highest overall in counseling quality (CTRS) and interpersonal skill (FIS-T). An expert evaluation with 20 licensed therapists also finds the simulated ruptures plausible and the repairs and replanning largely appropriate.

---


### 141. [Epistemic Social Learning: Latent Behavioral Structure under Endogenous Multi-Agent Interaction](https://arxiv.org/abs/2611.27545)

**<font color=#1a73e8>作者：</font>** Jainendra Shukla, Dhruv Jaiswal, Divyanshi Beniwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In multi-agent interaction, a learner's actions shape the observations from which it infers other agents' behavior. A behavioral model may predict these observations well yet support poor adaptation when opponents change. We introduce Epistemic Social Learning (ESL), which couples fast, interaction-specific Bayesian beliefs with slower online learning of population-shared behavioral prototypes. Belief-conditioned decisions influence subsequent observations and, in turn, the representations learned from them. Under explicit regularity and averaging assumptions, we provide a conditional stochastic-approximation characterization of these coupled dynamics. Across twelve synthetic $3\times3$ cooperative, coordination, and adversarial games, ESL achieves the lowest aggregate post-switch regret among the evaluated online latent-adaptation methods, including a switch-aware Bayesian filter. Additional experiments examine observation loss, noise, and asymmetric incentives. These findings illustrate how predictive fit can differ from decision-relevant adaptation under policy-dependent interaction.

---


### 142. [GameScrub: Learning HUD Removal from Real Gameplay with Recovered Targets](https://arxiv.org/abs/2611.27547)

**<font color=#1a73e8>作者：</font>** Mohammad Areeb Qazi, Yiyan Hu, Yanan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gameplay videos are a rich source of experience for learning virtual-world dynamics, yet their frames contain heads-up displays (HUDs) that follow interface rules rather than scene dynamics. Removing HUDs would make this footage directly usable for learning world dynamics. However, training a removal model requires paired clips with and without HUDs, whereas real recordings contain only HUD-overlaid footage. Existing work synthesizes pairs by compositing HUD graphics onto HUD-free footage, requiring a separately curated clean corpus and producing HUDs that only approximate real ones. Models trained on such pairs leave 40 to 50% of real HUD elements untouched. We instead recover pseudo-clean targets directly from real recordings by inpainting HUD regions with a pretrained video diffusion model. Preventing HUD traces from leaking into recovered targets is challenging because latent video autoencoders mix information across mask boundaries. Our training-free recovery pipeline, GameScrub-Data, pre-fills HUD regions with flow-guided background estimates before encoding, excludes HUDs from scene conditioning, and confines restoration to masked regions through pixel-space compositing. The resulting pairs train GameScrub, a video diffusion removal model that handles diverse HUDs without inference-time masks or clean reference images. On the in-the-wild Game2World benchmark, GameScrub achieves an artifact-adjusted removal score of 71.95, compared with 57.86 for the strongest reference-free GameCleaner configuration, and removes 90.06% of annotated HUD elements versus 59.07%. These results demonstrate that real recordings with recovered targets can support effective HUD removal, advancing HUD-free gameplay data for world models and controllable video generation.

---


### 143. [Minimax-Optimal Small-Loss Regret in Online Convex Optimization and Applications to Contextual Search and Online Inverse Optimization](https://arxiv.org/abs/2611.27572)

**<font color=#1a73e8>作者：</font>** Shinsaku Sakaue  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We give small-loss regret bounds for online convex optimization (OCO), using one subgradient per round. Let $\Delta_T^\star$ denote the cumulative loss of the best fixed decision in hindsight, measured relative to the per-round minima. Our algorithm achieves the regret bound $O(1+\sqrt{\Delta_T^\star})$ without knowing $\Delta_T^\star$, up to domain and gradient-scale factors. The bound is minimax optimal, including its domain dependence, on $\ell_p$ balls for every $1\le p\le\infty$. No smoothness or condition bounding gradient norms by loss values is assumed, and neither loss values nor the time horizon are needed. Algorithmically, we extend the metric-update revocation of Gupta et al. (2026), originally developed for online inverse optimization, to general OCO using the follow-the-regularized-leader framework and a mixture of multiple base learners. We also apply our algorithm to contextual search and online inverse optimization. In $d$-dimensional contextual search with comparison flips of unknown bias $\kappa>0$, we obtain minimax expected cumulative absolute error $\Theta(\sqrt{d}/\kappa^2)$ under Euclidean normalization using polynomially many arithmetic operations, resolving an open question of Liu et al. (2021). For online inverse optimization with the Euclidean unit-ball utility domain, our algorithm bounds the regret relative to observed actions by $O(\sqrt{d}+d^{1/4}\sqrt{D_T})$, where $D_T$ is their cumulative suboptimality; this matches the regret rate of Gupta et al. (2026) when $D_T=0$. Our guarantee extends to other utility domains; for example, on the probability simplex, the bound improves to $O(\log(d+1)+\sqrt{D_T\log(d+1)})$.

---


### 144. [Leakage-Free Is Not Confounder-Free: What a Patient-Level Split Cannot Certify About a Medical Imaging Benchmark](https://arxiv.org/abs/2611.27585)

**<font color=#1a73e8>作者：</font>** Ignazio Gallo, Mattia Gatti, Leonardo Sgroi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Patient-level splitting is the standard safeguard against subject leakage in medical imaging evaluation, but it cannot remove a confounder that every fold inherits: an acquisition variable aligned with the diagnosis across the whole cohort. We present a five-question audit of a candidate confounder: how well it predicts the diagnosis, whether it can be decoded from the images, whether diagnostic scores depend on it, whether the image adds predictive value beyond it and how much discrimination survives once it is controlled. We apply it to DMR-IR, the public dataset on which most machine-learning results in breast thermography rest. On 236 patients under a strict patient-disjoint protocol, the acquisition date alone predicts malignancy at AUROC 0.980, above the best of nine imaging arms (0.949), because benign and malignant patients were recruited in different years. The acquisition year is decodable from the pixels among patients who share a diagnosis, largely through a global thermal offset outside the breast, yet only one arm, the one pooling every frame of a visit, demonstrably carries it into its diagnostic score. No arm improves on the date on paired folds, and once the date is controlled, discrimination either collapses or survives only on comparisons the benchmark cannot attribute. The dataset contains only eight cross-label same-date pairs, from ten patients, which limits reliable evaluation within recorded acquisition-date groups. A second, independently acquired cohort, whose dominant channel is patient age, returns the same audit outcome from a different confounder. Mitigation may suppress such a confounder, but without cross-label acquisition support no evaluation on the benchmark can certify that what remains is pathology.

---


### 145. [Quantum-Informed Regularized Poisson Learning for Graph-Based Semi-Supervised Classification](https://arxiv.org/abs/2611.27609)

**<font color=#1a73e8>作者：</font>** Hamed Gholipour, Farid Bozorgnia, Hamzeh Mohammadigheymasi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce IPQSSL, a quantum-informed regularized Poisson framework for graph-based semi-supervised classification under scarce labels. Local graph feature contexts are QR factorized, lifted to unitary encodings, and processed by a shared variational circuit whose measurements yield node wise diagonal weights that stabilize a symmetrized Poisson system. We establish positive definiteness of the symmetrized, regularized operator under explicit spectral conditions and derive a Hermitian, block encoding compatible formulation that separates the classical NISQ oriented implementation from a future fault-tolerant pathway. Across seven benchmarks spanning tabular data and a citation network, the effect of regularization is dataset- and budget-dependent: IPQSSL improves over the Poisson baselines on Iris and Wine at all but the single-label budget, reaching 0.946 accuracy on Iris at ten labels per class and at every budget on German Credit, where, however, all methods remain below the majority class rate. Original Poisson remains preferable on Breast Cancer, Heart Disease, Optdigits, and Cora, with the deficit narrowing as the label budget grows on the two largest graphs. Ablations attribute the gains to diagonal stabilization rather than variational training. The result is a resource transparent bridge between Poisson graph learning and quantum linear algebra, with an explicit empirical delineation of when diagonal regularization helps.

---


### 146. [Circular Predictive Coding Unlocks Effective Depth](https://arxiv.org/abs/2611.27610)

**<font color=#1a73e8>作者：</font>** Tommaso Salvatori, Matteo Forasassi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive coding networks perform credit assignment through an energy minimization process. Despite their ability to train models with arbitrary network topologies, they have mostly been used to train feedforward architectures to match the performance of backpropagation. However, they fail to do so when the models become too deep, because error signals become unstable or vanish as they travel through many layers. We address this limitation with circular networks, which get their depth directly from the energy minimization, rather than from stacking layers. Formally, we prove that convergence to an equilibrium of the energy functional of a circular predictive coding network approximates the fixed-point iteration process of a deep equilibrium model, showing that circularity alone suffices to unlock effective depth. Empirically, we show that circular models (i) outperform other predictive coding models of the same size on image classification tasks, matching the accuracy of state-of-the-art predictive coding ResNets and VGG networks despite having substantially fewer parameters; (ii) solve constraint satisfaction problems that require many steps of iterative reasoning, a task not feasible with feedforward models at all, reaching 99.3% test accuracy on Sudoku-hard via nested energy minimization loops; and (iii) scale to autoregressive language modeling by training a circular transformer on TinyStories and WikiText-103, before out of reach for predictive coding models. These results have direct implications for physical neural networks, where computational depth can be traded for recursion on a fixed-size circuit.

---


### 147. [GAZEAIDE: Recording Gaze Context for Research on AI-Assisted Development](https://arxiv.org/abs/2611.27614)

**<font color=#1a73e8>作者：</font>** Heidi Albarazi, Ilya Zakharov, Ekaterina Koshchenko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Developers increasingly review code they did not write, much of it generated by AI. Where they look while reading may indicate what is relevant to them, but tools rarely have access to this information. We demonstrate GAZEAIDE, an open-source research prototype for collecting it. Using a webcam, GAZEAIDE estimates which parts of the code a developer looks at and for how long, and records this viewing history together with the text shown on screen. Such context can serve different purposes: providing visual feedback on what has been viewed, guiding code review, and preparing context for a question, which a developer can choose to send to an AI assistant. An IntelliJ plugin records work in the editor; a browser companion records assistant conversations. Attendees can record a short session, replay their viewing history, and try these scenarios.

---


### 148. [Benchmarks' Last Exam](https://arxiv.org/abs/2611.27622)

**<font color=#1a73e8>作者：</font>** James Zhu, Zekki Cat  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Public benchmarks guide model selection, post-training rewards and claims of progress in artificial intelligence, yet leaderboards report aggregate scores without verifying whether each task's prompt, environment and grader agree on what counts as success. How often that agreement fails in contemporary evaluations, and in which direction confirmed defects move scores, has remained unmeasured across grading designs. Here we synthesize task-level quality reviews of 749 tasks across eight frontier benchmarks and 767 public model evaluations spanning closed-form question answering, document rubrics and agentic execution to assess whether prompts, environments and graders align. Task validity stratifies sharply by grading architecture. Closed-form benchmarks revised after public error reporting reach 92.5% verified validity, compared with 29.3% across six multi-step suites that nevertheless already supply 161 verified complex tasks. Rubric suites fail through mismatches between prompts and reference checklists, whereas execution harnesses add incomplete state assertions, shared-channel leaks and grading-time collisions. Across confirmed defects, 71.7% withhold credit from compliant solutions while 28.3% permit shortcut passes, indicating that raw leaderboard ceilings understate frontier capability on many practical tasks. Grading committed patches inside a fresh container cuts confirmed runtime bypasses from 14.7% in shared containers to 2.7% (a 5.5x drop, and 0% in read-only or static suites), showing how targeted maintenance restores existing benchmarks at low cost. As the initial milestone of the long-term Benchmarks' Last Exam initiative, this synthesis launches sustained expansion across wider benchmark coverage and deeper evaluation-quality dimensions so that pursuing leaderboard gains directly advances genuine model capability.

---


### 149. [Points, Not Pixels: Keypoints, Masks and Oblique Geometry for Floating-Roof Tank Fill Estimation from Overhead Imagery](https://arxiv.org/abs/2611.27624)

**<font color=#1a73e8>作者：</font>** Mohd Shahid Kaleem, Mohd Hozaifa Khan, Maaz Khan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The floating roof of an oil storage tank rests on the stored liquid, so its depth below the rim measures how full the tank is. In optical overhead imagery, this depth appears only as the crescent shadow the rim casts on the roof, often a few pixels wide. Thin shadows are difficult to measure at overhead-image resolution, and nadir-based height conversions introduce errors in oblique views. Under a local affine camera, roof depth determines the rim-to-shadow displacement through the sun and camera geometry. We regress the boundaries as sub-pixel keypoints and invert this relation with a closed-form estimator that models oblique views. Available public tank datasets do not label roof position, so we introduce SynTank-25k, 24,987 physically based renders with exact roof, shadow and camera geometry. Using the oblique estimator, the keypoint pipeline reduces fill error by $22\%$ relative to the segmentation baseline on SynTank-25k. On shadows narrower than $6\text{ px}$, its error is also lower than that obtained by converting true binary masks. Our oblique estimator reduces the error of the nadir formula elevenfold at the steepest views. On 6,558 real NAIP tank crops defined by bounding boxes, about half of the fill estimates pass internal consistency checks; NAIP has no fill labels. Data and code will be released.

---


### 150. [Manipulation-resistant reputation for peer-to-peer scientific publishing: a combination-therapy approach](https://arxiv.org/abs/2611.27625)

**<font color=#1a73e8>作者：</font>** Frédéric Prost  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In open peer-to-peer networks, where publishing is nearly free and identities are cheap, reputation systems decide what deserves attention, and their metrics become targets for manipulation. We study how to choose and combine reputation signals so that manipulation does not pay while genuine contribution does. Inspired by combination therapies in medicine, we describe each gaming action by its effects on all signals. For aggregation by the minimum of the signals, we prove that, in a global linear model, either some mix of gaming actions raises every signal by more than it costs, or the net gain of gaming is bounded by the imbalance of the attacker's honest profile; locally, gaming brings no first-order gain exactly when an admissible weighting is supported on the attacker's weakest signals. We then specify, without implementing it, MagMell, a two-tier system for peer-to-peer scientific publication: a protocol that orders signed events by Byzantine fault-tolerant consensus, enforces budgets and settles staked assessments, and open reputation algorithms that any node can run. Simulations on synthetic data show that minimum aggregation makes networks of fake identities, collusion rings and floods of generated papers lose rank beyond small intensities, at the price of a lower correlation between rank and quality for honest accounts. They also show that criticism is rarely settled, because the evidence needed is seldom available. The replicated log should grow by about 26 kilobytes per identity and year (analytic estimate), and a full recomputation of reputations takes 1.0 to 1.6 seconds for 100,000 identities (measured).

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-206](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
