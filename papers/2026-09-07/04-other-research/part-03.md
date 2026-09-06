# 📦 其他研究 | 2026年09月07日

> 本类共 **194** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-194](./part-04.md)

---

### 101. [Tree-Structured Vector Quantization For Efficient And Progressive Image Compression](https://arxiv.org/abs/2609.03641)

**<font color=#1a73e8>作者：</font>** Xinkun Wang, Tianyi Xu, Qingyu Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vector-quantization based image compression has achieved strong rate--distortion performance, yet most of them still produce a separate compressed representation for each target bitrate. Such variable-rate behavior allows one model to operate at multiple rates, but it does not necessarily provide a progressive bitstream whose prefixes are themselves decodable and can be refined by appending additional bits. We propose \textbf{Tree-VQ}, a progressive tree-structured vector quantization framework for learned image compression. Tree-VQ organizes discrete codewords as a hierarchical binary tree and represents each latent token by a routed root-to-leaf path. Crucially, every prefix of this path corresponds to a valid quantized representation, so shallow internal nodes serve as coarse reconstruction codes and deeper nodes provide successive refinements. This allows a compressed image to be decoded from an early prefix and progressively improved as more branch symbols are received, rather than being re-encoded for different target rates. To make this structure practical for compression, we introduce a prefix-compatible tree entropy model that codes progressive continuation decisions and routed branch refinements using only causally available decoded contexts. We further use rate-aware refinement scheduling to decide which spatial blocks should receive additional tree bits under a given prefix budget, and hierarchical prefix supervision to ensure that internal nodes are directly decodable at low rates. Experiments show that Tree-VQ achieves a superior performance--efficiency trade-off, delivering the best perceptual compression results with much fewer parameters and lower latency than competing methods.

---


### 102. [PL-SCEA: Reconfiguring Pretrained Attention for Few-Shot Industrial Anomaly Detection](https://arxiv.org/abs/2609.03655)

**<font color=#1a73e8>作者：</font>** Xiaoyu Yang, Qixing Wu, Huixian Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Foundation Models (VFMs) provide transferable patch representations for few-shot industrial anomaly detection, but their attention computation is typically inherited from pretraining objectives centered on semantic aggregation. This creates a potential mismatch: token relations that support semantic recognition may not adequately expose the localized texture and structural deviations required for anomaly localization. We therefore investigate the hypothesis that the attention computation of a frozen VFM can be reconfigured as a task-relevant component of anomaly detection. We instantiate this idea with Power-Law Self-Correlation Enhanced Attention (PL-SCEA), which retains the semantic context of pretrained query-key attention while constructing token-adaptive self-correlations over contextualized value features. Positive-correlation filtering and power-law reweighting then emphasize relations that are salient relative to each token's relational background, without introducing additional trainable attention projections. The resulting features are modeled by a lightweight variational autoencoder that provides a fixed-size reconstruction-based representation of category-specific normality. The two stages serve complementary roles: attention reconfiguration shapes how local relational deviations are represented, while reconstruction-based modeling converts deviations from learned normality into anomaly scores. Across MVTec AD and VisA, the complete framework achieves competitive image-level detection and consistently strong pixel-level localization across the evaluated few-shot settings. Ablations further show that PL-SCEA improves localization with either the VAE or a memory bank under the tested setting. These results support the view that task-aligned attention reconfiguration can improve the anomaly-localization capability of frozen pretrained representations.

---


### 103. [Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations](https://arxiv.org/abs/2609.03657)

**<font color=#1a73e8>作者：</font>** Onat Şahin, Mohammad Altillawi, George Eskandar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D scene representations like NeRF and 3D Gaussian Splatting (3DGS) suffer severe artifacts in sparse-view settings. Recent generative 3D artifact fixers attempt to address this, but rely on paired corrupted and clean renders requiring costly, per-scene reconstructions across varying view configurations. While 2D image augmentations act as instant regularizers, no explicit equivalents exist for 3D representations to preserve spatial consistency across views, an essential property for 3D-aware training. We propose 3D Morphological Perturbations as an optimization-free regularizer that preserves spatial consistency. Leveraging explicit 3DGS, we treat each Gaussian as a fundamental building block - analogous to a 2D pixel - and apply perturbations across its morphological parameter space via scale, rotation, and pruning. Our method eliminates per-scene 3DGS optimization loops from dataset curation while enabling models to learn stronger geometric priors than sparse-view baselines in diagnostic ablations conducted on a lightweight video diffusion sandbox. Scaled to a 14B-parameter video model via ControlNet, our approach maintains visual fidelity while reducing mean depth error by 12.5% over state-of-the-art image-to-image 3D artifact refiners, ultimately boosting downstream robotics policy success rates by up to 8.0% across 3 of 4 manipulation tasks.

---


### 104. [Security and Privacy in the Musical Metaverse: Threat Analysis and Design Implications](https://arxiv.org/abs/2609.03659)

**<font color=#1a73e8>作者：</font>** Luca Turchet, Michał Kłosinski  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Musical Metaverse (MM) introduces immersive, real-time environments for collaborative musical interaction, characterized by ultra-low-latency constraints, continuous multimodal data streams, and heterogeneous devices. These properties create a distinctive security and privacy landscape that differs significantly from conventional XR or multimedia systems. This paper presents a multi-layer threat analysis of MM ecosystems, identifying key assets including live musical content, expressive interaction data, identity and session metadata, and intellectual property. Threats are analyzed across network, application, data/AI, device, intellectual property rights, and social layers, with particular attention to risks arising from expressive and neurophysiological data, which enable inference, re-identification, and potential privacy violations. We describe a stakeholder-driven survey involving 14 participants from 13 organizations, revealing that neurophysiological data leakage and real-time stream disruption are perceived as the most critical risks, followed by intellectual property infringement and avatar impersonation. We further evaluate the suitability of existing security protocols under strict latency constraints, showing that conventional approaches such as TLS over TCP are often incompatible with real-time musical interaction, while lightweight, stream-oriented mechanisms (e.g., SRTP, DTLS) provide a more suitable balance between security and performance. Based on these findings, we derive a set of design guidelines for MM systems, emphasizing latency-aware security, differentiation of interaction paths, data minimization, and edge-centric processing. The results support a security-by-design approach that enables trust and compliance without compromising real-time performance.

---


### 105. [Local Updates, Global Learning (LUGL): Playing Games with non-incremental Learners](https://arxiv.org/abs/2609.03660)

**<font color=#1a73e8>作者：</font>** David Milec, Spyridon Samothrakis, Michael Fairbank 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The dominance of Neural Networks (NNs) in RL is partially due to their incremental learning capability, which naturally suits the online, non-stationary nature of self-play training. However, gradient-boosted trees like LightGBM are widely recognised as the state of the art for tabular data in supervised learning, often outperforming NNs in accuracy and efficiency. Game states are inherently tabular---discrete actions, categorical card identities, structured board positions---which makes them an ideal candidate for tree-based methods. We introduce LUGL (Local Updates, Global Learning), a framework that decouples data collection from model fitting, enabling non-incremental learners such as GBTs to operate in RL settings where they would otherwise fail due to distributional shift. LUGL alternates between a local updates phase, where the agent plays self-play games and accumulates tabular updates (Q-values, V-values, policies, or regret values) in a finite table, and a global learning phase, where the table is used to train a function approximator that generalises to unseen states before the table is reset. We test our approach in four standard perfect-information games (Tic-tac-toe, Connect-4, Othello, and Hex) and five imperfect-information games (Kuhn's poker, Leduc Hold'em, Liar's Dice, Goofspiel, and Flop5 Hold'em), and show that our results are competitive with or superior to DQN and DeepCFR. Our experiments demonstrate that the community's strong bias towards NNs in game-playing may be unwarranted, since LightGBM-based agents achieve competitive or superior performance across all tested benchmarks.

---


### 106. [Point&Spawn: Mid-Air Reference-Free Object Instantiation Using Gaze and Hand Gestures in Extended Reality](https://arxiv.org/abs/2609.03661)

**<font color=#1a73e8>作者：</font>** Jihyeon Lee, Ken Pfeuffer, Jinwook Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mid-air object instantiation in XR requires users to specify a 3D position without spatial references, such as surfaces or existing objects. We present Point&Spawn, a staged pipeline for pre-instantiation position specification through Direction Setting, Depth Setting, and Position Refinement within a continuous gesture flow. We evaluated six controller-free techniques combining Gaze or Non-Dominant Hand (NDH) direction setting with Ray Intersection, Relative Gain, or Drag&Hold depth setting in a user study (N=24) across Near and Far spawn depths. Relative Gain and Drag&Hold yielded faster and more accurate spawning, lower workload, higher usability, and greater preference than Ray Intersection. The shoulder-referenced NDH ray improved speed and coarse accuracy, whereas the viewpoint-based Gaze ray reduced hand movement with comparable final accuracy. Farther spawn depth imposed greater temporal costs as well as Gaze and accuracy costs with Ray Intersection. These findings offer empirical guidance for designing direction and depth control in spawning in XR.

---


### 107. [Cross-Dataset Transfer and Reliability of Explainable Artificial Intelligence for RhythmFormer Remote Photoplethysmography](https://arxiv.org/abs/2609.03663)

**<font color=#1a73e8>作者：</font>** Louis Chen, Torbjörn E. M. Nordling  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background. Remote photoplethysmography estimates the cardiovascular pulse from facial video, and its explanations have rested on inspecting heatmaps rather than on quantitative evidence about where a model reads it. We quantified the explanations and asked whether such explanations transfer between datasets and track model performance. Method. We trained eight condition-specific RhythmFormer models on NCKU-rPPG, recorded under three illumination levels, speaking, rotation, and cycling, estimated one heart rate per 5.12-second clip, and set them beside a UBFC-rPPG reproduction. Raw attention, rollout, attention flow, and Beyond Intuition were assessed by skin coverage and the Salience-guided Faithfulness Coefficient (SaCo). Results. Beyond Intuition ranked highest on both datasets, at median coverage 0.789 and SaCo 0.837 on Static level 3 against 0.826 and 0.917 on UBFC-rPPG; lower ranks differed. Within one participant of one condition, neither measure was related to a clip's heart-rate error, waveform correlation, or signal-to-noise ratio on either dataset: 186 of the 252 coefficients fell below $|\rho|=0.10$ and 28 reached $p<0.05$ against the 13 expected by chance. Across the eight scenarios only Beyond Intuition's coverage followed the three performance measures, at $\rho=-0.43$, $+0.57$, and $+0.43$, while the attention-only methods' SaCo ran opposite to each. It failed at 40 lux alone, its median coverage falling to 0.180 and its median SaCo to $-0.178$, whereas motion degraded the estimates far more without such a drop. Conclusions. Skin coverage and SaCo carry information complementary to the performance measures rather than a proxy for them: attributing to the skin does not guarantee an accurate estimate. What an attribution reveals about a condition is where the model looks rather than how faithfully its map is ordered.

---


### 108. [PlanePivoting: Exploration and Optimization of Gaze-Mouse Cursor Alignment for Spatial Object Translation](https://arxiv.org/abs/2609.03665)

**<font color=#1a73e8>作者：</font>** Jinwook Kim, Sangmin Park, Jihyeon Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As XR matures into a ubiquitous computing platform, the disconnect between 2D and 3D input modalities remains a critical barrier to seamless workflow. Frequent transitions between the mouse for 2D precision and hand gestures for 3D manipulation induce significant physical fatigue and cognitive load. To address this, we introduce PlanePivoting, a multimodal interaction technique that extends standard mouse input into 3D space by leveraging gaze-mouse alignment. This technique dynamically modulates the translation plane based on the spatial overlap between the gaze and mouse cursor, eliminating the need for physical input modality switching. To systematically explore the foundational design space of gaze-mouse coordination and optimize key variables, we conducted a user study comparing PlanePivoting with a standard 3D Gizmo interface across two translation mapping profiles and two gaze cursor apertures. Results demonstrate that PlanePivoting outperforms the Gizmo on efficiency metrics while maintaining comparable precision and yielding higher subjective satisfaction. This study demonstrates the potential of gaze-mouse alignment for efficient spatial manipulation between 2D and 3D environments.

---


### 109. [Out-of-Distribution Generalisation with Sequence Models in Offline Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2609.03667)

**<font color=#1a73e8>作者：</font>** Oussama Hidaoui, Omer Ebead, Ulrich Armel Mbou Sob 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generalising to unseen tasks remains a fundamental challenge in offline multi-agent reinforcement learning (MARL). In this work, we present a principled analysis of zero-shot task generalisation in the offline setting and conduct an extensive empirical investigation into the scaling behaviour governing task diversity, dataset size, and network capacity. To facilitate this study, we extend offline sequence modelling architectures to handle multi-task observation and action spaces alongside variable agent counts across tasks. Our primary finding is that scaling task diversity---rather than sheer dataset size is the dominant factor in achieving robust zero-shot transfer. Through large-scale experiments across four challenging environments (Connector, RWARE, SMAX, and LBF), we demonstrate that our multi-task approach achieves a mean improvement of 3.2x on held-out test tasks compared to single-task models and consistently outperforms strong behaviour cloning baselines. These results suggest that the development of generalisable MARL agents should prioritise the diversity of the training distribution with varying numbers of agents, providing a roadmap for scaling offline MARL effectively.

---


### 110. [ARCOS: Zero-shot Boundary Localization for Corneal Layer Segmentation Across Optical Coherence Tomography Devices](https://arxiv.org/abs/2609.03668)

**<font color=#1a73e8>作者：</font>** Nuno Vivas Brás, Benjamin Memmi, Maëlle Bouhassane 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of corneal layers in optical coherence tomography (OCT) is essential for quantitative assessment of corneal morphology, including layer thickness and structural changes associated with disease or surgery. However, automatic segmentation remains challenging because corneal interfaces are thin, affected by speckle noise, and variable across acquisition devices. In this work, we propose ARCOS, a patch-based zero-shot boundary localization framework for corneal layer segmentation in clinical anterior-segment OCT images. Rather than performing conventional region classification, the method predicts boundary heatmaps for the main corneal interfaces from overlapping native-resolution patches. Patch-level predictions are stitched across the full B-scan and converted into boundary locations to obtain continuous, anatomically ordered layer segmentations. The network combines multi-scale feature fusion with a self-conditioned refinement module that uses intermediate boundary information to improve local heatmap predictions while preserving spatial detail. The method was evaluated on clinical OCT images acquired from multiple devices and compared with representative segmentation baselines using boundary localization and derived thickness metrics. The proposed method achieved an off-by-one boundary localization accuracy of 95.1% and a mean absolute boundary error of 0.514 pixels on the matched-device test set. In zero-shot cross-device evaluation, it maintained an average off-by-one accuracy of 84.3% and a mean absolute boundary error of 0.855 pixels across unseen acquisition devices, outperforming the baseline models. Thickness estimates derived from the predicted boundaries showed low error across corneal regions, supporting the method's use for quantitative corneal OCT analysis.

---


### 111. [Do Video Generators Track the World Across Segments? A Benchmark and Method for World-State Reasoning in Video Continuation](https://arxiv.org/abs/2609.03673)

**<font color=#1a73e8>作者：</font>** Yingmao Miao, Pengfei Zhang, Chaoran Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generators build long videos by composing shorter parts, either by generating segments one after another or by autoregressively extending chunks. Each new part usually depends on memories of historical observations, such as recent frames, selected key frames, memory banks, or cached features. These memories preserve visible evidence from the past, but current generators do not reliably turn such evidence into a world-state interface: what holds in the video world after previous actions and how it should change under the next prompt. A past frame remains valid history, but it may not describe the state needed by the next segment; some states must instead be inferred from occluded or implicit changes rather than copied from a directly observed frame. This creates a simple but overlooked question for video continuation: given a previous video, its prompt, and a new prompt, can a model generate a continuation that reflects the state determined by both the historical video and the new prompt? To answer this question, we introduce Statebench, a benchmark that targets this gap by testing continuations over three state categories: past-visible states, occluded-process states, and complex-transition states. We further propose Stateagent, which explicitly maintains an entity-state representation, updates it under the new prompt, grounds the predicted post-action state as a future end frame, and renders the next video. Experiments show that our method improves controlled video continuation by raising the all-case state score (SCS-All) from 45.2 to 69.3, and also benefits story generation at the one-minute scale. Code is avaliable at this https URL.

---


### 112. [Understanding Autonomous Driving Datasets by Describing Differences between Image Subsets in Natural Language](https://arxiv.org/abs/2609.03677)

**<font color=#1a73e8>作者：</font>** Julian Truetsch, Felix Hauser, Christoph Stiller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding the composition of large-scale autonomous driving datasets is essential for safety, robustness, and reliable operation across domains. For example, domain shift between locations could lead to the operating environment being misaligned with the training data, resulting in potentially dangerous performance degradation. Yet, existing data analysis pipelines largely rely on metadata, predefined labels, or manual inspection, which provide limited semantic insight or do not scale. This paper studies set difference captioning: given two subsets of images, the goal is to produce a natural-language hypothesis describing differences between the target and reference set. Building on a two-stage formulation, we adapt the method to autonomous driving by focusing on object-centric patches derived from object detection, which simplifies aggregation and enables attribution of differences to specific object instances or categories. To evaluate this setting in-domain, we introduce a new benchmark, AD-Diff Bench. Low-concentration experiments assess the suitability of set-difference-captioning approaches to sparse, real-world differences. We restrict our experiments to open-weight models to support reproducibility and ease of deployment. The proposed benchmark and analysis provide a step towards practical, human-interpretable dataset introspection for autonomous driving datasets. Our implementation and benchmark dataset are available at this https URL

---


### 113. [Exploratory Unstructured Data Analysis: A Formative Study and Implications for Human-AI Collaboration](https://arxiv.org/abs/2609.03678)

**<font color=#1a73e8>作者：</font>** Johannes Eschner, Dominik Eitler, Max Irendorfer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We propose a conceptual framework for exploratory data analysis of (large) unstructured data (EluDA), combining classical elements (querying, visualization) with active knowledge construction in the "search for structure". In a formative study, users conceptualized a structure for an image dataset during exploration. We found that users conceptualize by building faceted classifications bottom-up and rarely create meaningful spatial categorization during this process. We also evaluated CLIP for zero-shot assignment and semantic categorization, finding that it remains unreliable for assigning user-defined concepts to images but does support semantic grouping. Based on these findings, we identify and discuss four key opportunities for human-AI collaboration in EluDA: intelligent sampling and visualization to maximize data visibility; incremental and few-shot learning to minimize effort for reliable assignment; automatic category, concept, and facet suggestions to reduce effort during the search for structure; and the necessity for effective trust calibration methods.

---


### 114. [DropClick: Semi-Automated One-Click Segmentation for Agricultural Robotic Data](https://arxiv.org/abs/2609.03680)

**<font color=#1a73e8>作者：</font>** Patrick Zimmer, Michael Halstead, Chris McCool  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Labelling vision datasets, especially for segmentation tasks, is a laborious and costly process that stymies novel developments in agricultural robotics. In this paper, we present DropClick, a click-guided segmentation tool that simplifies the annotation process. Our system utilises single-click inputs on objects to generate pseudo-labels, which can replace manual annotations. DropClick stands out as it is a semi-automated approach and does not require a click for every object in the scene. It can therefore further reduce the required amount of user input drastically. We evaluate our method on two challenging agricultural robotic datasets, SB20 and BUP20 for plant and fruit segmentation, respectively. DropClick is first trained on a small subset of just 5 images from the original training data. This DropClick model can then be deployed as a one-click segmentation system and achieves comparable or higher performance than other one-click methods achieving an mIoU of 70.0 and 72.6 points, for SB20 and BUP20 respectively. DropClick then excels at maintaining high performance when clicks are not given (e.g. dropped); when 50% of the clicks are missing it still maintains an mIoU of 68.9 and 71.3 points, for SB20 and BUP20 respectively. We validate DropClick as a pseudo-labelling approach by taking its outputs to train a Mask2Former instance-based segmentation model in a semi-supervised manner. In this process, partially removing user input from DropClick yields similar high performance when compared to providing all clicks, at 70.1 vs 70.7 points AP50 for SB20 and no difference for BUP20 at 77.0 for both models; at the same time saving 46.3% of total input for SB20 and 31.9% for BUP20.

---


### 115. [Resolution-Aware Experimental Design under Partial Identifiability](https://arxiv.org/abs/2609.03686)

**<font color=#1a73e8>作者：</font>** Sofianos Panagiotis Fotias  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Experimental design is commonly framed as choosing the experiment expected to provide the most information. Under partial identifiability however, persistent nuisance uncertainty can make the same observation carry different structural meanings. We introduce Resolution-Aware Experimental Design (RAED), which selects an experiment by the smallest expected nonempty structural candidate set achievable subject to false-exclusion control. We prove an exact cross-nuisance aliasing separation: an experiment can be preferred by structural and full-latent information gain, average classification, and nuisance-marginalized informativeness while having arbitrarily poorer valid structural resolution. RAED nevertheless preserves the expected ordering under a genuine composite Blackwell comparison. To make this criterion operational, we develop a learned score-based implementation with finite-sample nuisance-average and positive-tail calibration, and characterize a rare-tail sample-complexity obstruction. Under constrained sensing, two subsurface-flow benchmarks exhibit genuine RAED--expected-information-gain (EIG) experiment-selection disagreements, with the clearest and largest held-out resolution differences in WCA. In a fluvial benchmark, tail protection changes the selected physical experiment and replaces hard-region false exclusions primarily with explicit ambiguity. In a mechanistic methane-oxidation benchmark, a prospectively specified 5\% false-exclusion tolerance also yields a nontrivial finite-sample population guarantee for tail-sensitive nuisance risk, with 95\% joint confidence across all three structural families.

---


### 116. [ToPO: Token-Conditioned Preference Routing for Attention-Based Latent Diffusion Models](https://arxiv.org/abs/2609.03688)

**<font color=#1a73e8>作者：</font>** Juntao Xu, Shihong Li, Hoi Fan Au 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pairwise preference labels rank complete images, yet Diffusion-DPO applies their effect over many spatial and denoising-time coordinates. For attention-based, noise-prediction latent diffusion, ToPO (Token-Oriented Preference Optimization) constructs a per-minibatch, detached, separable spatial-temporal route from branchwise squared-residual contrast in a frozen reference denoiser. Preferred-branch cross-attention uses content tokens to modulate the spatial factor, and an auxiliary pixel-midpoint ordering term is added without local labels or a learned reward model. In matched three-seed retrainings with a shared update schedule, ToPO has higher endpoint estimates than Diffusion-DPO on all five reported SD-1.5 metrics and on HPSv2, ImageReward, and CLIP for SDXL. It also receives larger raw win shares in an aggregate blind SDXL A/B study. These findings are scoped to the reported equal-update U-Net protocols rather than an equal-compute comparison.

---


### 117. [Semantic-Aware Subgraph State Space Model for WSI Classification in Histopathology](https://arxiv.org/abs/2609.03689)

**<font color=#1a73e8>作者：</font>** Feixing Chen, Hao Lu, Lin Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Histopathological subtyping relies on the recognition of characteristic histological patterns. These patterns may be expressed by individual tissue structures or by the spatial distribution and co-occurrence of multiple structures, and they often span irregularly shaped tissue regions, termed semantic units in this work. However, conventional patch-based representations may fragment such units and fail to explicitly preserve their internal spatial organization, while efficiently modeling relationships among numerous spatially separated units remains challenging. To address these limitations, we propose the Semantic-Aware Subgraph State Space Model (SASG-SSM), a flexible and efficient framework for whole slide image (WSI) classification. Semantic-Aware Subgraphs (SASGs) first approximate irregularly shaped semantic units by adaptively grouping spatially connected patches guided by class-agnostic visual-semantic priors. By representing patches as graph nodes with adjacency edges, SASGs preserve their internal spatial organization rather than treating them as an unordered set. A Subgraph State Space Module (SG-SSM) subsequently combines a graph neural network encoder for intra-subgraph topology encoding with a Mamba-based state space encoder for efficient contextualization across large numbers of subgraphs. This module integrates local structural information within semantic units with global contextual information arising from their distribution and co-occurrence across the WSI, while efficiently modeling a large number of spatially distributed regions. Extensive experiments across four WSI subtyping datasets demonstrate consistent advantages over representative state-of-the-art methods. Further evaluations under small-cohort and few-shot settings demonstrate robustness and data efficiency under limited training data. Code will be released at this https URL.

---


### 118. [Observation-Conditioned Latent Energy Priors for Sparse Implicit Neural Shape Completion](https://arxiv.org/abs/2609.03694)

**<font color=#1a73e8>作者：</font>** Paul Büschl, Ezequiel de la Rosa, Julia Wolleb 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit neural representations (INRs) can model continuous 3D shapes with a shared coordinate decoder and per-instance latent codes. At test time, autodecoder-style models commonly freeze the decoder and optimize a new latent code from sparse off-grid SDF samples. When these samples underconstrain inference, the latent can drift toward regions that fit the observations but decode implausible unobserved geometry. We propose a post-hoc observation-conditioned latent energy prior for frozen INR decoders. The energy scores standardized latents conditioned on a permutation-invariant encoding of the sparse observation set and is used as a residual expert alongside an L2 latent prior selected on validation data. We evaluate on a controlled cell-nucleus SDF dataset and a public MedShapeNet-derived SDF completion dataset. The proposed L2 objective augmented with conditional energy improves consistently over a validation-selected L2 baseline in the sparsest cell-nucleus regimes and, on MedShapeNet, outperforms both L2 and a six-component GMM latent-density prior across all reported readouts. A shuffled-context ablation is consistently weaker than matched context, supporting an observation-specific contribution. These results suggest that lightweight conditional energies can make pretrained INR decoders more observation-aware without retraining.

---


### 119. [SignSeek: Learning Transferable Representations for Sign Dictionary Retrieval](https://arxiv.org/abs/2609.03695)

**<font color=#1a73e8>作者：</font>** Sobhan Asasi, Ozge Mercanoglu Sincan, Richard Bowden  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign language dictionaries are essential resources for sign language learners, yet automatically retrieving a sign from a dictionary, given only a query video, remains a challenging problem due to the natural variability between signers. Existing sign representation learning methods are built for closed-set recognition, producing embeddings that do not generalise to the open-set, signer-independent setting that retrieval demands. \textbf{SignSeek} closes this gap by contrastively learning sign representations with saliency-guided articulator masking. A contrastive objective aligns same-gloss signs across signers, while our Articulator Saliency-Guided Masking (ASGM) pinpoints the single most critical articulator per sign. This drives two complementary objectives, a masked contrastive alignment (MAC) loss that sees the sign through a single articulator and a masked prediction (MAP) loss that reconstructs it in latent space from the surrounding spatio-temporal context. Pretrained on 266K samples ($\sim$5,700 glosses) across multiple sign languages, \textbf{SignSeek} sets a new state-of-the-art performance in cross-corpus retrieval on ASL-Citizen, WLASL, and NMFs-CSL without any downstream fine-tuning. Strikingly, it achieves zero-shot generalisation to an entirely unseen British Sign Language (BSL), surpassing methods explicitly trained on BSL, and transfers seamlessly to isolated sign recognition and subtitle alignment, outperforming prior skeleton-based methods.

---


### 120. [Federated Causal Discovery via Regression-Directed Cumulants](https://arxiv.org/abs/2609.03705)

**<font color=#1a73e8>作者：</font>** Pablo Torrijos, Fabio Stella, José A. Gámez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper we study linear non-Gaussian acyclic models (LiNGAM) when used in federated environments. These causal models allow one to go beyond Markov equivalence. However, in many domains data are scarce, and increasing the sample size by centralising data from different clients is not advisable due to regulations such as the GDPR. The federated environment offers an attractive option to balance privacy and causal discovery accuracy. Unfortunately, the standard centralised estimator in the LiNGAM setting, i.e., DirectLiNGAM, cannot be straightforwardly federated. Higher-order cumulant tensors offer a way around this obstacle: they depend only on the joint distribution of the variables involved and add exactly across independent sample groups, so a single communication round suffices in horizontal, vertical, and hybrid partitions.
However, FedISHC, i.e., the current federated method along these lines, breaks down under near-symmetric noise. To overcome the above limitation, we introduce the FedRCD family of causal discovery algorithms, and investigate three variants that trade off communication rounds against algebraic noise; two of them are exact federated counterparts of the centralised high-order cumulant (HC) and HC-LiNGAM algorithms, and the single-round variants further effectively support exact unlearning at any granularity, from a single observation to a whole client. Numerical experiments show that at sample sizes typical of real deployments, the entire cumulant-based federated family does not actually rank variables by the population asymmetry that the scores encode at zero. It ranks them by a variance ladder induced by the DAG along its directed paths, the cumulant counterpart of varsortability. Marginal standardisation collapses every cumulant method to near-random ordering, while scale-invariant DirectLiNGAM, not federable under this protocol, is unaffected.

---


### 121. [Counterfactual Routing Using Integer Programming with Constraint Generation](https://arxiv.org/abs/2609.03707)

**<font color=#1a73e8>作者：</font>** Daniël Vos, Sterre Lutz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present our submission to the IJCAI 2025 'Counterfactual Routing Competition' (CRC 25). The goal of the competition is to find counterfactual explanations for the shortest path problem. This requires deciding what the minimal changes to a road network would make a route chosen by the user the optimal route. This enables explanations such as "Your suggested route would indeed have been optimal, if road X were not a bicycle path." Our solution models the problem as an integer program, iteratively incorporating constraints until an exact solution is found. In the final evaluation on held-out test instances, our method ranked fourth in solution quality and obtained its solution fastest on every instance, with an average runtime of 9.0 seconds compared to 118.8 seconds for the next-fastest submission.

---


### 122. [Artificial Intelligence for Energy Optimization in Data Centers](https://arxiv.org/abs/2609.03716)

**<font color=#1a73e8>作者：</font>** Mohammed Basharath Ullah, Summaiya Unnisa Begum, Mohammed Nadeem Ullah  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data centers are increasingly optimized by artificial intelligence and, at the same time, increasingly loaded by it. The literature treats these as two unrelated problems: control studies model workload as an exogenous arrival process, while sustainability studies model infrastructure as a fixed multiplier. We screen roughly 194 papers retrieved through a documented protocol, code 63 of them, and report what the coding shows. Of 28 primary control-oriented studies, 18 are validated in simulation alone and 5 reach physical hardware or a production facility; none account for water withdrawal, and none account for embodied carbon. Reported savings intervals across four technique families overlap almost completely, which means the field cannot presently rank its own methods. Ten recurring gaps are scored for consequence and tractability, and we set out CLEAR-DC, a framework coupling a control-policy branch to a workload-demand branch through an explicit elasticity term, reads out net rather than direct benefit, and emits a schema-conformant record covering energy, carbon, water, embodied share and validation venue. The framework is an architectural and methodological proposal, not a trained system; the contribution we defend empirically is the corpus analysis and the reporting schema derived from it. Coding sheet, derived statistics and all result artifacts: this https URL

---


### 123. [Opening mind by opening architecture: analysis strategies](https://arxiv.org/abs/2609.03719)

**<font color=#1a73e8>作者：</font>** Francesco Vitucci, Giuseppe Silvi, Daniele Giuseppe Annese 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In numerical signal processing for electroacoustic composition, the progressive loss of specific development and research environments caused by the increasing use of digital market tools has favoured the dominance of the closed-architecture audio processor model. This model, while powerful, envisions the possibility of describing output data about its perceived characteristics, but at the cost of ignoring its internal process and interacting systems, which become complex, powerful environments but closed in an inscrutable black box, a loss we must consider. Any digital signal processing technique tells a story. Just as the words of a language incorporate social, historical and technical polysemic layers, a signal processor has its own story of implementation, a gradual technological achievement with its inevitable aesthetic consequences. Through the looking-glass of literature, one can access those environments with renewed awareness by reestablishing a scientific method and an attitude to research. In this specific case, starting from the case study of Manfred Schroeder's historical reverbs, we illustrate the process of building analytical evaluation tools, as well as practical implementation, at the basis of a conscious study path.

---


### 124. [Fill My Mirror: Geometry-Constrained Mirror Inpainting](https://arxiv.org/abs/2609.03740)

**<font color=#1a73e8>作者：</font>** Ofek Basson, Shimon Vainer, Yacov Hel-Or 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mirrors are common in real-world images, yet producing geometrically consistent reflections with generative models remains challenging. Unlike most objects, mirror appearance depends on scene geometry and viewpoint, making it hard to synthesize using learned appearance priors alone. We address this in the mirror inpainting setting, where the scene is fixed and only the mirror region is generated. Our key insight is that much mirror content is geometrically constrained by the visible scene and need not be hallucinated. We estimate scene geometry and project visible content into the mirror to recover reflection regions determined by geometry. A generative model then completes the mirror region via a two-mask diffusion strategy balancing geometric constraints with the model's learned priors, reducing projection artifacts and improving reflection consistency. The method is training-free and applicable to complex real-world scenes. We evaluate on MirrorBench-V2 (synthetic) and real images. Using standard and geometry-aware metrics, we show that explicitly using scene geometry improves consistency.

---


### 125. [KnowVis: Knowledge-Centric Visual Summarization for Video Lectures](https://arxiv.org/abs/2609.03742)

**<font color=#1a73e8>作者：</font>** Yi Xu, Yifan Hou, Xiaoyu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video lectures are valuable educational resources, but their dense and lengthy formats often overwhelm novice learners. This difficulty stems from a fundamental pedagogical mismatch: while videos deliver transient information linearly, human learning requires constructing interconnected cognitive networks, a task that induces severe cognitive overload for novice learners lacking prior domain knowledge. Existing video summarization methods fail to resolve this mismatch, as they primarily produce text-heavy, linear condensations that still demand high cognitive effort. To bridge this gap, we propose KnowVis, a framework that transforms linear video lectures into pedagogically grounded visual narratives. KnowVis first extracts a detailed concept map from multimodal video content to identify important and challenging threshold concepts, then constructs structured knowledge units, and finally synthesizes engaging visual summaries. Alongside the framework, we introduce a curated dataset of 125 educational videos across 10 academic disciplines, paired with 1,079 generated visual summaries. Extensive automated evaluations and a human study demonstrate that, compared to state-of-the-art baselines, KnowVis generates more accurate and clear visuals that successfully reduce cognitive load and significantly improve student learning effectiveness and knowledge retention.

---


### 126. [Projected Riemannian Gradient Descent for the Bures-Wasserstein Barycenter: Dimension-Independent Linear Convergence at Unit Step Size](https://arxiv.org/abs/2609.03762)

**<font color=#1a73e8>作者：</font>** A. Afham  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The computation of the Bures-Wasserstein (BW) barycenter of an ensemble of positive definite matrices arises throughout machine learning, optimal transport, and quantum information. Riemannian gradient descent (RGD) at unit step size -- the fixed-point iteration used in practice -- converges rapidly, yet existing analyses present a dichotomy: unit-step guarantees carry worst-case exponential dependence on the dimension, while dimension-independent guarantees require small step sizes that forfeit the empirical speed. We resolve this dichotomy, not by improving the guarantees for unit-step RGD, but by proposing a Projected RGD algorithm that achieves dimension-independent linear convergence at unit step size. The achieved rate, $(1 - \kappa^{-3/2})$, where $\kappa$ is the condition number of the ensemble, also polynomially improves on the best small-step guarantee ($\kappa^{3/2}$ versus $\kappa^{5/2}$ iteration complexity). The crux is a novel Projection Lemma: clipping the eigenvalues of a positive matrix to an interval $[\alpha, \beta]$ is the closed-form, non-expansive (1-Lipschitz) BW-metric projection onto the set $\{S : \alpha I \leq S \leq \beta I\}$ -- a statement which, unlike its known one-sided counterpart, does not follow from convexity. The projection is moreover free: it reuses an eigendecomposition the next iteration must perform in any case, so the projected and unprojected iterations cost the same per step. The same analysis covers the invariant matrix projection problem of Brahmachari et al. (2025), whose fixed-point algorithm we identify as unit-step RGD on a totally geodesic submanifold, thereby extending the dimension-independent guarantee to that setting verbatim.

---


### 127. [From Nowcasting to Forecasting: Adapting a Reanalysis-Trained](https://arxiv.org/abs/2609.03763)

**<font color=#1a73e8>作者：</font>** Mikko Partio, Leila Hieta, Ossi Laine  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate cloud-cover forecasts are important for temperature prediction, radiation forecasting, and solar-power operations. Short-range forecasting methods can preserve observed cloud placement during the first forecast hours, but their skill decreases when cloud fields evolve through formation, dissipation and deformation. Longer lead times require accounting for atmospheric evolution, but operational numerical weather prediction (NWP) forecasts may not accurately represent the satellite-observed cloud state at initialization. We develop CloudCast v2, a machine-learning model for 12-hour cloud-cover forecasting from observation-based initial conditions. The model is first trained on the Copernicus European Regional Reanalysis (Ridal2024) to learn cloud-evolution dynamics, and is then adapted to satellite-derived cloud fields using conditional flow matching (Lipman2023), a generative method that transforms noise into cloud-cover forecasts conditioned on the observed initial cloud fields and NWP inputs. CloudCast v2 reduces mean absolute error by 10% relative to its predecessor, CloudCast v1 (Partio2025), over the 1-12 h range. It also overtakes CloudCast v1 in fractions skill score, a neighborhood-based measure of spatial agreement, after approximately 3-6 h, depending on the cloudiness category. These results show that observation-initialized machine-learning forecasts can extend beyond the usual 1-3-hour nowcasting range while retaining spatial detail from satellite cloud fields.

---


### 128. [OBER+: Continuity-Aware Reporting and Traceable Continuous Improvement in Outcome-Based Education](https://arxiv.org/abs/2609.03770)

**<font color=#1a73e8>作者：</font>** Elakkiya Rajasekar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Institutions practising outcome-based education compute learning outcome attainment routinely, while reviews of curriculum analytics report an absence of evidence on how that computation informs decisions. This paper presents OBER+, an extension of a deployed institutional attainment platform that computes the step from a measured shortfall to an evaluated corrective action. Five connected stages accumulate attainment across deliveries of a course, signal a shortfall and a persistent shortfall, grade it on cutoffs the regulator already uses, record the decision against a catalogue of practices annotated with their evidence, log the change, and quantify the subsequent movement in the shortfall. A further rule compares successive statements of an outcome, so attainment is never read as a series across a point at which the outcome changed. Applying the rules to the live record of two real courses produced three results. Every outcome of a core course was substantively redefined between consecutive deliveries, with subject matter moving between outcome numbers, so a naive reading would have reported a twenty-five point collapse between quantities that do not refer to the same learning. Recomputing the platform's figures from its documented rule showed six of ten differing by more than rounding explains, in a pattern that identified a defect since reported to the institution. Across fifteen statement pairs from three transitions, five were identical character for character, and among the ten that were not, the outcome carrying a given number was nearest to a differently numbered earlier outcome in six, a result resting on an ordering of similarities and requiring no threshold and no labelling. The contribution is a computational design for outcome-based reporting, stated as rules any attainment platform can implement, with evidence of what they make visible in a live institutional record.

---


### 129. [Rethinking World Models for Safety-Critical Embodied Systems](https://arxiv.org/abs/2609.03774)

**<font color=#1a73e8>作者：</font>** Kailang Ma, Heye Huang, Inhi Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models have progressed from compact latent dynamics to generative, controllable, and interactive simulators of embodied environments. However, high predictive likelihood and visual fidelity do not necessarily ensure that a model preserves the evidence required for safe decision-making. This perspective identifies three structural mismatches in current world modeling: likelihood versus risk, prediction versus intervention, and finite-horizon prediction versus accumulated consequences. We propose the Risk-Informed World Model (RIWM) as a decision-centric research direction for safety-critical embodied systems. RIWM organizes world modeling around consequences, intervention, epistemic uncertainty, and recoverability, and integrates four interdependent capabilities: decision-relevant representation, counterfactual reasoning, safety-critical episodic memory, and runtime safety assurance. It distinguishes physical, social, and operational consequences while using epistemic uncertainty to qualify the evidence supporting action. We further discuss open challenges in identifying consequential futures, validating counterfactual reasoning, maintaining revisable safety memories, translating learned consequences into executable constraints, and determining when evidence is sufficient to act. This perspective argues that future world models should move beyond predicting likely futures toward identifying which futures matter, revising judgments through experience, and recognizing when to act, revise, sense, defer, or abstain.

---


### 130. [Auditing Contextual Bias in Human Ball-Strike Calls Using KBO's Automated Umpiring Transition](https://arxiv.org/abs/2609.03786)

**<font color=#1a73e8>作者：</font>** Kichang Lee, JeongGil Ko  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper uses the Korean Baseball Organization's adoption of the Automated Ball-Strike (ABS) system to audit long-standing claims about contextual bias in human ball-strike calls. Using pitch-level KBO data from 2021 through the available portion of the 2026 season, we model called-strike probability for taken pitches near the strike-zone boundary, with 2022-2023 as the primary human-umpire baseline and ABS seasons (2024 and onward) as a diagnostic benchmark. The strongest evidence concerns count pressure. Relative to 0--0 counts, human umpires called substantially fewer strikes in two-strike counts and more strikes in hitter-ahead three-ball counts. Specifically, in the main 0.25-ft boundary band, 0--2 was associated with a -17.17 percentage-point effect and 3--0 with a +6.61 percentage-point effect. Under ABS, the corresponding effects were close to zero and did not survive false-discovery-rate correction. Game progression shows a smaller but coherent pattern as human calls were less strike-prone in early innings and more strike-prone in innings 7--9+, especially in late-close situations, while complete ABS seasons were essentially flat. Other suspected biases are weaker or more localized. Salary-based reputation proxies provide suggestive but proxy-sensitive evidence, and catcher identity shows human-period residual heterogeneity that disappears under ABS. Home-context evidence is mostly null at the umpire level, with one FDR-significant human-period exception and an exploratory umpire-team gap best treated as an audit lead. Overall, the results do not show that human umpires were biased everywhere. Instead, they map where the human strike zone was most context-sensitive, where evidence was weaker, and where common suspicions received little support.

---


### 131. [DNative-Twin: Decision Graphs and Digital Twins for Reconstructable Agentic Decisions](https://arxiv.org/abs/2609.03787)

**<font color=#1a73e8>作者：</font>** Junjie Pang, Zhenzhen Xie, Haoke Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly gather evidence, invoke tools, apply constraints, and produce decisions that people or software may commit to action. A final output alone cannot show which evidence, tool state, rule, authorization, or action path produced it. We present DNative-Twin, a graph-native digital twin that records a committed agentic decision as a typed trajectory and re-executes its decision mechanism under declared conditions. The graph links the state observed by the agent, the path it followed, and the authority behind the resulting action. The twin synchronizes this information, replays the mechanism in isolation, and compares it under controlled changes. We instantiate the framework in enterprise decision processes using three public process logs and controlled replay suites. The experiments identify a specific failure: graph structure localizes represented changes but cannot determine the consequence of an unobserved tool state. In a three-condition controlled experiment with 300 injected instances, unresolved-divergence recall increased from 0 to 0.667 when replay-contract state was added and to 1.0 when verification results were also available; the held-out set contained no critical-class instance. Across 500--5,000 BPI 2020 cases, median end-to-end time increased from 0.794 to 8.889 seconds on the reported platform. These results separate the roles of graph structure, replay context, and verification evidence in reviewing a decision mechanism.

---


### 132. [Beyond the Trust Boundary: A Critical Reassessment of the FIDO2 Threat Model](https://arxiv.org/abs/2609.03789)

**<font color=#1a73e8>作者：</font>** Aditya Mitra, Kolluru Sai Abhiram, Sibi Chakkaravarthy Sethuraman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> FIDO2/WebAuthn has been widely deployed as a phishing-resistant authentication scheme. Because FIDO2 relies on public-key cryptography and hardware-backed authenticators, its security is often assumed to be guaranteed by design, provided that the cryptographic implementation is correct. In this work, we critically reassess the FIDO2 threat model and show that several commonly assumed security properties do not hold under realistic deployment conditions. We extend the threat model beyond the cryptographic layer to examine eight attack vectors across the FIDO2 stack: malicious browser extensions, platform-handler malware, passive sniffing, virtual device drivers, CTAP2-specific malware, USB/hardware implants, malicious USB hubs/docks/extenders, and NFC relay attacks. Our analysis shows that FIDO2 depends on environmental assumptions that may not hold in practice. We demonstrate how AAGUID and timing information can enable user profiling and targeted attacks, and how compromise of the browser, operating system, or hardware can undermine FIDO2 security even when the underlying cryptographic primitives remain uncompromised. We further show that attack chains spanning multiple layers can bypass the intended security guarantees of FIDO2. These findings indicate that the primary weakness in a FIDO2 deployment is often not the cryptographic layer, but the surrounding trusted environment. We also examine how these attack vectors can undermine device attestation by targeting the FIDO Metadata Service (MDS3), which serves as a root of trust for authenticator metadata. Finally, we characterize the attacks according to privilege, skill, and resource requirements. We conclude that effective FIDO2 security requires layered mitigations covering the browser, operating system, hardware, protocol stack, and metadata infrastructure.

---


### 133. [Landmark-Based Discrimination of Injury-Associated Athlete-Sessions from Minute-Resolution Multimodal Football Monitoring Data](https://arxiv.org/abs/2609.03790)

**<font color=#1a73e8>作者：</font>** Evangelos Chatzidimitriou, Konstantinos Tserpes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Athlete monitoring data may be recorded minute by minute throughout a match or training session, while injury information may only indicate whether the entire session was injury-associated.
This creates a modelling problem: assigning the same session-level label to every minute would imply that injury status is known at each exact time, even though within-session injury onset is unknown.
Our novelty is a fixed-landmark, one-representation-per-athlete-session formulation that directly addresses this mismatch. Instead of labelling every minute, we construct one representation per athlete-session at each landmark using information observed up to that point. This keeps the target at the session level and avoids unsupported minute-level injury supervision.
A landmark is a fixed time point within the same session, such as 10, 20, or 30 minutes. At each landmark, we assess whether the whole session is injury-associated or non-injury-associated and examine how discrimination changes as more within-session information becomes available.
Using 2020 SoccerMon data, we analyse 3,743 athlete-sessions from 48 elite women's football athletes, including 22 injury-associated sessions from five athletes. We evaluate pre-session, cumulative, dynamic, and combined representations with athlete-disjoint validation, athlete-cluster bootstrap uncertainty, common-cohort sensitivity analysis, alternative negative-athlete fold allocations, equal-athlete weighting, and Logistic Regression, Random Forest, and XGBoost benchmarks.
Primary CUM+DYN Logistic Regression yields ROC-AUC 0.367-0.607 and PR-AUC 0.0080-0.0150 across landmarks, with wide uncertainty. PRE-containing representations show higher point estimates at several landmarks but remain uncertain.

---


### 134. [Transfiver: Human-AI Co-Inference through a Shared Editable State](https://arxiv.org/abs/2609.03797)

**<font color=#1a73e8>作者：</font>** Minji Park, Seunghyun Yoon, Hyuk Lim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term human-AI interaction is difficult because the information that guides inference is updated implicitly by the model and is not directly inspectable or controllable by the user. We introduce the TRANSparent Framework for Interactive, Verifiable, Editable Representation (Transfiver), an architecture for human-AI co-inference through a shared editable state. Its central idea is that interaction-specific information is maintained in a single persistent state $(S_t)$ that both the model and the human update.
Transfiver distinguishes two modes of state evolution. In an implicit stream update, the model interprets ongoing interaction and decides whether new information revises an existing state item or creates a new one. In an explicit directed edit, a human inspects and modifies an addressed item. Both act on the same underlying state, so a human correction changes the state that subsequent computation reads, rather than adding another instruction or separate record.
The architecture separates shared parameters $(\theta)$, learned before ordinary use, from the persistent state $(S_t)$, which evolves during deployment without parameter retraining. Extending Transfiver to rich natural-language, relational, and large-scale shared states remains open.

---


### 135. [Govern the Model, Not Only the Data: Storage, Circulation, and Learning in Creative AI](https://arxiv.org/abs/2609.03800)

**<font color=#1a73e8>作者：</font>** Phoenix Perry, George Simms, Elizabeth Wilson 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Federated learning is increasingly presented as a privacy-preserving advance: personal data remain on the device, and only model updates are shared. It borrows the vocabulary of the federated social web, yet inverts its logic, distributing computation while the resulting model stays with whoever convened the training. We argue that federation is not in itself a remedy for extractive AI, because outcomes depend on who governs the data and the model and who has agency over the practices that shape them. We describe three layers at which a creative community can hold its work: storage, circulation, and learning. Examining artist-governed trusts, cooperatives, and consent infrastructures, we show that creator governance is established at storage and circulation but stops at learning: contributors can consent to training, yet have little say over the resulting model or its federation. We map the research space this opens, pairing technical open problems with the human questions from which they unfold. We propose four design principles for a creative data commons that governs models and their federation, not only datasets: govern the model, not only the corpus; make the terms legible at the moment of contribution; design for refusal as a first-class state; and decide stewardship in the open and account for it.

---


### 136. [From Ordered Bernoulli Levels to Critical-Line Geometry: Integer Quantization, Bernoulli Residual Phase, and Prime-Power Spectra](https://arxiv.org/abs/2609.03801)

**<font color=#1a73e8>作者：</font>** Y. Kenan Yılmaz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the ordered Bernoulli-word kernel f(p,n,k)=p^k(1-p)^(n-k) and the geometry generated by its inverse-integer level sets. The binary level 2^(-n) selects p=1/2 as the unique real split-independent anchor. Under complement-preserving complex continuation, the pair becomes z=1/2+iu and 1-z=1/2-iu, producing a conjugation-symmetric vertical geometry before any zeta-function input is introduced. The quadratic coordinate Q(z)=z(1-z)=1/4+u^2 has a sharp minimum at the central point and admits an exact integer quantization. For critical-line zero ordinates gamma_k, the induced levels L_k=1/4+gamma_k^2 are decomposed exactly as L_k=N_k+delta_k, where N_k is the nearest integer and delta_k is a periodic first-Bernoulli residual. Circularization gives Z_k=exp(2 pi i delta_k), isolating gamma_k^2 mod 1 as the residual phase variable. Unique factorization resolves the integer shells into prime-generator coordinates, while a distinct complex exponent s lifts the same construction to the Dirichlet atoms m^(-s), linking the Dirichlet-series and Euler-product assemblies. Exact identities, classical zeta connections, numerical controls, and open conditional Weyl tests are kept explicitly separate. No proof of the Riemann Hypothesis is claimed.

---


### 137. [Urban Boundaries, Social Barriers: A Benchmark and Vision-Centric Framework for Mapping Gated Communities and Equity Implications](https://arxiv.org/abs/2609.03804)

**<font color=#1a73e8>作者：</font>** Minwei Zhao, Weiming Zhang, Jiawang Du 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Communities are fundamental spatial units that shape urban form and social life. Whether a residential compound is spatially open or enclosed affects mobility, access to public services, and equity, yet studies of Chinese fengbi xiaoqu remain largely qualitative or small-scale, limiting reproducible city-scale analysis. We address this gap by introducing GBA-GCs, a metropolitan-scale multimodal benchmark for locally grounded gated/open community recognition in China's Greater Bay Area, covering 37,444 residential compounds with aligned boundary polygons, high-resolution satellite imagery, Chinese metadata, and structured attributes, together with expert-verified labels, inter-annotator reliability, and official evaluation splits. Built on this benchmark, we present Multimodal Classifier for Gated Community (MCGC), a vision-centric multimodal framework based on DINOv3-SAT that fuses imagery, text, and structured cues via modality-aware cross-attention and adaptive gating to mitigate modality imbalance. MCGC consistently outperforms strong unimodal and multimodal baselines. Finally, we apply the validated model to metropolitan-scale mapping and report equity-oriented findings including spatial clustering of GCs, privatized green space, and reduced pedestrian connectivity. The benchmark, code, and release documentation are available at this https URL.

---


### 138. [A Peer-Relative Representation Learning Framework for Energy Inefficiency Identification in Mobile Network Sites](https://arxiv.org/abs/2609.03809)

**<font color=#1a73e8>作者：</font>** Eliud Nyakweba Koto, Jaco du Toit, Adham Stoltz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Energy consumption is one of the largest operational expenditure items for mobile network operators, yet site-level energy inefficiencies such as faulty cooling controllers, idle radio equipment, and parasitic auxiliary loads often remain undetected because no ground-truth inefficiency labels exist and historical measurements may already contain embedded inefficiencies. This study proposes an unsupervised peer-relative approach based on the premise that sites with similar structural and operational characteristics should exhibit comparable energy consumption. To capture these relationships, a novel energy-aware Minimum Distortion Embedding (MDE) formulation is introduced that extends the standard MDE objective with an energy-based repulsion mechanism. This encourages sites with anomalously high energy consumption relative to comparable peers to become displaced from their local neighbourhoods in the embedding space. The resulting low-dimensional representation simultaneously preserves structural similarity and encodes energy-related deviations, enabling the identification of potentially inefficient sites through peer-relative comparison. The derived anomaly scores provide a practical mechanism for prioritising field investigations, allowing mobile network operators to focus engineering resources on sites most likely to yield energy savings. Experimental results demonstrate that the proposed approach outperforms conventional anomaly detection baselines and provides a robust foundation for large-scale energy-efficiency optimisation in mobile networks.

---


### 139. [SPARK: Input-Conditioned Sparse Activation Modulation for Frozen DiT-based Super-Resolution](https://arxiv.org/abs/2609.03813)

**<font color=#1a73e8>作者：</font>** Federico Putamorsi, Leonardo Zini, Marcella Cornia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world image super-resolution (SR) increasingly relies on Diffusion Transformer (DiT) backbones, whose internal activations can be dominated by a small number of massive channels. Yet improving perceptual quality in these models still typically requires fine-tuning the network or attaching additional adapters, leaving this structured activation space largely unexplored for adaptation. We investigate whether dominant channels can instead serve as a compact adaptation interface for frozen DiT-based SR models. We first characterize their behavior in pretrained SR backbones and show through controlled interventions that they strongly affect reconstruction quality. Building on this observation, we introduce SPARK, a lightweight input-conditioned controller that predicts bounded per-channel affine transformations for only the selected channels, while keeping the SR backbone and VAE frozen. Dominant channels are identified through an online activation-ranking procedure, and only a small predictor conditioned on the low-resolution VAE latent is optimized. Experiments on three DiT-based SR backbones across DIV2K, RealSR, and DRealSR show consistent gains in both fidelity and perceptual quality while modulating only eight channels per stream and block. Controlled comparisons further show that these gains cannot be explained by parameter budget or access to the selected channels alone.

---


### 140. [CauseCollab: Causal Unified and Modality-Agnostic Network for Heterogeneous Collaborative Perception](https://arxiv.org/abs/2609.03818)

**<font color=#1a73e8>作者：</font>** Weize Li, Yang Li, Quan Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Collaborative perception enhances environment understanding through multi-agent information sharing, but its performance in real-world scenarios is constrained by heterogeneous sensor modalities and model architectures. Recent protocol-based two-stage methods alleviate this problem by mapping heterogeneous features into a shared protocol space; however, independently trained modality-specific converters often generate modality-specific pseudo-protocol distributions, leading to semantic inconsistency and error accumulation, which is particularly pronounced in scenarios with large modality discrepancies. To address this issue, we propose CauseCollab, a causal unified and modality-agnostic network. CauseCollab formulates representation learning in the protocol space from a causal perspective, explicitly disentangling semantic factors from modality-specific statistical confounders via causal metric learning. Meanwhile, CauseCollab adopts context-guided Unified Converter for heterogeneous modalities to ensure cross-modal semantic consistency. In addition, integrating new modalities only requires training adapters with minimal parameters. Extensive experiments on the OPV2V and DAIR-V2X datasets demonstrate that CauseCollab achieves state-of-the-art performance, with more significant gains in scenarios involving large modality gaps.

---


### 141. [Witnesses Explain Anomalies](https://arxiv.org/abs/2609.03826)

**<font color=#1a73e8>作者：</font>** Lamine Diop  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised anomaly detection scores each point of an unlabelled, contaminated sample in a single pass, and increasingly must also explain why a point is flagged. Yet the dominant detectors give a score with no account of which features drive it, and explanations are bolted on post-hoc with SHAP or LIME, which re-query the detector thousands of times per point and only approximate it. We introduce WAND, an unsupervised tabular anomaly detector that is explainable by design. WAND organises its computation around directions on the unit sphere, scoring each point by how far its projection escapes a sub-Gaussian extreme-value baseline. The originality of our approach is that the witness directions that flag a point, being vectors in feature space, are its explanation, a per-feature attribution obtained at no cost over scoring and, since the score is differentiable, recoverable by gradients. Scoring is linear in the sample size, and a probe-efficiency bound guarantees every anomaly a witness, hence an explanation. Across 47 ADBench datasets WAND attains the best mean Friedman rank at ROC-AUC parity with 16 unsupervised baselines, so the gain is interpretability at no accuracy cost; its native explanations are more accurate and faithful than post-hoc SHAP/LIME and ECOD at a fraction of the query cost. WAND is thus a practical, interpretable solution for explainable anomaly detection.

---


### 142. [The impact of phase information for few-shot fine-grained image classification](https://arxiv.org/abs/2609.03829)

**<font color=#1a73e8>作者：</font>** Ruiling Liu, Linyue Zhang, Wenyi Zeng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot fine-grained image classification (FSFGIC) aims to classify similar images with limited labeled examples. This work highlights the critical yet underutilized role of phase information in capturing structural relationships within an image. This study introduces a novel plug-and-play amplitude-phase integration (API) module that effectively combines local and global frequency amplitude and phase information for obtaining more comprehensive feature descriptors. Additionally, a dedicated network, named PSF-Net, is proposed that adaptively fuses phase-based spatial and frequency information for FSFGIS. The designed PSF-Net can be easily integrated into standard episodic training architectures for end-to-end training from scratch. Extensive experiments on five public datasets demonstrate that the method outperforms existing state-of-the-art benchmarks.

---


### 143. [Multi-step Proximal Policy Improvement in Offline Reinforcement Learning](https://arxiv.org/abs/2609.03842)

**<font color=#1a73e8>作者：</font>** Soohyun Choi, Seonvin Cho, Songnam Hong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning (RL) must reconcile two competing requirements: policy updates should stay near dataset-supported actions to keep value estimates reliable, yet meaningful gains often require moving beyond the behavior distribution. We develop a geometric view of offline actor updates by modeling policies as a probability manifold endowed with a chosen metric geometry. Under this lens, a broad class of offline actor objectives can be interpreted as a single proximal policy improvement step (SPI), i.e., an implicit discretization of a manifold gradient flow induced by a critic-defined energy. Building on this insight, we propose multi-step proximal policy improvement (MPI), a plug-in refinement mechanism that composes sequential re-centered proximal steps. MPI enables controlled policy improvement beyond dataset support while retaining proximal control at each refinement. The framework accommodates multiple policy geometries and admits practical instantiations for deterministic and diagonal-Gaussian policies. Experiments on D4RL benchmarks show that small numbers of MPI refinements improve strong offline baselines, including TD3+BC, ReBRAC, and IQL, on many tasks. Focused diagnostics further distinguish re-centered refinement from fixed-objective update scheduling and characterize limitations under critic error.

---


### 144. [NACRE: Rethinking Confidential Containers through Native Architectural Support](https://arxiv.org/abs/2609.03849)

**<font color=#1a73e8>作者：</font>** Linke Song, Wenhao Wang, Weijie Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Linux containers achieve high density and fast lifecycle operations by sharing the host kernel, but this design also lets a compromised host inspect or modify container state. Existing
confidential-computing systems protect an enclave address space or an entire guest operating system, while recent container-granularity systems still add a separate protection context.
These abstractions do not make a dynamic group of host-managed Linux processes the architectural protection unit.
This paper presents NACRE, a RISC-V hardware-software co-design for native confidential containers. Its key insight is to separate the host's authority to manage resources from its
authority to access or commit protected state. Hardware-recognized container identities direct protected traps to an isolated S-mode agent, while an M-mode monitor commits security-
sensitive identity, mapping, and page transitions. The agent delegates services to host Linux without changing satp; services that neither access private bytes nor modify protected
state also avoid M-mode. We prototype NACRE by extending QEMU, OpenSBI, Linux, a trusted agent, and runc. The prototype implements the single-container private-memory substrate and
covered launch, fault, fork/COW, user-access, and teardown paths. Across five lmbench syscall and pipe metrics, the three-run means remain within 3.5% of the runc-origin baseline. With
the eight nginx object-size means weighted equally, aggregate throughput is 1.9% lower.

---


### 145. [Pushing the (Decision) Boundaries: Dynamically Calibrating Differentially Private Noise to Explainability in Federated Learning](https://arxiv.org/abs/2609.03851)

**<font color=#1a73e8>作者：</font>** Michael Khavkin, Kichang Lee, Jaeho Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) with Differential Privacy (DP) is increasingly adopted to preserve data confidentiality in distributed machine learning. However, DP noise distorts learned representations and degrades explanation fidelity, limiting differentially private FL where trustworthy explanations are required, such as assistive clinical diagnosis. Prior work adapted DP noise with static feature-importance signals, restricting explainability to post hoc analysis and precluding noise calibration to explanation quality during training. We propose XCal-FL, a closed-loop, explainability-driven local training algorithm for image classification in cross-silo FL that dynamically calibrates DP noise from three complementary signals: (1) prediction logit variations, measuring causal influence on model confidence, (2) counterfactual margins, capturing decision-boundary sensitivity, and (3) saliency concentration, quantifying spatial coherence of model attention, while enforcing formal DP guarantees via adaptive privacy accounting. Experiments on three medical imaging datasets across varying FL configurations show that XCal-FL yields more accurate and interpretable global models, improving predictive performance by over 10\% and explanation fidelity by up to 5$\times$ over static-noise FL, and outperforming state-of-the-art adaptive DP methods in fidelity. XCal-FL also achieves higher privacy-budget efficiency, turning each unit of cumulative privacy loss into larger gains in both accuracy and explanation fidelity. Our analysis further reveals that, unlike predictive performance, which scales roughly linearly with privacy loss, explanation fidelity exhibits non-linear dynamics. These findings suggest explainability is a distinct dimension of the privacy trade-off that cannot be inferred from utility alone, with implications for training and privacy-budget allocation in decision-critical applications.

---


### 146. [High-Dimensional Learning Dynamics of Attention-Indexed Models](https://arxiv.org/abs/2609.03858)

**<font color=#1a73e8>作者：</font>** Yizhou Xu, Margarita Sagitova, Lenka Zdeborová 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention mechanisms are central to modern foundation models, yet their training dynamics remain poorly understood, especially when the attention matrices have extensive rank. In this work, we study attention-indexed models, a broad framework that can represent multi-layer and multi-head attention architectures. First, we show that, in a suitable high-dimensional limit, the population-loss landscape is characterized by a finite set of trace order parameters. In contrast, online stochastic gradient descent (SGD) is governed by an infinite hierarchy of matrix moments, which we show can be exponentially well-approximated by a finite truncated system. Second, this framework reveals that attention parameterization itself can act as an architectural implicit bias. Direct optimization of an attention matrix $S\in\mathbb{R}^{d\times d}$ can remain trapped in an uninformative state. Tied attention ($S=WW^\top$) induces an automatic symmetry-breaking mechanism and yields weak recovery in $\Theta(d^2\log d)$ samples. For untied attention, $S=UV^\top$, we uncover a fast-slow mechanism: the pre-activation mean first evolves on a fast timescale, while the overlaps evolve on a slower one. Weak recovery on the $\Theta(d^2\log d)$ scale occurs when the state selected by the fast dynamics breaks the initial symmetry.

---


### 147. [GazeFS: Target-Centered Gaze-Trajectory Forecasting and Stabilization from Gaze-Head History](https://arxiv.org/abs/2609.03868)

**<font color=#1a73e8>作者：</font>** Yaozheng Xia, Zaiping Zhu, Bo Pang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Target-centered gaze interaction requires more than suppressing frame-to-frame fluctuations: target acquisition produces task-aligned changes in gaze-head dynamics, while a gaze trace may retain a persistent target-relative residual direction. We formulate gaze correction as online target-centered gaze-trajectory forecasting and stabilization and introduce GazeFS, which maps a variable-length gaze-head history to the next target-center direction and a short-horizon Search/Focus estimate without target information at inference. Across 7,960 acquisition episodes from 30 participants, Search-Focus differences remain stable under quality control, onset exclusion, and duration matching. History windows improve phase decoding over the current endpoint, but explicit task progress remains a strong control. Under the 30-participant, five-fold grouped out-of-fold protocol across three seeds, the reductions relative to raw hold in Focus episode bias, within-episode dispersion, and P90 target error are 0.182 degrees, 0.257 degrees, and 0.400 degrees, with participant-bootstrap 95% confidence intervals excluding zero. Endpoint-free replay from empty history preserves the Focus advantage and yields raw-network phase balanced accuracy/AUPRC of 0.925/0.993; coordinate controls further show that recent history contributes beyond explicit progress metadata. GazeFS therefore improves Focus target centering and empirical residual contraction while leaving temporal smoothness as a separate objective.

---


### 148. [Differentiable Interval Bottlenecks for Interpretable Anomaly Detection in Numerical Data](https://arxiv.org/abs/2609.03878)

**<font color=#1a73e8>作者：</font>** Lamine Diop, Marc Plantevit  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reconstruction-based anomaly detectors are accurate but opaque: a deep autoencoder flags a sample without telling a practitioner which feature ranges made it anomalous. We propose DIFFINT, an autoencoder whose latent bottleneck is structured as a set of soft, axis-aligned interval memberships learned end-to-end directly from raw numerical data, without any discretization or binarization. Each latent unit corresponds to a human-readable hyper-rectangle in feature space; an instance is encoded by how strongly it falls inside each interval relative to the other units, and its reconstruction error is the anomaly score. This keeps the power of differentiable representation learning while exposing an inspectable internal structure. We make the inductive bias precise: a certified reconstruction-error lower bound for points that fall outside every active coordinate of the learned support (with a Lipschitz-enforced decoder), and a graded, empirically verified suppression mechanism for the usual case in which only a few features are abnormal; and we provide a closed-form, label-free importance that ranks each (unit, feature) pair from quantities the model already maintains, turning trained intervals into auditable candidate constraints without ever seeing an anomaly label. On 48 ADBench benchmarks against 22 baselines under a common [-1, 1]-normalized protocol, DIFFINT attains the best mean rank overall on both metrics (4.10 on ROC-AUC, 4.16 on AUPR); among inlier-only detectors it leads its regime clearly, and it is competitive with the strongest contaminated-data detectors (see the stratified and complete-case analyses). It is the only interpretable detector in the statistically-tied leading cluster of seven methods.

---


### 149. [Inferring Affective Consciousness in an Artificial Agent: A Case Study](https://arxiv.org/abs/2609.03883)

**<font color=#1a73e8>作者：</font>** Mark Solms, St John Grimbly, Bruce Bassett 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Creatures that display 'hedonic place preference behaviour' are thought by many scientists to experience feelings, on the assumption that their attraction to pleasure-producing substances which lack nutritional value (e.g. cocaine, morphine) cannot easily be attributed to unconscious instinctual behaviour. In this paper, we discuss how a simple artificial agent that instantiates attributes of an affective system engaging in felt uncertainty about its intrinsic needs in relation to environmental resources can similarly display hedonic place preference behaviour -- through an apparently subjective form of information processing -- while simultaneously being entirely deter-ministic. We outline some implications of this artificially engineered behaviour for our understanding of the physical basis of consciousness and the experience of free will.

---


### 150. [Practice Makes (Im)Perfect: A Look Back at Benchmarking Practices for Microarchitectural Side-Channel Attacks](https://arxiv.org/abs/2609.03893)

**<font color=#1a73e8>作者：</font>** Iliana Fayolle, Antoine Geimer, Daniel De Almeida Braga 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Microarchitectural side-channel research has grown at an exceptional pace in recent years, increasing the need for rigorous and meaningful benchmarking. Early attack papers typically relied on indirect proxies, such as covert-channel bandwidth or key-recovery on naive AES and RSA implementations, setting de facto standards that many subsequent works continued to replicate, sometimes by directly comparing against raw numbers from prior work. While these practices offer convenient points of comparison, current benchmarks may not be the most relevant to assess specific properties of new primitives. Even more problematic, microarchitectural attacks are notoriously sensitive to experimental conditions: minimal changes in the target system can significantly alter outcomes and performance. As a result, inadequate evaluation practices undermine reproducibility and cast doubt on the relevance of comparisons, even in top-tier venues where such issues should be identified. This paper tackles the core problem of proper benchmarking for microarchitectural side-channel attacks and examines its broader impact on research quality in the field. We survey 83 attack papers published in top-ranked security and architecture conferences from 2014 to 2024. From this corpus, we identify and define 19 recurrent benchmarking flaws that affect evaluation completeness, relevance, soundness, and reproducibility. These flaws include unfair or absent comparisons, missing code or materials, and the failure to evaluate the key attack properties. On average, each paper exhibits 5.5 such flaws, highlighting how widespread the issue is, even in highly selective venues. Based on our findings, we identify and suggest key properties that are relevant to properly evaluate new attacks. We also highlight trends over time and different practices between security and architecture conferences.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-194](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
