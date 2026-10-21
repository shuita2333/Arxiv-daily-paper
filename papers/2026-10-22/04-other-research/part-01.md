# 📦 其他研究 | 2026年10月22日

> 本类共 **288** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-288](./part-06.md)

---

### 1. [AutoTerm-SST: Adaptive Terminology Memory with Zero Session-Time Setup for Streaming Speech Translation](https://arxiv.org/abs/2610.26865)

**<font color=#1a73e8>作者：</font>** Jiaxuan Luo, Siqi Ouyang, Lei Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented speech translation improves rare terminology, but systems such as RASST still assume that users provide a glossary before each session. That assumption is inconvenient for live talks, while merging every domain into one growing glossary eventually places too many irrelevant terms in the same retrieval and prompt competition. We present AutoTerm-SST, an interactive system that removes session-time glossary upload and domain selection. It organizes a large offline terminology catalog into topic slices, matches recent streaming translation context to bilingual slice prototypes, and activates a compact multi-slice working set under fixed retrieval and prompt budgets. On five ACL and five ESO oncology talks, AutoTerm matches a known-domain reference in terminology accuracy (88.3% vs. 88.1%) and mWER-resegmented BLEU (45.09 vs. 45.19), while requiring no domain input. Compared with a one-million-entry merged glossary, it improves terminology accuracy by 3.9 points and BLEU by 2.30. Routing plus four-slice retrieval remains lightweight: the complete system runs at 0.406 RTF, and the vLLM host sustains 32 real-time sessions. The live demo exposes active slices and retrieved terminology as the topic changes, providing zero-setup terminology-aware streaming translation.

---


### 2. [WaveCommitments: Private and Verifiable Speech-Agent Marketplaces](https://arxiv.org/abs/2610.26867)

**<font color=#1a73e8>作者：</font>** Oguzhan Baser, Kaan Kale, Sriram Vishwanath 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern speech systems are evolving into ecosystems of autonomous speech agents that speak together, negotiate, and trade assets such as embeddings, spectrograms, or raw data. In such markets, sellers cannot reveal assets for evaluation due to privacy constraints, and buyers cannot price what they cannot test. Thus, we open-source WaveCommitments, an end-to-end design that pairs confidential asset valuation via Data Shapley inside a trusted execution environment with multivariate polynomial commitments. It enables selective openings and tamper-evident provenance to prove that a delivered asset matches the valuation while hiding everything else. Our extensive experiments across three known datasets and various tasks with state-of-the-art encoders, including Whisper, reveal that we speed up the best benchmarks by up to 20x while reducing their proof sizes by up to 39x. We also systematically study how a speaker's value shifts across tasks and encoders, revealing agent-level market prices.

---


### 3. [Multimodal Ambivalence and Hesitancy Recognition with Bidirectional Audio--Text Cross-Attention](https://arxiv.org/abs/2610.26868)

**<font color=#1a73e8>作者：</font>** TingTing Gu, JinCheng Luo, WenQiu Guo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ambivalence and hesitancy (A/H) are subtle behavioural states that can be expressed through both what a person says and how it is spoken. This paper presents an audio--text framework for video-level A/H recognition. Full-video transcripts and speech waveforms are encoded using pre-trained multilingual BERT and wav2vec~2.0, respectively, and projected into a shared representation space. Two stacked bidirectional cross-attention blocks allow linguistic tokens to attend to acoustic frames and acoustic frames to attend to linguistic context without requiring explicit temporal alignment. The resulting sequences are aggregated through masked mean pooling and combined using concatenation, element-wise products, and absolute differences for binary classification. We evaluate the model on the subject-independent split of the Behavioural Ambivalence/Hesitancy (BAH) dataset. The proposed system achieves 72.19\% accuracy, 75.00\% precision, 81.13\% recall, 77.95\% A/H F1-score, and 70.16\% Macro-F1 on the test set. These results demonstrate the potential of jointly modelling linguistic and acoustic information for automatic A/H this http URL at:this https URL.

---


### 4. [EGGHead: Efficient Generalizable Gaussian Heads from a Single Image](https://arxiv.org/abs/2610.26898)

**<font color=#1a73e8>作者：</font>** Pilseo Park, Andrew Hou, Michel Sarkis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Creating photorealistic human heads typically involves trade-offs between representation power, efficiency, and generalizability. Traditional mesh-based solutions relying on 3DMMs generally sacrifice representation power but are efficient to render. On the other hand, NeRF-based methods improve representation power and fidelity while sacrificing efficiency. Gaussian splatting methods attempt to resolve these trade-offs by offering both high representation power and efficiency with real-time rendering. However, their efficiency nonetheless depends on the number of rasterized Gaussians, and the time needed to optimize and prepare the head (the enrollment time) is often high. In light of this, we propose EGGHead, which introduces a novel Gaussian allocation algorithm that efficiently assigns Gaussians to the head's semantic regions given a fixed Gaussian budget. Our algorithm reduces the number of Gaussians needed while minimizing the impact on representation power. EGGHead operates in a single forward pass and outperforms previous single-image face modeling methods in reconstruction quality, novel view synthesis, and rendering speeds.

---


### 5. [Beckmann World Models: Direct Terminal-Map Learning for One-Step Action-Conditioned Prediction](https://arxiv.org/abs/2610.26903)

**<font color=#1a73e8>作者：</font>** Adam Lee, Shobhit Agarwal, June Pyo Suh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action-conditioned world models support planning and policy evaluation by predicting future states. However, learning an accurate one-step predictor can require substantial training computation. We introduce Beckmann World Models (BWM), which learn a direct map from noise, visual history, and actions to future frames without a pretrained generative teacher. We adapt the terminal-map conservation law of Beckmann Transport Models to action-conditioned video prediction, training directly from noise-data pairs without conditional populations of generated samples required by DriftWorld. However, transport consistency on interpolated inputs does not ensure accurate prediction from the pure noise used at inference. We address this gap with endpoint-aligned training that directly supervises the source prediction, emphasizes motion and spatial structure, and teaches recovery from generated histories. All components train the same map and retain one network call per future chunk. On PushT and Robomimic Can, the final model reduces 64-frame prediction MSE by 68% and 57%, respectively, relative to same-backbone regression baseline. For policy evaluation, BWM achieves the lowest mean IoU error among the evaluated models, 0.0100, at 24.8 ms per four-frame PushT prediction. On Robomimic Can, the BWM stage trained with motion supervision and generated histories achieves 3.3 times higher throughput and 78% lower peak memory than local one-step DriftWorld. In a latent-space extension to RT-1 and Bridge-V2, equal-update controls show that feature supervision under generated histories improves perceptual prediction. These findings show how terminal-map learning can combine efficient training with accurate one-step visual prediction.

---


### 6. [InterType: Breaking the Single-Function Barrier in Neural Binary Type Inference](https://arxiv.org/abs/2610.26906)

**<font color=#1a73e8>作者：</font>** Shan Wang, Tianming Cui, Stephen McCamant 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Variable type recovery is a critical task in binary reverse engineering, enabling downstream applications such as vulnerability discovery, malware analysis, and security enforcement. While recent Transformer-based models have demonstrated strong performance in type inference by learning instruction-level semantics, they predominantly operate within single-function boundaries (i.e. intra-procedural analysis), ignoring the rich type constraints that propagate across function calls. Empirical studies have shown that nearly 44% of variables in real-world binaries propagate across function boundaries as arguments or return values, representing a significant source of type information that intra-procedural models cannot exploit. In this paper, we propose InterType, a method that embeds inter-procedural analysis into a pre-trained Transformer model for binary type recovery. Our approach builds on CodeArt, a state-of-the-art Transformer model for stripped binary analysis, and extends it by incorporating caller-callee data flow dependencies during fine-tuning. Specifically, we extract data flow dependence for each caller-callee pair from disassembled binaries and construct training instances that provide the model with cross-function context. By exposing the Transformer to inter-procedural variable propagation patterns, our model learns to resolve types that depend on cross-function data flow. We evaluate InterType on the coreutils benchmark compiled with optimization levels O0 through O3. On O1 binaries, InterType improves recall by 2.76 percentage points, from 89.00% for the intra-procedural CodeArt baseline to 91.76%, corresponding to a 25.1% reduction in recall error rate (1 - recall).

---


### 7. [Steerable Pluralistic Policy Alignment from Anonymized Crowd Feedback](https://arxiv.org/abs/2610.26914)

**<font color=#1a73e8>作者：</font>** Akansha Kalra, Ellen R. Novoseller, Vernon J. Lawhern 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pluralistic alignment requires AI systems to learn from diverse populations whose preferences may reflect heterogeneous or even conflicting objectives, and to personalize their behavior to individual users. Existing approaches in pluralistic alignment often assume access to annotator identities and rely on powerful pretrained representations to model individual preference variations. We propose Preference-PCA Pluralistic Learning (P3L), a novel framework for pluralistic alignment that jointly learns trajectory embeddings and the shared basis of preference directions via PCA decomposition from heterogeneous crowd feedback without requiring annotator identities. At test time, our approach enables rapid and accurate personalized reward learning and downstream policy optimization. Experiments across multiple embodied control tasks demonstrate that P3L enables steerable personal alignment that generalizes beyond the offline dataset to out-of-distribution new users and attains competitive RL and test performance, while substantially reducing computational cost and supporting variable adaptation query budgets.

---


### 8. [CodecMotion-OAD: Efficient Online Action Detection with Compressed-Domain Motion](https://arxiv.org/abs/2610.26915)

**<font color=#1a73e8>作者：</font>** Zepeng Sun, Naichuan Zheng, Hailun Xia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online action detection (OAD) identifies ongoing actions in streaming videos. Many existing OAD systems combine RGB appearance with optical flow, but dense-flow extraction remains a major computational bottleneck. Codec motion vectors (MVs) are available during decoding, avoiding a separate optical-flow computation. On THUMOS'14, optical flow exceeds MVs by 11.2 mAP points with motion-only inputs, whereas the gap narrows to 3.7 points after RGB fusion, with the largest reduction in action-category discrimination. We propose CodecMotion-OAD, which replaces optical flow with decoder-provided MVs while retaining existing temporal detector architectures. Its two-stage training first aligns MV features with a pretrained flow-feature interface without action labels and then trains RGB+MV detectors using ground-truth labels and soft predictions from a frozen RGB+Flow teacher. To the best of our knowledge, this is the first application of codec MVs to frame-level OAD. On THUMOS'14 with MiniROAD, CodecMotion-OAD achieves 68.3 mAP versus 70.9 mAP for matched-distillation RGB+Flow, while reducing decoder-to-prediction processing time by 11.48-fold on CPU and 2.04-fold on GPU.

---


### 9. [GTSM: Gaussian Splatting with Thermal State-Space Dynamics for Spatio-Temporal Thermal Field Reconstruction and Prediction](https://arxiv.org/abs/2610.26918)

**<font color=#1a73e8>作者：</font>** Yunpeng Zhao, Haoxiang Zhang, Chao Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temperature-field reconstruction and prediction are important for condition monitoring, process analysis, and state assessment in industrial and dynamic environments. This work aims to recover a four-dimensional spatio-temporal thermal state field directly from two-dimensional observations, without requiring a predefined 3D model, prescribed thermodynamic equation, or predefined heating/cooling trajectory. To this end, we propose the Gaussian Thermal State-Space Model (GTSM), which represents thermal evolution through a shared scene-level latent process and Gaussian-specific local thermal states. The resulting continuous dynamics are propagated using differentiable RK2 integration, allowing thermal evolution to be inferred from multi-view and multi-temporal observations and continuously extrapolated beyond the observed interval. GTSM is designed as a backbone-agnostic thermal dynamics module for Gaussian representations and can be integrated with both static 3D Gaussian Splatting and dynamic 4D Gaussian Splatting, supporting thermal reconstruction and prediction under both static and time-varying target geometry. The reconstructed representation further enables novel-view thermal rendering and future-time thermal-state prediction. Experiments on real infrared sequences and synthetic dynamic thermal data demonstrate improved reconstruction accuracy and substantially stronger temporal extrapolation than representative baselines, while also validating the applicability of GTSM to deforming targets.

---


### 10. [Controllable Multi-Object Insertion for Detection Data Augmentation](https://arxiv.org/abs/2610.26922)

**<font color=#1a73e8>作者：</font>** Jiyang Huang, Tianwei Zhang, Xiaoqin Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable object insertion provides a targeted approach to augmenting object detection datasets that require category--count fidelity, annotation alignment, and source-content preservation beyond visual realism. Several approaches have been proposed to address this grand challenge, but most suffer from different constraints in precise category--count requests and visual consistency, limited coordination across categories and instances, and poor localization of multiple objects of specific category and count. We design SceneP2F, a two-stage trainable framework that connects scene-aware joint planning with layout-aligned generation leveraging explicit instance-level layouts. SceneP2F consists of two novel designs. The first is ScenePlan which allocates one class-labeled query per requested instance, jointly predicts scene-compatible object centers, and separately estimates box sizes conditioned on the planned centers and scene context. The second is SceneAlign-Fill which combines geometry- and appearance-aware conditioning, box--class-guided regional attention, and an annotation-region-weighted flow-matching objective to render the planned objects while limiting unintended changes to source content. Extensive experiments on three challenging benchmarks UAVDT, VisDrone, and BDD100K show that SceneP2F outperforms representative general-purpose editors and object-insertion methods consistently, demonstrating the value of coordinating instance-level planning and generation for category-targeted detection augmentation.

---


### 11. [CaMeWM: A Causal Medical World Model for Generative Tumor Evolution and Treatment Planning](https://arxiv.org/abs/2610.26923)

**<font color=#1a73e8>作者：</font>** Huanlong Gao, Xuelei He, Fengjun Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Treatment planning is intrinsically counterfactual: clinicians must compare how a patient's tumor and survival would evolve under competing regimens, whereas a retrospective cohort records only the regimen received and one follow-up scan. A treatment-conditioned generator trained on such data can therefore reproduce historical treatment allocation rather than simulate the interventional disease dynamics needed to rank regimens. We introduce \textbf{CaMeWM}, a causal medical world model for supported post-TACE tumor evolution and treatment planning. CaMeWM implements one intervention-to-decision loop rather than three independent prediction tasks: it first admits a queried regimen only for clinically comparable histories with empirical treatment support; it then generates a distribution of lesion-local follow-up worlds through an action-conditioned response descriptor, deterministic anchor, and residual 3D diffusion transition; and it finally maps sampled worlds to restricted mean survival time (RMST) with a response-Cox utility model. Under pre-treatment adjustment and positivity, this loop estimates a prespecified, support-restricted g-formula target; all selection and nuisance estimation are fold-local, and the induced policy is evaluated by cross-fitted, censoring-adjusted doubly robust estimation. Across 79 paired out-of-fold episodes, CaMeWM achieves 0.618 SSIM and 0.528 change-map SSIM for follow-up CT transition, while its generated-world survival pathway attains a 0.615 C-index; factual-only AIPW estimates a 9.60-week RMST gain (95\% CI 0.61--18.13) for the frozen policy. CaMeWM provides an inspectable basis for retrospective, support-restricted treatment planning.

---


### 12. [DataPraxis: Scaling Analytics Tasks via Verified Workspace Evolution](https://arxiv.org/abs/2610.26924)

**<font color=#1a73e8>作者：</font>** Nan Jia, Wenxuan Shi, Jingqing Ruan 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> General-purpose agents are increasingly expected to perform professional analytics work, which requires sustained reasoning, iterative investigation, and reliable evidence. Training these capabilities requires diverse and challenging tasks. However, generating tasks directly from raw data often overlooks deeper questions that emerge through analysis and provides limited evidence for verification. To address these limitations, we introduce DataPraxis, an analytics task synthesis framework based on verified workspace evolution. The framework progressively enriches workspaces with validated findings and artifacts, then inherits and combines these workspaces to uncover deeper questions. It constructs tasks from accumulated findings and their dependencies, verifying analytical results both during evolution and after task assembly. Using this framework, we construct DataPraxis-5K, a dataset of 5,000 verified trajectories spanning diverse domains and output formats, to train DataPraxis-27B and DataPraxis-35B-A3B. DataPraxis-27B achieves 55.11 on DABStep and 51.9 on JobBench, matching or surpassing frontier models such as GLM-5.2. DataPraxis-5K is available at this http URL

---


### 13. [SuperClip Pyramid for Video Temporal Grounding](https://arxiv.org/abs/2610.26925)

**<font color=#1a73e8>作者：</font>** Sanghyeok Lee, Juyeon Ko, Joonmyung Choi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid expansion of online video content, video temporal grounding has become essential for localizing moments based on user-specific queries, comprising two subtasks: moment retrieval (MR) and highlight detection (HD). While recent approaches adopt DETR-style decoders or temporal pyramid architectures, they rely on single-scale feature maps or uniformly downsampled representations, limiting their ability to capture semantic boundaries and variable-length events. In this paper, we present SuperClip Video Temporal Grounding (SCVTG) built on a multi-scale temporal hierarchy that better captures distinctive events at various granularities. SCVTG constructs a SuperClip pyramid by grouping adjacent clips into semantically coherent segments, termed SuperClips. Further, to aggregate these SuperClips having variable duration and temporal location, we introduce a temporally adaptive kernel that aggregates SuperClips through temporally conditioned weights, enabling flexible aggregation. On top of this, we design relative saliency losses to guide the model in learning inter-clip importance, enhancing its ability to distinguish relevant events. Extensive experiments show that SCVTG achieves the best performance across five video temporal grounding benchmarks with promising gains.

---


### 14. [Rate as a Feature, Not a Nuisance: Curriculum FiLM Training for Event-Based Graph Neural Networks](https://arxiv.org/abs/2610.26933)

**<font color=#1a73e8>作者：</font>** Kavyansh Tyagi, Andreas Ziegler  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An event camera emits events at a rate given by the scene motion, object texture, illumination, its own contrast thresholds, and other settings. Across the N-Caltech101 dataset, recorded by a single event camera, the event rate varies by roughly 26x. Standard event-based Graph Neural Network GNN pipelines do not make use of the variable event rate. They either normalize each event's timestamp into a fixed window or train the network to be invariant to the event rate. We argue that both choices lose information that could instead be used to improve the performance of a pipeline. Per-recording normalization is non-invertible, incurring about 6pp (percentage points) of natural-rate accuracy loss in our setting. And invariance training trades accuracy for robustness to shifts in the event rate. We instead take a different path and condition on the event rate directly. We add a per-recording log-rate scalar that modulates every stage of a PointNet++ backbone through Feature-wise Linear Modulation (FiLM), initialized to identity, so that training begins at the unmodified baseline. A two-stage curriculum (natural event rates first, then rate-augmented fine-tuning) reaches 67.2% on N-Caltech101 (+6.3pp) and 82.5% on DVS128 Gesture (+14.0pp) with an additional ~0.2M parameters. A matched-capacity control experiment shows that the gain is not from the increase in model capacity but from the rate conditioning. We will make the implementation publicly available upon acceptance of this work.

---


### 15. [A Multi-granularity Interaction Network for Relational Triple Extraction](https://arxiv.org/abs/2610.26952)

**<font color=#1a73e8>作者：</font>** Xiaocheng Luo, Yanping Chen, Zaifu Zhan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Relational triple extraction identifies entity relations from raw sentences without depending on entity type information. The performance of traditional methods is seriously degenerated by ``unseen'' entities, because these methods can't build contextual dependencies relevant ``unseen'' entities. This paper addresses this challenge by proposing a multi-granularity interaction network that leverages word-word, entity-relation, and head-tail interactions to capture deep semantic dependencies. By incorporating multiple iterations, the multi-granularity interaction network is effective to refine the representations corresponding to head and tail entities. It enhances the global semantic features associated with relational triples, aiding in the remediation of triples that may have been overlooked or omitted in earlier steps. Strong and consistent performance is achieved by our method on two rearranged datasets, with a significant improvement in identifying relational triples, including those involving ``unseen'' named entities. For example, our model improves F1-score by 3.1%/20.5% over previous approaches on the NYT-R/WebNLG-R datasets in the Unseen metric. Code: this https URL.

---


### 16. [Deep Auxiliary Learning via Bilevel Feature Optimization for Label-Efficient Medical Image Segmentation](https://arxiv.org/abs/2610.26954)

**<font color=#1a73e8>作者：</font>** Fuping Wu, Xi Jia, Le Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Auxiliary learning (AL), which can improve the performance of a primary task by leveraging related auxiliary tasks, is commonly regarded as a special case of multi-task learning. Existing AL approaches typically require manually annotated auxiliary labels, increasing annotation costs, particularly in medical imaging where expert labeling is expensive. In this work, we investigate whether segmentation performance can be improved using auxiliary tasks whose labels are automatically derived from existing segmentation annotations, requiring no additional manual labeling. To address this, we propose a novel auxiliary learning framework, formulated as a bilevel optimization problem. Our method enables effective knowledge transfer between tasks via a feature communication module, enhancing the primary segmentation task. We evaluate the method on three medical image segmentation benchmarks under limited-label settings. The results demonstrate consistent improvements over state-of-the-art methods, achieving superior label efficiency. The code is publicly available at this https URL.

---


### 17. [SZED at ArGuard Shared Tasks: Multi-Task Label-Attention and Cross-Modal Fusion for Arabic Hateful Meme Detection](https://arxiv.org/abs/2610.26972)

**<font color=#1a73e8>作者：</font>** Selma Khelili, Zohra Abdeli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present SZED's submission to ArGuard 2026 Track A: Arabic hateful meme detection. The task has two parts: binary classification (A1) and fine-grained multi-label tagging (A2). For A1, we fuse MARBERTv2 and CLIP ViT-L/14 embeddings, comparing concatenation, self-attention, and ensemble heads. For A2, we use a multi-task label-attention architecture with per-class query vectors and an auxiliary head for cascade calibration. We reach macro-F1 = 0.7597 on A1 and 0.3142 on A2 (averaged over 10 active classes). We report reproducibility across runs, per-class error patterns, and the effect of cascade calibration on the long-tailed A2 label space.

---


### 18. [Transformers Learn Two Competing Sorting Algorithms, and Only One Length-Generalizes](https://arxiv.org/abs/2610.26974)

**<font color=#1a73e8>作者：</font>** Khashayar Gatmiry, Nathan W. Henry, Chloe H. Su 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that two-layer transformers trained to near-zero loss on a sorting task converge to one of two mechanistically distinct solution classes depending on their initialization. One solution class consists of solutions that do not use the second attention layer to sort, but also fail to length-generalize. The other, which uses both attention layers, length-generalizes perfectly, despite only being trained to sort sequences of a fixed length. By carefully choosing the weight initialization, we demonstrate that we can steer the model toward learning one solution or the other. We identify input types that are rare at the training length but increasingly common at longer sequence lengths as a source of this disparity in length-generalization, and find that layer-wise specialization of the second class of solutions allows them to handle these rare sequences more accurately. In the second class, we discover a mechanism by which the second layer attention can use the contextual information gathered by the first layer attention to reduce its search space. On the related task of finding the minimum of a sequence, we find a similar two solution-type phenomenon, but with the opposite generalization pattern, where a different form of layer-wise specialization causes the two-layer solution to length-generalize worse than the single-attention solution.

---


### 19. [Sharp Degree Bounds for Putinar Certificates in Terms of the Positivity Margin via Analytic Sums of Squares](https://arxiv.org/abs/2610.26976)

**<font color=#1a73e8>作者：</font>** Yuxiang Zhao, Ting Gan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We establish sharp degree bounds for Putinar sum-of-squares (SOS) certificates in terms of the positivity margin $\delta$. For any fixed Archimedean quadratic module with prescribed generators and any fixed bound on the degree of the objective, we prove a uniform certificate-degree upper bound of $O(\delta^{-1/2}\log^2(2/\delta))$ for normalized polynomial objectives. We show that this bound is sharp by constructing a matching lower-bound example in three variables, thereby establishing that the dependence on $\delta$ is optimal. These matching bounds also yield sharp worst-case convergence rates for the Lasserre hierarchy.

---


### 20. [Latent Projection for Latent Planning](https://arxiv.org/abs/2610.26979)

**<font color=#1a73e8>作者：</font>** Yoo Sung Jang, Michael Ryoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models let an agent plan in latent space. The planner searches for an action sequence that minimizes a cost, and that cost is often the $\ell_2$ distance between the predicted terminal latent and the goal latent. The latent, however, is partly noise: the regularizer that prevents collapse during world model training promotes variance in the directions carrying no signal. We show that the same regularizer also supplies the structure to prune that noise in the latent. SIGReg drives the latent marginal to a standard Gaussian at every step, and assuming further that the latent sequence is a Gauss-Markov process, the transition is linear with its covariance pinned by the map itself, $z' \mid z \sim \mathcal{N}(Az,\, I - AA^\top)$. Fitting the state dynamics $A$ therefore yields the covariance at no additional cost, and in its eigenbasis each latent direction carries its own uncertainty. Furthermore, constraining $A$ to be a normal matrix fixes that basis across timesteps, so one eigenbasis measures the uncertainty over an arbitrary number of steps and serves as a stable basis to compute the planning cost on. We then restrict the $\ell_2$ cost to the $k$-dimensional subspace the state dynamics carry forward with the least uncertainty. The correction is post hoc: the encoder, the predictor, the rollout, and the planner are all left untouched, and only a single constrained matrix, $A$, is fit. We evaluate across six environments and show large gains on the 2D navigation tasks, TwoRoom and PointMaze, raising success rate over the plain $\ell_2$ cost by up to $+54.7$ points under a harder planning setting. Code is available at this https URL.

---


### 21. [Think Before You Transcribe: Context-Steered Reasoning for Hotword-Aware Speech Recognition](https://arxiv.org/abs/2610.26986)

**<font color=#1a73e8>作者：</font>** Qihao Wang, Hang Su, Fan Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contextual automatic speech recognition (ASR) improves rare-entity recognition by supplying candidate hotwords, but retrieved candidates may be incomplete or incorrect. A reliable system must therefore exploit a relevant candidate without allowing unsupported alternatives to override the acoustic evidence. We propose a context-steered reasoning framework that generates a short, audio-grounded caption before transcription. This task-specific representation lets the model assess candidate relevance before making a lexical decision. Supervised fine-tuning establishes the structured caption-to-transcription behavior, while targeted trajectory injection strengthens group relative policy optimization when difficult utterances yield only unsuccessful rollouts. Experiments across diverse context conditions show that the proposed method consistently improves both transcription quality and hotword recognition while remaining robust to irrelevant candidates.

---


### 22. [REST: Reliability-Guided Spatial Transcriptomics Supervision for Gene Expression Prediction from Histopathological HE-Stained Images](https://arxiv.org/abs/2610.26988)

**<font color=#1a73e8>作者：</font>** Lanfeng Zhong, Xiangyu Sun, Guixuan Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Histopathology is central to cancer diagnosis, but morphology in Hematoxylin and Eosin (HE)-stained images does not directly reveal the molecular states that characterize disease heterogeneity and inform tumor characterization, prognostic assessment, and biomarker discovery. Spatial Transcriptomics (ST) measures spatially resolved gene expression, providing molecular information within tissue architecture, yet differences in assay coverage and spot informativeness make paired HE--ST observations unequally reliable for representation learning. We propose Reliability-Guided Spatial Transcriptomics (REST) supervision with Biological Program Bank (BPB), a program-structured and reliability-guided ST-supervised training framework for predicting molecular information from H\&E images. REST constructs BPB from curated signature, pathway, and cell-type gene sets to provide a shared structure for ST encoding, reliability estimation, and molecular reconstruction. Guided by BPB, Spot-Reliability Contrastive Alignment (SRCA) measures the reliability of each spot from assay-level program coverage and spot-level activity dispersion, and reweights HE--ST alignment accordingly. Biology-Informed Program Reconstruction (BIPR) further uses learnable program queries to reconstruct member-gene expression from histological morphology. REST's training corpus comprised 209 samples (407,475 spots across 16 organs); evaluation used 70 disjoint samples (230,056 spots across eight organs) for gene-expression, pathway-activity, and cell-signature prediction. REST achieved the highest Macro correlation among state-of-the-art ST-supervised training methods and outperformed existing pathology foundation models. Code is available at this https URL.

---


### 23. [CoASFL: Coupled Consistency Optimization for Asynchronous Split Federated Learning](https://arxiv.org/abs/2610.26992)

**<font color=#1a73e8>作者：</font>** Junhao Cheng, Yunming Liao, Hongli Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Split Federated Learning (SFL) has emerged as a promising paradigm for training large-scale deep models on resource-constrained edge devices. Although asynchronous SFL alleviates the straggler bottleneck caused by system heterogeneity, it inevitably introduces two coupled dimensions of inconsistency: horizontal inconsistency across clients and vertical inconsistency between clients and the server. These inconsistencies, further exacerbated by statistical heterogeneity, result in biased activation representations, model divergence, and severe client drift. To address these challenges, we propose CoASFL, an inconsistency-aware asynchronous SFL framework that incorporates a dynamic activation merging mechanism and a consistency-aware model aggregation mechanism. Specifically, CoASFL constructs more consistent activation sequences from heterogeneous clients to alleviate horizontal inconsistency, and dynamically adjusts aggregation weights according to client participation frequencies and progress gaps to mitigate vertical inconsistency. By jointly coordinating activation-level and model-level consistency, CoASFL effectively suppresses inconsistency propagation during asynchronous training. Extensive experiments on an 80-device heterogeneous edge testbed demonstrate that CoASFL consistently outperforms state-of-the-art SFL approaches, accelerating training by 1.61$\times$ to 3.74$\times$ and improving final model accuracy by up to 3.26\% under heterogeneous scenarios.

---


### 24. [TRACE: Training-aware Robustness and Challenge Evaluation for Text-Vision Embedding Models](https://arxiv.org/abs/2610.26993)

**<font color=#1a73e8>作者：</font>** Pume Tuchinda, Tinnakit Udsa, Peerat Limkonchotiwat  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing benchmarks for text-vision embedding models report aggregate scores that obscure whether performance comes from general capabilities, task-specific adaptation, or robustness to challenging tasks. We introduce TRACE, a Training-aware Robustness and Challenge Evaluation framework that reorganizes 168 tasks from various sources of datasets into three categories: General, Adaptability, and Challenge. Through controlled experiments on two text-vision embedding models, we show that combining general and adaptation data improves Adaptability performance by 7.67 and 7.09 points, respectively, while largely preserving General performance. However, Challenge performance remains below 5.0, with limited improvements from additional training data. Further analysis identifies multilingual and visual-document tasks as major weaknesses. Our findings demonstrate that data adaptation alone is insufficient to address these challenges, highlighting the need for methodological advances beyond data-centric improvements.

---


### 25. [How to get the best and fairest performance out of your ASR system using activation steering](https://arxiv.org/abs/2610.26994)

**<font color=#1a73e8>作者：</font>** Felix Herron, Alex Colagrande, Solange Rossato 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering for ASR systems is an underexplored technique in improving both ASR performance and demographic fairness. We investigate two forms of activation steering: paired activation subtraction, and supervised optimization. We find the former to be ineffective at ameliorating ASR performance whatsoever, while the latter is quite effective at deriving steering vectors (SVs) that improve at once overall ASR performance and demographic fairness along such diverse axes as gender, age, and dialect. We also explore what types of data---from the most to the least personal---are necessary for calculating or training SVs. First, we show significant performance in performance from training SVs using an eclectic group of speakers from the same dataset. Furthermore, we find that vectors trained using acoustically similar speakers leads to ASR performances that are competitive or superior to vectors trained on the same speaker, or speakers from the same labeled demographic group. This finding shows that we can harness activation steering for few-shot adaptation given access to a speaker's demography, or zero-shot adaptation to unseen speakers without the need for any labels at all.

---


### 26. [CorteXforge: Scenario-Based RF Dataset Generation on Real Testbeds](https://arxiv.org/abs/2610.26999)

**<font color=#1a73e8>作者：</font>** Andréa Joly, Leonardo S Cardoso, Jean-Marie Gorce  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning for radio frequency (RF) signal analysis relies on large annotated datasets, yet synthetic datasets trade physical realism for controllability, while uncontrolled over-theair measurements offer realism but limited reproducibility. We present CorteXforge, a scenario-based framework for generating realistic and reproducible RF datasets on programmable software defined radio (SDR) testbeds. High-level RF scenarios are automatically translated into synchronized experiments executed on the SLICES-RI/CorteXlab platform, producing fully annotated Signal Metadata Format (SIGMF) datasets that capture hardware impairments and propagation effects. We validate CorteXforge through automatic modulation classification using ModForge, an over-the-air (OTA) dataset generated with the framework. Cross-domain experiments reveal a synthetic-to-real performance gap and show that synthetic pretraining remains beneficial for adaptation to OTA data. CorteXforge provides a practical foundation for reproducible RF dataset generation and future research on domain generalization.

---


### 27. [ORBIT: Autoregressive Time Series Generation via Next Frequency-Band Prediction](https://arxiv.org/abs/2610.27000)

**<font color=#1a73e8>作者：</font>** Chunyi Hou, Xiangfei Qiu, Hanyin Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep generative models provide an effective modern solution to alleviating the problem of data scarcity by synthesizing realistic time series. However, despite the considerable progress achieved by existing deep time series generators, two key challenges remain: (1) learning hierarchical representations for heterogeneous temporal patterns; and (2) coordinating the generation process of heterogeneous temporal dynamics. To address these key bottlenecks, in this work, we propose ORBIT, a unified deep generative framework for time series. Specifically, we develop two key components: the Frequency-Hierarchical VQ-VAE (FH-VQ-VAE) and the Frequency-Band Autoregressive Transformer (FBAR). The former learns hierarchical representations by decomposing latent temporal representations into different frequency bands and applying residual quantization with increasing token budgets. The latter establishes a novel low-to-high frequency autoregressive direction, yielding a time series generation process that first constructs global temporal structures and then incrementally incorporates fine-grained temporal details. These compact designs not only disentangle heterogeneous temporal patterns for more effective representation learning but also mitigate potential interference among different temporal dynamics during generation. Extensive experiments on multiple challenging real-world benchmarks demonstrate that ORBIT achieves state-of-the-art overall performance while exhibiting superior inference efficiency compared with advanced baselines.

---


### 28. [HierDTA: Hierarchical Structure-Aware Representation Learning for Drug--Target Affinity Prediction](https://arxiv.org/abs/2610.27001)

**<font color=#1a73e8>作者：</font>** Huangchao Xu, Baohua Zhang, Qian Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drug--target affinity (DTA) prediction plays an important role in computer-aided drug discovery, where reliable computational models can help prioritize compound--protein pairs before experimental validation. A key challenge in DTA prediction is to effectively mine multi-level molecular information from drug structures while accurately modeling the binding-site environment of target proteins. To address these issues, we introduce HierDTA, a hierarchical structure-aware framework for DTA prediction. \textcolor{black}{HierDTA represents each drug as an atom--motif heterogeneous graph and introduces an augmentation module that propagates functional-motif semantics to the corresponding atoms. For proteins, kinase-domain structures are converted into residue interaction graphs. The resulting atom and residue representations are integrated using cross-attention to capture pair-specific relationships, while molecule fingerprints and pretrained ESM-2 embeddings provide complementary global information. Compared with state-of-the-art methods, HierDTA achieves superior performance on the Davis dataset across all metrics and attains the highest \(r_m^2\) of 0.791 on KIBA. It also exhibits strong generalization under cold-start settings, particularly on KIBA, where MSE is reduced by 21.7\% in the unseen-protein scenario. Ablation study and interpretability analysis supported the contributions of the hierarchical augmentation and interaction components.} Case studies further showed that HierDTA provided early enrichment of candidate bioactive compounds. These results indicate that HierDTA is an effective framework for affinity prediction and target-specific virtual screening.

---


### 29. [Decomposed Relation Extraction from Aviation Accident Narratives: Evaluating Transformer-Based Safety Knowledge Discovery under Relational Sparsity](https://arxiv.org/abs/2610.27013)

**<font color=#1a73e8>作者：</font>** Aziida Nanyonga, Mustafa Tahsin Yilmaz, Saad Ezzini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Relation extraction from aviation accident narratives is challenging because genuine safety relations are sparse among possible concept pairs. This study evaluates a decomposed framework separating relation classification from concept identification. A benchmark of 300 National Transportation Safety Board (NTSB) narratives containing 2,524 unique concept-text nodes was expanded into 21,038 ordered candidate pairs, with only 248 (1.18%) representing RESULTS_IN or CONTRIBUTES_TO relations. A TF-IDF Linear Support Vector Machine (SVM) and weighted RoBERTa classifier were developed using an independent graph-annotated resource with hard-negative sampling and frozen before sealed evaluation. Development Macro-F1 scores of 0.4738 (SVM) and 0.4809 (RoBERTa) declined to 0.2741 and 0.2420 under exhaustive evaluation, with Matthews correlation coefficients of 0.0128 and 0.0197. False positives dominated: the SVM recovered 96 reference relations but generated 7,018 false positives, while RoBERTa recovered 125 but generated 9,824. Post-test diagnostics revealed overlapping RoBERTa confidence distributions and false positives even within valid relation-category directions. Complementary end-to-end SmolLM2 evaluation identified missed and unsupported relations alongside malformed outputs. These findings demonstrate that known concept endpoints do not guarantee reliable relation extraction and that sampled-negative development performance may poorly reflect exhaustive evaluation. Controlling false positives and managing candidate-space sparsity remain essential for aviation safety knowledge extraction.

---


### 30. [Long-wave Infrared Polarimetric Remote Sensing Image Fusion for Vehicle Detection](https://arxiv.org/abs/2610.27018)

**<font color=#1a73e8>作者：</font>** Wenjuan Zhang, Xiangrui Peng, Zhen Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Blurred vehicle contours and low contrast limit detection performance in infrared remote sensing imagery, while existing fusion methods may introduce polarization noise and fail to integrate complementary information effectively. To address these limitations, we propose a Mamba-based infrared polarimetric remote sensing image fusion model. Infrared polarization information reflects surface material properties and geometry, providing complementary information to infrared intensity. The proposed method first combines long-wave infrared total intensity S0 and the degree of linear polarization (DoLP), using a physics-inspired polarization-response proxy and spatial structural continuity to extract guidance features. It then employs bidirectional state space scanning along horizontal, vertical, and both diagonal orientations to enable cross-modal feature fusion across the entire image. Prior-guided multi-window structural similarity, reconstruction constraints, and a relative lower-bound loss for polarization saliency are jointly introduced to suppress noise while preserving global background structures and target polarization features. In addition, we construct AIR-LWIR-Pol, a dataset of 1,901 accurately registered image pairs acquired using an airborne division-of-aperture long-wave infrared polarimetric imaging system, and evaluate downstream vehicle detection using YOLO11. The experimental results show that the proposed method outperforms the comparison methods on four fusion metrics, including entropy and structural similarity. Vehicle detection mAP50 and mAP50-95 reach 55.0% and 29.4%. These results demonstrate the effectiveness of combining physical priors with state space modeling for long-wave infrared polarization image fusion and support its use for target detection in complex remote sensing scenes.

---


### 31. [Reliable Estimation of Differential Privacy under Selection Bias](https://arxiv.org/abs/2610.27021)

**<font color=#1a73e8>作者：</font>** Valentin Dorseuil, Meenatchi Sundaram Muthu Selva Annamalai, Jamal Atif 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Statistical privacy audits are essential for verifying the theoretical privacy guarantees of differentially private (DP) mechanisms. Auditors typically use Membership Inference Attacks (MIAs) to estimate a lower bound on the true privacy leakage of DP mechanisms at a specified confidence level, which should not exceed the theoretical privacy upper bound guaranteed by DP. However, we found that many auditing implementations in prior work introduce a selection bias when running MIAs, which leads to statistically invalid and overestimated lower bounds. Because most audits are not tight, this bias has thus far gone unnoticed: the estimated lower bounds remained well below the theoretical upper bounds. Nevertheless, accurately evaluating this lower bound is critical, as a flawed statistical assessment could lead to false alarms on correct mechanisms or an incorrect evaluation of the guarantee's tightness. This work employs tools from the statistical literature to correct this bias. We present an overview of the different correction methods and assess their respective advantages. Furthermore, we perform a comprehensive re-analysis of results returned by prior audit implementations and show that without statistical correction, these audits violate the theoretical upper bounds up to four times more often than their claimed confidence level implies. With correction applied, the resulting lower bounds are statistically valid, and violations occur at no more than the nominal rate.

---


### 32. [EGiME: Entropy-Guided Model Evaluation in Few-Shot Learning](https://arxiv.org/abs/2610.27029)

**<font color=#1a73e8>作者：</font>** Dequan Jin, Tao Li, Lifeng Xing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The feature-extraction quality of pre-trained models sets the ceiling of downstream transfer learning, yet few-shot model selection remains difficult: supervised evaluation on scarce labels is unstable and yields fluctuating rankings. We propose Entropy-Guided Model Evaluation (EGiME), a semi-supervised criterion that assesses a candidate model from the clustering structure of its feature space without any classifier training. EGiME performs $K$-means clustering over all labeled and unlabeled samples, then combines two entropy terms: an inter-cluster entropy measuring global separability, and an intra-cluster entropy measuring the compactness of labeled anchors, fused through an inverse-frequency weight that emphasizes small clusters. On five few-shot benchmarks and nine pre-trained models, EGiME achieves a correlation score of 0.966 with the full-pool ground-truth accuracy obtained by averaging the accuracies of K-means, KNN, and SVM. At labeling ratios of 4\%--20\%, it produces markedly more stable model rankings than cross-validated supervised baselines, establishing it as a practical alternative to conventional supervised evaluation for pre-trained model selection under data scarcity.

---


### 33. [Hilbert-Scale Stability of Posterior Diffusion Priors for Ill-Posed Signal Recovery](https://arxiv.org/abs/2610.27030)

**<font color=#1a73e8>作者：</font>** Bahman Moraffah, Raha Moraffah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Indirect and noisy observations are difficult to invert when the forward operator smooths out the unknown signal. In this case, the unstable modes are precisely the modes that the data reveals least, thus the success of any reconstruction method depends on how prior information interacts with the geometry of the operator across regularity scales. Diffusion priors have become ubiquitous for such problems; however, the current theory still does not determine when a learned score remains informative under ill-posed forward operators. In this paper, we study posterior diffusion for linear inverse problems on Hilbert scales and derive a stability theory under an explicit score-amplification condition. Under a smoothing condition on the forward map, a source condition on the truth, and weak-norm control of score error, we derive non-asymptotic recovery bounds in \(\Hs^s\) that separate observation noise, score approximation, and reverse-time discretization. These bounds give a recoverable regularity threshold determined jointly by operator smoothing, truth regularity, score regularity, and the posterior correction. The threshold specifies the Hilbert-scale norms \(\Hs^s\) in which weak-norm score error remains controlled after propagation through the posterior reverse dynamics. For larger regularity indices \(s\), the inverse geometry magnifies the same error, and the Hilbert-scale recovery estimate no longer gives uniform stability. We also prove that a posterior correction adapted to the forward operator improves stability relative to isotropic guidance in the regularity ranges where the smoothing action of the forward map matters most. The recovery estimates give a regularity-sensitive theory of posterior diffusion and show how learned score error, operator smoothing, and reconstruction norm jointly determine the stable range predicted by the analysis.

---


### 34. [ECHO: Revealing Review-to-Submission Linkage in Anonymous Peer Review](https://arxiv.org/abs/2610.27044)

**<font color=#1a73e8>作者：</font>** Rong Wang, Mulong Luo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Anonymous peer review protects reviewers from retaliation, yet reviewer anonymity may also be weakened by artifacts released through the review process itself. This risk is growing as many venues require submitting authors to review, creating substantial overlap between authors and reviewers within the same review cycle. We identify review-to-submission linkage, where an anonymous review can be associated with the reviewer's own submission, substantially shrinking the reviewer anonymity set. To assess whether this linkage is practically exploitable, we develop ECHO, which combines technical-expertise and writing-style signals across reviews, papers, and rebuttals, and evaluate it on R2S-Bench, a ground-truth benchmark we construct. ECHO correctly identifies the reviewer's own submission in Top-1 for 34.6% of reviews, in the Top-5 for 54.0%, and in the Top-10 for 63.4%, compared with 0.5%, 2.6%, and 5.3% under random ranking, from the candidate submissions. With a stronger Stage-2 reranker, ECHO further reaches 56.4% Top-1 and 66.4% Top-10. These results demonstrate that review-to-submission linkage is feasible using only routinely released peer-review artifacts. Code and benchmark are available at this https URL.

---


### 35. [Physical AI: Concepts, Techniques, and Challenges](https://arxiv.org/abs/2610.27045)

**<font color=#1a73e8>作者：</font>** Weinan Zhang, Chunhua Shen, Tianfan Xue 等 52 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In recent years, physical artificial intelligence (physical AI) has experienced rapid development, capturing significant attention in academia and industry. However, the field has yet to reach consensus on its definition, technical landscape, and core challenges. To address this gap, this monograph seeks to define physical AI, present its technical landscape, and examine each key technical subfield in depth. In doing so, it establishes a unified framework for Physical AI: artificial systems that perceive, model, and act upon the physical world through continuous feedback under real-world constraints. Further, this monograph distinguishes physical AI from conventional digital AI, embodied AI, cyber-physical systems, and digital twins. It develops the foundations of physical AI across physics, control, cognition, learning, and reasoning. It reviews key methodologies, including multimodal perception, physical data and simulation, world models, embodied foundation models, motor-control systems, multi-agent coordination, and hardware-software co-design. Furthermore, it examines applications spanning robotics, manufacturing, infrastructure, scientific experimentation, and autonomous services. Particular attention is given to sim-to-real transfer, reliability, real-time execution, evaluation, safety, governance, and long-term deployment. By connecting perception, prediction, decision-making, action, and adaptation in a closed loop, this monograph identifies the technical challenges and research directions required to advance from narrow automation toward more generalizable physical AI and, ultimately, physical artificial general intelligence (Physical AGI).

---


### 36. [Discrete Neural Interlingua for Ontology-Agnostic EHR Modeling](https://arxiv.org/abs/2610.27047)

**<font color=#1a73e8>作者：</font>** Tong Ding, Caiwei Tian, Dongmin Bang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> EHR foundation models promise scalable clinical prediction across health systems, yet their deployment is constrained by a tokenization bottleneck. The same clinical concept can appear as different ontology codes, local identifiers, synonyms, or free-text descriptions, which standard EHR tokenizers treat as unrelated symbols. A model trained on MIMIC-III with a closed-vocabulary tokenizer can use only 13% of eICU events. We introduce MEDIATOR, a discrete ontology-agnostic tokenizer that maps any clinical concept expressed as text into a shared vector-quantized codebook, turning EHR harmonization into open-vocabulary tokenization without manual mappings or a fixed vocabulary. Trained with synonym supervision and guided by enriched concept descriptions, code co-occurrence, and relation graphs, MEDIATOR collapses equivalent expressions while organizing distinct concepts in a medically meaningful discrete space. Used as the token interface of an EHR Transformer, MEDIATOR improves mean AUPRC over the strongest prior tokenizer by 4.0 points (8% relative) on 20 MIMIC-III tasks and by 8.6 points (29% relative) in zero-shot transfer to 14 eICU tasks, where it uses all events. The transfer gain combines coverage and representation, as MEDIATOR remains the best tokenizer under identical inputs (+1.0 and +1.9 points on operational and subcohort-mortality tasks). Same-encoder controls show that the text encoder drives in-domain accuracy, while the learned objectives of MEDIATOR drive transfer robustness and entity-linking quality. MEDIATOR also enables transferable attribution across hospitals.

---


### 37. [VitronEdit: Universal Visual Editing across Images, Videos, and 3D Scenes](https://arxiv.org/abs/2610.27049)

**<font color=#1a73e8>作者：</font>** Jing Wang, Yanlin Li, Mong-Li Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in unified visual editing have begun to consolidate image and video editing within a single model, while 3D scene editing remains largely separate and constrained by scarce paired training data. Given the rich image and video editing supervision now available and the common editing semantics shared across modalities, a natural question is whether this knowledge can be transferred to data-scarce 3D editing. We present VitronEdit, a universal framework for image, video, and 3D scene editing. VitronEdit adopts a shared sequence representation and progressive multimodal training to transfer editing knowledge across modalities. We further introduce geometry-aware post-training, which leverages a pretrained geometry reconstruction model to provide depth and camera-pose supervision. Surprisingly, applying geometric supervision only to 3D samples yields the best overall performance, while image and video editing also improve despite receiving no direct geometric supervision, suggesting that geometric regularization transfers through the shared backbone. Our analysis further shows that image and video training mainly transfers editing semantics to 3D, whereas 3D supervision primarily improves multi-view consistency. The project page: this https URL.

---


### 38. [BUMP: Body-driven Unified Multi-object Physics for HOI Synthesis](https://arxiv.org/abs/2610.27066)

**<font color=#1a73e8>作者：</font>** Wonjung Woo, Hyeonwoo Kim, Hanbyul Joo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating human-object interactions (HOIs) with multiple objects is challenging because the resulting motions arise from different underlying causes. Human motion reflects semantic intent, intentionally manipulated objects must remain coordinated with the human, while surrounding objects move primarily as physical consequences of contact and collision. We present BUMP, a text-driven framework for multi-object HOI generation based on a simple principle: learn intentional motion and simulate physical consequences. Our method first generates full-body human motion from text and scene context, then predicts trajectories for a small number of intentionally manipulated driver objects conditioned on the human motion. We then obtain responder object motions through physics simulation, allowing the framework to handle varying numbers and configurations of surrounding objects without expanding the learned trajectory output space. To address the scarcity of paired full-body multi-object HOI data, we combine heterogeneous supervision from human-only motion, full-body HOI, and hand-centric manipulation data augmented with plausible body motion. We further introduce outcome-conditioned interaction editing, which infers a local modification of the causal driver object trajectory from a desired responder object behavior without requiring an explicit target driver object trajectory. Experiments demonstrate strong performance on both single-object and multi-object HOI benchmarks. Qualitative results showcase diverse scenarios involving inter-object relationships and edits, highlighting the advantage of our unified model formulation.

---


### 39. [LEAF: LUT-aware Efficient Attention on FPGAs](https://arxiv.org/abs/2610.27078)

**<font color=#1a73e8>作者：</font>** Arianna Cox, Chang Sun, Lauri Laatu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Lookup-table (LUT)-aware Efficient Attention on FPGAs (LEAF). LEAF is the first nanosecond-scale LUT-aware transformer for FPGAs. Deploying transformers that are large enough to perform well, small enough to fit on an FPGA, and fast enough to meet the sub-microsecond timescales required by real-time systems such as those at CERN remains difficult, since the same attention mechanism that gives these models their high expressivity also makes them costly to implement in hardware. LEAF converts the query, key, and value projections and the final output feed-forward layer into FPGA-native layers with LUT-aware training, creating the first LUT-aware transformer and linformer layers built for ultra-low-latency inference. Attention resists LUT-aware training because it multiplies two activations where the method needs a constant weight to tabulate; LEAF tabulates the attention block's constant matrix-vector multiplications and leaves the rest in arithmetic form. On a standard jet tagging benchmark this improves accuracy by 1.8 percentage points while using 2.9 times fewer LUTs than the previous state-of-the-art sub-microsecond transformer at the same input size. Our most efficient LEAF-based linformer with 64 input particles reaches 80.4% classification accuracy at 28k LUTs and 35ns.

---


### 40. [RGH-GNN : Risk-Gated Heterogeneous Graph Neural Network for Financial Fraud Detection](https://arxiv.org/abs/2610.27107)

**<font color=#1a73e8>作者：</font>** Mythreyee Hari, Subin Sahayam, Vegesna S M Srinivasavarma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Credit card fraud is a significant problem for financial institutions, resulting in substantial monetary loss each year. Fraud patterns and methods are continuously evolving, with fraudulent transactions often disguised to resemble legitimate activity. Real world transaction data for fraud detection is severely affected by class imbalance making it harder to detect these transactions. Fraudulent transactions are rarely isolated. Accounts, devices, and other common attributes are often shared across fraudulent activity, revealing relational patterns that individual transaction features alone cannot capture. Graph-based approaches model these relationships explicitly. However, standard graph neural networks aggregate neighbourhood information uniformly, which can dilute the already scarce signal carried by fraudulent transactions and limit detection of camouflaged fraud. This work presents RGH-GNN, a heterogeneous graph neural network that addresses this limitation by incorporating transaction-level risk scores, generated by a supervised LightGBM classifier as edge weights. It is used to guide message passing through a learnable risk-gated aggregation mechanism. It ensures that high-risk transactions contribute more strongly to learned representations rather than being diluted by uniform neighbourhood aggregation. RGH-GNN is evaluated on the IEEE-CIS fraud detection dataset against standard graph neural network models that are trained on the same heterogeneous graph. RGH-GNN outperforms all baselines across every evaluation metric, with an AUC-ROC score of 0.914. This demonstrates that incorporating engineered risk signals into graph-based message passing substantially improves fraud detection performance.

---


### 41. [Counting Contributions, Not Views: Occlusion-Aware Densification for 3D Gaussian Splatting](https://arxiv.org/abs/2610.27108)

**<font color=#1a73e8>作者：</font>** Marcel Rogge, René Schuster, Didier Stricker  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting grows a dense scene from a sparse initialization through adaptive density control (ADC), driven by per-Gaussian statistics gathered during rendering. These statistics pass a frustum-based visibility filter blind to occlusion: fully occluded Gaussians still count as observed, diluting the averaged gradient signal and suppressing densification precisely where geometry is occluded. We correct this with an occlusion-aware filter that restricts densification statistics to views in which a Gaussian actually contributes, and replace the criterion's raw view-count normalizer with an average-contribution one. Integrated into a StopThePop-based framework, the two together improve every image-quality metric over the occlusion-blind baseline on occlusion-heavy scenes (up to 6% lower LPIPS), at less than half the Gaussians a view-count normalizer requires. Under the longer schedules these large scenes require, the count stays bounded where most criteria diverge, and on smaller benchmarks our method stays competitive at a fraction of the competitors' count.

---


### 42. [MatchCityLoc: Aerial Localization in LoD City Models via Surface Normal Matching](https://arxiv.org/abs/2610.27110)

**<font color=#1a73e8>作者：</font>** Oussema Dhaouadi, Zuria Bauer, Johannes Michael Meier 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous Unmanned Aerial Vehicle (UAV) navigation in urban environments requires precise pose estimation. Because Global Navigation Satellite System (GNSS) signals are often unreliable in cities, visual localization serves as a crucial complement. Within this domain, textureless Level-of-Detail (LoD) city models provide a lightweight and privacy-preserving substitute for heavy 3D textured meshes. However, localizing against abstract geometry is challenging. Existing pipelines typically score 2D silhouette overlaps, which can suffer from severe geometric ambiguities. We present MatchCityLoc, a framework that shifts this paradigm to direct feature matching from a noisy 6-DoF pose prior. By extracting surface normals from the query image using a zero-shot foundation model and matching them against rendered LoD normals, we establish explicit 3D-to-2D correspondences. This enables a Perspective-n-Point (PnP) pose solve, which we iteratively refine through a render-and-match loop. Experiments demonstrate strong pose recall and accurate translation and rotation among the evaluated off-the-shelf LoD-based methods with very few renderings. By bridging the modality gap between aerial imagery and texture-free geometry, MatchCityLoc enables accurate localization using lightweight, privacy-preserving city models.

---


### 43. [Energy Consumption of Post-Quantum Cryptography on Constrained and General-Purpose Architectures](https://arxiv.org/abs/2610.27111)

**<font color=#1a73e8>作者：</font>** Olivier Gillot, William J. Buchanan, Madjid G. Tehrani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With Q-day approaching, the transition to post-quantum cryptography (PQC) has begun, with governments across the US, UK and EU mandating migration to quantum-resistant standards. This paper benchmarks the three NIST-standardised PQC algorithms - FIPS 203 (ML-KEM), FIPS 204 (ML-DSA) and FIPS 205 (SLH-DSA) - across key generation, signing and verification operations, measuring both computational performance and energy consumption on a range of constrained IoT-class devices, from the 32-bit Raspberry Pi 1 and Zero to the 64-bit Raspberry Pi 4, as well as commodity laptop hardware. Using the FNIRSI FNB58 USB power meter and OpenSSL~3.5, results show that ML-KEM and ML-DSA achieve energy and speed efficiency comparable to classical elliptic-curve cryptography across all tested architectures. However, SLH-DSA signing is inadvisable on constrained hardware: energy costs for SLH-DSA signing on 32-bit devices were up to 243\% higher than on equivalent 64-bit hardware, making it impractical for resource-limited IoT deployments. These findings have direct implications for IoT security practitioners planning PQC migration.

---


### 44. [Joint Constraint Aggregation for Qualifier-Sensitive Retrieval-Augmented QA](https://arxiv.org/abs/2610.27114)

**<font color=#1a73e8>作者：</font>** Jennifer Hsia, Zachary C. Lipton, Aarti Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented QA can fail even when the correct answer is in the retrieved evidence. This can happen when a competing answer satisfies some, but not all, of the question's requirements and is mentioned frequently in the retrieved documents, which can make it appear to be the best-supported answer. To test whether this retrieval skew actually affects the decision, we manipulate it directly: increasing the prevalence of passages that favor the competing answer makes the model more likely to select it. This points to a decision problem that candidate-level support alone cannot resolve. We therefore introduce Joint Constraint Aggregation (JCA), which compares candidates against the same question-derived requirements using the retrieved evidence. Across three evaluation settings and three instruction-tuned backbones, JCA improves overall accuracy, and its advantage grows when retrieval favors a competing answer. Together, these results suggest that when partial matches and retrieval prominence pull models toward a competing answer, comparing candidates against the question's full requirements can make selection more reliable.

---


### 45. [Glass-Box Deep Reinforcement Learning for High-Speed Flow Control](https://arxiv.org/abs/2610.27132)

**<font color=#1a73e8>作者：</font>** Ameya D. Jagtap  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning (DRL) is challenging long-held assumptions in active flow control. By learning directly from interaction with a flow, DRL agents can find actuation strategies for nonlinear, unsteady flows without explicit models, often exploiting mechanisms that classical control would not anticipate. High-speed flows are a demanding test of this promise: shocks, shock/boundary-layer interactions, transition, aerothermal loading and microsecond-scale dynamics strain both algorithms and hardware. Yet most demonstrations remain idealized, low-speed simulations with limited evidence of robustness, interpretability, transferability or experimental deployment. In this perspective, we examine what constrains DRL-based high-speed flow control, including compressible simulation cost and fidelity, data efficiency, sensing in extreme environments, reward design, explainability, and generalization across Mach and Reynolds number. We argue that these limits reflect a tension between data-driven optimization and the structured physics, constraints and uncertainties of real flows. We then highlight where DRL may go beyond conventional approaches: adaptive control of shock-induced separation and turbulent boundary layers, coordination of distributed actuators, and discovery of unconventional flow-manipulation this http URL central challenge, however, is translating these capabilities into reliable technology, which will require validated compressible simulation environments, physics- and constraint-aware learning, robustness to off-design conditions and sensor degradation, real-time operation, hardware-in-the-loop and wind-tunnel validation, and credible pathways to safety and certification.

---


### 46. [Mind Your Boundaries: Boundary-Aware Model Obfuscation against Cross-node Attack](https://arxiv.org/abs/2610.27135)

**<font color=#1a73e8>作者：</font>** Yuyang Zhang, Yihui Jin, Kangjie Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the advancement of powerful AI chips, on-device machine learning is gaining traction for its low latency and privacy protection. However, when edge devices are compromised, attackers can obtain white-box access to the deployed models by reversing the apps directly to obtain the knowledge of peer devices, which is known as Cross-Node Attacks, like performing efficient adversarial attacks. Most existing defenses target known vulnerabilities, yet white-box access still enables attackers to uncover more unknown weaknesses. This creates a critical risk for edge-device deployments, where one compromised device can endanger all models distributed from the same source. Motivated by findings that the model robustness is primarily influenced by the curvature of the decision boundary, we investigate how model parameters shape its curvature. In this paper, we propose a novel method, BMO, that obfuscates model parameters to diversify the decision boundary further resisting cross-node attack while preserving its benign accuracy. Specifically, we explore decomposing model parameters into boundary-position and boundary-curvature components based on null-space constraints, then models with differentiated decision boundaries are instantiated by injecting noise into the boundary-curvature component. Across all four major types of adversarial attacks with four widely-deployed on-device models, BMO achieves an average success rate of 68.68% in defense, far exceeding the most competitive baseline, which attains only 22.32% in defending against cross-node attacks. Moreover, BMO achieves comparable performance in benign accuracy compared with baselines.

---


### 47. [Ontic state recovery through prediction](https://arxiv.org/abs/2610.27139)

**<font color=#1a73e8>作者：</font>** Ping Zhang, Quang-Huy Nguyen, Yingtie Lei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We encounter a system through its responses, yet its state concerns how the system is. Predicting further responses promises knowledge beyond what is immediately observed. What that knowledge tells us about the system's state depends on what we mean by a state in the first place. We give this notion a model-relative meaning: a state is the complete response profile over a specified query universe, and configurations agreeing on every query are regarded as the same state. From this perspective, a learned state is understood through the distinctions between these profiles that it retains. Prediction concerns selected observations; recovery concerns the profile as a whole. We examine their relationship through query ambiguity, state-space geometry, and the choice of prediction targets. Synthetic systems with known response laws and neural recordings provide complementary settings for this investigation. The aim is to clarify how prediction can become a way of knowing a system, and what it would mean for a learned state to preserve the state being studied.

---


### 48. [Representing short-term movement to reveal animal identity and learning progress](https://arxiv.org/abs/2610.27140)

**<font color=#1a73e8>作者：</font>** Ping Zhang, Quang-Huy Nguyen, Yingtie Lei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How learning progresses over time and varies across individuals is a longstanding question in cognitive and behavioral science. However, a major challenge is identifying observable behavioral measures that faithfully capture learning progression. Existing approaches commonly rely on predefined behavioral features or task-level performance, while fine-scale posture and movement in freely behaving animals remain less explored. In this paper, we ask: can short-term movement trajectories reveal learning progress and individual identity? We introduce a self-supervised representation learning framework built on a simple hypothesis: behavioral characteristics associated with identity and learning remain relatively stable over nearby time intervals. Using temporal proximity as supervision, our framework learns compact representations directly from movement trajectories without manually defining behavioral states or kinematic features. Using behavior data from freely behaving rats, we show that the learned representations not only improve prediction of identity and learning-related readouts over existing methods, but also provide a tool for investigating broader scientific questions about when and how these signals appear in behavior. Specifically, trajectories as short as one second contain informative learning and identity signals. Egocentric pose dynamics are more predictive of identity, whereas allocentric motion is more predictive of learning-related variation, and both signals are strongest at decision junctions in the alternation cohort. We further use a representation-conditioned diffusion model to inspect movement patterns associated with identity and learning progress. Our findings establish short-term movement as an informative behavioral "fingerprint" for studying learning and individual differences. Our code is available at this https URL.

---


### 49. [PRIMFLOW: Learning Trajectory Primitives for Few-Step Distillation](https://arxiv.org/abs/2610.27146)

**<font color=#1a73e8>作者：</font>** Hongyi Fang, Benjia Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step trajectory distillation aims to learn accurate global updates from dense local supervision along a teacher's sampling trajectory. Existing approaches construct within-step dynamics using specific trajectory parameterizations or discrete interval predictions, tying the learned update to a prescribed temporal structure. We propose \method, which directly learns a continuous trajectory primitive representing cumulative displacement along the teacher trajectory. By supervising finite differences of the primitive with local teacher velocities, \method learns the accumulated motion directly, while obtaining global updates through endpoint differences. This formulation avoids prescribing a temporal basis or fixed query grid and instead learns the temporal evolution of cumulative displacement from local supervision. We further establish a local-to-global error bound to characterize how local regression errors affect full-interval displacement accuracy, and introduce endpoint absorption to eliminate the auxiliary primitive branch while preserving one-network-evaluation inference. Experiments on large-scale text-to-image generation show that \method achieves a T-FID of 20.92 and an HPSv2 score of 28.35 at one NFE, improving both metrics over a trajectory-distillation baseline. After endpoint absorption, it retains comparable performance, achieving a T-FID of 20.86 and an HPSv2 score of 28.33.

---


### 50. [GRID: Modeling Health Influencer Discourse as Argument Networks for Credibility Assessment](https://arxiv.org/abs/2610.27149)

**<font color=#1a73e8>作者：</font>** Nishanth Sridhar Nakshatri, Eylon Caplan, Dan Goldwasser  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Health-related discussions on social media are increasingly shaped by influencers who offer diverse, and often competing perspectives on the same issue. Yet, such content is typically evaluated in isolation, without considering the broader discourse in which it appears. We introduce GRID (Grounded Reasoning over Interconnected Discourse), a framework for evaluating influencer content through collective inference over the surrounding discourse. GRID represents each video as an argumentation graph connecting claims to its central message, or takeaway, links related claims and takeaways across videos, grounds claims in scientific evidence, and jointly infers credibility over the resulting network. We evaluate GRID on an end-to-end health-related content validation task using 569 influencer videos grounded in expert assessments. Our results show that accounting for the broader discourse improves influencer content validation. Finally, we use GRID-inferred credibility to demonstrate how argumentative strategies and moral framing differ between low- and high-credibility content.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-288](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
