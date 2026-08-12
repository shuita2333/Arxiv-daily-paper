# 📦 其他研究 | 2026年08月13日

> 本类共 **189** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-189](./part-04.md)

---

### 101. [IADD-TR: Intervention-Aware Dynamics Decoupling with Targeted Regularization for Model-Based Reinforcement Learning](https://arxiv.org/abs/2608.10634)

**<font color=#1a73e8>作者：</font>** Zefeng Liang, Jie Qiao, Ruichu Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based reinforcement learning (MBRL), which learns environment dynamics to generate synthetic experience, is a promising approach to sample-efficient decision making. Numerous methods have been developed to improve dynamics prediction and policy optimization for MBRL through uncertainty estimation, model regularization, and conservative value learning. However, these methods typically treat the transition model and critic as monolithic predictors, overlooking the policy-induced data bias. Consequently, action can become entangled with environmental evolution, while uneven action coverage may distort the counterfactual value estimates used for policy improvement. To address this, we propose IADD-TR, a unified framework combining Intervention-Aware Dynamics Decoupling (IADD) and Targeted Regularization (TR). IADD factorizes transitions into an action-intervention stage and an action-free natural evolution stage, using a zero-action anchor to resolve the non-uniqueness of this two-stage factorization for robust generalization. Its latent and state-aligned components are identifiable up to an invertible within-block transformation and pointwise, respectively. For policy learning, we derive TR from the efficient influence function of a replay-state policy-gradient functional. TR augments the critic with an action-density-scaled residual correction and optimizes a targeted loss, yielding doubly robust policy-gradient estimation when either the critic or the replay action density is consistently specified. Extensive experiments on five MuJoCo tasks show that IADD-TR achieves competitive returns with improved sample efficiency.

---


### 102. [Curate Before You Connect: Identity and Ontology Tagging in a Production Knowledge Graph](https://arxiv.org/abs/2608.10644)

**<font color=#1a73e8>作者：</font>** Vaibhav Dangaich, Kevin Lewis, Kundeshwar Pundalik  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Extraction produces candidate entities and relationships; writing them into a graph is where identity is decided, and identity decisions are destructive in a way extraction errors are not. A wrong type can be corrected later, but two records merged under one identity cannot be separated once their properties have been combined, and the merge leaves no error behind. This paper describes the ingestion and ontology-tagging layer that turns a validated extraction stream into a knowledge graph of 537,157 entities and 2,198,567 relationships drawn from 98,795 government documents. We describe a record-identity ladder that decides sameness from identifier columns, name columns, display names and type-scoped position rather than from name similarity. The ladder governs de-duplication within parsed tables, while the graph write applies a coarser canonical-name key, so records sharing a canonical name merge automatically on exact equality. We argue rather than demonstrate that this is where the automation line belongs: no identity benchmark is reported, and the over-merges the key permits are undetectable by construction. That policy, under which entity resolution only ever flags candidates, followed an incident in which two surface forms of one name were merged, corrupting a correct record and deleting eight entities from an unrelated document. We then describe multi-class ontology tagging and an evidence asymmetry we did not anticipate: an entity name is an instance label rather than a type assertion, so matching name fragments against a class index invents classifications. Requiring anchored evidence cut role assignments on an enriched sample from 36 to 4, all confirmed correct. We quantify the graph's conformance debt, show secondary classifications compensating for a mis-parented primary class, and describe a curation queue grown to 48,403 pending proposals against 775 human decisions.

---


### 103. [ProtoGIB-Workload: Learning Workload-Specific Neural Topology Prototypes across Subjects](https://arxiv.org/abs/2608.10647)

**<font color=#1a73e8>作者：</font>** Yuzhe Zhang, Yixi Zhang, Shengdian Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Reliable electroencephalography (EEG)-based mental workload recognition is crucial for adaptive human-centered systems, yet practical deployment requires models to generalize to users unseen during training. Although functional connectivity graphs are widely adopted to capture workload-related neural interactions, they inherently entangle task-relevant structures with subject-specific physiological traits and sample-level noise. This entanglement often leads models to learn structural shortcuts, severely degrading cross-subject generalization. To address this, we propose ProtoGIB-Workload, a novel framework that explicitly regularizes and aligns graph structures for subject-independent workload recognition. Our approach introduces a Stochastic Graph Information Bottleneck (SGIB) to compress dense correlation priors into compact, task-relevant subgraphs, filtering out input-related redundancy. Crucially, to prevent the retention of subject-specific spurious edges, we propose a Class-Conditional Topology Stabilizer (CTS). Leveraging the fixed electrode coordinates of EEG data, CTS operates directly on graph-generation probabilities to encourage consistent edge-generation statistics across different subjects sharing the same workload class. Extensive experiments on two public EEG workload datasets and one in-house EEG cognitive load dataset of air traffic controllers under strict leave-one-subject-out (LOSO) protocols demonstrate that ProtoGIB-Workload significantly outperforms state-of-the-art temporal and graph-based baselines, improving the cross-subject Macro-F1 score by an average of 5.15% (up to 6.34%). Further analyses confirm that our method successfully extracts stable, cross-subject consistent neural connectivity patterns.

---


### 104. [Precise Top-Layer Fabric Segmentation for Fabric Destacking with Edge- and Shape-Aware Deep Networks](https://arxiv.org/abs/2608.10648)

**<font color=#1a73e8>作者：</font>** Wenbo Dong, Dipankar Bhattacharya, Akinari Kobayashi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fabric destacking requires precise segmentation of the topmost fabric layer, a task complicated by subtle fabric boundaries and high visual similarity between fabric layers. Existing semantic and edge-based segmentation approaches often struggle with these complexities, limiting the performance of robotic manipulation for different tasks. In this work, a novel segmentation training architecture tailored for top-layer fabric segmentation in stacked fabrics is proposed. The method extends the classical encoder-decoder framework by introducing two specialized branches - an edge-aware branch and a shape-aware branch - that are used to supervise the backbone network for better tuning. The edge-aware branch enhances boundary delineation, while the shape-aware branch guides the network to capture and align the overall fabric shape with reference masks derived from Computer Aided Design (CAD) models. Experiments on a real-world fabric dataset demonstrate that the training approach outperforms established baselines, verifying the effectiveness of the multi-branch design through both quantitative results and ablation studies.

---


### 105. [PolypVision: A Three-Stage Hierarchical Deep Learning Framework for Classification and Segmentation of Colorectal Polyps](https://arxiv.org/abs/2608.10649)

**<font color=#1a73e8>作者：</font>** Hamidreza Bolhasani, Hamidreza Rastad, Amir Mohammad Akbari 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Colorectal cancer (CRC) remains one of the leading causes of cancer-related mortality worldwide, predominantly arising from precancerous polyps. Accurate detection, segmentation, and endoscopic and histological classification of colorectal polyps are crucial for timely clinical intervention. In this study, we present PolypVision, a three-stage hierarchical deep learning framework that sequentially performs: (Stage 1) binary classification of polyps as adenomatous or hyperplastic, with simultaneous Paris and JNet classification, using EfficientNetV2-M with Focal Loss; (Stage 2) polyp segmentation with recommended resection method using a UNet++ decoder with the Stage 1 backbone as encoder, optimized with Dice and BCE losses; and (Stage 3) adenoma subtype classification (tubular, tubulovillous, villous) using EfficientNetV2-M with transfer learning from Stage 2. Evaluated on three public datasets -- PolypGen, Kvasir-SEG, and CVC-ClinicDB -- PolypVision achieves an AUC of approximately 0.99 for frame classification and a detection mAP@50 of 94.4% on Kvasir-SEG, outperforming or matching state-of-the-art methods. Gradient-weighted Class Activation Maps (Grad-CAM) confirm that the model attends to clinically relevant lesion features. The framework is device-independent, operating across diverse endoscopic imaging systems without hardware-specific adaptation. These results demonstrate that a hierarchical, transfer-learning-driven pipeline with task-specific loss functions offers a robust, device-independent, and clinically meaningful approach to automated colorectal polyp analysis. PolypVision is freely available as a web application at this https URL, a DataBioX initiative, with a free usage tier open to all users.

---


### 106. [Decision-Aware Approximation of Belief Functions for Evidential Combinatorial Optimization](https://arxiv.org/abs/2608.10650)

**<font color=#1a73e8>作者：</font>** Sohaib Afifi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reducing the number of focal elements of a mass function is classically driven by an intrinsic distance, such as Jaccard or Jousselme, that keeps the approximation close to the original as a body of evidence. We consider instead the case where the mass function feeds a linear combinatorial optimisation problem with evidential costs. What should then be preserved is not the closeness of the two mass functions, but the quality of the decision they induce. We introduce a decision-aware approximation that targets the regret of the decision: one decides with the cheaper approximation and is evaluated under the true mass function. On a minimal shortest path, the distance-optimal approximation flips the decision while a decision-aware merge preserves it, and this occurs on a non-negligible fraction of random instances. We prove a one-point bound that localises the regret at the true optimum, turn it into an exact dynamic program for the scalar case, and extend it to an online version that prunes focal elements before the final cost is known. In experiments the decision-aware compressor flips the decision less often than representation-aware compression, for both the linear criterion and a non-linear proxy read-out.

---


### 107. [Cross-View Sequential Visual Localization with Spatio-Temporal Context Modeling for Autonomous Driving](https://arxiv.org/abs/2608.10660)

**<font color=#1a73e8>作者：</font>** Jiaping Wang, Shaobo Li, Zhen Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous and reliable localization is essential for autonomous driving. Cross-view visual localization matches ground images with satellite maps, providing complementary localization cues for pipelines that depend on Global Navigation Satellite System (GNSS) signals and high-definition (HD) maps. Most existing cross-view visual localization methods process each frame independently, leaving temporal information underused and limiting accuracy under dynamic occlusion, illumination variation, and repetitive textures. This study proposes a temporal-context-enhanced framework for cross-view sequence visual localization. The proposed recurrent cross-frame module aggregates historical context from the previous state to enhance the coarse ground feature of each current frame. These enhanced features facilitate satellite candidate-region classification, while hierarchical fine-grained features enable precise local offset estimation. On the CVIS dataset, the proposed method reduces mean localization error from 3.80 m to 1.57 m and increases R@1 m from 8.14% to 40.22%. Direct transfer to KITTI-CVL achieves a mean error of 2.61 m, with target-domain fine-tuning further reducing the mean error to 2.27 m. Zero-shot field experiments on a real-world vehicle achieve a mean error of 2.84 m and R@5 m of 96.86%. These results demonstrate that temporal context enhancement significantly improves cross-view localization accuracy and supports robust deployment on public benchmarks and real-world roads.

---


### 108. [Operationalising Relative Causal Knowledge: Backbone Identifiability from Private Reports on a Shared Outcome](https://arxiv.org/abs/2608.10664)

**<font color=#1a73e8>作者：</font>** Fabrizio Russo, Mark Somers  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Relativity of Causal Knowledge (RCK) explains how a network of agents with different structural causal models can exchange causal knowledge through a shared interventionally consistent abstraction, or backbone. We ask the prior identification question that this transport mechanism presupposes: when is that backbone determined by the agents' private causal knowledge? In the basic two-agent common-effect case, two private causes influence one shared outcome and each agent identifies only the single-cause causal marginal relevant to its own perspective. We show that, under standard compatibility, non-degeneracy, and local overlap assumptions, those local causal marginals do not identify a unique backbone. Infinitely many joint intervention kernels can induce exactly the same private reports while disagreeing on joint interventions. We then give a conditional recovery result. Additive separability removes the hidden interaction degree of freedom, but observational residual summaries remain insufficient. Identification becomes possible when agents communicate causally identified response functions. An education value-added example illustrates why this is first a communication problem, and only then a policy-composition problem.

---


### 109. [FITTER: Vocabulary-Agnostic Cross-Domain Inference on Temporal Knowledge Graphs](https://arxiv.org/abs/2608.10668)

**<font color=#1a73e8>作者：</font>** Jiaxin Pan, Mojtaba Nayyeri, Osama Mohammed 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Temporal knowledge graphs are central to many uses of the Semantic Web, but existing completion methods assume the entities, relation names, and timestamps to be reasoned about are already known at training time, restricting each model to a single graph and vocabulary. We propose FITTER, the first fully-inductive structural model for temporal knowledge graph link prediction that supports cross-domain transfer: the inference graph may contain entirely unseen entities, relation names, and timestamps drawn from a different domain. FITTER represents each predicate by its interaction patterns with others and time through encodings of relative rather than absolute ordering; message-passing fuses local and global temporal context to produce vocabulary-agnostic embeddings. We prove the temporal encoding is time-shift invariant and evaluate FITTER on cross-domain, cross-graph transfer over six temporal knowledge graph benchmarks of diverse domains, granularities, and time spans. FITTER consistently outperforms inductive baselines without retraining, indicating that vocabulary-agnostic structural learning is a viable foundation for inference over the heterogeneous knowledge graphs of the Semantic Web.

---


### 110. [Seeds Before Objectives: Rethinking Evaluation for Low-Resource Garhwali ASR](https://arxiv.org/abs/2608.10670)

**<font color=#1a73e8>作者：</font>** Karamvir Singh Batra, Prathamjyot Singh, Ashima Sood 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> At corpus sizes typical of low-resource dialects, single-run comparisons can yield gains that do not replicate. We show this for Garhwali, an under-resourced Indo-Aryan language of the central Himalaya, building the first reproducible multi-seed ASR benchmark on the official VAANI splits, with per-seed outputs and significance testing. Re-examining plausible gains, we find them fragile: neither Focal CTC nor a matra-weighted objective beats standard CTC under seed-level testing, the matra objective fails to cut even its targeted errors, and Hindi-to-Garhwali transfer gives no gain over direct fine-tuning. What holds up is mundane: w2v-BERT 2.0 with standard CTC reaches 47.0% WER over five seeds, beating the larger MMS-1B and comparable models; pretraining design, not parameter count, drives performance, and speed augmentation gives a small, largely consistent gain. Multi-seed evaluation on official splits separates real gains from seed noise.

---


### 111. [Chartography: A Benchmark for Professional Chart Understanding](https://arxiv.org/abs/2608.10677)

**<font color=#1a73e8>作者：</font>** Suhaas Garre, Chris Mutty, Sushant Mehta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Professionals across medicine, engineering, finance, manufacturing, and the sciences often make consequential decisions from charts. Existing chart benchmarks do not sufficiently measure this ability: they are dominated by bar, line, and pie formats, rely on shorter reasoning chains, and are nearing saturation, with frontier models already scoring 80-90%. We introduce Chartography, a benchmark of 100 tasks that pair charts drawn from professional practice, in domain-specific formats that standard chart benchmarks rarely include, with questions written by professionals who read these charts for a living and independently verified by three additional experts. In an evaluation of 30 frontier-model configurations (20 scored trials per task), the best configuration reaches only 45.0% mean pass@1; the remainder span 9.0-39.5%. Failures concentrate in visual perception: models can miss nuanced features, misread values along sparsely labeled axes, mishandle projected 3D geometry, and violate domain conventions encoded in the chart. We release all tasks, images, provenance metadata, and evaluation code.

---


### 112. [Bridging Severe Cross-Modal Misalignment: End-to-End Visible-Infrared Object Detection via Explicit Feature-Domain Affine Registration](https://arxiv.org/abs/2608.10680)

**<font color=#1a73e8>作者：</font>** Qi Ming, Yuyang Wang, Mingjing Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visible-infrared object detection relies on complementary RGB and thermal cues, but its performance is often degraded by cross-modal spatial misalignment. Most existing methods rely on implicit feature adaptation to handle weakly misaligned scenarios, while large-offset geometric discrepancies remain insufficiently addressed. In this paper, we propose a Joint Feature-domain Registration and Detection network (JFRDet), an end-to-end visible-infrared oriented object detector tailored for severely cross-modal geometric discrepancies. JFRDet introduces a Cross-Modal Affine Alignment (CMAA) module to estimate an image-level affine transformation for explicit multi-level feature alignment. Note that illumination changes directly affect the reliability of RGB cues, an Illumination-Guided Complementary Fusion (IGCF) module adaptively exploits modality reliability under varying illumination conditions for cross-modal fusion. Then, an Alignment Quality-Consistency Gating (AQCG) strategy stabilizes joint optimization by modulating detection supervision according to alignment reliability and gradient consistency. We further construct DroneVehicle Misaligned (DVMA), a benchmark for evaluating visible-infrared oriented object detection under severe cross-modal geometric misalignment. The proposed JFRDet achieves 69.7\% $\mathrm{mAP}_{50}$ on DVMA, which represents state-of-the-art (SOTA) performance. The code and dataset will be available on GitHub.

---


### 113. [Visual Geometry Foundation-Aware Gaussians for Single-Frame Surround-View Driving Reconstruction](https://arxiv.org/abs/2608.10682)

**<font color=#1a73e8>作者：</font>** Junhong Lin, Jinlong Wang, Xianda Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-frame surround-view reconstruction faces severe geometric instability and rendering artifacts due to minimal inter-camera overlap. While existing methods rely on complex decoders or auxiliary cues, they remain bottlenecked by the weak geometric capacity of upstream features. We argue that leveraging pretrained visual geometry priors strengthens upstream representations and alleviates the geometric ambiguity in sparse surround views. To this end, we propose VGGD, a visual geometry foundation-aware 3D Gaussian Splatting framework for feed-forward surround-view driving reconstruction, which shifts geometric modeling to the frontend and adapts foundation priors to the driving camera setting. First, VGGD leverages VGGT to provide transferable multi-view geometric prior tokens. Next, we introduce a Dual-Path Neck to decouple geometry-consistent and appearance-aware representations, improving appearance completion in weakly observed regions. We further apply Scale Warmup to stabilize early geometry learning and suppress scale drift under ego-pose changes. Finally, we use a hybrid pixel--volume Gaussian decoder to produce a renderable 3D Gaussian scene for novel-view synthesis. Experiments on the nuScenes single-frame benchmark show that VGGD achieves the best overall rendering quality among the compared methods and improves relative geometric consistency.

---


### 114. [Embedding Rotation Invariance for Provable Multi-Oriented Scene Text Recognition](https://arxiv.org/abs/2608.10684)

**<font color=#1a73e8>作者：</font>** Zhibin Ma, Pengwen Dai, Yi Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-oriented text is ubiquitous in real-world scenes and remains a major challenge for scene text recognition (STR). Existing rotation-aware methods explicitly estimate text orientation. However, due to the lack of theoretical guarantees, they are prone to error accumulation, increased computational cost, and strong reliance on data. In this work, we incorporate rotation invariance into the STR framework to address these limitations. Specifically, we adopt an encoder-decoder architecture, embedding rotation equivariance in the encoder and rotation invariance in the decoder to construct a fully rotation-invariant network. On the decoder side, we first identify and prove the rotation-invariant property of the cross-attention mechanism and use it to formulate a rotation-invariant text decoder that maps visual features to output text in a rotation-invariant manner. On the encoder side, we propose a rotation-equivariant local-global extraction network that integrates deep equivariant convolutions with self-attention, enabling rotation-equivariant feature extraction while modeling inter-character dependencies and preserving fine-grained visual details. By integrating the encoder and decoder, we obtain an end-to-end Rotation-Invariant Scene Text Recognition network (RISTER). RISTER provides rotation invariance with theoretical guarantees, enhancing robustness on multi-oriented samples without introducing additional inference computation or relying on data-driven orientation correction. Experiments show that RISTER achieves state-of-the-art performance on both standard and multi-oriented benchmarks, surpassing the second-best model by 4.0 percent in accuracy on the general multi-oriented dataset.

---


### 115. [Leveraging Human Reading Behavior for Keyphrase Extraction: A Webcam-based Eye-tracking Corpus](https://arxiv.org/abs/2608.10688)

**<font color=#1a73e8>作者：</font>** Chengzhi Zhang, Xinyi Yan, Wenqi Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Purpose: Keyphrases are statistically and semantically important textual units that can also attract readers' attention during comprehension. However, existing keyphrase extraction (KPE) studies mainly focus on improving textual representation while largely overlooking human reading behavior. This study examines whether lightweight webcam-based eye-tracking features can improve KPE from Chinese academic abstracts in Library and Information Science (LIS).
Methodology: To address the limited availability of eye-tracking data for Chinese academic reading, we developed a lightweight webcam-based data collection platform using the open-source SearchGazer library and constructed the Chinese LIS Eye-Tracking Corpus (CLIS-ET). Three character-level eye-tracking features, first fixation duration (FFD), fixation number (FN), and total fixation duration (TFD), were incorporated into KPE models to evaluate their effects on extraction performance.
Findings: Eye-tracking features consistently improved KPE performance. The combination of FN and TFD achieved the best results on the Att-BiLSTM+CRF model, indicating that readers' fixation behavior provides useful signals for identifying keyphrases in academic abstracts.
Originality/value: This study introduces a cost-effective webcam-based eye-tracking approach for KPE and presents CLIS-ET, a Chinese academic eye-tracking corpus containing FFD, FN, and TFD features. The results demonstrate the value of incorporating human reading behavior into keyphrase extraction. Dataset and code: this https URL and this https URL.

---


### 116. [The Signal Rail: A Deterministic Motion Grammar for Communicating Conversational Agent State in Terminal Interfaces](https://arxiv.org/abs/2608.10689)

**<font color=#1a73e8>作者：</font>** Matteo Grella  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Terminal interfaces to conversational agents report rich internal state (listening, thinking, executing tools, awaiting input, failing) almost entirely through text, while the motion channel beside it, the one peripheral vision monitors without reading, carries a single bit: alive. We present the Signal Rail, a one-row terminal status instrument that gives that channel a grammar. Four ideas govern it: spatial semantics (input, processing, and output zones, with direction as meaning), a motion grammar (one kinetic rule per state, never color alone), determinism (frames as a pure function of explicit inputs, golden-frame testable), and honesty (no invented progress or activity). We contribute a 45-section normative specification and a reference implementation inside a working full-duplex local voice agent driven by real signals.

---


### 117. [SQuaT: Self-Supervised Knowledge Distillation via Student-Aware Quantized Teacher Features](https://arxiv.org/abs/2608.10709)

**<font color=#1a73e8>作者：</font>** HyeonJun Lee, Hyeonsik Jo, Jinwoo Chung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization-Aware Training (QAT) enables the deployment of quantized models with minimal accuracy degradation. However, in practical scenarios, training labels are often unavailable due to privacy, copyright, or cost constraints. Knowledge Distillation (KD) is a common approach to address this challenge, but we observe that prior work combining QAT with KD suffers from a fundamental limitation: during distillation, the range mismatch between the teacher and the quantized student model induces an unattainable residual, resulting in an irreducible lower bound on the distillation loss. Motivated by this observation, we propose SQuaT (Student-Aware Quantized Teacher Features), a label-free QAT framework with KD that theoretically eliminates this lower bound by applying the student's quantization parameters to quantize the teacher's features during distillation. Through comprehensive experiments across diverse settings, we demonstrate that SQuaT consistently outperforms strong baselines, with particularly pronounced gains in extreme low-bit (e.g., 1- and 2-bit) settings. Furthermore, extensive evaluations across various model design choices show that our approach does not rely on specific architectural assumptions, making it broadly applicable across diverse architectures and quantization settings. The source code is available at this https URL.

---


### 118. [Compact Feed-Forward 3D Gaussians via Saliency-Guided Primitive Merging](https://arxiv.org/abs/2608.10712)

**<font color=#1a73e8>作者：</font>** Tim-Felix Fassch, Jochen Kall, Cyrill Stachniss  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D scene reconstruction, modeling, and rendering are highly relevant for numerous tasks, and 3D Gaussian splatting has become a standard choice in this context. Its feed-forward variants provide fast reconstruction from sparse input views but often produce per-pixel primitives, leading to highly redundant and thus inefficient representations. We present a structure-aware merging pipeline that takes per-pixel primitives from any feed-forward method and consolidates them into a compact, content-adaptive Gaussian set while largely retaining visual quality at just $\frac{1}{20}^\text{th}$ of the Gaussians of a per-pixel method. We group spatially coherent Gaussians of similar appearance into variable-size clusters via adaptive superpixel segmentation guided by a saliency map, which allocates fine segments to textured regions and coarse segments to homogeneous areas. We compress each cluster into a compact latent representation through a learned encoder, then match and consolidate representations across views based on geometric overlap and feature similarity via a learned merger. A level-of-detail decoder then produces the final Gaussians at a controllable resolution, enabling a flexible quality-efficiency trade-off at inference. As a post-processing module, the pipeline is backbone-agnostic, leveraging the strengths of existing feed-forward methods. This leads to better and more robust quality than achieved by previous approaches that target a reduction in primitive count, while providing a highly compact representation, that can be rendered efficiently.

---


### 119. [Ex-Omni-2D: Expressive Omni-Modal Dialogue Models with Native Visual Presence](https://arxiv.org/abs/2608.10720)

**<font color=#1a73e8>作者：</font>** Haoyu Zhang, Zhipeng Li, Xiaoying Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Omni-modal dialogue models can understand multimodal inputs and synthesize spoken replies, yet their responses remain visually disembodied. We introduce \textbf{Ex-Omni-2D}, an omni-modal dialogue framework that generates a coordinated response comprising text, personalized speech, and reference-conditioned video. Given a multimodal query, reference image, and reference audio, the model predicts a structured \textit{Visual Thought Plan} (VTP) describing scene, emotion, and motion, followed by response text and native multi-codebook speech units. These units form a shared acoustic-temporal interface: they are decoded into speech and aligned online with video frames. This interface enables the response and avatar pathways to be learned from heterogeneous speech, dialogue, and avatar-video data, avoiding the need for large-scale query--text--speech--video supervision. A full-sequence Video Generator serves as the primary Teacher. For efficient incremental generation, we further distill it into a few-step block-causal \emph{Streaming Student} whose Prefix Streaming mechanism carries a clean latent across consecutive chunks to reduce cumulative late-chunk degradation. With four-step inference, the complete four-GPU pipeline achieves an end-to-end RTF of 1.293 at $400\times720$/$720\times400$, providing a practical quality--efficiency operating point.

---


### 120. [Grid-Preserving Knowledge Distillation: Transferring Convolutional Inductive Bias to Vision Transformers under Data Scarcity](https://arxiv.org/abs/2608.10723)

**<font color=#1a73e8>作者：</font>** Junyong Choi, Cheolhyeon Park, Jaehoon Cho  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers underperform convolutional networks when training data is scarce, and distilling convolutional inductive biases from a CNN teacher is an effective remedy that leaves the deployed model unchanged. General-purpose feature distillation, however, transfers little in this setting. The pooling, flattening, and logit-space projections it inherits from CNN to CNN pipelines discard the spatial grid in which locality and translation equivariance are encoded, and unlike a convolutional student, a ViT cannot rebuild that structure on its own. In this paper, we propose iBKD, a distillation framework that preserves the grid along the entire transfer path. Its core module, the Inductive Bias Attention Module, aggregates every student layer onto the teacher grid with learned weights, sharpens structural cues with channel and deformable spatial attention, and injects them through convolutional cross-attention that operates between grids rather than between token sets. The module is used only during training, so the deployed model is an unmodified ViT with no inference overhead. Across seven Transformer backbones and six data-scarce benchmarks, iBKD outperforms both locality-guidance methods and general knowledge distillation baselines, and its margin widens as training data shrinks.

---


### 121. [InterPruner: Interactive Structured Pruning via Taylor-Implicit Criterion and Language-Prior Modulator for Multimodal Object Detection](https://arxiv.org/abs/2608.10724)

**<font color=#1a73e8>作者：</font>** Qi Ming, Zihan Yang, Shaoguang Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal object detection proves effective in remote sensing, especially the RGB-Infrared paradigm. The parallel feature extractors provide rich multimodal information for robust detection, yet introduce substantial channel redundancy and computational overhead. Existing pruning methods can reduce channel redundancy, but they are designed for unimodal backbones, overlooking cross-modal interactions and dynamic scene-wise redundancy. In this paper, we propose InterPruner, the first interactive structured channel pruning framework for RGB-infrared object detectors. Specifically, we first derive a Taylor-Implicit Criterion(TIC) to quantify channel importance via high-order Taylor expansion and the implicit function theorem. Then, a Modality Interaction Redundancy Analyzer (MIRA) identifies redundant channels via mutual compensability assessment. Finally, a Scene-Prior Channel Anchor (SPCA) uses language priors as semantic anchors to measure channel-scene relevance for dynamic channel importance estimation. Cross-modality channel pruning for RGB-Infrared detection is yet unexplored. Extensive experiments on RGB-infrared object detection dataset demonstrate that InterPruner maintains high performance with negligible degradation. Specifically, it even achieves a 0.6% mAP increase on the FLIR dataset when pruning 50% of the channels. Code will be available on GitHub to facilitate future work.

---


### 122. [A Lightweight Fault-Detection Scheme for Barrett Modular Multiplication Using Multiple Conditional Reduction Paths](https://arxiv.org/abs/2608.10736)

**<font color=#1a73e8>作者：</font>** Rourab Paul, Paresh Baidya, Krishnendu Guha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Polynomial multiplication is the most resource-, time-, and energy-critical operation in lattice-based Post-Quantum Cryptography (PQC) and Fully Homomorphic Encryption (FHE) schemes. Lattice-based PQC schemes such as Kyber and Dilithium have already been standardized, while lattice- based FHE schemes such as BGV, BFV, and CKKS are widely recognized as leading candidate in FHE area. Barrett Modular Multiplication (BMM) for polynomial multiplication is widely adopted in PQC and FHE hardware accelerators due to its hardware friendly nature and efficient modular reduction capabilities. However, Side-Channel Attacks (SCAs) and Hardware Trojans may introduce intentional faults, while aging and various other factors can cause unintentional faults. These faults may target the BM M unit, one of the most critical components of PQC and FHE infrastructures, potentially leading to information leakage and compromising system security. In this paper, we employ a Statistical Reduction Monitoring (SRM) method to protect the BM M unit against such adversarial conditions. The proposed approach incurs minimal hardware overhead while providing efficient detection of both random and bur

---


### 123. [Long-Time Trajectory Approximation via SA-NODEs: Model Predictive and Floquet Strategies](https://arxiv.org/abs/2608.10738)

**<font color=#1a73e8>作者：</font>** Ziqian Li, Nikolaos M. Matzakos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the approximation of dynamical systems by semi-autonomous neural ordinary differential equations (SA-NODEs) over long time horizons. For a single network trained on the whole horizon, the available error bound deteriorates double exponentially in the horizon length. We develop two training strategies that avoid this barrier, each built on a reset of the state. The model predictive strategy partitions the horizon adaptively and restarts every window from observed data: when training meets a prescribed tolerance on every window, the composite model meets it uniformly in time, with a parameter budget linear in the horizon for targets with a bounded, uniformly regular reachable tube. The Floquet strategy addresses autonomous targets with a stable limit cycle and uses no data at deployment: a certified contraction of the learned return map confines the error to linear growth in the number of elapsed periods. For the time-periodic architecture we deploy, the scalar certificate degenerates; we prove instead a uniform-in-time orbital guarantee whose hypotheses are measured on the trained model, and an obstruction showing that, for an exactly periodic learned field, small one-period error and a contracting stroboscopic map cannot hold at once. Numerical experiments on four benchmarks confirm the predicted error laws and measure the hypotheses of every guarantee.

---


### 124. [Tree-of-Ideas: Automated Research Ideation via Cross-Trajectory Reasoning over Scholarly Evolution](https://arxiv.org/abs/2608.10740)

**<font color=#1a73e8>作者：</font>** Xun Li, Yiying Yang, Pengtao Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective research ideation requires moving beyond a static understanding of prior work to trace how research problems and solutions evolve across the literature. Existing methods either treat papers as unstructured context or model scholarly evolution as isolated citation chains, overlooking interactions among research trajectories. We propose Tree-of-Ideas (ToI), a two-stage framework. EvoTrace reconstructs branching scholarly trajectories from citations, tracking evolving methods, resolved problems, and gaps. EvoAgent then reasons across trajectories to identify convergent problems and complementary solutions, generating grounded research ideas. Across six AI research topics, ToI achieves the highest score among automatic methods (6.27 vs. 5.36 for the strongest baseline on a 10-point scale), with strong Novelty (6.36) and Groundedness (7.00). Also, its score approaches that of human-paper references (6.29), demonstrating the value of cross-path evolutionary reasoning.

---


### 125. [Beyond Pixels: From Video Priors to 4D Worlds](https://arxiv.org/abs/2608.10744)

**<font color=#1a73e8>作者：</font>** Zihao Liu, Xiaolong Shen, Zhenglin Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D generation synthesizes dynamic 3D scenes from conditions such as text or images. Existing methods either reconstruct generated RGB videos with a separate 4D model or adapt a particular video generator to predict geometry directly. The former suffers from distribution mismatch and error propagation, whereas the latter ties 4D prediction to a specific generator and may require retraining when the generator or conditioning regime changes. We ask whether the final denoised latents of video models that share a variational autoencoder (VAE) can instead provide a reusable interface to explicit 4D prediction. Building on this insight, we introduce direct latent-to-4D generation and instantiate it as Latent-to-4D, which bypasses RGB by aligning a video latent with the token grid of a pretrained 4D decoder and refining it through frame-wise and global spatiotemporal attention. Trained on roughly 1K existing reconstruction clips, a single checkpoint transfers unchanged across multiple video diffusion transformers within the same VAE family. On Text4D-200 and I4D-200, Latent-to-4D surpasses matched same-latent Wan+4RC cascades in projection-based DINO-F1 by 2.88--3.45 and 5.81 points, respectively, while also being preferred by human raters for geometry, temporal stability, and overall quality.

---


### 126. [Playable Pressure: Affective Dramaturgy and Selective Realism in the Design of a VR Emergency-Response Serious Game](https://arxiv.org/abs/2608.10763)

**<font color=#1a73e8>作者：</font>** Jan K. Argasiński  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Professional simulations stage not only procedures but models of what should command attention, which emotions belong in competent practice, and whose distress becomes part of the task. This article develops affective dramaturgy through critical design-document analysis of a virtual-reality emergency-response project. The corpus comprises two non-public production records. We identify six families of specified pressure and examine how sensory staging, proximity, trigger authority, task conflict, and response allocation imply a selectively receptive triage professional. The documented design can make emergency work morally and socially crowded, yet it can also turn grief, vulnerability, and mental-health-coded behavior into adjustable difficulty. We propose answerability at two levels-in-play response and post-play debriefability-and derive case-based questions about occupational purpose, representation, adaptation, and accountability. These questions are sensitizing propositions, not a validated framework for user effects or emergency practice.

---


### 127. [Compositional Benchmark Synthesis for Hierarchical Human Action Recognition](https://arxiv.org/abs/2608.10765)

**<font color=#1a73e8>作者：</font>** Farnaz Soleimani, Abdelghani Chibani, Yacine Amirat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recognizing human behavior across levels of abstraction, from atomic actions to long-horizon intentions, requires data annotated along a semantic hierarchy. Large corpora provide isolated, atomically labeled clips without temporal composition, whereas recorded composite-activity corpora offer shallow, domain-narrow, fixedhierarchies. A benchmark-generation and evaluation frameworkis proposed that synthesizes a four-level hierarchical-intention benchmark, spanning actions, activities, low-level intentions (LLIs), and high-level intentions (HLIs), from a flat single-label action corpus while retaining real pre-extracted features at the action level. Episodes are assembled by a transition model under a subject-consistency constraint, and a coverage-aware sampler reduces the subject usage Gini from 0.566 to 0.248. Synthesizing such a benchmark raises a circular-supervision risk that recorded datasets avoid: if the rules generating the episodes also govern the evaluation, models can succeed by recovering the generator rather than through genuine reasoning. Validity is addressed by design, holding sequence-generation rules disjoint from the first-order-logic rules used at evaluation. The instantiation yields 15,002 episodes. Four reference baselines from different model families characterize difficulty, not as recognition methods. A compositional held-out gap of 0.13 to 0.17 macro-F1 appears across all baselines, including a graph-aware model that recognizes best yet does not close the gap, indicating a structural property of the benchmark rather than a model artifact. A logic-free baseline still violates the held-out semantic rules above their intrinsic data rate, and the order-destroying control changes macro-F1 within seed variation, serving as a generator-consistency check. Theontology, transition model, and generator are released so the benchmark can beregenerated and extended.

---


### 128. [Path Integral Value Matching for Linear Quadratic Stochastic Optimal Control](https://arxiv.org/abs/2608.10777)

**<font color=#1a73e8>作者：</font>** Bangyan Liao, Chenglei Yu, Yuchen Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear Quadratic Stochastic Optimal Control (LQ-SOC) establishes a fundamental framework for steering noisy dynamical systems and has recently gained renewed interest in the machine learning community. However, current state-of-the-art policy-based methods suffer from prohibitive computational costs and instability due to their heavy reliance on full-trajectory simulation. To overcome these limitations, we propose a paradigm shift toward a value-based approach by revisiting Path Integral Control (PIC). Although standard PIC suffers from the same high-variance bottleneck as policy-based methods, we discover that by truncating and marginalizing the original path integral formulation, we can derive a temporal recursive form of the value function. Building upon this theoretical foundation, we propose the Path Integral Value Matching (PI-VM) algorithm. Specifically, we employ temporal-difference learning to approximate the recursive value dynamics, and further integrate the Girsanov theorem with experience replay to enable off-policy training. We benchmark PI-VM against SOTA policy-based methods across various SOC benchmarks and sampling tasks. Empirical results demonstrate that PI-VM matches SOTA precision with an order-of-magnitude efficiency gain in low-dimensional settings, while effectively mitigating mode collapse in high-dimensional scenarios. Consequently, PI-VM offers a scalable solution for solving complex SOC problems.

---


### 129. [MVTrack: Ultrafast Appearance-Free Moving Object Tracking from Compressed Bitstreams](https://arxiv.org/abs/2608.10790)

**<font color=#1a73e8>作者：</font>** Iñaki Erregue, Kamal Nasrollahi, Sergio Escalera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying modern video trackers at scale is bottlenecked by the computational cost of RGB-based object detectors. To this end, we present MVTrack, an ultrafast tracker for moving objects that operates directly on H.264 bitstreams. MVTrack combines MVDet, a lightweight detector for motion vector fields, with MVLink, a minimalist kinematic association module. On VIRAT, MVTrack outperforms YOLO26n while using 60$\times$ fewer parameters, requiring 40$\times$ fewer FLOPs, and reducing CPU latency by 8.6$\times$. These results demonstrate that compressed video data alone can enable accurate and scalable surveillance tracking, thereby bypassing the need for pixel reconstruction.

---


### 130. [ChemWorld: Programmable Chemical Worlds for Controlled and Replayable Agent Experimentation](https://arxiv.org/abs/2608.10792)

**<font color=#1a73e8>作者：</font>** Jiangjie Qiu, Yijun Li, Xiaonan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous chemistry increasingly depends on environments in which agents can repeatedly act, observe, and this http URL laboratories provide essential real-material evidence but are costly to repeat and difficult to use for tightly matched interventions, whereas most digital environments keep the underlying experimental world largely fixed. We introduce ChemWorld, a programmable chemical environment in which reusable process and observation components are compiled into executable worlds. ChemWorld separates the public experimental contract available to an agent from evaluator-owned chemical and material laws. Researchers can therefore vary world composition and operating conditions, or change a single hidden law while holding the public task and interaction conditions fixed. Transactional execution records operations, failures, resource changes, and state transitions, allowing complete environment-action trajectories to be replayed exactly and audited. Full-census qualification covered the reference registry, 52 generated compositions, and module, interface, compilation, and invalid-action tests. Eight deterministic experimental cases demonstrated shared lifecycle semantics, failure recovery, and exact replay, while six parent-child world-fork pairs isolated the effects of single private-law interventions under matched public conditions. An independent agent also completed a full lifecycle in a non-reference world through the same public interface. Within the declared component and model domain, ChemWorld provides a controlled and replayable substrate for studying experimentation across systematically varied chemical worlds, complementary to physical-laboratory evidence and calibration.

---


### 131. [Beyond Fixed Luminance: Towards Panchromatic and Orthochromatic Image Colorization](https://arxiv.org/abs/2608.10798)

**<font color=#1a73e8>作者：</font>** Swarnim Maheshwari, Syed Imam Ali, Vineeth N. Balasubramanian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most image colorization systems operate in $Lab$ space by predicting chroma ($ab$) while preserving an input-derived luminance channel ($L$). While effective on standard benchmarks, this fixed-luminance design restricts brightness changes and becomes unreliable when grayscale formation deviates from natural-image luminance, as in historical orthochromatic photography. We propose a luminance-agnostic colorization framework that formulates colorization as full-RGB image editing using a foundation image-editing model. To bridge modern panchromatic and historical orthochromatic conditions, we introduce a mixed grayscale objective that trains the model under both standard luminance grayscale and a red-insensitive grayscale formation. Experiments on COCO, ImageNet, and a multi-instance benchmark show that our method is competitive on standard grayscale inputs and substantially more robust under orthochromatic inputs, with qualitative comparisons and a human study indicating fewer visible color artifacts.

---


### 132. [BPG: Balancing Plasticity and Generalization for Domain Incremental Learning](https://arxiv.org/abs/2608.10804)

**<font color=#1a73e8>作者：</font>** Qiang Wang, Songlin Dong, Shaokun Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks excel in various tasks but struggle to generalize across evolving data distributions, leading to significant performance degradation under domain shifts. Domain incremental learning (DIL) addresses this challenge by enabling models to continuously adapt while retaining prior knowledge. Among existing DIL approaches, the parameter-isolation paradigm achieves state-of-the-art performance. However, these methods often adopt a one-size-fits-all approach to adapt to new domains, resulting in either insufficient learning capacity or redundant parameters. In this work, we propose BPG, a unified framework that addresses both challenges through two complementary components: BPG-Adapter, which dynamically determines each domain's adapter hidden dimension based on domain-specific feature separability, and BPG-Inference, a soft domain mixture strategy that integrates multiple domain-specific models at test time, mitigating domain ID misselection. Experimental results on DomainNet, CDDB, and CORe50 demonstrate that BPG consistently outperforms uniform adapter-based approaches and hard domain selection strategies, achieving state-of-the-art average accuracy while reducing forgetting to as low as 0.22% on DomainNet.

---


### 133. [Fast and Memory-Efficient Wavelet Convolutions via I/O-Aware Reformulation](https://arxiv.org/abs/2608.10805)

**<font color=#1a73e8>作者：</font>** Amit Aflalo, Shahaf E. Finder, Roy Amoyal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wavelet convolution (WTConv) has emerged as an increasingly popular drop-in replacement for standard convolutions, expanding a network's receptive field exponentially with the number of decomposition levels while keeping the parameter count linear. However, its reference implementation is severely memory-bound due to excessive data movement through high-bandwidth memory (HBM). We develop an I/O model of WTConv to characterize this bottleneck and use it to guide three algebraic reformulations: (1) recomputing the inexpensive Haar analysis butterfly on chip, (2) collapsing the multi-level synthesis cascade into a single closed-form pass indexed by output-coordinate bits, and (3) folding learned per-channel scales into the convolution weights. Together, these reformulations enable an I/O-aware fused implementation that substantially reduces HBM traffic. We evaluate the WTConvNeXt configuration across decomposition levels and a broad range of tensor shapes. Despite performing comparable arithmetic, the reference WTConv is substantially slower than the depthwise convolution it replaces. Our reformulation reduces modeled HBM traffic by approximately $2.55\times$, yielding up to a $4.35\times$ training speedup over the reference while roughly halving peak memory usage. Thus, our reformulation preserves the benefits of WTConv while substantially reducing its execution time and memory footprint, removing the systems overhead that previously limited its practical efficiency.

---


### 134. [Modelling Geographic Atrophy Progression using Implicit Neural Representations](https://arxiv.org/abs/2608.10807)

**<font color=#1a73e8>作者：</font>** Simone Sarrocco, Paul Friedrich, Florentin Bieder 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Age-related Macular Degeneration (AMD) is the major cause of blindness in the Western world. Its late dry phase is characterised by irreversible atrophic areas, namely Geographic Atrophy (GA). Longitudinal Fundus Autofluorescence (FAF) image acquisitions are currently the main tool for assessing lesion growth over time at the image level. However, due to its highly individualised progression, the evolution of late AMD remains poorly understood. In this work, we propose using Implicit Neural Representations (INRs) to model GA progression at the individual level in a low-data setting. Our approach generates both FAF and GA segmentation at both past and future time points. Among the comparison models, our method achieves competitive segmentation quality across different scenarios, yielding the lowest Mean Absolute Error (MAE) for the GA lesion area and the highest DICE score, without sacrificing FAF image quality. The code is available at this https URL.

---


### 135. [Surfacing the Unsaid: CUE-Bench for Affective Stance in Chinese Discourse](https://arxiv.org/abs/2608.10810)

**<font color=#1a73e8>作者：</font>** Zhenyan Zheng, Yunyao Zhang, Junxi Sheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion understanding in discourse requires reasoning beyond surface sentiment because speakers often convey affect through indirect, implicit, polite, ironic, or deliberately mismatched expressions. Existing emotion benchmarks mainly annotate surface polarity or final emotion categories, while lacking a structured account of how explicit expression, implicit affect, pragmatic intent, and fine grained emotion interact. This limitation makes current evaluations insensitive to cases where affective meaning is concealed, weakened, inverted, or pragmatically reshaped, thereby obscuring model failures in deeper emotion understanding. To address this gap, we introduce CUE Bench, a Chinese Unsaid Emotion benchmark that centers on Affective Stance and covers diverse communicative scenarios. CUE Bench constructs nine human interpretable affective stances from explicit implicit polarity interaction and further provides intent and fine grained emotion annotations for structured affective inference. Experiments show that incorporating Affective Stance improves fine grained emotion recognition by 3.5 percentage points and pragmatic intent detection by 7.8 percentage points over strong baselines.

---


### 136. [AI-Generated Interactive Fiction for Educational Use: A Pilot Study of Perceived Comprehensibility, Coherence, and Engagement](https://arxiv.org/abs/2608.10818)

**<font color=#1a73e8>作者：</font>** Finn Rogosch, Andreas Schrader  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence (AI) can produce educational content at scale, including interactive and narrative learning experiences, but technical generation alone is not sufficient: scenarios that are confusing, narratively inconsistent, or unengaging are unlikely to be useful in practice. This paper presents a pilot user-centred evaluation of AI-generated interactive fiction (IF) for educational use in higher education. Using a previously described domain-agnostic pipeline and a shared STEM content base, we generated a controlled pool of scenarios and asked participants (N = 22, STEM higher-education) to play one generated episode and rate it on narrative clarity, story-content coherence, engagement, and length acceptance. A free-text prompt captured open feedback. Narrative clarity and length acceptance were rated positively, engagement sat near the neutral mid-point of the scale, and story-content coherence was the weakest dimension by a clear margin. Qualitative feedback points to quiz integration as the bottleneck. Artificial in-fiction motivation for quiz prompts and abrupt setting changes were reported. Feedback also pointed to missing story-level consequences for wrong answers. From these observations, we derive concrete design implications that can inform larger follow-up studies, including later work on learning effectiveness.

---


### 137. [The GENEA Challenge 2026: A Large-Scale Disentangled Evaluation of Speech-Driven Gesture Generation on the Seamless Interaction Dataset](https://arxiv.org/abs/2608.10839)

**<font color=#1a73e8>作者：</font>** Rajmund Nagy, Silvia Arellano García, Hendric Voss 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This preprint presents the results of the fourth GENEA Challenge, a large-scale human evaluation of five speech-driven gesture-generation systems trained by participating teams on the Seamless Interaction dataset of dyadic conversations. As in the 2023 GENEA Challenge, we used a disentangled evaluation methodology to assess motion quality and speech alignment without confounding between the two, and performed a dyadic mismatching study to isolate the effect of listening and reacting to the interlocutor. We additionally introduce a new semantic gesture-generation task and a text-mismatching evaluation methodology using the Grounded Gestures subset of the data. In total, we ran four large-scale user studies, collecting over 23,000 votes from 869 test-takers.
In the motion-realism study, the dataset's filtered segments had substantially higher motion quality than all challenge submissions (68-95% pairwise winrate). In the speech-alignment study, the motion-capture segments provided a conceptual ceiling at 62% alignment score, with the top submission significantly behind at 32% and the rest only slightly above the 0% expected of an input-independent system. In the dyadic study, motion capture again set the ceiling at 65% appropriateness score, but no submission scored substantially above chance, indicating that the systems could not yet respond to the interlocutor. Finally, the semantic mismatching evaluation found highly expressive gestures in the dataset (test-takers identified the matching transcript 79% of the time), yet almost all submissions failed to generate semantically expressive motion, with the best achieving only an 8% appropriateness score.
The collected votes and outputs will be made publicly available at this https URL to facilitate reproducibility and further research.

---


### 138. [FiGuRO: Intrinsic Dimension Estimation for Multi-Modal Data](https://arxiv.org/abs/2608.10857)

**<font color=#1a73e8>作者：</font>** Viktoria Schuster, Sana Tonekaboni, Caroline Uhler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Determining the complexity, or Intrinsic Dimension (ID), of data is fundamental to efficient and interpretable representation learning. This is particularly challenging in multi-modal settings when trying to learn disentangled representations for shared and private information. Existing techniques leave a critical gap: they are often static, uni-modal, or in the case of contrastive methods, adapt only to the shared ID implicitly. We introduce Fidelity-Guided Rank Optimization (FiGuRO), a framework for approximating the ID of uni- and multi-modal data under constraints of model capacity and hyperparameters. FiGuRO learns the dimensions of low-rank projections using truncated singular value decomposition and an algorithm that determines when to reduce or increase dimension and in which latent space. Disentanglement of shared and private information arises as an emergent property of this optimization, eliminating the need for complex auxiliary loss functions. We demonstrate that FiGuRO outperforms existing ID estimation techniques and is more robust to hyperparameter changes. Across simulations and real-world data, FiGuRO captures distinct ID scales and varying subspace ratios, and decomposes shared and private information successfully. Furthermore, we show that FiGuRO can be applied to modern uni-modal pretrained models, enabling efficient, post-hoc disentanglement of multi-modal representations.

---


### 139. [Optimistic Rates for Multiclass PAC Learning](https://arxiv.org/abs/2608.10869)

**<font color=#1a73e8>作者：</font>** Xiaoyu Li, Andi Han, Jiaojiao Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Worst-case multiclass bounds do not become smaller when the best classifier is already nearly correct: what is missing is an optimistic rate, a guarantee whose fluctuation scales with the oracle risk itself. For a class of Natarajan dimension $d_N$ and Daniely-Shalev-Shwartz dimension $d_{DS}$, the optimal excess risk is known at the two endpoints ($d_{DS}/n$ realizable, $\sqrt{d_N/n}+d_{DS}/n$ agnostic [HMZ24, CEH+26, Pab26]) and open in between. We close the gap: at every fixed oracle risk $L^\star$, the optimal excess risk is $\widetilde{\Theta}(\sqrt{L^\star d_N/n}+d_{DS}/n)$, uniformly in the alphabet size, attained by a learner that knows neither $L^\star$ nor the confidence level. The upper bound composes the cover-menu-compression architecture of [CEH+26], at the realizable rate of [Pab26], with a new comparator-facing relative compression theorem: a size-$k$ compression rule that empirically dominates a comparator $h$ has population risk at most $L(h)+O(\sqrt{L(h)\Gamma}+\Gamma)$ with $\Gamma=(k\log n+\log(1/\delta))/n$, without stability; this transfers the comparison principle of the sharp binary theory [MQZ26] while discarding its Boolean-cube geometry, which does not lift to multiclass labels. The lower bound forces both terms using one class and one distribution at every fixed $L^\star$, by a pair-Assouad scheme calibrated to $L^\star$ and a fiber argument on the pseudo-cubes underlying the Natarajan-versus-DS separation of [BCD+22]. Both theorems extend to list learning: against the best $r$-tuple of hypotheses, the same architecture and the same two engines yield an optimistic rate and a lower bound of the same shape, forcing the fluctuation term that [Pab26] expected to be necessary against list comparators, and removing the factor $r$ from the known realizable list lower bound.

---


### 140. [X2-Turn: Frame-Synchronous Dual-Head Modeling for Joint Streaming ASR and Turn State Prediction](https://arxiv.org/abs/2608.10878)

**<font color=#1a73e8>作者：</font>** Kaiqi Fu, Rime Wen, Altman Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accurate and responsive turn-taking is essential for spoken dialogue systems, which must distinguish in real time between user interruptions, backchannels that should be ignored, and the completion of an utterance. Prior modular approaches typically optimize turn state prediction at the utterance or fixed-chunk level, creating a mismatch with the continuous turn state estimate, and often depend on an auxiliary ASR model, which limits responsiveness and increases overall system complexity. Therefore, we present X2-Turn, a frame-synchronous turn state prediction method via delayed-stream modeling. Specifically, building on the pretrained Voxtral Realtime model, we introduce a frame-synchronous turn state head that operates in parallel with the ASR head on shared streaming representations, jointly predicting ASR tokens and fine-grained turn states at the frame level. We evaluate our method on the bilingual Chinese-English Easy-Turn test sets, and the results demonstrate its effectiveness in achieving accurate turn-taking detection while maintaining low latency.

---


### 141. [Enhanced Filtering Algorithms for the Euclidean Traveling Salesperson Problem and its variants in Constraint Logic Programming](https://arxiv.org/abs/2608.10881)

**<font color=#1a73e8>作者：</font>** Alessandro Bertagnon, Marco Gavanelli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Traveling Salesperson Problem (TSP) is one of the best-known problems in computer science and arises in many engineering applications, such as smart vehicles and intelligent transportation systems. In the "Euclidean" case, each node is defined by its coordinates in the plane and distances are computed using the Euclidean metric. In the Constraint Programming (CP) literature, the Euclidean TSP is typically addressed by computing the full distance matrix and treating it as a general case; however this approach ignores the geometric information carried by the points' coordinates. In this work, we propose new filtering algorithms, implemented in Constraint Logic Programming (CLP), that exploit such geometric information to achieve stronger constraint propagation than existing approaches. Moreover, we show how this methodology can be extended to other Euclidean variants of the TSP, including the Euclidean Generalized Traveling Salesperson Problem (EGTSP), which is relevant in practical routing and logistics applications. Experimental results demonstrate the computational advantages of the proposed approach.

---


### 142. [GESTO: Human-Centric Spatio-Temporal Memory for Reasoning in Dynamic Scenes](https://arxiv.org/abs/2608.10886)

**<font color=#1a73e8>作者：</font>** Ermanno Bartoli, Buwei He, Dennis Rotondi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robots operating in human environments need memories that capture not only what objects exist and where, but also how people use them over time and how individual interactions compose into goal-directed activities. Existing 4D scene graphs preserve object and place histories but omit activity structure, whereas activity representations are either not grounded in persistent 3D scenes or rely on externally provided event boundaries and object associations. We present GESTO (Grounded Event and Spatio-Temporal memOry), a spatio-temporal memory that couples a persistent 4D scene graph with a two-level hierarchy of atomic human--object interactions and goal-driven events. From an RGB-D observation stream, GESTO automatically extracts timestamped interactions, grounds them to persistent scene entities, groups them into events, and uses event context to refine uncertain object associations. A relation-aware tool-calling agent queries the resulting memory for activity-centric spatio-temporal reasoning. We evaluate GESTO on the reproducible text, binary, and time categories of an existing benchmark, together with 40 new Space2Event and Event2Space queries. GESTO achieves scores of 0.71, 0.75, and 0.70 on the standard categories, approaching a method supplied with ground-truth event and object grounding, while substantially outperforming the same reasoning framework when these inputs are removed. It further achieves 0.73 and 0.75 on Space2Event and Event2Space queries. Ablations show that hierarchical event structure and context-aware grounding refinement provide complementary benefits, supporting activity-grounded hierarchical memory for retrospective reasoning in dynamic human environments.

---


### 143. [Sensor-Informed Per-Point Covariance for Structured-Light 3D Imaging](https://arxiv.org/abs/2608.10888)

**<font color=#1a73e8>作者：</font>** Sehoon Tak, Jae-Sang Hyun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Per-point uncertainty models are important in structured-light 3D reconstruction for probabilistic registration, fusion, and quality assessment. In practice, however, point-cloud covariances are often modeled as isotropic constants or inferred from local surface geometry and therefore do not explicitly reflect the measurement process. This is a limitation in fringe projection profilometry (FPP), where phase noise propagates through calibrated reconstruction and produces strongly anisotropic 3D uncertainty. This paper presents a sensor-informed first-order method for constructing a per-point 3 x 3 covariance field from experimentally measured phase precision and calibrated phase-to-depth and phase-to-3D mappings. The formulation separates a rank-1 phase-induced covariance from an effective full-rank completion obtained by incorporating fitted lateral image-space perturbation scales. Repeated-plane experiments under fixed imaging conditions show close alignment of the dominant covariance direction with the viewing ray, and consistency between the dominant phase-induced uncertainty scale and scalar depth uncertainty. In G-ICP registration, the proposed covariance substantially improves over a constant isotropic model while providing a sensor-derived uncertainty representation complementary to conventional geometry-based covariances.

---


### 144. [Benchmarking Time Series Generation Methods for Privacy-Preserving Forecasting](https://arxiv.org/abs/2608.10891)

**<font color=#1a73e8>作者：</font>** Luis Amorim, Vitor Cerqueira, Moises Santos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting in privacy-sensitive domains often requires training models on released data rather than original observations. Synthetic time series generation has been developed primarily for data augmentation, where generated series supplement the original training set. How well these methods perform when fully replacing the original data - and how much privacy risk the released series carry - remains underexplored. We address this gap through a benchmark evaluating synthetic generation methods and noise-based anonymization baselines under a Train on Synthetic, Test on Real (TSTR) protocol. We jointly assess forecasting performance and distance-based empirical privacy risk across seven datasets, characterizing the trade-off between these objectives. We also introduce Grasynda-P, a privacy-motivated extension of the graph-based generator Grasynda, incorporating matrix ensembling and kernel density estimation. Our results show that: (1) no generation method fully substitutes for original training data; (2) noise-based anonymization yields the strongest privacy but the worst forecasting performance; (3) simple transformation-based generators outperform deep generative models for forecasting in this setting; and (4) Grasynda-P lies on the Pareto frontier, achieving competitive forecasting with stronger privacy separation than other generators. This benchmark establishes a reference point for evaluating and developing new privacy-aware synthetic time series generation methods.

---


### 145. [Certify or Refuse: A Cross-Model Map for Selective Risk Control with Coverage Floors under Covariate Shift](https://arxiv.org/abs/2608.10893)

**<font color=#1a73e8>作者：</font>** Jiamiao Liu, Dewen Qiao, Yu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Certified selective predictors attain whatever coverage they attain; operators impose an automation floor: answer at least a $\beta$-fraction of shifted target traffic with at most an $\alpha$-fraction of answers wrong. Under bounded-ratio covariate shift we prove the Floor Certification Map: once that floor must be certified alongside the selection-conditioned risk $\alpha$, certification acquires a feasibility frontier and a two-resource complexity map, additive up to constants: risk in labeled source, the floor in unlabeled target samples. The rates are local, needing a regular frontier margin, slack below the local-regime threshold, and lattice conditions: pre-registered with a lattice margin for the upper bounds, compatible per-slack for the lower. The displayed split is the operational route; oracle weights also allow a labeled-source floor estimate. Three model-tagged results: a lower bound (Model-B), a matching oracle-weight upper bound (Model-A), and an implementable upper bound (Model-B') valid under a pre-registered exact stratified-shift model with nuisance cost priced explicitly. The match is across these models rather than a single-model minimax theorem, and necessarily so: over the full bounded-ratio class no unknown-weight procedure matches at any sample size (Model-B is inconsistent, witnessed at $\alpha=\beta=1/2$). The nuisance's necessity is only partially settled. Complexity tracks a localized accepted-region functional, not global effective sample size (ESS), on both sides, though a fixed-ESS separation theorem is left open; both lower-bound axes vanish as $\beta\to0$, so the floor creates the map. Empirically, the registered bite family diverges with log-log slope $-2.002$ within its pre-registered band; a 1,024-cell audit records 0 violations where the formal certificates fire; and a single-corpus SQuAD-to-NewsQA feasibility audit returns honest refusal.

---


### 146. [Partially Observable Learning for Multi-Platform Dispatch Optimization](https://arxiv.org/abs/2608.10897)

**<font color=#1a73e8>作者：</font>** Fengming Yao, Man Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Instant delivery platforms have become a critical component of urban logistics, increasingly relying on crowdsourced couriers to fulfill highly dynamic orders. In real-world systems, couriers are not exclusive to a single platform and may concurrently serve multiple platforms, while each platform can only observe its own orders and couriers' interactions due to privacy and operational constraints. This results in a multi-platform dispatch environment with inherent partial observability. However, most existing works on dispatch optimization assume full courier observability and mandatory assignment acceptance, causing substantial performance degradation when deployed in realistic multi-platform settings. In this paper, we propose POLO, a partially observable multi-agent reinforcement learning framework for dispatching optimization in multi-platform instant delivery systems. POLO firstly models each platform-grid pair as an independent agent that learns dispatch policies solely from platform-local observations, aligning the learning process with real-world privacy and operational constraints. To support effective decision-making under incomplete and heterogeneous courier information, POLO introduces a novel attention-based policy representation that selectively aggregates inter-courier information. Moreover, we design a counterfactual reward shaping mechanism to mitigate the non-stationarity induced by joint actions across grids, leading to more stable and scalable learning. We develop a high-fidelity simulator to evaluate dispatch performance under varying numbers of platforms and system scales. Extensive experiments demonstrate that POLO consistently outperforms strong baselines in terms of platform revenue and courier travel efficiency, highlighting its robustness and effectiveness in realistic multi-platform settings.

---


### 147. [VIDS-Seg: Towards Reliable Uncertainty Quantification in Pediatric Cardiac Ultrasound Segmentation](https://arxiv.org/abs/2608.10903)

**<font color=#1a73e8>作者：</font>** Paul Fischer, Ece Ozkan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable clinical deployment of machine learning requires models that know when they are likely to fail, particularly for subgroups underrepresented in training data. A common case is pediatric care, where models trained on adult cohorts can silently under-perform on children with no indication that something has gone wrong. As retraining with labeled pediatric data is often infeasible, detecting such failures at inference time is a critical clinical need. Building on the VIDS (Variational Inference under Distribution Shifts) framework, we introduce VIDS-Seg, which applies amortized variational inference over a lightweight prediction head to make this adaptive, OOD-aware prior tractable for dense image segmentation. We evaluate VIDS-Seg on left ventricular segmentation in echocardiography, a setting where pediatric anatomy differs systematically from the adult population most segmentation models are trained on, training on an adult cohort (EchoNet-Dynamic) and evaluating zero-shot on a pediatric cohort (EchoNet-Pediatric). Across all age strata, VIDS-Seg matches competitive baselines in segmentation accuracy while producing substantially higher spatial correspondence between predicted uncertainty and segmentation error, an advantage that persists even after applying temperature scaling to all baselines. Downstream, it yields more accurate and stable ejection fraction estimates and more reliable detection of cardiac malfunction in the infant subgroup. Our results indicate that OOD-aware uncertainty quantification can serve as a practical safety layer for deployed segmentation models, enabling detection of silent failures in underrepresented subgroups without retraining or additional labeled data.

---


### 148. [ComBodied Agents: a New Paradigm of Human-Centric Agentic AI](https://arxiv.org/abs/2608.10915)

**<font color=#1a73e8>作者：</font>** Qianggang Ding, Xingyao Wang, Rui Feng 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> After an older adult misses a medication dose, a software agent can send another reminder and an embodied agent can bring the medication. Yet neither explains whether the person forgot, is confused, has side effects, or deliberately refused, nor what support is appropriate. This reveals a structural gap in Agentic AI: Digital Agents primarily transform software states, while Embodied Agents transform physical states; neither makes a person's evolving state and agency the primary object of modeling, intervention, and evaluation. We introduce Combodied Agents, a human-centered paradigm that perceives, models, predicts, and supports individual human-state trajectories over time, using software tools, sensors, wearables, robots, and human services as action channels rather than end goals. We unify fragmented capabilities across personal assistants, health agents, AI companions, and adaptive human--AI systems into a closed loop: event-based multimodal perception reconstructs meaningful personal events; longitudinal, correctable memory provides temporal context; Personal World Models estimate future personal states and outcomes under alternative decisions and interventions; and an admissible intervention policy selects proportionate support under consent, uncertainty, safety, reversibility, and user control. Feedback from the person and environment updates the loop. Rather than requiring an exhaustive Human Digital Twin, the framework uses purpose-bounded, uncertainty-aware, user-correctable representations. We organize the design space by human-state targets, relational contexts, and agent roles, and propose scenario-centered evaluation, agency-preservation metrics, benchmark requirements, edge-native personal models, and governance directions. Combodied Agents shift Agentic AI from external task completion toward sustained human benefit.

---


### 149. [FedCGR: Federated Cross-Domain Generative Recommendation](https://arxiv.org/abs/2608.10929)

**<font color=#1a73e8>作者：</font>** Zhuodong Liu, Hugen Lv, Xiangyu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cross-domain recommendation (CDR) transfers preference knowledge across related domains, but federated deployment makes cross-domain alignment difficult because the behavioral anchors that align item spaces, such as overlapping users and shared interaction signals, are often sparse, unavailable, or privacy-sensitive across clients. To address this tension, we revisit federated CDR as generation over a stable semantic item language. By representing items as discrete semantic ID (SID) sequences derived from public item-side metadata, cross-domain item alignment is induced by a shared vocabulary rather than by exchanging private interactions or aligning domain-specific embeddings. Directly federating SID-based generators, however, introduces two design constraints: the SID tokenizer must remain fixed to preserve cross-client token consistency, which creates a semantic-only bottleneck because local collaborative filtering (CF) signals cannot be globally shared or aligned; meanwhile, standard federated averaging can cause negative transfer under domain heterogeneity. To overcome these constraints, we propose FedCGR, a federated generative CDR framework that keeps the item language stable and makes adaptation explicit. FedCGR injects local CF evidence through a reliability-aware semantic interface and trains a prototype-personalized generator that selectively aggregates shared parameters according to domain relatedness while keeping domain-specific quantities local. Experiments on six Amazon cross-domain scenarios show that FedCGR consistently outperforms federated generative baselines and achieves competitive performance against strong sequential and federated CDR methods under both full-ranking and sampled evaluation protocols.

---


### 150. [GS-CPE: Unified 6-Degree-of-Freedom Camera Pose Estimation via 3D Gaussian Splatting](https://arxiv.org/abs/2608.10938)

**<font color=#1a73e8>作者：</font>** Huaiyuan Weng, Chul Min Yeum, Su-Min Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite substantial progress in visual localization, from scene coordinate regression to direct camera pose regression, achieving both robust generalization and high accuracy remain challenging. This study introduces GS-CPE (Gaussian Splatting based Camera Pose Estimation), a coarse-to-fine framework for 6-DoF camera pose estimation that unifies geometry-based coarse pose estimation with robust 3D Gaussian Splatting (3DGS) warping based pose refinement. GS-CPE first estimates a coarse pose via retrieval-guided geometric pose estimation on a 3DGS scene representation, then refines it by minimizing a visibility aware masked RGB warping objective in a multi-scale optimization framework, with adaptive re-rendering. Extensive experiments on indoor and outdoor benchmarks including 7Scenes, Cambridge Landmarks, FAST-LIVO2 datasets, and a custom dataset demonstrate state-of-the-art performance, consistently outperforming in both accuracy and generalization.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-189](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
