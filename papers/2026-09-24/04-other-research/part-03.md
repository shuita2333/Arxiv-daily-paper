# 📦 其他研究 | 2026年09月24日

> 本类共 **275** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-275](./part-06.md)

---

### 101. [OmniFysics-Nano-V2 Technical Report: Understanding the Physical World Across Modalities](https://arxiv.org/abs/2609.25738)

**<font color=#1a73e8>作者：</font>** Yizhou Liu, Jinghang Han, Kaixiang Qiu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Omni-modal models have expanded multimodal interaction across vision, audio, speech, and language. However, their training is predominantly organized around semantic descriptions and general-purpose objectives, leaving physical attributes, interaction states, and causal mechanisms only partially specified. This gap is not simply a matter of modality coverage: adding more modalities does not by itself provide the supervision needed to connect observations with the physical structure of the world. We present OmniFysics-Nano-V2, a compact omni-modal model for physical-world perception and understanding. The model supports image, video, audio, speech, and text inputs within a shared reasoning framework, together with text and speech generation. To address the lack of explicit physical supervision, we construct a dual-branch physics-aware data pipeline that grounds salient objects in structured physical attributes and aligns visual changes with acoustic events, intermediate responses, and interaction outcomes. To address homogeneous training objectives, we curate reinforcement-learning prompts by reward diversity and adopt a two-stage Group Relative Policy Optimization curriculum that progresses from general task correctness to fine-grained physical perceptual reasoning. Experiments across multimodal, audio-visual, and physical reasoning benchmarks show that the proposed data and training strategy improves physical-world understanding while preserving broad omni-modal competence. The proposed model achieves leading result on 17 of 21 benchmarks against SOTA omni-modal models. By equipping AI systems with both omni-modal and physical-world perception capabilities, OmniFysics-Nano-V2 is poised to become a cornerstone of next-generation Physical AI.

---


### 102. [Fysiverse-3D-Vision Technical Report: Generating Executable 3D Worlds from Images through Unified Spatial Reasoning](https://arxiv.org/abs/2609.25741)

**<font color=#1a73e8>作者：</font>** Dingkang Yang, Yizhou Liu, Wendong Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models have advanced image-conditioned 3D content creation, yet generating controllable and executable 3D scenes from a single image remains challenging. Existing 3D generative approaches can synthesize visually plausible objects and scenes, but their spatial layout estimation is coupled with specific asset generators. They struggle to jointly model object semantics, metric geometry, and scene-level spatial relationships, which are essential for interactive editing, physical simulation, and embodied applications. We propose Fysiverse-3D-Vision, a unified vision-language-geometry framework for generative 3D scene reconstruction and executable asset construction from a single image. We establish a shared representation where spatial reasoning and geometric reconstruction mutually enhance each other, allowing object layouts to be inferred beyond the constraints of individual asset generators. Our model integrates textual supervision, semantic visual cues, and geometric representations within a unified Transformer to capture scene context, metric geometry, and object-level interactions. An object-conditioned layout module performs cross-attention between target object representations and global geometric features to predict object translation, rotation, and scale. Training progressively learns geometry-language alignment, introduces layout reasoning while preserving reconstruction capability, and refines physical consistency through collision-aware optimization. By separating spatial layout reasoning from asset synthesis, Fysiverse-3D-Vision provides an adaptable interface for interactive scene editing, object-level manipulations, and executable 3D content generation. Experiments demonstrate that our framework achieves superior geometric consistency, layout estimation, rendering quality, and physical property understanding compared with existing approaches.

---


### 103. [SAMI3D-DW: Interactive Segmentation of Any 3D Medical Images](https://arxiv.org/abs/2609.25743)

**<font color=#1a73e8>作者：</font>** Ping Gong, Shiyuan Su, Fandong Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive segmentation of 3D medical images supports quantitative analysis of anatomical structures and disease while allowing users to specify and refine their targets.
Despite substantial progress by nnInteractive and VISTA3D, reliable segmentation across diverse clinical targets remains challenging, particularly for complex anatomical
structures and the heterogeneous, long-tailed spectrum of pathology. We present SAMI3D-DW V1 (hereafter SAMI3D-DW), an interactive 3D segmentation model trained on
Deepwise's large-scale proprietary medical image datasets. We evaluate the model under simulated user interactions on a CT/MR benchmark comprising 4,326 cases from 219
source datasets, spanning 107 anatomical and pathological categories, organized by a medical taxonomy and evaluated with a category-balanced DSC score. SAMI3D-DW achieves
the highest category-macro Dice among evaluated methods in both interaction modes. With one point, it scores 0.5764 versus 0.5315 for nnInteractive, the strongest
baseline, rising to 0.7771 versus 0.7494 with five points. With bounding-box initialization, the scores are 0.7130 versus 0.6530. After five corrective clicks, SAMI3D-DW
reaches 0.8002 versus 0.7868, making it the only evaluated box-compatible model to exceed 0.80. For radiologists and clinicians, SAMI3D-DW enables segmentation of complex
anatomical structures, including intracranial vessel trees on CT and MR angiography, with a few clicks. In a preliminary in-house comparison involving neurofibromatosis
type 1 (NF1), SAMI3D-DW-assisted tumor annotation took minutes per case and approximately one-fifteenth of the time required for manual annotation, highlighting its
potential to support volumetric treatment-response assessment.

---


### 104. [Minimal Recurrent Behavioral Memory for Imitation under Partial Observability](https://arxiv.org/abs/2609.25757)

**<font color=#1a73e8>作者：</font>** Xianyao Li, Fang Xu, Rui Min 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What is the least recurrent memory needed to reproduce a specified expert under partial observability? The instantaneous requirement is the conditional entropy of the expert's behavioral quotient, but recurrence must also preserve distinctions that future observations will not restore before use. We characterize this minimal recurrent behavioral memory by a compatibility relation: under transitivity its classes attain the exact minimum, while the general case is an entropy minimization over closed compatible state assignments, with exact certificates on finite instances. A sole-carrier measurement protocol separates behavioral sufficiency, excess code rate, and information carried by observations or other memory paths; experimental bit requirements refer to the induced symbolic behavioral model under the stated occupancy. Across manipulation tasks, learned code rates remain near zero- and two-bit requirements as hidden modes grow to $512$, and anticipatory memory follows a $2\to1\to0$ requirement despite zero instantaneous demand during waiting. Learning this representation remains difficult: event-agnostic future-behavior supervision yields $36/40$ sufficient seeds with one frozen configuration and improves the longest-horizon pixel setting from $0/8$ to $6/8$ sufficient held-out seeds (closed-loop success from $0.08$ to $0.57$). On unmodified community benchmarks, the protocol certifies delay-independent requirements, which sufficient codes match at mid-delay. The supervision aids commitment but can induce predictive surplus; annealing it lets imitation and rate training reduce that surplus, separating the information-theoretic target from the ability to learn it.

---


### 105. [Neurosymbolic Action Model Learning under Partial Observability](https://arxiv.org/abs/2609.25766)

**<font color=#1a73e8>作者：</font>** Adem Kikaj, Lennert De Smet, Giuseppe Marra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI planning studies how an agent can reach a goal by executing a sequence of actions. To plan correctly, the agent needs an action model describing when each action can be executed and how it changes the world. Constructing such models by hand requires domain expertise, and can be costly and error-prone. Action models can instead be learned from available data using existing neurosymbolic approaches, but they currently assume access to complete traces of fully observable images . These approaches fail to learn action models under partial observability where some of the images might not be present or are not fully informative of the current state of the world. Hence, this paper proposes NeSyAM, a novel neurosymbolic modeling paradigm for action model learning under partial observability. In addition, the paper presents a unified variational framework for theoretically analysing the limitations of existing methods compared to our proposed approach. NeSyAM is then tested extensively on six visual planning domains and three observation regimes to show it consistently recovers relevant parts of the true action model under partial observability.

---


### 106. [Towards Omni-dimensional GUI Agent Navigation with Masked Trajectory Prediction](https://arxiv.org/abs/2609.25769)

**<font color=#1a73e8>作者：</font>** Yan Zhang, Pei Fu, Daiqing Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graphical User Interface (GUI) Agents autonomously interact with software to fulfill user requests, where GUI navigation stands out as the most critical and challenging capability. Mastering this capability demands a complex synergy of step-wise decision-making, state-action alignment, and long-horizon planning. While directly mixing these corresponding navigation tasks seems intuitive to simultaneously acquire these skills, such a direct combination is severely bottlenecked by inconsistent optimization objectives and profound data heterogeneity. To overcome these barriers, we propose the MaP (stands for ``\textbf{M}asked Tr\textbf{a}jectory \textbf{P}rediction''), a unified framework that seamlessly harmonizes divergent GUI navigation tasks. By modeling multi-turn GUI interactions as a trajectory and defining training objectives through component masking and prediction, MaP shifts the optimization from task-specific marginal distributions to a consistent objective. Furthermore, to handle the data heterogeneity across multiple navigation tasks, we design a role-aware adapter learning module that dynamically routes each token to a specialized representation space. Extensive experiments on five representative GUI navigation benchmarks demonstrate that MaP effectively mitigates gradient conflicts and significantly outperforms the direct mixture training, establishing a robust paradigm for multi-task GUI navigation.

---


### 107. [TRACE: Trajectory Representation and Consistency Estimation for AI-Generated Video Detection](https://arxiv.org/abs/2609.25775)

**<font color=#1a73e8>作者：</font>** Huangsen Cao, Hongkang chu, Siyao Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative video models have enabled the synthesis of visually realistic content, posing significant challenges to synthetic video detection. Existing detectors often rely on appearance artifacts, semantic inconsistencies, and temporal patterns that may be generator-specific, limitating generalization to unseen synthesis models. We investigate whether responses to a pretrained generative model provide more transferable forensic cues. Our key observation is that real and AI-generated videos exhibit distinct \emph{velocity responses} under a pretrained Flow Matching video model. This distinction persists when different pretrained video-generation backbones are used as probes, suggesting that velocity responses offer transferable forensic signals beyond visual artificts. Motivated by this observation, we propose \textbf{TRACE} (\emph{\underline{T}rajectory \underline{R}epresentation \underline{a}nd \underline{C}onsistency \underline{E}stimation}), a generation-process-aware framework for AI-generated video detection. TRACE leverages a pretrained video DiT as a velocity-field probe to extract representations at multiple flow time points, and models cross-frame consistency through velocity differences between adjacent frames. We further introduce a \emph{Real-Centered Trajectory Optimization} objective that encourages generator-invariant representation learning. Extensive experiments on AIGVDBench demonstrate that TRACE generalizes effectively across diverse generators, substantially outperforming prior state-of-the-art methods on unseen open- and closed-source video generation models.

---


### 108. [Disentangling Heterogeneous Traffic Dynamics for Multi-Step Traffic Forecasting via Adaptive Spectral Decomposition](https://arxiv.org/abs/2609.25777)

**<font color=#1a73e8>作者：</font>** Zijun Huang, Chenrui Fu, Wenhao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate multi-step traffic forecasting remains challenging because observed traffic signals contain heterogeneous temporal dynamics with different characteristics and levels of predictability. Existing approaches typically model these dynamics within a unified representation or rely on predefined decomposition rules, which may limit their ability to flexibly separate persistent patterns from rapidly varying fluctuations. To address this issue, we propose the Adaptive Decomposition Network (ADNet), a component-specific forecasting framework that adaptively disentangles traffic dynamics into dominant and residual components. ADNet introduces a learnable complementary spectral decomposition mechanism that determines the contribution of each frequency bin to the two components. Unlike hard frequency partitioning, every frequency bin can contribute to both components with different learned proportions, allowing the decomposition to be optimized jointly with the forecasting objective. The reconstructed components are then modeled by two dedicated spatiotemporal forecasting branches, and their predictions are integrated to generate the final multi-step forecast. Experiments on the Alameda and Orange regions of the TraffiDent dataset show that ADNet achieves the best performance in 20 of the 24 reported region-horizon-metric comparisons, with particularly clear gains at longer forecasting horizons. Capacity-controlled ablation experiments further show that the learnable decomposition substantially outperforms a fixed decomposition and provides additional improvements beyond the dual-branch architecture alone. These results demonstrate the effectiveness of adaptive decomposition and component-specific modeling for multi-step traffic forecasting.

---


### 109. [A Lightweight Plastic-Memory Framework for Graph Few-Shot Class-Incremental Learning](https://arxiv.org/abs/2609.25781)

**<font color=#1a73e8>作者：</font>** Zihan Mei, Zhili Qin, Tongze Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Incremental Learning has garnered increasing attention as dynamic graph data continues to emerge across diverse fields. Conventional approaches primarily address catastrophic forgetting by preserving node-related knowledge through replay or distillation techniques; however, they often incur high computational costs and inefficiency. This issue is further exacerbated in real-world scenarios where labeled data for new classes is scarce. In this paper, we propose a novel lightweight plastic-memory framework specifically designed for few-shot incremental learning on graphs. The core idea of our framework is the construction of a plastic-memory module that evolves over time, continuously updating and expanding its memory to accommodate new classes while retaining previously learned knowledge. In contrast to existing techniques, our memory module is both lightweight and effective, featuring an innovative evolving micro-clustering structure that dynamically updates representations of class prototypes, sub-prototypes, and their interaction weights. Building on this memory module, we introduce a memory-driven meta-learning framework that enhances adaptability to new tasks in its inner loop while maintaining stability for earlier tasks in the outer loop. Extensive experiments on four benchmark datasets demonstrate the framework's superior performance in balancing stability for old knowledge and adaptability to new knowledge.

---


### 110. [Adaptive Traffic Camouflage: Causal and Resource-Aware Defense Against IoT Fingerprinting](https://arxiv.org/abs/2609.25787)

**<font color=#1a73e8>作者：</font>** Daniel Adu Worae, Spyridon Mastorakis, Nuno Moniz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Encryption hides IoT payloads, but traffic shape can still reveal device identity through packet sizes, timing, direction, and packetization. We present Adaptive Traffic Camouflage, a causal, leakage-aware controller that characterizes traffic-shape leakage without runtime device labels and selects a budget-feasible transformation for the next traffic window from previous-window context. The controller chooses among padding, packet splitting, timing, and composite transformations, or leaves traffic unchanged when camouflage is unnecessary. We evaluate the design on CIC-IoT-2022, IoT Sentinel, and UNSW using classical and sequence-based fingerprinting models under clean-trained, defense-aware, and incremental-exposure settings, with fixed, random, and mean-bandwidth-matched baselines. Under the Balanced profile, camouflage reduces mean Macro-F1 by 13.2-23.3% relative to clean traffic with 4.88-7.47% average bandwidth overhead and at most 0.64 ms added latency. Under the larger Privacy profile, the reduction increases to 28.0-43.5%. Defense-aware training recovers much of the lost attacker performance on CIC-IoT-2022 and UNSW, while IoT Sentinel retains a substantial privacy gap. A non-causal same-window reference provides only modest additional benefit over previous-window control, and metadata-rich attackers remain effective outside the targeted traffic-shape surface. These results show that causal, resource-aware camouflage can reduce IoT traffic-shape fingerprintability under explicit communication constraints, while the persistence of protection depends on how readily the defended distribution can be learned.

---


### 111. [When Point Clouds Outperform Pixels: Rethinking Zero-Shot Multimodal Anomaly Detection](https://arxiv.org/abs/2609.25793)

**<font color=#1a73e8>作者：</font>** Chenglin Ye, Lupeng Liu, Dongbo Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot multimodal anomaly detection commonly assumes that RGB and point cloud modalities are equally reliable and can contribute uniformly to anomaly localization. We challenge this assumption. Using a set of recently proposed stringent metrics that penalize false anomaly responses in normal regions, we find that point clouds are substantially more reliable than RGB under zero-shot category shift. Motivated by this observation, we propose WOOPS (\textbf{W}hen P\textbf{o}int Cl\textbf{o}uds Out\textbf{p}erform Pixel\textbf{s}), a reliability-aware zero-shot multimodal anomaly detection framework. To strengthen the more reliable geometric modality, we design a Multi-view Information Decoupling module to suppress heterogeneous information from multi-view point cloud projections and enhance point cloud feature quality. To avoid unconditional fusion, we further introduce a Modality Reliability Calibration module to adaptively calibrate modality contributions according to their reliability. Extensive experiments show that our method achieves the best or competitive performance under the new metrics in both unimodal and multimodal settings. Further analysis demonstrates that point cloud information also improves RGB-only inference, while ablations verify the effectiveness of both modules. Code will be released upon acceptance.

---


### 112. [LiFR v2: Completion-Augmented Event Propagation for High-Rate Dense Prediction](https://arxiv.org/abs/2609.25803)

**<font color=#1a73e8>作者：</font>** Tao Wan, Xiaoshan Wu, Yifei Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-rate dense perception in dynamic environments is limited by the low update rate of RGB cameras, as rapid scene changes can occur between frames. Event cameras offer temporally dense but spatially sparse measurements, complementary to spatially dense RGB observations. Direct fusion cannot fully exploit this complementarity, while event-guided propagation fails on newly appearing or disoccluded regions without valid RGB support. We present LiFR v2, a unified propagation-completion-memory framework for causal anytime and streaming dense prediction from an RGB keyframe and events. LiFR v2 introduces an Event-Guided Completion Module (EGCM) to recover task-relevant representations where propagation is unsupported, and a History Retrieval Module (HRM) to reuse completed representations across successive queries. The framework supports semantic segmentation, monocular depth estimation, and multi-task dense prediction, and we further introduce SHF-Emerge to evaluate rapid object emergence and disocclusion. LiFR v2 achieves 74.37% mIoU on DSEC and 56.13% on SHF-Emerge, improving LiFR-Seg by 1.85 percentage points on the latter, while reducing SHF-Emerge depth RMSE from 1.564 m to 1.118 m over the propagation baseline. It also exceeds 100 FPS for both segmentation and depth, demonstrating accurate and efficient high-rate perception beyond RGB frame rates.

---


### 113. [When Are Aggregate Agent Traces Diagnosable? Traffic-Governed Interpretation and Calibrated Abstention](https://arxiv.org/abs/2609.25806)

**<font color=#1a73e8>作者：</font>** Peiying Zhu, Sidi Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Runtime traces can appear transparent, but a closed-loop policy determines which states are visited and which failures become visible. We study a simulated hotel-pricing agent mapping time, inventory, and market state to discrete price actions under varying demand regimes. A fault may leave no aggregate trace when the policy rarely visits affected cells. We treat entry into aggregate-only fault interpretation as a diagnosability decision preceding scoring or localization. A reference-map gate requires repeated clean-policy support; a matched runtime gate then requires joint support in clean and current streams. Signal analysis occurs only after both pass. We calibrate false admission on a disjoint clean stream at the physical-component level and model detection by affected clean traffic rather than nominal cell coverage. In a frozen one-shot heldout, 55/72 (76.4%) regime-component units were reference-admitted, representing 20 physical components; 54/55 passed matched runtime admission, while the rejected unit abstained. Stable false admission was 0/20, with a one-sided exact 95% upper bound of 0.1391, meeting the frozen 0.20 criterion. Across 540 repeated unit-arm rows nested in those 20 clusters, affected clean traffic reduced negative log likelihood by 29.3% relative to cell coverage, a gain of 0.1264 nats per row (cluster-bootstrap 95% interval [0.0593, 0.1918]). Adding mask family and its interaction improved log loss by 0.0015 nats per row (one-sided upper bound 0.0066), below the frozen 0.01 practical-sufficiency margin. A development audit found that exact minimum hitting set and greedy selection chose identical supports in 12/12 scenarios because singleton evidence had resolved the conflicts. The result is a bounded rule for interpreting aggregate agent behavior: first establish exposure, then score change, and abstain when the trace cannot support the claim.

---


### 114. [Auditing Proxy-Based Validation Across Text Spans](https://arxiv.org/abs/2609.25808)

**<font color=#1a73e8>作者：</font>** Daein Weon, Dong Ho Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluation scores are often validated by their agreement with inexpensive proxy labels. When the score and the proxy are computed from the same text span, however, that agreement can arise from surface evidence the two share rather than from the semantic construct the proxy is meant to represent. We make the distinction explicit by declaring the score, its span, the proxy and the target construct as a validation contract, then re-evaluating that proxy rule strictly outside the scored span. In a controlled HotpotQA correctness experiment varying only the shared text boundary, the score agrees with its proxy far better than with correctness at a 50-character prefix: the gap is +0.184, collapsing to at most +0.045 from 120 characters onward. At that short prefix the score still predicts whether the answer string appears later (AUC 0.634) while an equivalence test places its agreement with correctness at chance, so the reported proxy agreement does not establish that the score ranks correctness. On OR-Bench, suppressing each model's recurring opening templates removes most of the score's association with the refusal proxy, while matched-volume deletion removes almost none and construct agreement stays at chance. Only three of eleven external contracts support the off-span control, and none of the routing studies we sampled released the generations it needs. We therefore ask that a proxy-based validation claim declare the span each label is read from, report the construct agreement beside the proxy agreement, and release the generations that let the proxy be re-read off the scored span.

---


### 115. [Multi-View Fair Clustering Guided by Cross-View Sensitive Information Discrepancy](https://arxiv.org/abs/2609.25811)

**<font color=#1a73e8>作者：</font>** Mudi Jiang, Jiahui Zhou, Xinying Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-view clustering (MVC) aims to uncover latent cluster structures by exploiting complementary information from multiple views. Despite substantial progress in clustering performance, fairness remains an important concern when MVC is applied to socially sensitive scenarios. Recent fair multi-view clustering methods have introduced fairness constraints into representation learning or clustering assignments. However, these methods generally treat different views under a largely uniform fairness mechanism, without explicitly distinguishing their varying levels of sensitive dependence during cross-view learning. In practice, different views may encode substantially different levels of sensitive information. Ignoring such cross-view discrepancy can allow highly sensitive-dependent views to influence less sensitive-dependent ones during cross-view learning, potentially degrading both clustering performance and fairness. To address this issue, we propose a novel multi-view fair clustering framework guided by cross-view sensitive information discrepancy. Specifically, we estimate the sensitive dependence of each view and develop a bias-ranked asymmetric alignment mechanism that encourages views with higher sensitive dependence to learn from those with lower sensitive dependence, while cross-view discrepancies are further exploited to adaptively regulate the alignment process. Moreover, fairness regularization is imposed on the consensus soft assignments to further promote group fairness. Extensive experiments on benchmark datasets demonstrate that the proposed method achieves a favorable balance between clustering quality and group fairness.

---


### 116. [CacheDyG: Decoupling Temporal Propagation for Efficient Dynamic Graph Learning](https://arxiv.org/abs/2609.25814)

**<font color=#1a73e8>作者：</font>** PinHeng Zong, Ye Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic graphs are widely used to model time-evolving relational systems in real-world applications. Dynamic graph neural networks provide an effective framework for capturing both structural dependencies and temporal dynamics in such data. However, they typically intertwine temporal graph propagation with every optimization epoch and often maintain large trainable representations for each node-time pair. This design repeatedly recomputes largely unchanged historical structures, leading to substantial training and parameter overhead. To address this critical issue, we propose CacheDyG, a Cache-refine framework for efficient Dynamic Graph learning. Specifically, it decouples temporal propagation from routine parameter updates by constructing a time-ordered temporal dependency cache that stores graph-aware node-time representations in non-trainable buffers. During standard training epochs, CacheDyG reads from the cache and updates only a lightweight cache refiner, an adaptive residual gate, and the link predictor. Selective cache refresh further keeps cached representations aligned with the supervised objective while avoiding epoch-wise sparse propagation. Experiments on five dynamic graph benchmarks show that CacheDyG adopts substantially fewer trainable parameters and lower runtime to obtain more competitive predictive performance than baselines. These results demonstrate that cache-based decoupling provides an effective principle for scalable dynamic graph learning.

---


### 117. [MorphoSHAP: Rethinking the Unit of Attribution in Explanation for Deep Visual Models](https://arxiv.org/abs/2609.25815)

**<font color=#1a73e8>作者：</font>** Anirudh Prabhakaran, Alexandre Rocchi, Gianni Franchi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual attribution methods typically explain predictions using pixels, superpixels, or regular patches. These representations can localize important regions, but provide limited information about their structure. We introduce MorphoSHAP, a model-agnostic post-hoc method that instead uses morphological shapes as the players of a Shapley attribution game. Using the Tree of Shapes, each shape is described by its scale, geometry, and signed contribution, providing explanations of where the evidence lies, what type of structure carries it, and how strongly it affects the prediction. This shared morphological vocabulary enables spatial, textual, and global class-level explanations beyond image-specific heatmaps. To the best of our knowledge, MorphoSHAP is the first SHAP-based image attribution framework to combine these different forms of explanation. Across five diverse datasets and three architectures, MorphoSHAP achieves strong insertion/deletion performance and outperforms competing attribution methods on several benchmarks. Finally, a user study shows that MorphoSHAP provides explanations that are easy to use and are preferred over standard attribution baselines.

---


### 118. [On the Construction of Trapdoor Claw-Free Functions with Certifiable Key](https://arxiv.org/abs/2609.25819)

**<font color=#1a73e8>作者：</font>** Charles Lim, Yao Ma  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trapdoor claw-free functions (TCFs) underpin much of classical-quantum cryptographic interaction, yet every TCF-based protocol states its guarantees relative to an honestly generated key. We give a family-agnostic abstraction of key certification for (noisy) TCF constructions, built on two notions: a certifiable key relation, an NP relation capturing a family's honest keys with witnesses recoverable from the trapdoor; and certified key generation, which emits with each key a certificate of membership satisfying completeness, certificate soundness with extractability, and key privacy. We instantiate certifiable key relations for different constructions, each met generically by a zero-knowledge argument of knowledge for the relation. As our main application, a generic compiler turns any TCF-based proof of quantumness into a zero-knowledge one, with each security property following from its counterpart in the certification scheme. Finally, we delimit the primitive's reach: for protocols resting on injective invariance, an accepting certificate is itself a family distinguisher, leaking exactly the bit such protocols must hide.

---


### 119. [Protocol before progress: leakage-aware evaluation of AIS trajectory prediction](https://arxiv.org/abs/2609.25827)

**<font color=#1a73e8>作者：</font>** Zobeir Raisi, Vali Mohammad Nazarzehi Had  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reported gains in vessel-trajectory prediction from Automatic Identification System (AIS) data are credited to new architectures, but the evaluation protocol is rarely measured as a source of error reduction. We build a leakage-aware protocol with vessel-, time- and region-disjoint splits and apply it to two corpora with different traffic: 31 days of Danish national AIS traffic and 30 days of US Gulf coast traffic off Houston and Galveston. On both, we audit TrAISformer, GATransformer, and controlled AISFormer-inspired reconstructions. Three protocol effects appear in both corpora. First, TrAISformer's best-of-16 oracle decoder lowers error by a factor of 2.1-3.2 relative to greedy decoding. Second, a split that shares vessels lowers its greedy error by 23-25% at one hour, against 2% or less for a compact 0.43 M-parameter encoder. Third, a region-disjoint split raises TrAISformer's one-hour error from 2.2 to 24.6 km on the US corpus, because 99.9% of the test contexts fall in longitude bins never seen in training; the encoder built on local offsets is unaffected by this. Architectural mechanisms matter less: GATransformer's graph attention gives no measurable benefit on either corpus, while its waterway feature is worth 12-22%. The effect of a time-disjoint split is not stable across corpora (13% versus 2%). We release the splits and code.

---


### 120. [PartLLM: A Unified Multimodal Foundation for 3D Part Segmentation](https://arxiv.org/abs/2609.25832)

**<font color=#1a73e8>作者：</font>** Zhe Zhu, Yiheng Zhang, Peng Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Part segmentation is a fundamental problem in computer graphics and 3D vision. Recent works have expanded 3D part segmentation beyond fixed taxonomies, but existing approaches typically only address a specific setting, such as text-guided part segmentation or point-based interaction. In this work, we argue that these settings can be unified as an intent-conditioned generative problem, where different prompts specify the desired part decomposition. To this end, we introduce PartLLM, a unified multimodal model that formulates 3D part segmentation as autoregressive semantic decomposition. Conditioned on an input shape and a user prompt, PartLLM autoregressively generates semantic part hypotheses as queries for mask prediction and feeds them to a decomposition-aware decoder that jointly predicts coherent part masks. This unified design supports text-guided part segmentation, interactive segmentation, and full-shape semantic decomposition with controllable granularity within a single model. Extensive experiments across these task settings show that PartLLM consistently outperforms task-specific baselines, demonstrating the effectiveness of unifying 3D part segmentation under an intent-conditioned generative formulation.

---


### 121. [Identity-Centric Video Summarization via Hierarchical Fusion of Biometric, Appearance, and 3D Body Features](https://arxiv.org/abs/2609.25837)

**<font color=#1a73e8>作者：</font>** Milad Mirjalili, Enrique Alegre Gutiérrez, Eduardo Fidalgo Fernández 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work presents a video summarization algorithm based on multi-object tracking and person reidentification. We integrate facial embeddings, 3D body-shape features, and visual appearance into a unified tracking framework. These representations enable hierarchical identity assignment and tracking through bidirectional anchoring, which robustly recovers trajectories under severe occlusion or low visual quality. From these stable trajectories, we generate a compact set of summaries for each identity. We select keyframes using a multi-factor weighting scheme that optimizes biometric clarity, social interaction, and motion dynamics, while Adaptive Non-Maximum Suppression ensures temporal diversity. Evaluation on a custom dataset demonstrates tracking stability, achieving an IDF1 of 97.89% and a MOTA of 95.79%. Compared to Top-K selection, our algorithm also increases visual diversity by 146%, temporal coverage by 89%, and information retrievability by 3.5%.

---


### 122. [Gaussian Flow-Matching Schedules: Implications for Sampling and Training](https://arxiv.org/abs/2609.25839)

**<font color=#1a73e8>作者：</font>** Arsène Claustre, Hugo Negrel, Claire Boyer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow-matching schedules affect both sampling dynamics and the variance of the regression target. For centered commuting Gaussians, we show that a direction-dependent schedule decomposes into two independent design choices: a variance path, which fully determines the intermediate laws and probability flow, and a factorization, which leaves this flow unchanged while controlling irreducible regression variance. On the sampling side, we analyze finite-step Euler accuracy and derive a necessary drift bound for exact N -step sampling, connecting the geodesic and the logarithmic path. On the training side, for any fixed path, we derive closed-form factorizations that either minimize time-averaged regression variance or make it constant along the path.

---


### 123. [Less Is More in the Long Tail: Stage-Adaptive Sample Selection for Annotation-Efficient Dense Prediction](https://arxiv.org/abs/2609.25850)

**<font color=#1a73e8>作者：</font>** Xiaofei Du, Lei Zhang, Shuyu Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning performance generally improves with increasing training data, yet this scaling is fundamentally constrained by annotation cost in large-scale dense prediction tasks with long-tailed category distributions, where pixel- or voxel-level annotation is prohibitively expensive. We propose SASS (Stage-Adaptive Sample Selection), a stage-adaptive data-selection framework for pool-based active learning in long-tailed dense prediction. SASS combines three components: label-free self-supervised gradient scoring, prior-guided category rebalancing with validation-driven feedback, and stage-adaptive acquisition aligned with model training dynamics. This design avoids candidate ground-truth masks during gradient scoring while making acquisition responsive to long-tail imbalance and evolving representations. We evaluate SASS on a multimodal 3D medical segmentation testbed comprising over 100,000 samples spanning 108 anatomical structures. SASS recovers 98.3% of full-dataset performance with a 40% training-pool annotation budget, outperforming BADGE by 5.1 percentage points. Moreover, SASS exhibits a statistically supported less-is-more pattern, surpassing full-dataset training at the Hard-group level and, at the structure level, for the pancreas and gallbladder. More broadly, SASS shows that annotation-efficient learning depends not only on which samples are selected, but also on how the annotation budget is distributed across categories and when model-derived scores begin to guide selection.

---


### 124. [Prediction Is Not Detection: Evaluating Pre-Recognition Claims in Longitudinal Clinical AI](https://arxiv.org/abs/2609.25852)

**<font color=#1a73e8>作者：</font>** Jing Yang, Long R. Jiao, Xiujun Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinically useful early detection requires validated pre-recognition lead time. Yet event-based evaluations of longitudinal clinical AI can treat recognition-mediated care-process signals as shortcuts and recognition-dependent endpoints as reference standards, inflating apparent performance and lead time while undermining cross-center transport. Such results may serve prognosis without establishing detection before recognition. We define an interval-censored pre-recognition transition, an independent as-of reference standard, and a prespecified recognition proxy to make the claim testable.

---


### 125. [MemoryAthena: Adaptive Routing over Latent and Generated Memories](https://arxiv.org/abs/2609.25853)

**<font color=#1a73e8>作者：</font>** Mingyuan Li, Guangsheng Yu, Juyuan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Learned-memory methods store information in an explicit table and consume it through a separate reader, allowing addressing, storage, and reading to be modified independently. We study whether useful memory can also be generated rather than only retrieved. MemoryAthena uses three pathways: direct Engram retrieval (E), generation from retrieved Engram cues (GE), and generation from causal backbone states without consulting the memory table (GH). Generated memory is conditionally useful: it can complement E in one context but interfere with it in another. MemoryAthena therefore treats E as an anchor and learns when a generated representation should intervene. With the backbone, memory, generators, and readers frozen, a lightweight causal routing head is trained from counterfactual future-token likelihood advantages of GE and GH relative to E. At inference time, an admitted candidate modifies the E residual through bounded interpolation, while rejection recovers the direct pathway exactly. On question answering, MemoryAthena raises the five-task average from 37.65 to 39.28 over the direct pathway of the same checkpoint, while the six-task general-NLP average increases from 76.73 to 79.13. The complete memory-side system contains approximately 201M parameters, excluding the frozen backbone. Further analyses show complementary strengths among E, GE, and GH across tasks and inputs. These results support generated memory as a selective correction to direct retrieval and highlight routing when, which, and how strongly to intervene as the central challenge.

---


### 126. [MatchFusion: Explicit-Implicit Instance Matching for Spatio-Temporal Multimodal Autonomous Driving](https://arxiv.org/abs/2609.25860)

**<font color=#1a73e8>作者：</font>** Xiaoyu Li, Jiajia Fu, Long Shi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse instance representations provide a compact interface for spatial LiDAR-camera and temporal past-current interaction in multimodal perception and E2EAD. Effective interaction requires reliable instance correspondences despite geometric discrepancies and heterogeneous semantic representations. Attention-based methods exploit contextual semantics but often require specialized representation alignment, increasing computational overhead. In contrast, association based on structured object states is efficient and interpretable but lacks contextual evidence to resolve ambiguous matches. To combine these complementary strengths, we propose MatchFusion, a learnable instance matching and fusion module for spatio-temporal multimodal autonomous driving. MatchFusion initializes pairwise affinities using geometric similarity and category consistency, then selectively refines structurally plausible associations using instance embeddings. The resulting soft matchmap guides a common residual aggregation operator for adaptive information exchange. This unified matching-fusion formulation supports spatial LiDAR-camera and temporal past-current interaction, using multi-view image-plane geometry and motion-compensated BEV geometry as the respective structural priors. Experiments on nuScenes demonstrate consistent perception gains across diverse front-end configurations. Compared with a prior instance-centric fusion method, the MatchFusion-equipped system achieves higher perception accuracy while reducing FLOPs by 55.3% and GPU memory usage by 39.3%, with the matching-fusion module accounting for only 3.7% of total perception latency. Integrating temporal MatchFusion into SparseDrive further improves perception within an E2E framework without additional supervision. These results establish explicit-implicit matching as an effective and efficient mechanism for spatio-temporal instance interaction.

---


### 127. [Isolated Sign Language Recognition for Icelandic Sign Language: Experiments in a Low-resource Setting](https://arxiv.org/abs/2609.25862)

**<font color=#1a73e8>作者：</font>** Finnur Ágúst Ingimundarson, Guðný Björk Þorvaldsdóttir, Mathias Müller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present the first experiments on isolated sign language recognition (ISLR) for Icelandic Sign Language (ÍTM). We use ÍTM SignWiki, a dataset derived from a bilingual Icelandic--ÍTM online dictionary. It is genuinely low-resource: 1,845 videos cover 849 classes, 86% of which have only two examples, making the full task effectively one-shot recognition across signers. We compare two open-source ISLR frameworks, OpenHands and SPOTER, on three tasks of increasing vocabulary size (22, 117 and 849 classes), and evaluate three pose estimators and two forms of cross-lingual transfer. With ÍTM data alone, SPOTER outperforms OpenHands on all three tasks, and MediaPipe poses give better results than AlphaPose or SDPose. Cross-lingual transfer brings the largest gains: pretraining SPOTER on American Sign Language data before finetuning on ÍTM raises accuracy by 14--24 percentage points, to 72.7%, 47.9% and 22.6% on the three tasks, and multilingual training with data from six other sign languages lifts OpenHands from 1.41% to 28.86% on the full task. Although far from practical use, the results suggest that transfer from better-resourced sign languages is promising for very low-resource ones. We release our adapted versions of both frameworks.

---


### 128. [Neural Approximation by Function Composition: Rigidity and Doubly Exponential Convergence](https://arxiv.org/abs/2609.25874)

**<font color=#1a73e8>作者：</font>** Wentao Huang, Haizhang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks approximate functions by composing affine maps with nonlinear activations, but how composition itself creates approximation power is not yet fully understood. We investigate a fundamental mechanism: geometrically weighted sums of iterates of a single scalar generator function. This mechanism underpins the classical tent-map construction of the function \(x - x^2\) and related recursive representations used by Yarotsky, W. E, et al., to analyze the approximation powers of deep neural networks.
First, we establish a rigidity theorem: for continuous piecewise linear generators with a finite number of segments, any \(C^3\) function that can be represented in this way is at most quadratic. For non-affine quadratic functions, the geometric factor is at least $1/4$. This result both reveals limitations of the tent-map approach and complements existing methods based on hierarchical bases and recursive polynomial constructions. Second, using an exact remainder identity as guidance, we construct a smooth generator whose iterates yield doubly exponential error decay in total depth for square approximation and, through multiplication modules, for each fixed polynomial. For power series with absolutely summable coefficients on \([-1,1]^d\), distributing depth according to monomial degree yields a uniform approximation error of order \(O(e^{-cL^{1/d}})\) on each interior cube. These findings demonstrate how generator dynamics and remainder estimates govern depth allocation and approximation rates of deep neural networks.

---


### 129. [Evaluating the Effectiveness of SechKAN on 1D Data](https://arxiv.org/abs/2609.25876)

**<font color=#1a73e8>作者：</font>** Hoang-Thang Ta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The connection between the Kolmogorov-Arnold representation theorem (KART) and neural network design has led to the development of Kolmogorov-Arnold Networks (KANs), with applications ranging from STEM problems to AI tasks. In this paper, we investigate the effectiveness of a KAN variant, SechKAN, which relies on hyperbolic secant (sech) functions as basis functions, with a 1D projection to reduce the number of parameters to a level comparable to MLPs. We evaluate SechKAN on three 1D classification datasets: UCI Human Activity Recognition (UCI HAR), ElectricDevices, and Crop, and compare it with several effective networks, including EfficientKAN, MLP, CNN1D, ResNet1D, and DSCNN1D, using approximately comparable parameter budgets. The results indicate that SechKAN achieves competitive performance across the three datasets, with particularly strong performance on Crop. Ablation studies further show that grid size and normalization affect performance, suggesting that SechKAN's effectiveness depends on the dataset and architectural choices. Our source code and experimental implementation are publicly available at: this https URL.

---


### 130. [COBRA: A Content-Agnostic Framework for Zero-Day Detection of Suspicious Domains](https://arxiv.org/abs/2609.25882)

**<font color=#1a73e8>作者：</font>** Alexandros Fourtounis, Emmanouil Papadogiannakis, Panagiotis Papadopoulos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The use of malicious domains is central to cyberattacks such as phishing, malware distribution, impersonation, and fraudulent transactions. Because domains are inexpensive to register and easy to deploy at scale, they remain one of the most common and damaging tools used in cybercrime across industries. Proactive detection is essential to reducing this window of vulnerability and preventing harm to users. In this work, we propose COBRA: a content-agnostic, registration-time detection framework for identifying and analyzing suspicious domains from day zero. Our approach does not rely on any content-based features, allowing us to classify a domain even before it is populated with content. We analyze the names of newly registered domains and employ a clustering technique to group them based on lexical and structural similarity. We evaluate our methodology using real-world data consisting of 1.5M newly created domains, demonstrating that COBRA detects suspicious domains with a precision of 98.5%, identifying more than 47K distinct newly registered suspicious domains. Furthermore, our results show that domain-name clustering enables accurate early detection, allowing us to identify 80% of suspicious or malicious domains earlier than one of the most widely used threat-intelligence services, which in some cases may require up to 7 days.

---


### 131. [The Impact of Deep Care Isa on Reducing Musculoskeletal Disorders and Enhancing Productivity Among Office Employees: A Comprehensive Study](https://arxiv.org/abs/2609.25883)

**<font color=#1a73e8>作者：</font>** Quanmin Liang, Junjie Yang, Mohammad Ali Nasseri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Prolonged sedentary behavior, a pervasive issue in modern workplaces, has been closely linked to musculoskeletal disorders (MSDs) and reduced productivity. This study evaluates the effectiveness of Deep Care Isa, an advanced digital health assistant, in addressing these challenges. Utilizing data from over 2,300 participants across 50 corporations, the study demonstrates significant improvements in ergonomic practices, physical activity, hydration habits, and overall productivity, with notable reductions in MSD-related sick leave. The findings highlight the role of innovative ergonomic interventions in enhancing employee well-being and organizational efficiency. Comprehensive statistical analysis underscores the reliability and practical significance of these outcomes.

---


### 132. [LoRango: It Takes Two LoRAs to Unlock Hidden Behaviors in Diffusion Models](https://arxiv.org/abs/2609.25884)

**<font color=#1a73e8>作者：</font>** Jin Wei, Rundong Li, Ruihao Yang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Users commonly combine multiple Low-Rank Adaptation (LoRA) adapters to personalize images with different subjects, styles, and visual attributes. Yet inspecting adapters individually does not establish the safety of their composition. We identify and characterize a pair-conditioned attack in text-to-image diffusion: individually useful and benign-appearing adapters redirect image generation when co-loaded with a specifically matched partner, whose identity serves as the trigger. We introduce LoRango to realize this attack through complementary Signature and Payload adapters. The Signature writes a pair-specific code into intermediate carrier representations, while the Payload uses code-selective responses and opposing signal/reference branches. These branches approximately cancel for standalone adapters and mismatched pairs; matched code-reader alignment breaks cancellation within native GEGLU blocks and releases the programmed action. Both adapters are exported as ordinary static LoRA files compatible with standard loaders, requiring no prompt trigger or base-pipeline modification. LoRango achieves matched-pair attack success rates of 97.9\% on SD v1.5 and 98.7\% on SDXL, compared with 2.8--4.6\% when implanted adapters are loaded individually. Further experiments evaluate pair selectivity, standalone fidelity, robustness to deployment variations, and applicability across denoiser architectures. These findings show that individual-adapter inspection is insufficient to assess the security of multi-LoRA personalization and motivate auditing adapter compositions.

---


### 133. [How It's Made: Uncovering Detection Engineering Processes for Network Intrusion Detection Rules](https://arxiv.org/abs/2609.25901)

**<font color=#1a73e8>作者：</font>** Koen T. W. Teuwen, Emmanuele Zambon, Luca Allodi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Many Security Operations Centers rely on signature-based Network Intrusion Detection Systems like Suricata, yet detection rule engineering remains understudied. We investigate this process by introducing SuriCap, a platform for rule engineering exercises, and hosting CTF-style workshops where 60 participants, trained MSc students, and experienced SOC professionals, created rules for four scenarios. Participants produced 3146 valid rules, enabling analysis of their methods, performance, and iteration patterns. Surprisingly, prior experience had limited impact on rule quality, suggesting that less experienced engineers can produce rules comparable to experts. We also observed challenges in generalizing rules beyond available tests, underscoring the need for sufficient labeled data. From our study, we identify three phases and a common pattern in rule engineering, offering SOC managers insights to improve their processes and expectations of engineer expertise.

---


### 134. [NaCR: Visual Localization via NeRF-aided Camera Ray Regression](https://arxiv.org/abs/2609.25907)

**<font color=#1a73e8>作者：</font>** Yesheng Zhang, Xiang Dai, Xu Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual localization (VL) is a fundamental technology for vision applications such as virtual reality. Recently, a novel VL paradigm, Camera Ray Regression (CRR), has emerged, which maps 2D image patches to 3D camera rays, but its accuracy is limited. To improve CRR accuracy, we notice a compelling duality: the inverse of this mapping is inherently performed by the novel view synthesis model, \ie, Neural Radiance Fields (NeRF). While NeRF renders image patches from camera rays via differentiable ray marching, CRR predicts the rays from image patches. Motivated by this complementary relationship, we propose NeRF-aided Camera Ray Regression (NaCR), a unified framework that seamlessly bridges NeRF and CRR at the ray level. First, NaCR incorporates three simple yet effective enhancements into the CRR baseline. Second, leveraging a pre-trained NeRF, NaCR augments the training data by synthesizing novel views tailored for efficient, patch-level consumption. Finally, exploiting the differentiability of NeRF, NaCR forms a closed-loop supervision pipeline where photometric rendering errors are back-propagated to optimize the predicted camera rays. To ensure stable convergence within the highly non-convex image space, we introduce a two-stage training curriculum. Extensive experiments across indoor and outdoor benchmarks demonstrate that NaCR achieves competitive accuracy. Comprehensive ablation studies validate the efficacy of each proposed component.

---


### 135. [AURA: Angular Update Rate Adaptation for training complex-valued neural networks](https://arxiv.org/abs/2609.25914)

**<font color=#1a73e8>作者：</font>** Enrico Ballini, Allan Peter Engsig-Karup, Tito Andriollo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complex-valued neural networks (CVNNs) are increasingly adopted for complex-valued data; however, they are often trained with first-order optimizers inherited from the real-valued case. The efficiency of these methods depends largely on the step size, and their step-size rules ignore the angular information available in the complex plane. We address step-size adaptation in the complex domain by introducing AURA (Angular Update Rate Adaptation), a per-parameter step-size adaptation that can be added on top of any first-order optimizer, and removed from it, without altering its update direction. AURA measures the agreement between consecutive updates of each complex parameter, in length, alignment, and sense of rotation, and enlarges the step when they are consistent and reduces it when they are not. It requires no additional gradient evaluations and only inexpensive vector operations per step. We combine AURA with Adam and Muon and compare the resulting methods with well-known first-order optimizers on four test cases of increasing complexity, ranging from the approximation of scalar complex functions to physics-informed training. Fully connected neural networks are used throughout this work. All hyperparameters other than the step size are held fixed across test cases; for one case, we also tune the hyperparameters of each optimizer under the same budget. Our empirical tests show that AURA improves the convergence of its base optimizer in most cases with a small per-step overhead, and we identify the conditions under which it fails to do so.

---


### 136. [Toward Responsible AI-Augmented Cyber Defense: Pattern Recognition, Defense-in-Depth, and the Case for Human-AI Collaboration](https://arxiv.org/abs/2609.25921)

**<font color=#1a73e8>作者：</font>** Mustafa S. Aljumaily, Hayder Kareem Abed, Nawar S. Alseelawi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cybersecurity literature has extensively documented the operational benefits of artificial intelligence (AI) for threat detection, incident response, and prevention, while raising qualitative concerns about over-automation, algorithmic bias, and analyst-skill erosion. What remains largely absent is a formal, falsifiable model connecting three constructs that recur across this literature: Defense-in-Depth Theory, the Artificial Intelligence Theory of Pattern Recognition, and human-AI collaboration in security operations. This paper develops such a model. We formalize layered defense as a Bernoulli detection cascade in which AI augmentation enters multiplicatively across layers; we formalize each layer's pattern-recognition behavior as a Neyman-Pearson/Bayesian detector with a derived closed-form optimal threshold; and we formalize human-AI triage as a capacity-constrained cascade with an explicit, quantifiable trade-off between detection probability and false-alarm ("alert fatigue") rate. A Monte Carlo/analytical simulation evaluated at illustrative but realistic operating points shows that (i) AI augmentation compounds across defense layers, delivering its largest marginal gains exactly where traditional layering saturates, and (ii) full human review of AI-flagged alerts is not optimal: increasing analyst capacity toward 100% coverage cuts false alarms by roughly 20-fold but simultaneously lowers system-level detection probability, because imperfect analyst accuracy is then applied to every alert rather than a filtered subset. These results give the widely repeated qualitative recommendation of "balanced human-AI collaboration" a precise, testable form and suggest an interior-optimum capacity ratio as a concrete design target for security operations centers (SOCs), including those securing IT/OT-converged critical infrastructure.

---


### 137. [AT3D-AD: Anomaly Type-Aware 3D Anomaly Detection via Hierarchical Point-Language Alignment](https://arxiv.org/abs/2609.25930)

**<font color=#1a73e8>作者：</font>** Jingyu Zeng, Haoquan Lu, Can Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting and localizing 3D point-cloud defects is essential for industrial inspection. However, existing methods often suffer from imprecise localization due to the lack of anomaly supervision and reliance on single-granularity representations. To address these limitations, we propose Anomaly Type-Aware 3D Anomaly Detection (AT3D-AD), a unified framework for joint detection, localization, and classification. Specifically, we first design the Physics-Driven Parametric Anomaly Synthesis (PDPAS) module employing multiple parametric functions to generate synthetic anomalies, providing explicit anomaly supervision. Then, we propose the Hierarchical Global-Local Anomaly Alignment (HiGLA) module to align global and local representations within the normal and anomalous groups. Finally, we propose the Semantic-Geometric Anomaly Classification (SGAC) module to jointly learn localization and classification, yielding spatially precise and type-discriminative anomaly representations. Extensive experiments establish new state-of-the-art performance on all four benchmarks. AT3D-AD achieves Object/Point AUROC scores of 98.1\%/98.9\% on Anomaly-ShapeNet and 95.0\%/95.2\% on Real3D-AD, while reaching 74.2\% Macro-F1 for anomaly-type recognition on Real3D-AD.

---


### 138. [Calibrating Retrieval Geometry: Reliability-Guided Training-Free Aggregation for Visual Place Recognition](https://arxiv.org/abs/2609.25937)

**<font color=#1a73e8>作者：</font>** Xin Li, Zhimin Mao, Shang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frozen visual foundation models provide transferable features for visual place recognition, but fixed aggregation can suppress useful distinctions in new environments. We introduce TFA, a reliability-guided, training-free aggregation method requiring neither place labels nor task-specific weight updates. Our key observation is that reproducible retrieval need not be discriminative: independent codebooks can consistently retrieve a few database hubs. TFA combines cross-codebook agreement, retrieval coverage, and spectral statistics to control residual assignment, spectral shaping, and global-feature fusion. Its spectral kernel exactly recovers original descriptor similarity at zero intervention. Database-only TFA fixes its rules before accessing queries; TFA-C64 uses 64 disjoint unlabeled target images to calibrate retrieval for subsequent queries. Across 20 ground protocols with a fixed DINOv2-B backbone and matched resolution, database-only TFA improves Recall@1 over AnyLoc by 17.39 percentage points on MSLS-val and 9.55 on SPED. C64 mitigates failures of database-only calibration in driving environments. Across eight aerial/cross-view protocols, TFA achieves the highest Recall@1 among compared training-free heads in 14 of 16 DINOv2/DINOv3 backbone-protocol combinations. In a separate native-system comparison, DINOv2-G-based TFA-C64 reaches 91.46% Recall@1 on Pitts30k and 76.29% on VPAIR, outperforming the displayed training-free comparators on all five benchmarks. These results show that reliability-guided aggregation can recover additional retrieval capability from frozen representations, providing a practical baseline for new environments with scarce place supervision.

---


### 139. [Certified Against Which Oracle? Execution Labels Set the Reported Risk of Conformal Abstention for Text-to-SQL](https://arxiv.org/abs/2609.25938)

**<font color=#1a73e8>作者：</font>** Jiamiao Liu, Dewen Qiao, Yu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A conformal abstention certificate for text-to-SQL is only as truthful as the correctness labels it is calibrated on. The uncertainty pipelines that read confidence off execution consistency take those labels from the single database a benchmark ships, an oracle known to be lenient. We run a preregistered intervention on Spider-Realistic, swapping that database for the benchmark's distilled multi-instance test suite. Across four SQL-specialist checkpoints and two split schemes, the swap raises the certificate's held-out risk 2.73 to 10.23 points above the risk its own labels report. Neither oracle reports the risk experts assign. Under blinded labels from two SQL experts, a certificate calibrated at a nominal 0.10 carries 20.0 and 17.2 points of risk on two checkpoints. The stricter oracle errs in both directions: most of the answers it rejects are not judged wrong, and some of those it accepts are. An AI-assigned census of what it rejects finds a semantic error in a quarter to a third of them, depending on the population. It attributes most of the rest to underspecified questions, synthetic instances or suspected reference-query defects, a flag supported by a preregistered blinded expert audit. The oracle also decides how a confidence score is judged. Every execution-consistency score looks better under the labels of the oracle that built its clusters, in 16 of 16 combinations. Under expert labels, building such a score on suite clusters instead of shipped-database clusters raises its area under the ROC curve (AUROC) by 6.96 points on one checkpoint and 1.53 on the other. On the second, the expert interval excludes the 8.3 points the suite labels report. A certificate should be reported with both oracles, and an oracle-relative difference read as semantic risk only after the benchmark is audited. A consistency score should be evaluated under an oracle that did not build it.

---


### 140. [Calibration Is Not Verification: Falsifiability-Aware Conformal Routing for Mixture-of-Agents](https://arxiv.org/abs/2609.25959)

**<font color=#1a73e8>作者：</font>** Nada Rahali, Zijia Wang, Zhisong Liu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent language systems often treat agreement as evidence, yet heterogeneous agents can jointly repeat an unsupported claim or omit a correct specialist fact. We introduce C-MoA, an agreement-based conformal filter that turns inter-agent semantic support into a claim-level nonconformity score and calibrates a retention threshold at the example level, giving distribution-free within-domain factuality control for heterogeneous Mixture-of-Agents. C-MoA is effective: it nearly doubles retained-claim precision on long-form generation (from 0.41 to 0.75), certifies a human-labelled medical set, and transfers across domains without recalibration; its one failure mode is short-form answering, where consensus is cheap and the score is left near chance. We then ask whether counterfactual falsifiability can push past consensus, and introduce CONTRA-MoA, which adds a blinded near-miss tournament, leave-one-agent-out stability, and availability-aware fusion. This extension helps only where the verifier holds domain knowledge, dropping half of the false medical claims at 0.940 precision, whereas with a memory-only judge the added signals are near chance (AUC 0.531 and 0.511) and naive max fusion degrades the working agreement signal from 0.687 to 0.652. The message is twofold: agreement-based conformal calibration delivers reliable, transferable factuality control, while moving beyond consensus requires a knowledgeable verifier, availability-aware signals, and robust fusion.

---


### 141. [Exploring Solver-Level Warmstarting for Neural Network Verification](https://arxiv.org/abs/2609.25962)

**<font color=#1a73e8>作者：</font>** Annelot Bosman, Minghao Liu, Marta Kwiatkowska 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural network verification has become a key tool for providing formal guarantees on the behaviour of neural networks. However, many verification problems remain computationally intractable in the worst case: even for common adversarial robustness specifications, verification is NP-complete. Here, we explore the application of solver-level warmstarting for neural network verification to exploit information from previous solutions. We study the effect on running time as several properties are modified, including perturbation radii, input data and the networks themselves, using a pipeline that is generalisable and potentially adaptable to state-of-the-art verifiers. Our results show that warmstarting can significantly reduce verification time in most cases. Moreover, warmstarting enables the successful verification of instances that could not be solved from scratch within the given time limit.

---


### 142. [GeoPair: Geometry-Preserving Cross-Layer Factorization for Training-Free Transformer Compression](https://arxiv.org/abs/2609.25963)

**<font color=#1a73e8>作者：</font>** Baher Mohammad, Ammar Ali, Stamatios Lefkimmiatis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer architectures exhibit cross-layer redundancies, yet post-training compression pipelines typically optimize layers in isolation or rely on heuristic grouping strategies that disregard layer-specific activation geometries. We introduce a principled, training-free framework that sequentially optimizes cross-layer weight pairings and shared-dictionary factorizations. Rather than forcing weights of adjacent layers to share a basis or heuristically merging activation statistics, our approach identifies structurally compatible projections and learns a shared representation that better preserves each layer's distinct calibration geometry. Coupled with structured sparsity, this yields highly efficient weight decompositions without sacrificing functional fidelity. Across diverse architectures, scales, and modalities, our method achieves state-of-the-art results, consistently outperforming independent structured weight decompositions and alternative pairwise weight factorizations, which operate under heuristic grouping strategies. By replacing heuristic engineering strategies with a convergent, optimization-driven pipeline, we establish a theoretically grounded foundation for scalable, transformer compression across different modalities.

---


### 143. [GRIP: Gaussian Rendering as a Cross-Modal Bridge for Image-to-Point Cloud Registration](https://arxiv.org/abs/2609.25966)

**<font color=#1a73e8>作者：</font>** Karim Slimani, Catherine Achard, Eric Marchand 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces GRIP, a pose-conditioned refinement framework for pixel-to-point matching and 2D to 3D registration. Given an initial coarse pose estimate, GRIP addresses the structural mismatch between grid based image descriptors and unordered point cloud descriptors by softly rendering learned 3D point features onto the image grid through Gaussian feature splatting. The rendered point derived feature map is then fused with image features by a pixel aligned transformer, enabling visual semantic and geometric cues to interact in a shared 2D representation. The refined features are decoded and propagated to finer resolutions for dense correspondence estimation and final pose refinement. Experiments on RGB D Scenes V2 and 7 Scenes demonstrate state of the art inlier ratio and competitive registration recall, with stronger performance under stricter evaluation thresholds.

---


### 144. [NAWE: Digital Watermarking with Neural-Assisted Watermark Extraction](https://arxiv.org/abs/2609.25972)

**<font color=#1a73e8>作者：</font>** Roman Chaban, Vitaliy Kinakh, Lilian Rouzaire 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> NAWE (Neural-Assisted Watermark Extraction) combines an explicit signal-processing watermarking construction with a pretrained neural host predictor. A periodic, perceptually masked watermark carrier provides synchronization, Polar coding supplies redundancy, and denoising followed by subtraction extracts the embedded watermark. The denoiser remains frozen, without watermark-specific training. A one-factor-at-a-time study compares Wiener, BM3D, DRUNet, and GS-DRUNet host estimators. Comparisons with TrustMark, SSL Watermarking, PixelSeal, and WAM show NAWE's lowest geometric and photometric class BER and strong message recovery, while filtering and noise remain limitations consistent with the non-adaptive selection of the watermark extractor. The comparison retains the systems' different payloads and coding.

---


### 145. [Faithful Faithfulness Evaluations: Challenges & Pitfalls Learned from a Breast MRI Case Study](https://arxiv.org/abs/2609.25978)

**<font color=#1a73e8>作者：</font>** Peachapong Poolpol, Henrik H. J. Detjen, Eike Petersen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Saliency maps are widely used to explain deep learning predictions in medical imaging, yet visually plausible explanations do not necessarily reflect a model's true decision process and may therefore mislead clinicians. We investigate this problem using a Vision Transformer-based breast MRI classifier trained on the ODELIA Breast MRI Challenge dataset and evaluate multiple saliency methods, including Last-layer Attention, Attention Rollout, Grad-SAM, Gradient Attention Rollout, GMAR, Grad-CAM, and HiResCAM. Our study highlights two often-overlooked challenges in perturbation-based faithfulness evaluation. First, method rankings depend strongly on the perturbation strategy, varying across intensity-based perturbations and transformer-based attention masking. Second, benchmarking saliency methods requires distinguishing between class-specific and class-agnostic explanations. To enable fair comparisons, we introduce non-class-specific variants of gradient-based methods and evaluate both settings separately. Across protocols, Grad-CAM and Gradient Attention Rollout consistently emerged as the strongest class-specific methods, although their relative ranking depended on the evaluation design. These findings expose important limitations of current saliency-based explainability approaches and highlight the need for more robust and standardized evaluation frameworks for trustworthy clinical AI systems.

---


### 146. [Theory for groupoid equivariant neural networks: an approach for steerable CNNs on bounded domains](https://arxiv.org/abs/2609.25987)

**<font color=#1a73e8>作者：</font>** Alberto Ibort, Maria Jimenez-Vazquez, Juan M. Perez-Pardo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equivariant convolutional neural networks are usually built from a group acting globally on the space of signals. This hypothesis is inappropriate for many bounded or stratified domains: an ambient rigid motion may be admissible only on part of the domain, and the boundary introduces geometric types that are invisible to a transitive group action. We develop a theory of groupoid-equivariant neural networks in which the symmetry datum consists of a groupoid, a selected pseudogroup of local bisections, a measure, and input and output representation bundles. For integral channels on the object space, we prove a bisection-equivariant kernel theorem: equivariance is equivalent to a transport constraint on the two-point kernel, and its solutions are classified by one joint-stabilizer intertwiner on each orbit of pairs. As a case study we apply the theory to bounded planar domains.
The resulting architecture is implemented through offline nullspace bases and sparse gather--transform--scatter operations. A Poisson--Dirichlet kernel study is used separately to assess boundary-aware inductive bias; the exact inverse is shown to preserve the global symmetries of the rectangle but not general proper local bisections. The numerical results show that the proposed architectures provide significant advantages when symmetries cannot be globally implemented by group actions and provide an accuracy improvement of at least one order of magnitude with respect to the models tested.

---


### 147. [MATES: Learning Multi-Agent Interactions by Transforming Observations for Frozen Single-Agent Policies](https://arxiv.org/abs/2609.26010)

**<font color=#1a73e8>作者：</font>** Elie Abboud, Oren Gal  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent reinforcement learning (MARL) commonly trains decentralized policies from scratch, requiring agents to acquire individual task competence and coordination simultaneously. Yet many multi-agent problems admit a compatible single-agent counterpart in which the underlying task can be learned in isolation. We introduce Multi-Agent Observation Transformation for Existing Single-Agent Policies (MATES), an input-side adaptation framework for tasks whose multi-agent observations preserve the solo-task information while exposing separately identifiable neighbor information. From multi-agent experience, MATES learns a small adapter that maps this observation into the format expected by a frozen single-agent policy, inducing actions suited to the shared environment without updating the single-agent policy itself. MATES leaves the pretrained policy's internal architecture unchanged and retains the objectives and update procedures of the underlying MARL algorithm. We evaluate MATES using both on- and off-policy algorithms on lifelong pathfinding, navigation, and cooperative discovery, spanning discrete and continuous observation and action spaces. Across all evaluated settings, MATES optimizes only 3.5-7.3% as many parameters as full-policy training while consistently outperforming MARL training from scratch. It approaches the performance of full fine-tuning, remains competitive overall with demonstration-based baselines, and retains strong task performance at team sizes not encountered during training. These results provide evidence that, under this observation structure, effective multi-agent behavior can be learned without modifying the policy that encodes individual competence.

---


### 148. [The Dynamics of Quasiregular Neural Learning](https://arxiv.org/abs/2609.26018)

**<font color=#1a73e8>作者：</font>** Matthia Sabatelli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many learning problems combine a dominant regularity with systematic exceptions. Motivated by U-shaped learning in language acquisition, we study this interaction in controlled quasiregular regression problems where regular and exceptional solutions are explicitly known. Neural networks can partially acquire exceptions, subsequently regress toward the dominant regularity, and finally recover. This overregularization becomes substantially stronger when exceptions are rare, despite their early acquisition, but does not emerge equally across all regularities considered. Our results isolate a simple form of competition between regularities and exceptions during neural learning.

---


### 149. [BOBA: Dynamic Bayesian Optimization through Bayesian Active Inference](https://arxiv.org/abs/2609.26021)

**<font color=#1a73e8>作者：</font>** Merlin Angel Kelly, Rishan Patel, Alexander Thomas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic black-box optimization presents significant challenges for Bayesian Optimization (BO), as the objective function evolves over time, causing optimal locations to shift continuously. Existing dynamic BO (DBO) methods using standard acquisition functions such as Upper Confidence Bound (UCB) fail to explicitly account for temporal variations, leading to suboptimal sample allocation and poor tracking of moving optima. Here, we propose BOBA (Bayesian Optimization through Bayesian Active Inference), a novel acquisition function inspired by free energy principles from active inference that explicitly minimizes predictive uncertainty about future states in dynamic environments. BOBA extends traditional acquisition functions by incorporating a forward-looking uncertainty quantification that estimates uncertainty in function changes, enabling more informed exploration-exploitation trade-offs in non-stationary settings. We evaluate BOBA on synthetic dynamic benchmarks, comparing against state-of-the-art DBO methods. Our experiments demonstrate that BOBA significantly improves regret in query-restricted settings, while remaining competitive in time-limited settings. We further analyze variants of BOBA with different exploration strategies, showing how the exploration-exploitation balance can be tuned for different types of dynamic functions. This work contributes both a free energy-based acquisition function for DBO and insights into how active inference principles can enhance optimization in non-stationary environments, with implications for real-time applications requiring continuous adaptation.

---


### 150. [MICRO: Multi-Fidelity Active Search for Severe Error Discovery](https://arxiv.org/abs/2609.26025)

**<font color=#1a73e8>作者：</font>** Orlando Leone, Niclas Pokel, Pehuén Moure 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human feedback can vary in cost and informativeness. Strong feedback can reveal severe errors but is costly, so cheaper quality ratings can help decide which items to annotate. We propose MICRO (Multi-Fidelity Impact Clustered Rollout), an active search framework that allocates a shared budget to these feedback types to maximise confirmed severe error discoveries. MICRO jointly models ratings and annotation losses conditional on item features to steer acquisition. It clusters acquisitions by their predicted impact on severity probabilities to select diverse candidates, then uses rollout to estimate their discovery value. Experiments on WMT20 English-German show that ratings improve both loss reconstruction and severity prediction. MICRO achieves the highest mean discovery count across four budget and rating cost settings, with similar performance to adapted MF-ENS in one and significant gains over all six comparison policies, including two rollout controls, in the other three $(p<.001)$.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-275](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
