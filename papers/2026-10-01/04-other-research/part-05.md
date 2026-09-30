# 📦 其他研究 | 2026年10月01日

> 本类共 **447** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-447](./part-09.md)

---

### 201. [GlassFormer: Learning Real-time Glass Segmentation using Radar-Depth Fusion](https://arxiv.org/abs/2609.36844)

**<font color=#1a73e8>作者：</font>** Suhani Grover, Astik Srivastava, Viswas Dinesh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transparent surfaces are ubiquitous in built environments, yet they remain a persistent failure case for robotic perception. RGB cameras perceive the background behind glass rather than the surface itself, while depth sensors such as LiDAR, time-of-flight, and RGB-D often return invalid or background measurements in transparent regions. As a result, systems that rely solely on optical sensing may misinterpret glass walls, doors, or mirrors as free space, compromising safe and reliable navigation. Existing glass segmentation approaches address this by learning visual cues such as reflections, boundaries, and semantic context from RGB images. While effective under favourable lighting and viewing conditions, these cues degrade in low-light environments, under glare, or when glass surfaces are featureless or partially occluded. In this work, we propose a multimodal framework that fuses millimetre-wave radar with RGB-D sensing for real-time transparent surface segmentation. Radar reflects strongly off glass surfaces, providing a geometric cue that remains reliable precisely where vision and depth fail. We exploit this cross-modal inconsistency to generate a radar-guided spatial prior, which is integrated into a lightweight transformer-based segmentation network, GlassFormer, via cross-modal attention. We report results on a mixed-condition test split covering all scene types and a dedicated low-light split designed to stress vision-only methods. GlassFormer achieves 0.88 mIoU on the mixed split, and 0.59 mIoU on the low light split, demonstrating substantial robustness gains over vision-only baselines while maintaining real-time performance on resource-constrained platforms.

---


### 202. [Automated Screw Planning for Reduced Pelvic Fractures Based on Statistical Shape Models and Deep Learning](https://arxiv.org/abs/2609.36847)

**<font color=#1a73e8>作者：</font>** Yang Gao, Sutuke Yibulayimu, Yanzhen Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Percutaneous iliosacral screw fixation is an important minimally invasive treatment for unstable pelvic fractures. Because the sacroiliac region has complex anatomy and narrow screw corridors, the accuracy and safety of screw placement directly affect surgical outcomes. Accurate and reliable preoperative screw planning is therefore essential to improve surgical success and reduce intraoperative risks. Conventional preoperative planning typically requires surgeons to determine screw trajectories through manual measurements, a labor-intensive process that depends on subjective clinical experience. To address these challenges, we propose a fully automated pipeline for preoperative iliosacral screw planning in patients with pelvic fractures. Using patient-specific three-dimensional anatomy, the pipeline automatically identifies safe screw corridors and generates individualized insertion trajectories to support clinical preoperative planning. We evaluated the proposed pipeline on 200 clinical cases of pelvic fractures. Compared with conventional manual measurements, the safety margin of the safe insertion corridors increased by 2% across the four screw types, the mean planning time decreased by more than 90%, and the clinical acceptance rate reached 95%.

---


### 203. [An Effective, Reliable, and Robust Framework for Human Activity Recognition Using Wearable Sensors](https://arxiv.org/abs/2609.36848)

**<font color=#1a73e8>作者：</font>** Nafees Ahmad, Ho-fung Leung, Muhammad Adil Abid 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human Activity Recognition (HAR) through wearable sensors greatly improves the quality of human life through its multiple applications. For HAR, multi-sensor channel information is vital for optimal performance. Current work states that applying an attention neural network to prioritize discriminatory sensor channels helps the model classify activity more precisely. However, obtaining discriminatory information from multisensory channels is not always trivial, such as when collecting data from older hospitalized patients. In this context, existing HAR methods struggle to classify activities, particularly activities with similar natures. Moreover, HAR models predominantly suffer from overfitting due to the small size of available datasets, which leads to poor performance. Data augmentation (DA) is a viable solution to this problem. However, available DA methods have various drawbacks, including the possibility of being domain-dependent, resulting in distorted models for test sequences. To address these HAR problems, we propose a novel framework, ALAE-TAE-CutMix+, which focuses on two aspects. First, it enhances the latent information across each sensor channel and learns to exploit the relation among multiple latent features and the ongoing activity. Consequently, the discriminatory feature representations of each activity is enriched. Second, a new augmentation strategy is introduced to address the shortcomings of existing multi-sensor channel data augmentation. We then extend the framework to create a further enhanced version, namely ALAE-CIE-TAE-CutMix+, which learns to capture the interactions between the features of each pair of sensor channels. We find that although the first framework performs slightly better than the latter, the latter is nonetheless more reliable and robust. Both frameworks significantly outperform SOTA approaches on the four HAR datasets from diverse domains.

---


### 204. [Socialality Anchors: Towards Group-bounded Trajectory Prediction](https://arxiv.org/abs/2609.36852)

**<font color=#1a73e8>作者：</font>** Ziqian Zou, Conghao Wong, Qinmu Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Trajectory prediction is a key component for understanding human behavior patterns in dynamic scenes. Researchers have devoted substantial efforts to modeling social interactions, especially group-wise interactions, since group membership often reflects shared intention, coordinated motion, and stable mutual adaptation, thus providing a persistent and semantically meaningful social prior for forecasting. However, existing group modeling methods may rely on a fixed threshold and infer groups mainly from agents' relative positions within the observation window, overlooking the fact that grouping rules should be agent-specific, temporally coherent, and context-adaptive across diverse personalities, culturalities, and evolving interaction contexts. Inspired by human social perception that alternates between interpersonal distance in boundary-sensitive situations and relative speed consistency in dynamic interactions, we propose Socialality, a human-inspired trajectory prediction framework with interpretable Socialality anchors and an extended grouping window for stable, context-aware grouping inference. Concretely, Socialality introduces a duo-scalar-controlled grouping kernel Socialality that jointly leverages historical observations and short-term future trajectory previews to learn agent-specific grouping rules, and employs a group-wise perception mechanism to model in-group and out-of-group interactions in an intuitive and explainable manner. Furthermore, we conduct extensive experiments on standard benchmarks to demonstrate the performance gains of Socialality, and provide qualitative analyses and statistical studies of anchor distributions to verify the interpretability and stability of the proposed Socialality anchors.

---


### 205. [Markovian Nonconvex ADMM for Reinforcement Learning: Bellman-Resolvent Stability Beyond Smooth Blocks](https://arxiv.org/abs/2609.36859)

**<font color=#1a73e8>作者：</font>** Zhaojun Peng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We identify and study a structural mechanism for Markovian nonconvex ADMM in reinforcement learning. Using finite discounted MDPs as a canonical proving ground, we show that the discounted Bellman resolvent $(I-\gamma P_\pi)^{-1}$ can provide the multiplier stability that classical nonconvex ADMM analyses often obtain from a designated smooth block. Starting from this mechanism, we establish convergence under controlled Markov sampling and then under stochastic observations using an empirical Bellman surrogate that jointly represents the random residual and its Jacobian. Markov mixing, initialization drift, observation noise, and decaying bias enter as one operator perturbation, avoiding unbiased product and double sampling requirements. When the perturbations are square summable, the true KKT residual converges almost surely to zero. Under a finite conditional fourth moment condition, a companion iterate satisfies $ \mathbb{E}[\widetilde G_{K+1}] \le A/T+(B/T)\sum_{k<T}m_k^{-1}, $ which becomes $O(T^{-1}+T/N)$ for total Markov sample budget $N$, giving $O(\epsilon^{-1})$ iteration complexity and $O(\epsilon^{-2})$ sample complexity for squared KKT accuracy $\epsilon$. Beyond stationarity, discounted occupancy coverage yields $J^\star-J(\pi)=O(\sqrt G)$ for direct tabular policies, so covered exact KKT points are globally optimal, while a statewise quadratic Bellman-improvement condition sharpens the relation to $O(G)$. Finally, nonlinear policy, projected Bellman, and explicit occupancy formulations exhibit the same chain of operator invertibility, dual representation, and multiplier stability. This supports discounted operator invertibility as a reusable structural principle for primal-dual reinforcement learning.

---


### 206. [S2T-Unet: A Structure-to-Style Framework for Inter-Modality MRI Translation](https://arxiv.org/abs/2609.36866)

**<font color=#1a73e8>作者：</font>** Yichao Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inter-modality MRI translation aims to synthesize missing MRI modalities from available acquisitions, reducing the need for additional scanning while preserving clinically relevant anatomical information. However, existing image translation methods often learn intensity mappings without explicitly separating modality-invariant structural information from modality-specific appearance, which may lead to structural information loss or unrealistic image details. In this work, we propose S2T-Unet, a structure-to-style framework that explicitly models these two aspects. Specifically, vector quantization is introduced at the lower-level bottleneck to encode modality-invariant structural information using a learned discrete codebook. At higher levels, a modality transformation module uses decoder features to condition and transform encoder representations toward the target modality, thereby recovering modality-specific intensity and contrast information. Experiments on the IXI multi-contrast MRI dataset across four translation tasks demonstrate that S2T-Unet is comparable or outperform with state-of-art method.

---


### 207. [State Trace Rationale As Auxiliary Task in Reinforcement Learning](https://arxiv.org/abs/2609.36867)

**<font color=#1a73e8>作者：</font>** Muhammad U. Nasir, Alex Vogt, Steven D. James 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose STRAT, an auxiliary task that trains deep reinforcement learning (RL) agents to predict a short textual trace of their own state. Inspired by human spatial navigation, the description combines landmark, route, and survey knowledge, tracking the agent's position, inventory, goals, and immediate progress. Environment rules generate this text online without human labelling. Our method adds a single auxiliary head to a standard policy. Across 60 sparse-reward XLand-MiniGrid tasks, STRAT solves complex environments where standard RL fails outright, while compacting state representations and preventing rank collapse. Beyond performance gains, the predicted trace provides a readable account of agent beliefs at every step for no extra cost.

---


### 208. [Seeing Time: Visual-Temporal Representation Learning for Interpretable Time Series Clustering](https://arxiv.org/abs/2609.36873)

**<font color=#1a73e8>作者：</font>** Zheng Zhu, Zexi Tan, Yuming Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate Time Series (MTS) clustering is an important tool in temporal data mining, aiming to discover latent group structures from complex observations without supervision. Although existing deep clustering methods can learn discriminative temporal representations, the resulting latent clusters are often difficult to relate back to waveform characteristics that practitioners can directly inspect and compare, limiting their ability to assess whether the discovered patterns reflect meaningful temporal behaviors. This paper, therefore, proposes WAVE (Waveform Aligned Visual-temporal Embedding), which treats time series and their deterministically rendered waveform plots as complementary views of the same observations. To produce discriminative representations whose cluster structures can be traced to observable waveform characteristics, WAVE aligns and integrates fine-grained temporal variations with holistic visual patterns, while associating each discovered cluster with its centroid-nearest authentic sample. Accordingly, interpretability in this work specifically refers to waveform-level traceability rather than a general explanation of model decisions. Extensive evaluations across 10 real-world public datasets show that WAVE achieves the highest macro-averaged clustering performance and the best average rank among the compared methods, while qualitative case studies illustrate how the discovered clusters can be inspected through authentic waveform records. The source code is available at this https URL.

---


### 209. [What You Observe Determines How You Identify Causal Effects: Evaluating Causal Models across Observational Views](https://arxiv.org/abs/2609.36881)

**<font color=#1a73e8>作者：</font>** Heejin Jung, Gyeongdeok Seo, Hoyoon Byun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal foundation models (CFMs) pre-trained on data generated from various structural causal models (SCMs) have been proposed for estimating causal effects from observational data. However, differences in pre-training environments and evaluation protocols make it difficult to assess how their performance depends on the information available for causal identification. To enable controlled comparisons, we introduce CausalIDView, a multi-view benchmark that holds fixed SCM realization and target estimand while varying only the observational view available to the estimator. Each observational view corresponds to a distinct identification regime under the benchmark's maintained causal assumptions. Across these matched views, no CFM consistently performs best and model rankings vary substantially. Under controlled structural changes, CFMs exhibit model-specific failures to maintain stable estimates when true effects are unchanged and to track genuine effect changes. We also examine whether combining explicit identification with strong predictive estimation is effective. A modular approach that pairs a predictive tabular foundation model with regime-specific identification procedures is competitive with CFMs and outperforms several of them. These findings motivate cross-regime comparisons to assess the empirical value of CFMs.

---


### 210. [Less Supervision, Better Generalization: Weakly Supervised Fake Region Localization in Diffusion-Edited Images](https://arxiv.org/abs/2609.36882)

**<font color=#1a73e8>作者：</font>** Junhee Lee, Donghyeon Jeon, Taeoh Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Localizing AI-edited regions is essential for interpretable forensic analysis, but remains challenging due to subtle and spatially distributed artifacts that are misaligned with semantic or object boundaries. Existing approaches rely on pixel-level supervision from controlled editing pipelines, which is difficult to scale and can introduce misleading signals: artifacts frequently extend beyond annotated regions, while out-of-mask pixels are treated as authentic. This limits models' ability to capture transferable evidence and generalize across generators and datasets. To address these issues, we propose ReGFLoW, a Reconstruction-Guided Fake Localization framework under Weak supervision, which is the first weakly supervised approach for diffusion-edited fake region localization. ReGFLoW requires only real/fake labels at the image-level and uses diffusion reconstruction errors as dense spatial guidance to inject them into both feature and score spaces. Furthermore, by artifact-centric multiple instance learning, ReGFLoW utilizes localized diffusion evidence without relying on semantic-affinity or boundary-based pseudo-mask priors. Extensive experiments demonstrate that ReGFLoW achieves stronger out-of-domain generalization than fully supervised learning baselines.

---


### 211. [SINO: Scale-Invariant Neural Operator](https://arxiv.org/abs/2609.36890)

**<font color=#1a73e8>作者：</font>** Kaichen Ouyang, Chenglei Yu, Chuanrui Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In scientific machine learning, physical fields governed by partial differential equations exhibit low-rank structure and scale invariance. When solving equations on coarse grids, missing information leads to the closure problem: modeling unresolved physics to recover lost dynamics. Although closure terms depend on grid resolution, they represent scale-invariant physical laws. A model truly learning physics should capture these mechanisms with low-rank parameterization rather than memorizing grid-specific patterns. Inspired by this, we propose the Scale-Invariant Neural Operator (SINO), which learns on normalized physical scales via a dual-branch architecture operating in spectral and spatial domains. SINO uses bottleneck MLPs to generate continuous convolution kernels, embedding an explicit low-rank inductive bias that concentrates more than 95 percent of variance in 2-3 modes, as validated by PCA across benchmarks, while drastically reducing parameters. This principled design yields 38 times steeper scaling law exponents than FNO, demonstrating superior parameter efficiency. We compare SINO with traditional models (U-Net, DeepONet), Transformer models (Transolver, Oformer, GK-Transformer), and frequency-domain models (FNO, AMFNO, UFNO) on closure problems spanning externally forced Burgers turbulence, decaying Burgers turbulence, KS turbulence, Kolmogorov-forced NS turbulence, and decaying NS turbulence. Experiments show SINO achieves 1.5-38 times error reduction and 2-23 times parameter efficiency over baselines, with superior scaling laws reflecting exceptional data efficiency from principled low-rank design. Code is available at this https URL.

---


### 212. [ProGuT: Label-Efficient Panoptic Segmentation for Forest Scenes](https://arxiv.org/abs/2609.36891)

**<font color=#1a73e8>作者：</font>** Pankaj Deoli, Karsten Berns  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoptic segmentation in forest environments is bottlenecked not by semantic quality but by instance separation; existing unsupervised panoptic approaches produce usable stuff maps but near-zero thing quality. Depth or flow-based instance discovery methods needs sensors that are not always available. We present ProGuT (Prototype Guided Training), which produces panoptic pseudo-labels without per-image training masks, needing only unlabeled images and one-time cluster-to-class mapping. ProGuT clusters CLIP patch features, then recovers trunk instances through multiscale geometric prior that falsifies non-trunk structures via structure-tensor. This is cheap compared to depth, flow or class-supervision methods to create pseudo labels. These are then used for downstream tasks which we evaluate against other unsupervised baselines. ProGuT achieves a Panoptic Quality (PQ) of 65.2 on Our-forest dataset (2.6x improvement over the initial pseudo-label quality) and reaches 65.9 mIoU on Freiburg Forest, outperforming unsupervised baselines like PiCIE (45.3 IoU) and STEGO(57.6IoU). Additionally, ProGuT outperforms existing unsupervised methods for class-agnostic trunk instance benchmark.

---


### 213. [DiffReID: Discriminative Diffusion Model for Object Re-Identification](https://arxiv.org/abs/2609.36894)

**<font color=#1a73e8>作者：</font>** Yingquan Wang, Pingping Zhang, Dong Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As a fundamental image processing task, object Re-Identification (ReID) aims to retrieve objects across non-overlapping cameras. Recently, with the development of deep learning, significant advancements have been made in object ReID. However, most existing methods suffer from generalization due to the limited size and diversity of ReID datasets. Meanwhile, current models tend to focus on extracting semantic patterns rather than learning identity-aware feature distributions. To address these issues, we propose a novel feature learning framework named \textbf{DiffReID} for object ReID. It leverages a discriminative diffusion model to gradually learn identity-aware distributions and generate identity-invariant features. More specifically, with the Contrastive Language-Image Pre-training (CLIP) model, we first obtain identity-aware text features by prompt tuning. Then, we propose a Vision-guided Noise Generator (VNG) to initialize probabilistic noises and gradually corrupt identity-aware text features. Afterwards, we take visual features as conditions and propose a Light Weight Denoiser (LWD) to denoise the corrupted text features step-by-step for identity-aware distribution learning. To obtain discriminative features, we further generate identity-invariant guided features from randomly sampling visual-guided noises. Finally, we propose a Mutual Enhancement Constraint (MEC) to facilitate mutual learning between visual features and guided features to enhance the representation robustness and discrimination. Extensive experiments on five object ReID benchmarks demonstrate that our method shows better results than most state-of-the-art methods. The source code is available at this https URL.

---


### 214. [HorizonFlow: Variable-Length Planning for Offline Goal-Conditioned RL](https://arxiv.org/abs/2609.36896)

**<font color=#1a73e8>作者：</font>** JunHyeok Oh, Zian Jang, Byung-Jun Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative planning have made trajectory inpainting a promising approach to offline goal-conditioned reinforcement learning. However, these methods typically specify the planning horizon before generating plan content, even though the appropriate horizon depends on the route itself. A horizon that is too short can force infeasible transitions, whereas one that is too long can introduce redundant motion. We introduce HorizonFlow, a hierarchical planner that treats plan length as an output of generation rather than a prescribed input. Its subgoal route planner guides its action-prefix controller through a sequence of latent subgoals. Both components combine insertion-based generation with flow matching to jointly generate continuous plan content and length, using the partially generated plan to guide token insertion. HorizonFlow reuses the resulting length information to select candidates and steer generation toward shorter plans without a separate learned value model. Across Maze2D, Multi2D, and OGBench navigation and visual manipulation benchmarks, HorizonFlow achieves the highest average performance among the compared methods.

---


### 215. [RAEGNet: Relation-Aware Evidence Graph Network for Harm-Aware Multimodal Fake News Detection](https://arxiv.org/abs/2609.36902)

**<font color=#1a73e8>作者：</font>** Wenbin Shen, Guoxuan Qin, Guangxu Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing multimodal fake news detection methods often introduce external information to assist detection. However, most of them rely on entity-level retrieval and are therefore prone to introducing event-irrelevant noise. Meanwhile, existing methods mainly focus on improving overall performance and do not account for differences in the degree of harm posed by different instances of fake news. To address these limitations, we design an Event-Level Evidence Retrieval Framework (ELERF) and propose a Relation-Aware Evidence Graph Network (RAEGNet). ELERF retrieves external evidence based on the complete event semantics of a news item. RAEGNet constructs a directed graph that incorporates news-evidence stance relations and evidence-evidence interaction relations, and introduces a conditional-harm branch to jointly model authenticity and potential harm. Experimental results demonstrate that RAEGNet outperforms multiple baseline methods across all evaluated metrics on Weibo-21, Fakeddit, and our self-constructed SSS dataset.

---


### 216. [Variational Mixtures and Multi-Marginal Flow Matching: Advancing Statistical Inference with Biological Applications](https://arxiv.org/abs/2609.36911)

**<font color=#1a73e8>作者：</font>** Oskar Kviman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this thesis I develop methods for statistical inference when the distributions arising from complex biological systems are multi-modal, geometrically structured, and sometimes only defined up to a normalizing constant. I start from variational inference and, when analytic update equations are unavailable, move to black-box variational inference. To build intuition regarding inference challenges and the proposed methodologies, I introduce a novel unnormalized target density (the CoLN distribution) and reuse it as a controlled test case in the kappa. I then trace a trajectory of increasingly expressive approximations: ensembles evaluated with the multiple importance sampling ELBO (Paper A) and variational mixtures that automate component cooperation and exploration (Paper B). Because expressivity comes at a cost, I develop efficient mixture learning ideas, including Monte Carlo objective estimators to scale mixture learning more efficiently (Paper C). As a new result in the kappa, I overturn a three decades long misconception regarding the potential performance benefits of using mixtures in variational inference. Finally, I move from variational inference to flow matching, where I address the need for specialized treatment of interpolant learning in multi-marginal settings (Paper D). By combining insights from Papers A-D, I derive in Section 5.5 a new method: multi-marginal flow matching with mixtures of variational interpolants. I connect these methodological developments to biological applications, with special emphasis on three-dimensional spatial transcriptomics, where stacked tissue slices induce multi-modal dynamics across space.

---


### 217. [Seg3DParts: Segmentation-Grounded Controllable Part-Level 3D Generation](https://arxiv.org/abs/2609.36918)

**<font color=#1a73e8>作者：</font>** Jiantao Lin, Meixi Chen, Yingjie Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Part-level 3D assets are essential for editing, reassembly, and interaction, yet recovering such structure from a single image remains challenging due to occlusion, ambiguous boundaries, and the need for coherent multi-part reasoning. Existing approaches struggle to achieve both controllable part-level generation and coherent multi-part structure, as part identity and spatial allocation are typically inferred implicitly. We present Seg3DParts, a segmentation-grounded framework for controllable part-level 3D generation from a single image. By treating segmentation as an explicit grounding signal, our method defines part identity during generation, enabling each component to be anchored to a corresponding image region. To ensure coherent assemblies, we introduce structured cross-part interaction that allows components to exchange global context throughout the generative process. As a result, Seg3DParts directly generates well-aligned part meshes in a shared canonical space without post-hoc alignment, supporting flexible and controllable decomposition. We further introduce PartObjectNet, a large-scale dataset with over 200K objects and 1M annotated parts. Experiments demonstrate that Seg3DParts achieves superior geometry quality, cross-part coherence, and part-level controllability over existing methods.

---


### 218. [Benchmarking Automatic Speech Recognition Tools for Iberian Languages](https://arxiv.org/abs/2609.36920)

**<font color=#1a73e8>作者：</font>** Fernando López, Pablo Gómez, David Solans 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Comprehensive evaluations of automatic speech recognition (ASR) for Iberian languages remain limited, and low-resource languages, biases, and efficiency trade-offs are underexplored. We benchmark eleven systems, ten open-weight models and one commercial API, across five Iberian languages (Basque, Catalan, Galician, Portuguese, Spanish), with German and Turkish as controls. Evaluation uses an 85-hour dataset covering read speech, broadcast media, and audiobooks, assessing accuracy and efficiency via word error rate (WER) and real-time factors (RTF/RTFx). Results show no single model dominates: accuracy, efficiency, and language coverage present clear trade-offs. Low-resource languages, especially Basque, degrade significantly, highlighting the role of training coverage. We observe consistent sex disparities across most systems, highlighting fairness challenges in multilingual ASR. Overall, the benchmark provides practical guidance for real-world model selection.

---


### 219. [PrecogUI: Proactive GUI Agents via Pre-cognitive Simulation and Experience Retrieval](https://arxiv.org/abs/2609.36923)

**<font color=#1a73e8>作者：</font>** Bin Kang, Jiarui Ouyang, Li Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing reactive Graphical User Interface (GUI) agents often fail in long-horizon, dynamic scenarios, where unexpected disturbances trigger attention-diverting and cascading failures. To address this, we propose PrecogUI, a pre-cognitive architecture that shifts the paradigm from reactive execution to proactive decision-making. Specifically, we design a Proactive Experience Pool (PEP), which caches recurring anomaly and success patterns as "state-action-result" tuples in a dual-memory repository. Furthermore, we introduce a Proactive Simulation Executor (PSE) that learns to forecast the next symbolic UI layout given a candidate action, enabling early anomaly avoidance and ranking candidate actions by predicted reliability. Finally, a Pre-cognitive Execution Controller (PEC) fuses these priors and predictions, prioritizes handling of foreseen anomalies, and ensures execution robustness through a closed-loop error correction mechanism. For robust evaluation, we develop AutoTraj, an automatic data-generation engine, to construct InterfereBench, a benchmark for long-horizon tasks with strong disturbances. Experiments demonstrate that PrecogUI surpasses state-of-the-art methods on InterfereBench while maintaining competitive performance on public benchmarks. The code will be publicly available.

---


### 220. [State Transport Routing for Short-horizon Adaptation in Multi-horizon Photovoltaic Forecasting](https://arxiv.org/abs/2609.36926)

**<font color=#1a73e8>作者：</font>** Xu Yuqing, Zhou Liguo, Sun Ze 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent power measurements provide valuable information for photovoltaic(PV) power forecasting, but directly extrapolating short-term trends can introduce substantial errors over longer forecast horizons. To address this challenge, we propose state transport routing (STR), a lightweight adapter that refines the predictions of a frozen forecasting model. STR combines the original forecast with two complementary trajectories derived from the latest measured power level and its recent trend. A horizon-conditioned router adjusts their contributions over the first 120 min, while leaving subsequent predictions unchanged. Experiments on four public PV datasets show that STR consistently outperforms a parameter-matched residual adapter. On PVDAQ, the same approach improves five neural forecasting backbones, reducing all-horizon normalized mean absolute error by 0.0201-0.2364 percentage points, with paired 95% confidence intervals excluding zero. No reliable improvement is observed for LightGBM. These findings demonstrate the potential of structured state adaptation to improve short-term forecasting across different neural architectures without retraining the underlying models or altering their longer-horizon predictions.

---


### 221. [SFE-VGGT: Source-Free VGGT Distillation for Event-Based Monocular Depth Estimation](https://arxiv.org/abs/2609.36929)

**<font color=#1a73e8>作者：</font>** Thai Duy Nguyen, Addison Lin Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent event-based depth estimation methods successfully transfer geometric priors from vision foundation models via cross-modal distillation. However, their reliance on synchronized RGB-event pairs or depth annotations during training severely restricts practical deployment. To overcome this bottleneck, we propose SFE-VGGT, a novel source-free framework that distills the geometric priors of VGGT to the event domain without any paired RGB observations. Our core idea is to reconstruct surrogate frames directly from the target event stream to act as a frozen geometric teacher, entirely eliminating the need for genuine source RGB data. Crucially, as these surrogate frames inherently yield imperfect and spatially varying supervision, directly distilling from them propagates artifacts. To resolve this, we introduce a novel reliability-aware distillation strategy. This includes Density-Aware Feature Distillation to emphasize informative event regions, and Confidence-Weighted Depth Distillation to dynamically regulate supervision based on relative teacher-student prediction confidence. Meanwhile, we propose a Cross-Frame Relational Consistency loss that enforces temporal geometric stability using reliable inter-frame correspondences, bypassing the need for temporally consistent teacher's depth. Extensive experiments demonstrate that, despite source-free, our SFE-VGGT closely matches the accuracy of RGB-dependent baselines under standard conditions and significantly surpasses them in challenging nighttime scenarios. Across MVSEC nighttime sequences, SFE-VGGT reduces the average 10 m depth error by 15.3% compared with EventVGGT. Moreover, our method exhibits robust zero-shot generalization across real-world datasets, proving that highly effective geometric priors can be transferred to event cameras using strictly source-free supervision.

---


### 222. [WeLike2Party! In-Context Motion Transfer for Multi-Human Image Animation](https://arxiv.org/abs/2609.36937)

**<font color=#1a73e8>作者：</font>** Sangeyl Lee, Seunghyun Shin, Seungho Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human image animation aims to transfer motion from a driving video to subjects in a reference image. Despite remarkable progress in video generation, achieving high-fidelity animation of multiple interacting subjects remains a challenge. Many existing approaches rely on explicit motion representations such as 2D skeletons or parametric body meshes and struggle to preserve identity-motion binding under inter-person occlusion. To address this limitation, we propose WeLike2Party, a multi-human animation framework built on direct in-context video conditioning without explicit pose or mesh extraction at inference. We further introduce Reference Asymmetric RoPE Conditioning to preserve fine-grained appearance details, and Identity Binding Supervision to associate each reference identity with its intended motion trajectory. To support cross-identity training, we construct MotionTwin, a large-scale synthetic dataset comprising 14.4K cross-identity video pairs with shared subject and camera motions, totaling 84.3 hours of photorealistic video. We additionally present MotionTwin-Bench, a cross-identity benchmark specifically designed to evaluate subject-level visual fidelity and identity-motion binding. Extensive experiments on MotionTwin-Bench and real-world videos demonstrate that WeLike2Party outperforms recent state-of-the-art methods in subject-level visual fidelity, identity-motion binding, and overall perceptual quality, particularly in multi-person interactions with substantial occlusion.

---


### 223. [SCA: Spatial Credit Assignment for Reinforcement Learning of GUI Agents](https://arxiv.org/abs/2609.36939)

**<font color=#1a73e8>作者：</font>** Shengtian Yang, Ziyu Xiong, Kaibing Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GUI agents automate tasks on digital devices by grounding language instructions in visual interfaces. Existing group-relative reinforcement learning improves GUI action prediction by comparing the rewards of multiple responses sampled from the same GUI state. However, binary evaluation treats spatially different failed clicks as identical and provides no relative signal when all sampled clicks fail. To address these limitations, we propose Spatial Credit Assignment (SCA), which uses the screen coordinates of sampled clicks to refine group-relative credit. Specifically, SCA predicts each held-out response's reward from the other responses in groups containing both successes and failures, then uses the prediction residual to adjust credit. When all sampled clicks fail, SCA instead orders them by distance to the annotated target. These spatial references are used only to construct the training update; the deployed policy remains unchanged. We evaluate whether this correction improves the policy update itself by comparing its error and directional alignment with the exact return gradient in a controlled synthetic study. Across GUI grounding and offline action-prediction benchmarks, SCA improves grounding across professional domains and achieves the strongest results among reinforcement-fine-tuned models on most action-prediction metrics, with consistent gains across the reported GUI suites.

---


### 224. [DispFlow-GS: Displacement Flow Supervision with Motion Disentangling for Monocular Deformable 3D Gaussian Splatting](https://arxiv.org/abs/2609.36940)

**<font color=#1a73e8>作者：</font>** Thai Duy Nguyen, Haitian Zhang, Addison Lin Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate dynamic scene reconstruction is important for robotic perception, where temporally consistent representations of dynamic environments are essential. Deformable 3D Gaussian Splatting (3DGS) models dynamic scenes through deformation fields, and recent methods incorporate motion supervision by aligning rendered Gaussian flow with optical flow. However, we find that such Gaussian-flow-based supervision provides only limited improvements in motion modeling. We identify a fundamental limitation of this supervision paradigm, namely a domain gap between rendered Gaussian flow and optical flow. To address this limitation, we propose a motion supervision framework built on Displacement Flow, which splats per-Gaussian 3D displacements onto the image plane to provide direct and stable optimization signals. We further disentangle scene motion from camera motion via intermediate-view rendering, enabling more reliable motion priors and targeted constraints on deformation and geometry. We also observe a discrepancy between motion fidelity and image-based evaluation, where improved motion awareness does not necessarily translate into better rendered image quality or higher image-based metric scores. Motivated by this mismatch, we introduce Deformation-Rendering Consistency (DRC), a motion-aware metric that measures the alignment between predicted deformation and rendering improvement. Experiments on dynamic scene benchmarks show substantial improvements in motion localization and motion--rendering consistency, reaching up to 39% and 6%, respectively, while image-based metrics change by only about 0.1%. These results confirm the observed mismatch between motion fidelity and image-based evaluation, demonstrating the significance of DRC for motion-aware evaluation.

---


### 225. [Safe-by-Design Learning via Energy-based Neural Networks](https://arxiv.org/abs/2609.36942)

**<font color=#1a73e8>作者：</font>** Simone Betteti, Morteza Lahijanian, Luca Laurenti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning neural-network models of dynamical systems with safety guarantees is a fundamental requirement for their deployment in safety-critical settings. Safety is commonly established by proving the invariance of a desired subset in state-space, ensuring that every trajectory initialized in this subset remains confined to it for all time under admissible inputs. Existing frameworks, however, either rely on computationally expensive post-hoc verification or employ safety-enforcing mechanisms without formal correctness guarantees. In this paper, we introduce a novel neural architecture grounded in energy-based modern Hopfield networks to guarantee safety-by-design while retaining sufficient expressiveness to model complex nonlinear dynamics. Specifically, we integrate modern Hopfield networks with a port-Hamiltonian neural ODE, enabling by design the construction of barrier functions yielding explicit admissible-input sets and quantitative robustness radii. Across several benchmarks, including an 12-dimensional nanodrone model, our framework achieves state-of-the-art performance while producing certified invariant sets that are more robust to external solicitations than comparable existing approaches.

---


### 226. [Dual-Channel Robust Group-Relative Policy Optimization via Advantage and Sequence-Weight Estimation](https://arxiv.org/abs/2609.36944)

**<font color=#1a73e8>作者：</font>** Zhongyi Li, Wan Tian, Xiang Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Group-relative policy optimization relies on reward-derived advantages and sequence-level likelihood weights, both of which can be sensitive to localized outliers. Extreme rewards can collapse the contrast among clean responses after group normalization, while token-level log-ratio perturbations can alter sequence weights and clipping decisions. We introduce RoVR-GSPO, a dual-channel robust optimizer that addresses these failure modes separately. Its reward channel combines robust reference estimation with bounded residual credit, while its ratio channel uses differentiable SoftRoVR aggregation to construct robust sequence weights. We provide stability and efficiency analyses for both channels. Experiments on mathematical reasoning, long-context summarization, and tool-call annotation show consistent improvements over GSPO, while controlled perturbation studies demonstrate stronger robustness to reward contamination and token-ratio anomalies.

---


### 227. [Scalable Diffusion SBI for Compositional Inference under Simulator Misspecification](https://arxiv.org/abs/2609.36950)

**<font color=#1a73e8>作者：</font>** Vincent D. Zaballa, Elliot E. Hui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simulation-based inference is challenging when many heterogeneous observations must be composed, hierarchical latent structure must be preserved, and the simulator is misspecified relative to observed data. We develop sampling and fine-tuning methods for diffusion-based inference in design-conditional settings, where the same simulator is queried across different experimental conditions $\xi$. We extend compositional score-based inference with a continuous-time diffusion coefficient that accounts for the number of observations, avoiding Jacobian and auxiliary-covariance corrections. We introduce Hierarchical Blockwise Diffusion Sampling (HBDS), which infers shared parameters and group-specific latent states using a single pretrained model, with the hierarchy specified only at sampling time. Together, these methods support variable observation sets and groupings without retraining. To address misspecification, we introduce path-regularized fine-tuning that adapts the learned likelihood to observations and transfers corrections to posterior inference. Using Girsanov's theorem, we quantify path divergence between pretrained and fine-tuned models across experimental designs and interpret it alongside predictive errors to distinguish candidate misspecification correction from unnecessary adaptation. We evaluate compositional sampling on exact-score Gaussian and Simple Likelihood, Complex Posterior benchmarks, HBDS with analytic and learned scores on a controlled hierarchical model, and fine-tuning and localization on a separate analytic model with known design-dependent discrepancy. Finally, we apply the framework to 940 measurements across four cell lines in a mechanistic Bone Morphogenetic Protein signaling model, where fine-tuning improves posterior-predictive accuracy relative to the pretrained model and shifts posterior marginals toward the least-squares reference while retaining spread.

---


### 228. [VStress: Correlation-Aware Auditing and Adaptive Budget Allocation for Repeated Verifiers](https://arxiv.org/abs/2609.36958)

**<font color=#1a73e8>作者：</font>** Miaobo Hu, Shuhao Hu, Xiaobo Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Repeated verifier calls are useful only when they contribute conditional information. We introduce VStress, an auditable replay contract, and VStress-CA, a correlation-aware allocation policy that estimates the conditional marginal information of an unqueried verifier on a sealed calibration split, discounts uncertainty, normalizes by call cost, and stops or abstains when the next call is not informative. The controller freezes its decision and cost ledger before joining the clean oracle; a dependence-shift alarm disables channel preference and falls back to exact-stop. The controlled audit gives the mechanism boundary: at 35% symmetric corruption, majority-5 improves balanced accuracy from 0.6578 to 0.7739, whereas at 65% it loses 0.1226 points. In the matched fixed-budget comparison, breadth, redundancy, and adaptive allocation obtain balanced accuracies 0.6048, 0.6375, and 0.6538, with 3.4216 calls per item and an RLVR score of 0.6417 for VStress-CA. Dependence diagnostics also increase from same-model repeats to cross-family channels, with conditional marginal gains of 0.0126, 0.0462, and 0.0913. These measurements turn correlation from a post-hoc warning into an auditable allocation decision.

---


### 229. [Prior-Driven Enhancements in 3D Gaussian Splatting: Normals and Depths Regularization](https://arxiv.org/abs/2609.36969)

**<font color=#1a73e8>作者：</font>** Gyeonggwan Lee, Seunghwan Hong, Junghun Suh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) is a state-of-the-art technique for 3D scene rendering, offering high efficiency and excellent visual quality. However, because 3DGS relies on an initial sparse point set from Structure-from-Motion (SfM) and view-dependent properties, it can suffer from geometric inaccuracies and visual artifacts, particularly in complex scenes. To address these challenges, we propose an improved 3DGS approach that regularizes the optimization process by integrating geometric priors, including surface normals and dense depth information. Surface normal regularization improves geometric consistency by aligning Gaussian covariance with local surface structures, while dense depth priors combined with an initial points from SfM enhance per-pixel depth estimation, increasing accuracy and reducing ambiguities. These enhancements enable robust handling of diverse and complex real-world scenarios, minimizing visual distortions and improving reconstruction quality across various environments. To validate our method, we evaluate it on challenging datasets, including street-view scenes and highly reflective environments, while testing it across multiple SfM pipelines. Our results demonstrate compatibility across diverse environments and highlight the robustness of our approach. Experimental findings further show that our method enhances geometric accuracy and visual quality, establishing a reliable solution for real-time 3D scene rendering in complex environments.

---


### 230. [Equally Good, Yet Different: Benchmarking Rashomon sets in AutoML packages](https://arxiv.org/abs/2609.36970)

**<font color=#1a73e8>作者：</font>** Katarzyna Woźnica, Katarzyna Rogalska, Zuzanna Sieńko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Rashomon effect describes the existence of multiple near-optimal models that achieve comparable performance while offering fundamentally different explanations. This creates a critical vulnerability in AutoML: x-hacking, the selective post-hoc choice of a model based on its explanation rather than predictive merit. No existing AutoML framework exposes this risk. We introduce ARSA ML, an open-source Python framework that quantifies Rashomon set structure and predictive multiplicity within AutoML pipelines. Using ARSA ML, we benchmark AutoGluon and H2O across 28 binary classification datasets, and conduct a post-hoc x-hacking analysis revealing a consistent structural asymmetry: AutoGluon produces larger, diverse sets with stable explanations, while H2O generates compact sets with markedly higher prediction divergence and explanation instability -- making H2O users considerably more exposed to x-hacking. This gap persists across all evaluated metrics and epsilon thresholds, pointing to a fundamental difference in each framework's model-building strategy. ARSA ML is available at this https URL .

---


### 231. [Structured Visual Target Learning For Cross-Subject eeg-to-image retrieval](https://arxiv.org/abs/2609.36971)

**<font color=#1a73e8>作者：</font>** Salini Yadav, Taveena Lotey, Mickaël Coustaty 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-subject EEG-to-image retrieval requires a neural represen- tation trained on source subjects to remain aligned with a visual embedding space for an unseen subject. Whereas existing methods primarily focus on the EEG side, we address this problem from the perspective of the visual target. Our approach preserves the spatial information of the Perception Encoder, converts its patch grid into a compact set of learned visual views, and aggregates them for each image with a block-structured, content-dependent router. The target is learned jointly with the EEG encoder through contrastive learning with MMD regularization across source subjects. For deployment, we propose a training-free representation refinement that aligns frozen embeddings without updating either encoder. Under leave- one-subject-out evaluation on THINGS-EEG2, the structured target achieves 35.3%/65.6% Top-1/Top-5 accuracy, the best among com- pared methods. Refinement raises this to 48.1%/77.1%, an 18.5% Top-1 gain over the strongest compared method, improving all ten held-out subjects.

---


### 232. [Repetition, Not Length: Isolating the Counting Failure in Neural Text-to-Speech](https://arxiv.org/abs/2609.36974)

**<font color=#1a73e8>作者：</font>** Kirill Borodin, Vasilii Kudryavtsev, Maxim Maslov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-speech models loop, truncate and lose count on text that repeats a phrase many times. We show that repetition itself is what breaks them, not the length that comes with it. Every repeated sentence in our test set is paired with a control of matched sentence and word count in which no word ever repeats back-to-back. Six models from three architectures render the controls almost perfectly and fail the repeated twins: 94.3% against 18.2% exactly right at k >= 6. The gap survives greedy decoding, repetition-penalty sweeps, four independent speech recognisers and 420 analysis specifications without once reversing sign; a held-out fourth architecture lands within a point of its predicted gap, and one of two non-autoregressive baselines shows the same failure. Varying the period of the text shows the failure grows smoothly with periodicity, half of it surviving when no word is adjacent to itself.

---


### 233. [A Dual-Track Curation-and-Classification Framework for Resolving Ground-Truth Label Noise in Operational Sentinel-2 Wheat Area Estimation](https://arxiv.org/abs/2609.36975)

**<font color=#1a73e8>作者：</font>** Kasimali Agharia, Ujjwal Kumar Gupta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Operational estimation of wheat-cultivated area is persistently constrained by discordance between administrative record-keeping and remotely sensed classification products. We address this administrative reference discordance for the 2022 Rabi season in Patiala district, Punjab, India, using a thirteen-timestep Sentinel-2 NDVI time series. A curated 849-sample reference dataset, developed through an iterative rule-based bootstrapping procedure, underpins both a feature sensitivity analysis and an operational classifier. Feature sensitivity independently assessed via Cohen's d and gradient-boosted information gain converges on the February-to-March grain-fill window as most discriminative. Four classifiers (1D-CNN, LSTM, hybrid CNN-LSTM, and XGBoost) were benchmarked on an identical 679/170 sample split. XGBoost achieved the highest overall accuracy (78.82%) against deep-learning baselines (64-66%), consistent with tree-based ensembles' favourable parameter-to-sample ratio in low-sample regimes. At full-population deployment across 36.25 million valid district pixels, the operational classifier attained 86.31% precision and 71.05% recall. The predicted wheat extent deviated by only +2.99% from the official tabular target, whereas the government's spatial reference mask exhibited a +25.11% positive area bias against the identical target. This asymmetry indicates that a classifier trained on an auditor-curated reference set reconciles more closely with the official tabular area than the spatial product conventionally used to validate it. We present this dual-track curation-and-classification framework as a methodological reference for crop-area reconciliation in label-noisy administrative settings.

---


### 234. [UltraMatch: Transport Path Routing for Ultra-Fast and Memory-Efficient Image Matching](https://arxiv.org/abs/2609.36980)

**<font color=#1a73e8>作者：</font>** Jiajun Le, Yifan Lu, Zizhuo Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent advances in accuracy and efficiency, coarse matching remains an indispensable yet costly stage in existing semi-dense matchers due to dense token-level matching. We present UltraMatch, an ultra-efficient and scalable semi-dense matching framework that bypasses the quadratic computation and memory cost of dense token-level matching by routing only a small fraction of candidate matching paths. At its core, a lightweight Transport Path Router operates on coarse block representations to rank candidate target blocks for each source block and retain only a small set, restricting subsequent token-level matching to the selected paths and avoiding the construction of the full token-to-token matching matrix. We further design a sparse global Dual-Softmax that performs matching only over the routed block candidates while retaining global competition across the sparse matching space. Beyond matching acceleration, UltraMatch employs deployment-oriented structural reparameterization for feature extraction and a tiny fine matching head with shared parameters, further reducing inference cost and memory consumption. UltraMatch achieves competitive accuracy among semi-dense matchers, while running 1.67$\times$ faster than SuperPoint+LightGlue with only 0.44 GiB peak inference memory. Its scalability enables inference at up to 6K resolution on a single RTX 3090, whereas existing semi-dense matchers run out of memory before reaching 2K. Our routing strategy is also transferable, delivering about 2$\times$ end-to-end speedup in EDM and ELoFTR without accuracy loss. The project repository is available at this https URL.

---


### 235. [REALHOP: Rethinking Multi-Hop Reasoning Evaluation via Behavioral Auditing](https://arxiv.org/abs/2609.36984)

**<font color=#1a73e8>作者：</font>** Jiawen Tao, Xiaokun Yuan, Yaoming Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complex questions often require multi-hop reasoning that connects facts distributed across sources or distant regions of a long context through intermediate steps. Benchmarks commonly evaluate this ability with questions built around predefined reasoning chains, treating a correct answer as evidence that the intended composition was used. Yet answer correctness alone leaves open whether success depends on the evidence associated with each intended step: models may instead rely on memorized associations, shorter paths, or partial evidence. We examine this dependence using the Behavioral Necessity Rate (BNR), which measures how often targeted evidence removal prevents answer recovery on initially correct instances. Across five existing benchmarks, panel-mean BNR ranges from 16.6% to 48.9%, exposing a substantial gap between annotated structure and observed dependence. Guided by this diagnosis, we introduce REALHOP, a diagnose-construct-verify framework that rebinds entities, factorizes selected relations, adds complete competing paths, and places evidence at traceable locations. Structural and semantic checks precede freezing; behavioral interventions follow. On 790 paired MuSiQue questions, REALHOP raises panel-mean BNR from 27.4% to 94.4% while retaining high Full accuracy. It also yields high BNR on REALHOP-FRAMES and REALHOP-LONGBENCH. On 216 long-context questions, the matched multiple-choice spread across 16 models grows from 13.9 to 59.2 points and persists under repeated open-ended evaluation. Together, these results show that a conceptually coherent chain and a correct final answer do not by themselves establish multi-hop reasoning. Verifying that success depends on every intended hop is therefore as fundamental to multi-hop evaluation as measuring answer accuracy itself.

---


### 236. [Abductive World Modeling via Causal Representation Learning](https://arxiv.org/abs/2609.36985)

**<font color=#1a73e8>作者：</font>** Ziqi Liu, Songhan Yang, Linfan Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The central challenge of world modeling is to learn representations that capture how the world evolves. However, existing world models predominantly represent future states without explicitly capturing the latent causes underlying their evolution, limiting their ability to reason about why and how the world changes. To address this limitation, we propose Abductive World Modeling (AWM), a framework that learns structured causal representations by abductively inferring latent causes from predicted futures. Specifically, we realize AWM through the Hierarchical Abductive State Pyramid (HASP), which organizes the inferred world state into three complementary components - Entity, Dynamic, and Relation - capturing what exists, how it changes, and how entities interact, respectively. By jointly reasoning over the current observation and its predicted future, HASP abductively infers these latent factors and integrates them into a structured state representation for downstream reasoning. To the best of our knowledge, AWM is the first framework to introduce abductive state inference into latent-space world modeling for learning structured representations of world dynamics. Experiments across physical prediction, causal reasoning, and action understanding demonstrate the effectiveness of our approach. Compared with V-JEPA, a state-of-the-art latent-space world model, AWM improves physical prediction AUROC by 10.7%, causal reasoning accuracy by 16.8%, and action Top-1 accuracy by 68.0%.

---


### 237. [CF-LoRA: Decoupled Factor Aggregation and Adaptation-Aware Client Clustering for Federated LoRA Fine-Tuning](https://arxiv.org/abs/2609.36986)

**<font color=#1a73e8>作者：</font>** Mengjun Yi, Langxing Yang, Suhan Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Federated LoRA fine-tuning enables parameter-efficient adaptation of pre-trained models without sharing private data, but suffers from two fundamental mismatches under heterogeneous client data: a structural aggregation mismatch caused by independently averaging LoRA factors, and a statistical collaboration mismatch caused by enforcing a single global adapter across divergent clients. To address these issues, we propose CF-LoRA, a clustered federated LoRA fine-tuning framework that combines decoupled factor aggregation with adaptation-aware client clustering. CF-LoRA first learns a globally shared $A$ factor while retaining personalized $B_i$ factors, then identifies clients with similar adaptation patterns based on the cosine similarity of their learned $B_i$ factors, and finally performs intra-cluster $B$-factor aggregation with a frozen $A$ factor. By decoupling LoRA factor aggregation, CF-LoRA preserves the low-rank structure and mitigates the structural aggregation mismatch, while adaptation-aware clustering promotes collaboration among clients with similar adaptation patterns and reduces negative transfer caused by statistical heterogeneity. Experiments on four language tasks and four vision datasets with RoBERTa and ViT show that CF-LoRA achieves the highest average accuracy in both modalities while communicating only one LoRA factor per optimization round.

---


### 238. [CypherTurn: A Multi-Turn Benchmark for Conversational Text-to-Cypher Evaluation and the Autonomy Divergence](https://arxiv.org/abs/2609.36987)

**<font color=#1a73e8>作者：</font>** Yuzhe Zhang, Weijie Zhu, Haolin Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Graph databases are increasingly queried through natural language, yet every existing benchmark evaluates isolated single-turn queries rather than the multi-turn sessions through which analysts actually work. We introduce CypherTurn, the first benchmark for conversational Text-to-Cypher evaluation, comprising 721 sessions and 5,927 turns across 7 knowledge graphs and 13 conversational phenomena. We evaluate 15 models under a guided oracle protocol and a fully autonomous agentic protocol, yielding four findings. First, the best model reaches only 64.7% execution accuracy, and session-level correctness remains below 5%. Second, despite strong overall rank correlation, frontier models exhibit a consequential reordering of the top of the leaderboard under autonomous operation, a phenomenon we term the Autonomy Divergence, which reveals error-management as a partially independent capability from raw generation skill. Third, scaling action budgets from x3 to x10 fails to close the autonomy gap, as the strongest frontier models self-limit to approximately two actions per turn regardless of available budget. Fourth, single-turn Cypher fine-tuning degrades multi-turn instruction following, while architecture-appropriate specialization outperforms several frontier models. These results establish CypherTurn as an open challenge for conversational graph database reasoning. Code and data are available at this https URL.

---


### 239. [Salt++: Context-Aligned Post-Training for Few-Step Streaming Multimodal Generation](https://arxiv.org/abs/2609.36995)

**<font color=#1a73e8>作者：</font>** Xingtong Ge, Yutong Wang, Lunjie Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step streaming audio--video generation requires both causal modeling and step distillation, yet standard training recipes face two context-related challenges. Teacher forcing pairs clean history with a noisy target, but supervises predictive contextual representations only indirectly through velocity prediction. Meanwhile, directly reusing bidirectional score models in causal Distribution Matching Distillation (DMD) creates a mismatch between generation and scoring contexts. We address these challenges with Salt++, a two-stage post-training framework comprising Causal Self-Flow (CSF) and context-aligned autoregressive DMD. CSF exploits contextual information asymmetry by varying the history while keeping the noisy target fixed: a noise-mixed-history student aligns its intermediate representations with those of a clean-history exponential-moving-average teacher. This self-supervised signal encourages the student to extract semantic information and improves cross-modal alignment. Context-aligned AR DMD shares the causal mask and prefix across generator sampling, fake-score training, and real-score evaluation to match generated and reference distributions under a block-conditional KL objective. With calibrated teacher guidance, it performs clean-prefix few-step distillation and then adapts to generated histories without switching objectives or requiring separate consistency distillation. At 480p, Salt++ improves visual and motion quality by 57% and 45% over OmniForcing on JavisBench under the same 4-step causal setting. A separate scale-wise post-training stage extends Salt++ to 4-step $1664\times960$ generation, outperforming bidirectional LTX-2 on six of seven reported metrics. Project page: this https URL

---


### 240. [ImbalancE: Inference-Time Latent Search Against Degree Imbalance in Link Prediction](https://arxiv.org/abs/2609.36996)

**<font color=#1a73e8>作者：</font>** Alberto Bernardi, Luca Costabello, Christophe Gueret  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge Graph Embedding models have been extensively used to learn representations of entities and relations in Knowledge Graphs for predicting missing links. However, the quality of the learned representations varies a lot across different areas of the graph. If previous research has loosely linked the problem to relation types or degree bias, we show that it is more widespread and it correlates with the degree imbalance of the entities in test triples. In particular, the prediction of a target entity that has a degree much smaller than the degree of the anchor entity is extremely problematic. This is critical in recommender systems and other use cases, where these triples represent important corner cases. To address this issue, we propose an inference-time latent search optimization method capable of significantly improving model predictions on the most imbalanced triples. Built on top of a pre-trained model, it explores the embedding space at evaluation time, blending known and out-of-band information to mitigate the degree imbalance bias. We show the value of our approach on imbalanced triples from common benchmark datasets, where we outperform conventional methods, opening the door to the successful adoption of Knowledge Graph Embedding models on these critical corner cases.

---


### 241. [Parameterized Stripe Attention for Efficient Video Generation](https://arxiv.org/abs/2609.37001)

**<font color=#1a73e8>作者：</font>** Xingyu Jia, Baole Ai, Ang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) enable high-quality video generation but suffer from substantial inference latency, primarily attributable to the computationally expensive full spatio-temporal attention. While sparse attention methods offer potential solutions, existing approaches face an inherent flexibility--efficiency dilemma: predefined masks lack the flexibility to capture diverse attention patterns, while runtime-determined masks introduce overheads and sacrifice hardware efficiency. We identify the lack of a unified structural characterization of DiT attention as a key limitation of existing methods, and establish that video DiT attention exhibits \textbf{periodic diagonal stripe structures} along both temporal and spatial dimensions. To formally encode these structured patterns within a single efficient kernel, we present {\bf PSA}, a parameterized stripe attention that formalizes the observed stripe regularity, unifying diverse attention patterns for efficient mask generation. This unified representation enables a single hardware-efficient CUDA kernel to process all sparse patterns, achieving FlashAttention-3-level Model FLOPs Utilization. To determine optimal sparsity configurations, we propose a training-free offline search algorithm that automatically maximizes sparsity under a specified error tolerance for each attention head. Experiments on HunyuanVideo and Wan~2.1 demonstrate that PSA achieves 1.57$\times$ and 1.37$\times$ end-to-end speedups over FlashAttention-3 baselines, with acceptable visual quality degradation.

---


### 242. [VesselBench-800K: A Large-scale Perception Benchmark for Multimodal Vessel Detection, Counting, and Density Estimation](https://arxiv.org/abs/2609.37003)

**<font color=#1a73e8>作者：</font>** Danfeng Hong, Chenyu Li, Jocelyn Chanussot  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vessel perception from space is crucial for a wide range of maritime applications, from traffic monitoring to environmental protection. However, most existing datasets predominantly focus on general object detection tasks in optical remote sensing (RS) images. Relying solely on single-modality optical RS images proves inadequate for effectively perceiving vessel objects in complex maritime scenarios, where ever-changing weather conditions (e.g., clouds and rain), the need for day-and-night coverage, and the inherent limitations of a single imaging modality pose significant challenges. To fill this gap, we introduce VesselBench-800K, the largest-to-date benchmark dataset on a global scale for vessel perception in multimodal RS images. As its name suggests, VesselBench-800K comprises 800,000 images, each at a resolution of 512x512 pixels, specifically curated for vessel perception tasks such as detection, counting, and density estimation. These multimodal image pairs (i.e., optical, SAR) are collected from diverse platforms, sensors, scenes, shooting heights, and synthetic sources, spanning spatial resolutions from 4.5m to 0.1m. Furthermore, we evaluate numerous state-of-the-art detection, counting, and density estimation models on VesselBench-800K through both qualitative and quantitative comparisons. By revealing previously unrecognized cues, this dataset holds immense potential to significantly advance our understanding of marine traffic. Our VesselBench dataset will be publicly available at this https URL to support and contribute to community development.

---


### 243. [World2Motion: Turning Video World Models into 3D Human Motion Generators](https://arxiv.org/abs/2609.37004)

**<font color=#1a73e8>作者：</font>** Tu Fangyuan, Xiangyue Zhang, Yiyi Cai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present World2Motion, a framework that generates scene-aware 3D human motion and corresponding video from a single image and a text prompt. While existing 3D motion generators learn from motion datasets, their generalization is constrained by limited coverage of environments. In contrast, video world models such as Cosmos 3 offer broader environmental priors but are not designed for full-body motion generation; recovering motion from their generated videos requires costly two-stage inference. To address these, we turn Cosmos 3 into a single-stage 3D motion generator. This adaptation has two challenges: the scarcity of paired video--motion data and temporal instability in the generated motion. First, we construct a training dataset combining synthetic video--motion pairs with real videos paired with estimated 3D motion. Second, we propose a shift-decoupled noise schedule that assigns different noise levels to video and motion through shared denoising progress. This design accommodates the different denoising requirements of the two modalities, reducing motion jitter. Experiments on a multi-source interaction benchmark show that World2Motion has better motion--text alignment and scene interaction compared with the evaluated 3D motion generators. It also matches the interaction success rate of the two-stage baseline while achieving approximately 3.3$\times$ faster inference.

---


### 244. [One Pipeline Does Not Fit All: TAILOR, a Type- and State-Aware Framework for CVE Reproduction](https://arxiv.org/abs/2609.37006)

**<font color=#1a73e8>作者：</font>** Ji He, Huang Zhang, Lijie Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Growing vulnerability disclosure and widespread software reuse increase security teams' need for reproducible evidence to diagnose vulnerabilities, validate patches, and build regression tests. Producing such evidence at scale requires automated end-to-end CVE reproduction. Existing methods typically process different CVEs through a uniform pipeline, but differences in runtime form, trigger interfaces, and prerequisite state impose different execution requirements on individual stages, making fixed workflows difficult to adapt to diverse reproduction needs. To address this problem, we present TAILOR, a type- and state-aware multi-agent framework specialized for complex vulnerability reproduction. TAILOR converts static vulnerability information into auditable reproduction evidence and packages reconstructed environments and trigger evidence into reproduction artifacts. Its first-level type-aware mechanism adaptively matches each vulnerability to an execution path. Within the Web path, its second-level state-aware mechanism constructs the required prerequisite state before exploitation, decouples prerequisite-state construction from core vulnerability triggering, and shares execution constraints across exploitation and verification. We construct a dataset of 200 CVEs with an emphasis on cases with complex execution requirements. TAILOR successfully reproduces 59.24\% of Web vulnerabilities and 44.19\% of traditional vulnerabilities. Further ablation experiments show that the two control levels respectively mitigate execution-path mismatch and missing Web prerequisite state. Overall, TAILOR broadens the coverage of automated CVE reproduction and provides auditable evidence for vulnerability diagnosis and defense.

---


### 245. [CADOC: Cache-Aware Dynamic Object Context for Long-Horizon Agents](https://arxiv.org/abs/2609.37012)

**<font color=#1a73e8>作者：</font>** Junjie Yao, Zhangchen Zhou, Zhi-Qin John Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For a long-horizon agent, context is the bottleneck: the history is resent with every request, the window caps task length, and reasoning degrades as the history grows. Replacing structured objects with compact retrieval Cards shortens the prompt and keeps the exact originals retrievable, but editing the history can break prefix-cache reuse, and prior recoverable methods time their edits by forecasts of future reuse or by preset intervals. We propose CADOC (Cache-Aware Dynamic Object Context), an online algorithm that replaces structured objects with compact Cards while preserving exact, on-demand retrieval of their original contents. CADOC schedules replacements in batches by balancing accumulated waiting cost against shared cache-reconstruction cost. Its scheduling rule follows from an economic order quantity trade-off, recovers the optimal integer batch under stationary assumptions. Across evaluation, CADOC consistently achieves the lowest aggregate input cost among the compared configurations, which reduces input cost by approximately 40\% on average while maintaining task performance close to full context. CADOC thus provides a cost-derived approach to compressible context management, demonstrating that efficient compression depends not only on shortening prompts but also on scheduling edits to preserve cache reuse.

---


### 246. [Embedded Bi-Temporal Building Damage Assessment for On-Board Data Reduction](https://arxiv.org/abs/2609.37013)

**<font color=#1a73e8>作者：</font>** Thomas Goudemant, Benjamin Francesconi, Marjorie Bellizzi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid assessment of building damage after natural disasters is essential to support emergency response. Earth Observation satellites can acquire relevant imagery shortly after an event, but exploitation is limited by uplink and downlink capacity and by ground-processing latency. We address this with a bi-temporal building damage assessment pipeline built on a siamese detector derived from YOLOX, designed to compress information at both ends of the ground/space link. On the ground, pre-disaster reference images are encoded into a compact latent space -- compressed by up to a factor of 64 -- and uplinked to the satellite. On board, this reference is compared with a fresh post-disaster acquisition so that the downlink carries only actionable object-level products, bounding boxes and damage classes, instead of full scenes. This cuts the data exchanged in both directions, while on xBD the strongly compressed reference still preserves most of the detection performance.
Because on-board acquisitions suffer from residual pre/post co-registration errors, we introduce a latent-space shift estimation and correction module that regresses the global offset from the coarse feature level and realigns the post-disaster features before fusion. It substantially improves robustness to de-registration -- especially under large shifts, where fusion-only variants collapse -- while also raising nominal accuracy and remaining compatible with the strongest compression. We finally port the pipeline to two embedded targets, a Xilinx Versal VCK190 and an NVIDIA Jetson AGX Orin, and report hardware performance (latency, throughput, power efficiency). The core detector and its compression port cleanly to both, but the operators needed for long-range robustness survive only on the Jetson GPU, whereas the Versal DPU does not.

---


### 247. [RBF-GNN: Rational Basis Functions for Pseudo-Coordinate based Graph Convolutions](https://arxiv.org/abs/2609.37015)

**<font color=#1a73e8>作者：</font>** Paweł Batorski, Abtin Pourhadi, Paul Swoboda  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose RBF-GNN, a new pseudo-coordinate based graph neural network architecture that takes into account Euclidean, spherical or angular coordinates and uses them to induce a powerful spatial inductive bias. Similar in architecture to SplineCNN, we improve upon the latter by replacing the less efficient sparse-activation based B-splines whose number grows exponentially with dimension by rational Padé basis functions. For effective training we propose a spline-subspace initialization and a variance-preserving weight rescaling. Experimentally, we evaluate on a number of popular neural network architectures that use SplineCNNs. We replace only the SplineCNNs with RBF-GNN. We achieve improved results, including on semantic keypoint matching, shape matching, event based camera computer vision tasks. We will make our implementation publicly available upon acceptance of the paper.

---


### 248. [Back2Struct: Making Structured Images Editable Again](https://arxiv.org/abs/2609.37016)

**<font color=#1a73e8>作者：</font>** Pengyu Yan, Yixin Wu, Yunjie Tian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structured images, such as diagrams, charts, and flowcharts, are inherently symbolic and can be compactly represented in an editable format, yet in practice, they are often rendered as images, and therefore not graphically editable. This mismatch presents a significant challenge for researchers, engineers, and designers who wish to incorporate modified versions of existing graphic content into new materials without manually reconstructing it. In this study, we presentBack2Struct, which "makes structured images editable again" by directly recovering vector graphics code (SVG / XML) from image representations. Given an image of a structured graphic, Back2Struct predicts semantically object-level SVG / XML code that explicitly encodes text, shapes, topology, and layout, rather than performing low-level pixel vectorization. The generated code can be seamlessly imported into tools such as PowerPoint, allowing users to edit, refine, restyle, and reuse graphic content while preserving structural fidelity. Beyond supervised fine-tuning on ground-truth SVG token sequences, we further optimize Back2Struct with reward-based learning to better match deployment-time requirements: the output should be syntactically valid, properly concise, and visually faithful to the input diagram. Specifically, we design a composite reward that jointly encourages SVG / XML compilability, length consistency with the reference code, and structural or semantic similarity between the generated and ground-truth graphics. These complementary signals guide the model to produce SVGs that are not only closer to the training distribution, but also more complete, editable, and renderable in practice. Experiments show that Back2Struct improves accuracy, editability, validity, and user alignment over baselines. Dataset and code are available at: this http URL

---


### 249. [Physics-Informed Multi-Agent Coordination for Hospital Patient Flow Optimization](https://arxiv.org/abs/2609.37022)

**<font color=#1a73e8>作者：</font>** Guoqing Zhang, Rafik Hadfi, Takayuki Ito  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient patient flow coordination across autonomous hospital departments is critical for mitigating overcrowding and balancing resource utilization. While classical queueing theory, specifically open Baskett--Chandy--Muntz--Palacios (BCMP) networks, provides an interpretable mathematical topology for healthcare operations, analytical models rely on stationary assumptions and fixed routing matrices that degrade under state-dependent real-world dynamics. Conversely, centralized reinforcement learning approaches struggle to accommodate the decentralized structure of hospital governance, where individual clinical departments function with localized observations, heterogeneous resources, and divergent operational objectives. In this paper, we present a Multi-Agent Systems (MAS) framework titled \emph{Physics-Informed Multi-Agent Coordination}, which embeds empirically calibrated BCMP queueing topologies as physical priors within a decentralized multi-agent reinforcement learning architecture. Formulated as a Decentralized Partially Observable Markov Decision Process (Dec-POMDP) under coupled resource constraints, our method enables autonomous departmental agents to cooperatively negotiate patient routing and dynamic service scaling. To mitigate environmental non-stationarity without inducing excessive communication overhead, agents exchange localized action fingerprints along network edges and optimize a spatially decomposed reward structure. Empirical evaluations driven by real-world MIMIC-IV patient trajectories indicate that this cooperative multi-agent approach substantially reduces cumulative system delay compared to static Markovian approximations, heuristic dispatching, and independent multi-agent baselines, while maintaining clinical safety constraints.

---


### 250. [Beyond Low-Rank Parameterization: Narrowing the Gap Between LoRA and Full Fine-Tuning via Gradient Decomposition](https://arxiv.org/abs/2609.37027)

**<font color=#1a73e8>作者：</font>** Yihao Ouyang, Shiwei Li, Haozhao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) is a widely used approach to parameter-efficient fine-tuning (PEFT), yet a performance gap can remain relative to full fine-tuning (FFT). Many LoRA variants improve the initialization or optimization of low-rank factors. At each training step, however, their first-order weight-space directions are constrained by the current parameterization. We characterize the corresponding LoRA-accessible gradient space and show that it coincides with the tangent space induced by the current LoRA parameterization. This characterization yields an orthogonal decomposition of the full weight gradient at the current model parameters. We term the component orthogonal to this space the normal gradient. Based on this decomposition, we propose GDLoRA (Gradient-Decomposed Low-Rank Adaptation). GDLoRA reconstructs the full weight gradient from forward activations and backward signals, extracts its normal component, and directly updates the base weights with this component, while retaining standard AdamW optimization for the LoRA factors. GDLoRA incorporates complementary normal gradients without increasing standard LoRA's optimizer-state memory budget under matched adapter and optimizer configurations. Experiments on natural language understanding, mathematical reasoning, commonsense reasoning, and image classification show that GDLoRA consistently improves over LoRA and narrows the performance gap to FFT. The code is available at this https URL.

---


> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-447](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
