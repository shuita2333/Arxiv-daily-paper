# 📦 其他研究 | 2026年08月10日

> 本类共 **167** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-167**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-167**

---

### 151. [Residual Algebra for Representation-Preserving Learning](https://arxiv.org/abs/2608.07349)

**<font color=#1a73e8>作者：</font>** Yao Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning from heterogeneous representations is usually reduced to feature concatenation, which erases which representation produced an error. We instead algebraize the residual: a representation is a typed object that owns both a coordinate system and the residual it leaves unresolved, and learning is an ordered composition of operators that preserve or deliberately erase that type. Fold realizes the objects as point-in-time conditional-mean fields on 10x10 rank grids. FPRC-PQ realizes the algebra as relax-aggregate-close: each field is relaxed by a correction fitted to its own residual in its own coordinates; corrected fields meet at a fixed mean that is the sole identity-erasure boundary; and a shared learner closes only the aggregate's fresh residual. The composition telescopes exactly into representation, local residual estimate, and residual-of-residual estimate. Its aggregate is a learned control-variate interface with population variance reduction, while refitting the closer along perturbations of the backbone yields first-order coupled-path mean orthogonality. As an analytical extension, a reflective rumination operator reads the displacement of a global reconstruction from the aggregate anchor, reflects it, and fixes its gain by a unique orthogonal projection rather than return-tuned grid search. On 3.67M Chinese A-share stock-day observations (2023-2026) under a frozen point-in-time protocol, the evaluated base algebra raises net-of-cost return from 13.52% to 19.10% and Sharpe from 1.42 to 2.09. Matched-capacity, unified-residual, identity-free two-stage, and pairwise-only controls all trail it. The gain is therefore not explained by more features or more trees, but by making residual ownership and composition explicit while representation identity is still available.

---


### 152. [QFCQT: A Chaotically Gated Quantformer Framework for Volatile Time-Series Forecasting](https://arxiv.org/abs/2608.07363)

**<font color=#1a73e8>作者：</font>** Junkai Lin, Siqi Hou, Raymond Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Forecasting non-stationary time series remains difficult due to long-range dependencies, local volatility bursts, structural shifts, and nonlinear oscillatory behaviors. Although Transformer-based forecasters are effective for modeling long-term temporal dependencies, their feed-forward blocks typically rely on smooth static activations that are insufficiently sensitive to abrupt regime changes. Motivated by quantitative Transformer designs and oscillator-based nonlinear activations, we propose QFCQT, short for Quantum-Fractal-inspired Chaotically Gated Quantformer, for robust forecasting under complex volatile dynamics. Here, "quantum-fractal-inspired" denotes a computational analogy based on soft oscillator superposition and multi-scale nonlinear responses, rather than a formal quantum-mechanical or fractal-theoretic derivation. QFCQT consists of three main components: (1) a Quantformer-style numerical encoder that directly processes multivariate inputs via linear embedding; (2) a learnable Lee-oscillator activation module that maps scalar pre-activations to dynamic oscillatory responses and summarizes them through Max-over-Time pooling; and (3) a smooth-chaotic gated fusion mechanism that adaptively balances conventional smooth activations and chaos-sensitive responses. Furthermore, instead of using a single fixed oscillator, QFCQT employs a soft superposition of eight parameterized Lee oscillator families to adaptively capture different nonlinear response patterns across regimes. Experiments on ETTh1, ETTh2, and A-share Stock Index benchmarks show that QFCQT consistently outperforms strong baselines, including Informer, LogTrans, LSTMa, HAT, and COTN.

---


### 153. [Beyond Call and Response: Modelling Reciprocal Coordination in Human-AI Vocal Ensembles](https://arxiv.org/abs/2608.07376)

**<font color=#1a73e8>作者：</font>** Polina Proutskova  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Musical interaction with AI is often organised as a response loop: a human performs, the system interprets that action, and the system answers, accompanies, or schedules a musical event. Unconducted vocal ensembles pose a different problem. Singers act simultaneously and continuously affect one another; neither timing nor pitch is fixed by a conductor, metronome, accompaniment, score, or tuning source. Collective organisation emerges from many-to-many reciprocal adjustment. This paper frames such ensembles as coupled dynamic systems and proposes a research architecture for vocal agents that enter, rather than merely track, their collective states. Some target repertoires are metrical, while others exhibit non-isochronous temporal contours that cannot be reduced to a beat grid; we treat the latter as a hard case for a general framework. The architecture connects multichannel capture in the field to dialect- and singing-aware representation, collective-state inference, vocal generation, and in-situ evaluation. The resulting agenda asks not only whether an artificial singer can synchronise, but how its presence reorganises human coordination, leadership, style, and musical transmission.

---


### 154. [SkySeaLand: A Wide-Format Satellite Transportation Benchmark with an Ultra-Lightweight Detection Baseline](https://arxiv.org/abs/2608.07382)

**<font color=#1a73e8>作者：</font>** Md. Zahid Hasan Riad, Md Sultanul Islam Ovi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Satellite object detection is challenged by small targets and wide-format scenes that lose detail under standard square-input resizing. We introduce SkySeaLand, a public dataset of 1,307 high-resolution satellite images and 19,101 verified bounding boxes across airplane, boat, car, and ship classes in terrestrial and maritime scenes. Native COCO and YOLO annotations are provided. The collection is dominated by large source images and wide scene geometry: 84.5 percent exceed 3,836 pixels on the longest side and 73.1 percent are near a 3:1 aspect ratio. We evaluate twelve detectors from the YOLO, RT-DETR, DETR, and Faster R-CNN families using a common split and COCO metrics. The tested YOLO and RT-DETR variants obtain 84.4--88.2 mAP50, with no consistent accuracy gain from larger parameter counts under the reported model-specific recipes. We also report SkyDet, a 1.22 M parameter anchor-free baseline that obtains 60.5 mAP50 and 24.32 mAP50-95 in a 4.90 MB footprint, with 13.74 ms latency (72.8 FPS) on a Tesla T4. SkySeaLand provides a compact benchmark for mixed land--maritime transportation detection, while SkyDet establishes a documented low-footprint reference rather than a state-of-the-art accuracy claim.

---


### 155. [Omni-modal decomposition autoencoders learn full-stack wearable disentangled representations](https://arxiv.org/abs/2608.07385)

**<font color=#1a73e8>作者：</font>** Ioannis Ziogas, Ensieh Khazaei, Bilal Taha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning disentangled representations is a key requirement for developing versatile, general-purpose, and sustainable models in multi-modal wearable computing. However, existing approaches do not operate as full-stack wearable processors, i.e., they do not simultaneously address task-specific classification performance, disentangled and interpretable representation learning, fusion, and generative modeling of highly heterogeneous multi-modal time series. To address this gap, we introduce Omni-modal Variational Decomposition Autoencoders (OmniDecVAEs), a framework that efficiently learns multi-purpose representations in a unified and scalable manner from arbitrarily many modalities. OmniDecVAEs extend DecVAEs by learning modality-conditioned time-frequency latent subspaces through a multi-view self-supervised decomposition loss and a shared asymmetric autoencoder (AE) architecture. Results on a challenging omni-modal human activity recognition (HAR) setting with up to thirty modalities, demonstrate the ability of OmniDecVAEs to learn full-stack wearable representations. When compared to transformer-based and VAE-based methods, OmniDecVAEs full-stack disentangled representation properties lead to accuracy improvements of 1.01% and 6.75% in activity and identity recognition, respectively. Furthermore, OmniDecVAEs synthesize realistic omni-modal time-frequency data that manifest with enhanced reconstructions (mean absolute error improves by 76.84%) and distributional similarity between real and synthetic data (maximum mean discrepancy improves by 13.85%). Our results highlight OmniDecVAEs potential as a lightweight model suitable for intelligent edge wearables and clinical healthcare, unifying processing requirements and abilities in a single model, through its enhanced representational capacity, modality-invariant spatial complexity (4.1M parameters), and real-time latency.

---


### 156. [FedDOSE: Federated Learning Framework Decomposing Site Effects for Modeling Brain Dynamic Functional Connectivity](https://arxiv.org/abs/2608.07393)

**<font color=#1a73e8>作者：</font>** Deepank Girish, Yi Hao Chan, Yubin Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Functional Magnetic Resonance Imaging ( fMRI ) data are often pooled into collaborative multi-site consortia, as deep learning models for analyses require large datasets to generalize well. While Federated Learning (FL) offers a privacy-preserving paradigm for collaborative training, standard approaches continue to struggle with statistical heterogeneity. In particular, site differences pose a key challenge in multi-site data settings. Additionally, existing FL approaches for fMRI rely on static Functional Connectivity ( FC), omitting dynamic information in brain networks. To address this, we propose FedDOSE, a novel framework that explicitly decomposes site differences for analysis of dynamic FC (dFC). FedDOSE introduces a Modularity-Guided Tucker Decomposition block to encode high-dimensional dFC tensors and capture modular-level spatio-temporal patterns efficiently. Class-specific prototypes are generated across all sites and subsequently aligned at the global level by using a combination of Optimal Transport (OT) barycenter formulation and Procrustes analysis. Extensive experiments for diagnosing Autism Spectrum Disorder (ASD) and Attention-Deficit Hyperactivity Disorder (ADHD) on three multi-site resting-state fMRI datasets: ABIDE-I, ABIDE-II, and ADHD-200, demonstrate that FedDOSE outperforms state-of-the-art methods in ASD and ADHD detection. Our results highlight its effectiveness in learning robust representations from multi-site datasets for reliable analysis.

---


### 157. [FinRank: An Evidence-Grounded Benchmark for Financial Question Answering and Retrieval over SEC Filings](https://arxiv.org/abs/2608.07400)

**<font color=#1a73e8>作者：</font>** Sasan Mansouri, Daniel Saad, Mark Wahrenburg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial question answering is typically evaluated by answer correctness, yet in SEC filings a plausible and even numerically correct answer can be grounded in the wrong evidence. Similar facts and disclosures recur across sections of a filing, across reporting periods of the same firm, and across comparable firms. FinRank targets this provenance-sensitive retrieval problem by requiring systems to identify evidence for the intended entity, reporting period, and disclosure context. The benchmark contains 1185 manually authored question-answer records over the 10-K and 10-Q filings of 22 companies. Each record includes a reference answer, gold supporting passages, and hand-curated hard negatives drawn from confusable passages within filings, across reporting periods, and across comparable firms. FinRank evaluates passage retrieval, reranking, and hard-negative discrimination as separately measured tasks. Baseline results demonstrate the difficulty of this setting: among the evaluated systems, even a 7B instruction-tuned embedder reaches only 44.8% Recall@10 on the pooled evidence corpus; sub-billion-parameter encoders gain at most 3.5 points over BM25, a finance-adapted embedder trails BM25 by 9.7 points, and pairwise accuracy falls by 13.0-20.5 percentage points when random negatives are replaced with the curated hard negatives. FinRank provides an evidence-first benchmark for developing financial question answering systems that are not only accurate but also grounded in the correct disclosure.

---


### 158. [GeoDistill-Refine: Silhouette-First Geometry Distillation for Annotation-Free Spacecraft Segmentation](https://arxiv.org/abs/2608.07405)

**<font color=#1a73e8>作者：</font>** Yonglong Zhang, Zongwu Xie, Yang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation segmentation models can provide supervision for spacecraft imagery without manual training masks, but their predictions vary with textual prompts and may contain geometric errors that are amplified during distillation. This paper presents GeoDistill-Refine, a two-stage framework that transfers offline SAM 3 pseudo-masks to a compact segmentation network. Six fixed prompts are fused by an unweighted 50% vote to stabilize the teacher output. The student first learns the foreground silhouette and is then refined with signed-distance-field, skeleton, and area objectives derived from the pseudo-mask. A sample-level gate, computed from prompt agreement, the valid-prompt ratio, and pseudo-mask area plausibility, reduces the influence of unreliable pseudo-geometry. On the SpaceSense-Bench HJM lockbox set, GeoDistill-Refine improves Image IoU and Boundary F1 by 0.0456 and 0.1380, respectively, over a plain pseudo-label student. External evaluations on the SPEED+ Lightbox and Sunlamp domains and on TANGO show competitive regional overlap together with gains in boundary quality or foreground precision. The deployed TinyUNet contains 0.263 M parameters and requires approximately 1.1 ms per image on an RTX 4090; SAM 3 pseudo-mask construction and the auxiliary geometry branches are used only during training.

---


### 159. [Addressable Memory for Video World Models](https://arxiv.org/abs/2608.07408)

**<font color=#1a73e8>作者：</font>** Xindi Wu, Sven Elflein, James Lucas 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study visual persistence in interactive video world models. These models rely on a Key-Value (KV) cache as a growing visual memory to carry forward previously generated frames. However, we find that models can no longer reliably address stored content once rollouts extend beyond the training horizon, because temporal Rotary Positional Embeddings (RoPE) offsets then fall outside the range seen during training and the model struggles to retrieve the relevant visual information through attention. Moreover, naively compressing the cache in the RoPE-rotated space corrupts memory by averaging together incompatible positional phases. To address this, we propose WorldTrace, a training-free memory framework for long-horizon visual persistence. WorldTrace keeps compressed memory addressable by assigning each summary slot a distinct, in-distribution virtual position. Within this addressable cache, we study two memory compression approaches: WorldTrace-Field compresses history for temporal coherence, while WorldTrace-Landmark stores verbatim scene traces at detected transitions for episodic recall. We further introduce LoopBench, a benchmark evaluating whether a compressed cache can reconstruct a previously visited scene after a long detour. WorldTrace-Field improves temporal consistency by +15.5%, and WorldTrace-Landmark improves episodic recall by +19.5% on LoopBench, extending visually persistent generation without retraining.

---


### 160. [UniJEPA: A Unified Joint-Embedding Predictive Architecture for Task-Agnostic Visual World Modeling](https://arxiv.org/abs/2608.07409)

**<font color=#1a73e8>作者：</font>** An Lanji, Dawei Liu, Jin Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPAs) have emerged as a principled framework for self-supervised learning of world models in compact latent spaces, yet existing methods are fragmented: some predict masked parts of a single image in latent space (I-JEPA), others learn to predict global photometric transformations (Image World Models), while video-scale JEPAs predict future temporal states and are post-trained for action-conditioned planning (V-JEPA~2, DINO-World, DINO-WM). These objectives are treated as distinct recipes with separate encoders, predictors, and anti-collapse regularizers, hindering a single model from unifying image-level and video-level world modeling. We present UniJEPA, a unified JEPA that jointly learns photometric prediction (image-level transformations) and temporal prediction (video-level next-state dynamics) in one shared latent space. A single end-to-end objective, composed of a next-embedding prediction loss and a Gaussian regularizer, yields a provably anti-collapse encoder-predictor pair trainable from raw pixels without EMA, stop-gradient, or pre-trained encoders. We show that the same latent space supports controllable abstraction: photometric prediction learns invariant structure while temporal prediction learns equivariant dynamics. After action-conditioned post-training on offline trajectories, UniJEPA enables zero-shot planning by treating goal features as prediction targets. On image, video, and control benchmarks, UniJEPA matches or surpasses task-specific JEPAs while requiring a single loss hyperparameter, and plans up to tens of times faster than generative world models at comparable accuracy.

---


### 161. [Beyond Myopic World Models: Long-Horizon End-to-End Training for Direct Future Prediction](https://arxiv.org/abs/2608.07420)

**<font color=#1a73e8>作者：</font>** Xinyi Li, Zaishuo Xia, Chenjie Hao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models are expected to support imagination over extended temporal horizons, yet most are still trained through local few-step prediction objectives and deployed by recursively rolling out their own predictions. This creates a fundamental mismatch: few-step losses optimize local transition fidelity, while long-horizon prediction depends on how errors and gradients propagate through the entire trajectory. As a result, transitions with different downstream influence on the endpoint are treated uniformly during training, and small local errors are amplified through recursive inference. We argue that long-horizon accuracy is better achieved by optimizing directly, through an end-to-end endpoint prediction objective. To instantiate this paradigm, we introduce the Direct Prediction World Model (DPWM), a non-recursive architecture that compresses an action sequence of arbitrary length into a single embedding and predicts the endpoint observation in a single forward pass. This design avoids recurrent rollout in both prediction and gradient propagation, making long-horizon end-to-end training practical at horizons where unrolled autoregressive training becomes unstable. Empirically, DPWM substantially improves long-horizon endpoint prediction over recursive world-model baselines on continuous-control and pixel-based benchmarks, with larger gains as the prediction horizon increases. We further show that recurrent baselines benefit similarly when retrained with the same long-horizon endpoint objective, supporting our central claim that the training objective, rather than the particular backbone choice, is the main driver of long-horizon prediction accuracy. Our results suggest that world models can benefit from being trained and evaluated at the temporal scales where they are ultimately used, shifting the focus from local transition modeling toward long-horizon predictive accuracy.

---


### 162. [Hands-Off or Hands-On? Variation in Area Chair Practices and Implications for AI Support](https://arxiv.org/abs/2608.07425)

**<font color=#1a73e8>作者：</font>** Ines Arous, Neha Nayak Kennard, Andrei Mircea 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Area chairs (ACs) play a critical role in the peer-review process, managing conflicts and ensuring fair outcomes. Although AI tools have been proposed to support ACs, little is known about the challenges they face and their perceptions of these technologies. In this paper, we conduct interviews including a design probe with 27 ACs in AI to explore their challenges, strategies, and perspectives on potential AI tools. Through thematic analysis, we identify key tensions arising from the growing volume of submissions, uneven reviewer expertise, and the complex task of managing the relationship between reviewers and authors. Most importantly, we find substantial variation in how ACs engage with submissions and influence outcomes: some adopt a largely hands-off approach, while others take a more hands-on role in guiding discussions and decisions. This variation challenges the notion of a single, universal AC practice and highlights the need to account for diverse approaches. When reflecting on the potential use of AI tools, ACs expressed a cautious stance, drawing on their domain knowledge and heightened awareness of AI limitations. From these findings, we derive three design implications: tailoring AI assistance to diverse AC practices, design assistance for discussion moderation, and embedding human-centered AI principles that preserve human agency in decision-making.

---


### 163. [Post-Grokking Collapse at the Representation-Readout Interface in Muon-Trained Transformers](https://arxiv.org/abs/2608.07436)

**<font color=#1a73e8>作者：</font>** Ali Janati, Kaoutar El Maghraoui, Andrei Kanavalau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Under the standard split, Muon gets hidden matrices and AdamW embeddings/output head. Muon groks modular addition faster, but its solutions do not hold. All nine configurations on $(a+b) \bmod 113$ grok and later lose generalization. Across five seeds the selected AdamW reference falls below threshold on four, reaching 27.59%. Instability persists across two moduli, two widths, two training fractions, subtraction, and depth.
The failure arises at the representation-readout interface, identified only jointly up to an invertible map unselected by the loss. After solving the training set, the gradient falls to order $10^{-6}$ and the optimizers respond differently: step-size elasticity is -0.03 for Muon versus +1.5 for AdamW, and the Muon group moves 8.0 times faster per parameter. From bit-identical states, freezing either group prevents failure. Freezing embeddings/readout removes it in five runs over 451,400 post-grokking steps and five paired seeds: unfrozen arms record 137-321 sub-threshold evaluations, frozen arms none. Removing Muon's normalization and orthogonalization is no substitute: it collapses representation from 326 effective conjugate pairs to 4, shows no recurrent collapse, and fails terminally.
Fourier filtering separates circuit failure from masking. Across 43 checkpoints over five seeds and three regimes, the task-aligned family reaches exactly 100% alone. In circuit failure it no longer solves the task; in masking it remains perfect while the full model reaches 45.85%, giving a positive margin on every example, including errors, but being outvoted by a near-equal adversarial remainder. Rescaling it restores 99.9%; grokking is the same condition resolving upward. The task selects the family, swapping $(k,k)$ for $(k,-k)$ under subtraction. Across an abrupt collapse, standard Fourier support is unchanged and the power-distribution cosine remains 0.9899.

---


### 164. [An Analysis of Architectural and Operational Dynamics of Phishkits in the Wild](https://arxiv.org/abs/2608.07451)

**<font color=#1a73e8>作者：</font>** Behzad Ousat, Mohammad Ali Tofighi, Estefan Schafir 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Phishing attacks have always been a favored vector for adversaries to defraud users, bypass modern defense mechanisms, and penetrate critical systems. Among all the elements contributing to the creation and deployment of successful phishing attacks, phishkits stand out as a crucial parameter. Phishkits often facilitate creating and deploying compelling phishing pages, implement evasion strategies, and establish and maintain backdoors with remote adversaries for exchanging leaked data. In this work, we performed an analysis of 1,300 modern phishkits collected from 2020 to 2023. We analyzed the architecture, source code, communication channels, and the nature of leaked data shared with adversaries. We identified mechanisms for dynamic redirection and attributing incoming web traffic as part of the evasion and cloaking mechanism. We also observed heavy reliance on current messaging services for exchanging stolen data with phishers. That said, our analysis shows that the number of phishkits with advanced functionalities is quite small. We identified 284 (21.8%) phishkits that did not use any form of evasion mechanism. We also observed that while there were differences in the implementation details of phishkits, the major components that keep phishing pages functional were very similar or even identical across kits. The level of code reuse and heavy reliance on known tricks to build pre-packaged phishing pages make a large number of cases predictable, which can potentially make the detection of these adversarial operations even easier at scale.

---


### 165. [Interaction Creates Dynamical AI Behavior Absent in Isolation](https://arxiv.org/abs/2608.07457)

**<font color=#1a73e8>作者：</font>** Bella Xinrui Li, Frank Yingjie Huo, Neil F Johnson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What will happen when AI agents interact in daily life, e.g. when one AI starts bossing another around? We find a counterintuitive answer that opens new avenues for out-of-equilibrium Physics. When a boss AI directs a stream of messages at the subordinate AI while ignoring its replies, it drives the subordinate into an alien behavioral state that it would never have exhibited alone. Although the two AIs share the same well-defined (decoding) temperature, the subordinate neither copies its boss nor returns to how it behaves on its own; instead, it adopts an entirely different behavior. The boss's added value is similar to a pre-recorded tape. When the boss listens, they both adopt a similar alien dynamical state. A simple kinetic theory captures the principal effects, such as why the way in which the same messages are delivered will matter in future AI-AI interactions.

---


### 166. [MirrorWorld: Taming Video Diffusion Models for Mirror Reflection Generation](https://arxiv.org/abs/2608.07463)

**<font color=#1a73e8>作者：</font>** Youjun Zhao, Alex Warren, Gary K.L. Tam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video diffusion models (VDMs) have enabled high-fidelity video synthesis. However, generating mirror reflections remains challenging because the content within a mirror must remain consistent with the surrounding scene. Existing VDMs are not specifically designed to model scene-to-mirror relationships, which can lead to reflections with incorrect content or inconsistent spatial arrangements. We observe that mirror reflection generation involves two complementary challenges: determining what scene content should be reflected and how the reflected content should be spatially arranged within the mirror region. Motivated by this observation, we propose MirrorWorld, a reflection-aware video inpainting framework that models scene-to-mirror relationships during generation. Specifically, we introduce Semantic Relation Distillation (SRD), which transfers relational information from a frozen visual foundation model to encourage semantic associations between visible scene content and mirror regions. We further propose Geometric Transformation Alignment (GTA), which learns a transformation that guides the spatial arrangement of reflected content. The two components play complementary roles, with SRD modeling what should be reflected and GTA modeling how it should be arranged. To facilitate research on this problem, we construct a benchmark for video mirror reflection generation by repurposing four existing video mirror datasets into a unified reflection reconstruction task. Experimental results show that MirrorWorld achieves improved reflection reconstruction quality over representative image-based reflection generation methods and strong video inpainting baselines.

---


### 167. [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)

**<font color=#1a73e8>作者：</font>** Zongchuang Zhao, Xin Zhou, Tianyang Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-Action Models (WAMs) improve end-to-end autonomous driving by transferring video dynamics priors to action prediction, but existing methods require costly future generation at inference. We present SimWAM, a simple yet effective WAM that uses video generation purely as a training signal. It co-trains a pretrained video expert and a lightweight action expert with joint flow matching. An isolated attention mask keeps action prediction independent of future frames, allowing the video branch to be discarded after training and leaving a self-contained planner that directly predicts trajectories. Since the two experts share no parameters and interact only through a unified attention interface, the video backbone could be replaced and the action expert scaled independently without modifying the learning objective or inference pipeline. We further apply reinforcement learning to optimize a compositional driving reward beyond trajectory imitation. Our SimWAM achieves $91.5$ PDMS on NAVSIM, surpasses state-of-the-art WAM-based planners with substantially lower latency, and transfers zero-shot to nuScenes. These results position SimWAM as a simple yet solid baseline that could readily benefit from advances in video generation for efficient autonomous driving. The code and model weights are available at this https URL

---


> [!TIP]
> 当前位于：**151-167**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-167**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
