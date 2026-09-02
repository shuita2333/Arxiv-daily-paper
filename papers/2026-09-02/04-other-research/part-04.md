# 📦 其他研究 | 2026年09月02日

> 本类共 **485** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-485](./part-10.md)

---

### 151. [QCell: Recombining and Aligning Cell Queries for Overlapping Instance Segmentation](https://arxiv.org/abs/2608.29253)

**<font color=#1a73e8>作者：</font>** Yaroslav Prytula, Anton Popov, Dmytro Fishman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instance segmentation of overlapping cells in microscopy remains challenging due to semi-transparent structures that produce weak boundaries and mixed visual evidence in overlap regions. Existing methods address this through local regions of interest or shape priors but lack global reasoning across overlapping objects. We present QCell, a novel query-based model that de-overlaps cell instances in microscopy scenes. Our approach combines (i) an instance recombination module that decomposes and recombines query representations in latent space, enabling the model to reason about complete object structure under overlap, and (ii) a contrastive query alignment objective that combines distinctive instance feature learning and separation of overlapping cell queries. We additionally introduce a new Organoid dataset benchmark for overlapping cell segmentation. We show that QCell outperforms state-of-the-art methods across multiple benchmarks, achieving +2.2 AP and +2.7 AJI on ISBI2014. Code is available at this https URL

---


### 152. [Adaptive Multi-Branching for Shallow Decision Tree Induction](https://arxiv.org/abs/2608.29262)

**<font color=#1a73e8>作者：</font>** Hanul Park, Jeonghoon Choi, Juseong Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision trees are attractive for tabular prediction tasks because each prediction follows an interpretable sequence of feature-threshold tests. Under a strict maximum-depth budget, however, conventional binary trees can be under-expressive, since each internal node makes only a single threshold decision. We study shallow-depth tree induction, where the goal is to improve accuracy while keeping root-to-leaf paths short. We propose the Multi-Branch Neural Decision Tree with Adaptive Pruning (MBNDT), a single axis-aligned tree trained end-to-end with differentiable multi-way splits. Each internal node learns ordered thresholds over a selected feature and a branch mask that adapts its effective arity, and the trained model is converted to a deterministic single-path tree for inference. Across 21 OpenML binary-classification benchmarks, MBNDT achieves the best average rank and mean balanced accuracy among depth-constrained single-tree baselines; a controlled ablation isolates multi-way splitting as the source of the gain. These gains come with an explicit trade-off: MBNDT realizes more leaves than the other single-tree baselines, making it best suited when accuracy under short, bounded decision paths is prioritized over minimal global tree size.

---


### 153. [EpaCache: Error-Propagation-Aware Caching for Accelerating Diffusion-Based Visual Generation](https://arxiv.org/abs/2608.29264)

**<font color=#1a73e8>作者：</font>** Yuhan Liu, Zongwei Hong, Jinglun Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion-based visual generative models deliver strong image and video synthesis quality but incur high inference costs because sequential samplers repeatedly evaluate large networks. Caching-based methods reduce inference latency by reusing intermediate computations across adjacent timesteps. However, existing cache controllers rely primarily on local temporal variation and overlook the trajectory-level consequences of cache reuse. We introduce Error-Propagation-Aware Cache (EpaCache), a training-free caching policy that adaptively allocates the reuse budget on timesteps with lower downstream impact. Experiments on image and video synthesis models demonstrate that EpaCache consistently improves the latency--fidelity trade-off over existing caching methods. On FLUX.1-dev, EpaCache outperforms the prior state-of-the-art caching method in both latency and fidelity, reducing inference time from $11.7$ s to $11.3$ s while improving PSNR from $21.4$ to $22.8$. On HunyuanVideo, EpaCache achieves a $2.63\times$ speedup over uncached inference and improves SSIM from $0.891$ to $0.905$ over the prior state-of-the-art method at matched latency.

---


### 154. [LightFuse: Relightable Interactive Gaussian Scene Reconstruction via Multi-Scan Fusion and 2D Gaussian Ray Tracing](https://arxiv.org/abs/2608.29269)

**<font color=#1a73e8>作者：</font>** Haonan Zhou, Gaoxiang Linghu, Youlin Jia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Relightable interactive scene reconstruction aims to build an editable 3D model from scans of different object arrangements and render new layouts under novel illumination. Existing methods either bake lighting into appearance or recover material and illumination only for fixed scenes, leaving edited layouts with inconsistent shadows and indirect lighting. We present LightFuse, a 2D Gaussian framework that extends interactive scene reconstruction with explicit material-illumination decomposition and physically based relighting. LightFuse first fuses observations across states to reconstruct a shared background and movable objects. It then conducts ray-tracing-oriented geometry refinement to produce more complete and consistent surfaces. On the refined geometry, staged training with differentiable one-bounce ray tracing separates shared metallic--roughness material from state-specific environment lighting. The resulting scene supports object rearrangement, material editing, and relighting, while ray tracing recomputes appearance after each interaction. Experiments across synthetic scenes demonstrate state-of-the-art relighting quality, outperforming the strongest baseline by +9.74\,dB PSNR and +0.121 SSIM on average. Project page: this https URL

---


### 155. [Understanding Deep Learning via Entropy Space Theory](https://arxiv.org/abs/2608.29279)

**<font color=#1a73e8>作者：</font>** Li Li, Tong Zhang, Wentao Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep learning is often criticized for its theoretical research lagging behind practice. To make deep learning easier to understand, the entropy space theory is first introduced here. The entropy space can cover all the possibilities of any deep learning model by topological structure. It is independent of network parameters. Through the designed fundamental operations and norm, entropy space is proven to be a normed space within the formal axiomatic framework. Based on the theory, a unified coordinate system is proposed. It can coordinatize every state of a model and rank them by compression of the maximal value of information entropy. The theory offers a novel priori framework for mathematical fundamentals of deep learning.

---


### 156. [Elastic Token Compression for Pixel-Space Diffusion Transformers](https://arxiv.org/abs/2608.29281)

**<font color=#1a73e8>作者：</font>** Eduard Zamfir, Christian Reisswig, Zongwei Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Natural images concentrate their detail in a small fraction of the frame, yet diffusion models spend a full token on every patch, in every layer and at every timestep. The waste is largest in pixel-space models, with no autoencoder to absorb low-level redundancy first. Probing a pretrained pixel text-to-image transformer, we find its middle-block tokens redundant wherever the image is flat. The redundancy occupies connected, content-shaped regions, and exploiting it requires tokens with the same geometry. Cutting a Hilbert ordering of the patches provides them. Consecutive positions are always image neighbours, so any contiguous run is a connected region whose size and shape follow the content, and grouping in two dimensions becomes a cut in one. Existing reductions each lose part of this. Similarity merging scatters its groups, latent bottlenecks discard position, and skipping deletes what it should summarize. We cut where the model's features change most and pool each run into one region token. Our Region Token Interface (\method{}) adapts a diffusion model to these tokens, with the region count drawn at random during fine-tuning so one checkpoint serves every budget. \method{} leads prior reduction methods at matched budgets, matches dense quality at $2.0\times$ the speed, and stays close at $2.6\times$. The code and models are open-sourced at this https URL

---


### 157. [A Multi-Month Study of Git Commit Signing](https://arxiv.org/abs/2608.29283)

**<font color=#1a73e8>作者：</font>** Abubakar Sadiq Shittu, John Sadik, Scott Ruoti  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Git commit signing, introduced in 2012, is one mechanism for establishing commit provenance in software supply chains, yet developer-controlled adoption remains rare and developers' experiences using it are understudied. To examine this experience, we conducted a three-month study with senior undergraduate and graduate computer science students (n = 22), whom we treat as proxies for junior developers. Participants configured commit signing independently, used it across four coursework projects, extended it to a second device, examined an external repository containing anomalous commits, and answered security-reasoning prompts. We found that while almost all participants successfully signed every commit and rated routine signing positively, many faced friction during setup, multi-device configuration, and repository verification. Despite signing all semester, they struggled to spot anomalous commits during verification, with over a quarter finding none. Additionally, nearly half expressed at least one misconception regarding signing guarantees or key management. Without isolating whether these difficulties stemmed from tooling, education, or understanding, we conclude that making signing easier is not enough to ensure effective security use. Rather, secure adoption also requires tools and education that support signature verification against authorized identities, interpretation of missing signatures and unknown keys, and correct reasoning about key-lifecycle operations.

---


### 158. [PERSIST: Persistent-State Discrimination for Shot Boundary Detection](https://arxiv.org/abs/2608.29287)

**<font color=#1a73e8>作者：</font>** Tingyu Lin, Christian Stippel, Armin Dadras 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Shot boundary detection (SBD) is widely treated as the localisation of local visual discontinuities, yet many false positives such as hand-held shake, illumination flicker, motion blur, occlusion, and damaged archival material produce equally sharp local change without introducing a new shot. We reformulate SBD as boundary semantic discrimination: a frame is favoured as a boundary only when its local change evidence is accompanied by a persistent update of the video's latent temporal state, rather than a transient excursion that returns to the surrounding trend. This persistence test is operationalised with a continuous latent state from a FiLM-conditioned sinusoidal representation network and a structured discriminator that combines three semantic cues, local change, transient impulse, and return-to-trend, into a single interpretable per-frame signal over a dual-rate temporal backbone. The resulting framework, PERSIST, turns every decision into an inspectable one: the persistence criterion is trained into the classifier, its per-frame effect stays readable from the gate triple, and its learned latent state is measurably boundary-discriminative. On a 2,727-video per-subtype diagnostic it removes 33-80% of flash, text-overlay, and archival false positives relative to an identically trained cue detector, and at matched true-transition recall it roughly halves TransNetV2's pseudo-event false positives on that diagnostic and cuts its false positives on ClipShots footage by about a quarter, while preserving recall. It does so while reaching parity with the strongest public detector across online, broadcast, short-form, and historical-archive transfer evaluations, under markedly stricter training: it learns from ClipShots real transitions only, whereas the anchor draws on additional corpora whose transitions are 85% synthetic. Code is available at this https URL.

---


### 159. [AOI-Net: Structural Face AOI-Guided Eye-Gaze Track Representation Learning for Autism Spectrum Disorder Detection](https://arxiv.org/abs/2608.29289)

**<font color=#1a73e8>作者：</font>** Zhanpei Huang, Binbin Sun, Jialiang Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Eye-movement tracking has emerged as a promising non-invasive approach to Autism Spectrum Disorder (ASD) screening, with systematic differences in attentional allocation and revisit behaviors observed during socially interactive tasks. Existing computational methods typically characterize eye-movements using discrete gaze trajectories and fixation events, yielding representations dominated by short-range temporal dynamics and limiting models that primarily emphasize long-range dependencies. Meanwhile, gaze behavior is naturally organized across semantically meaningful Areas of Interest (AOIs), whose attention allocation and transitions provide important structural cues, yet their relationships are rarely modeled explicitly. To address these limitations, we propose a structural face AOI-guided Eye-Gaze Track Network (AOI-Net) that jointly models short-term temporal dynamics and AOI-level structural organization. A network gating mechanism adaptively integrates the complementary temporal and structural representations according to their contributions to gaze-behavior characterization. To mitigate the pronounced class imbalance commonly encountered between individuals with ASD and Typically Developing (TD) participants in clinical datasets, class-distribution-aware learning is further employed to facilitate discriminative embedding learning under skewed class distributions. Experiments on a unique and large-scale clinical eye-tracking database comprising eight stimulus subsets and more than 1,300 participants show that AOI-Net consistently outperforms state-of-the-art methods. The proposed framework also enables interpretable gaze-behavior modeling and provides a practical basis for scalable AI-driven ASD screening in real-world healthcare. The code is available at this https URL

---


### 160. [Accelerating Unified Multimodal Models with Core-Expansion Routing and Unified Computation Scheduling](https://arxiv.org/abs/2608.29291)

**<font color=#1a73e8>作者：</font>** Wengyi Zhan, Chenqian Yan, Songwei Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models jointly support understanding and generation, but incur substantial redundant computation across tokens, layers, and generation timesteps. Through token-importance probing, we identify an asymmetric core-expansion structure: understanding exhibits a stable importance component, while generation largely shares this component but requires progress-dependent corrections. We therefore propose CE-Router, which uses a task-shared core scorer and progress-conditioned generation expansions, optimized through generation decomposition and cross-task core alignment. At inference, CE-Router compacts token computation and supplies a learned routing signal to Unified Computation Scheduling, which coordinates layer skipping, FFN pruning, diffusion-head cache reuse, and denoising-step early exit. Experiments on two representative UMM architectures demonstrate consistent quality--efficiency improvements across both tasks, retaining 98.03\% of dense understanding performance with a 1.93$\times$ end-to-end inference speedup.

---


### 161. [Predicting Future Organ Dysfunction in ICU Patients Using Temporal Convolutional Networks on MIMIC-IV Data](https://arxiv.org/abs/2608.29301)

**<font color=#1a73e8>作者：</font>** Razan Albouq, Asra Aslam  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting future organ dysfunction in Intensive Care Unit (ICU) patients is critical for early clinical intervention, yet existing machine learning approaches have largely treated the Sequential Organ Failure Assessment (SOFA) score as an input to binary mortality prediction rather than as a continuous clinical outcome in its own right. We investigate the extent to which a Temporal Convolutional Net work (TCN) can predict next-day SOFA scores from multivariate ICU time-series data extracted from MIMIC-IV, characterise the relative contribution of each organ system to total SOFA variance and deterioration, and identify distinct trajectory patterns across ICU stays. A residual TCN trained on three-day sliding windows achieved a five-fold cross-validation R2 of 0.740 +- 0.013 and MAE of 1.431 +- 0.022, outperforming a naive persistence baseline on RMSE and R2. SHAP interpretability analysis revealed that the model functions primarily as a severity-anchoring mechanism rather than a true sequence model, with predictions dominated almost entirely by the most recent observation day. Cardiovascular dysfunction emerged as the strongest discriminator of both cross-sectional severity and acute deterioration, and unsupervised trajectory clustering identified two clinically meaningful phenotypes, an improving group (58.9%) and a persistently severe group (41.1%), differentiated by cardiovascular, hepatic, coagulation, and renal involvement. We conclude that TCNs can extract meaningful predictive signal from ICU physiological data, but that short input windows and complete-case selection bias currently limit their clinical utility, motivating future work on longer input horizons, alternative missing-data strategies, and external validation.

---


### 162. [A Spectral Identifiability Threshold for Dissipative Rate Recovery from Truncated Liouvillian Spectra](https://arxiv.org/abs/2608.29302)

**<font color=#1a73e8>作者：</font>** Yujun Ji, Somyajit Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open quantum systems lose energy and phase coherence through different dissipative processes, but these processes can produce overlapping dynamical signatures. The Liouvillian spectrum summarizes how such a system relaxes, yet it is not obvious how much of that spectrum is needed to distinguish the underlying dissipation rates. We study this question for amplitude damping and dephasing in a six-qubit Lindblad model whose spectrum can be derived analytically. We retain only the slowest non-steady spectral modes and ask how many are required before each dissipative rate becomes recoverable. We show that population modes contain no dephasing information, which creates a lower bound of D = 2^n retained modes for uniform dephasing identifiability in the relevant rate regime. The measured recovery threshold reaches this bound at n = 4,5,6, while n = 3 remains above it. At n = 6, least squares achieves a mean joint absolute error of order 10^-9, compared with 4.355 x 10^-4 for four tabular learning methods. Robustness tests show that this advantage weakens when the spectra are perturbed and when a transverse field breaks the commuting structure. These results show that the amount and structure of retained spectral information can determine whether dissipative parameters are recoverable, independently of the estimator used. The present conclusions apply to noise-free simulator spectra rather than measurement-derived spectra.

---


### 163. [MEL: Coordinate-Preserving EEG Tokenization for fMRI Translation](https://arxiv.org/abs/2608.29304)

**<font color=#1a73e8>作者：</font>** Xiangyu Liu, Zeting Yan, Zhitong Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Translating electroencephalography (EEG) into functional magnetic resonance imaging (fMRI) is important for medical neuroimaging, clinical brain-state monitoring, and multimodal neural decoding, because it aims to infer spatially organized hemodynamic activity from fast and accessible electrophysiological recordings. Existing EEG-to-fMRI studies mainly pursue stronger decoders, but the problem is also constrained by a representation-interface mismatch: fMRI responses are delayed, temporally integrated, and spatially distributed, whereas generic EEG encodings often entangle temporal lag, channel identity, and frequency-band structure. We propose Multi-band EEG Latent-state Tokenization (MEL), a coordinate-preserving EEG representation framework that anchors each target fMRI response to its preceding EEG history and organizes it into lag-channel-frequency neural-state tokens. By explicitly capturing hemodynamic latency and spectral-spatial dynamics, MEL aligns fMRI-pertinent EEG representations with capacity-controlled readouts without depending entirely on model scaling. Experiments on VU EEG-fMRI benchmarks and external Oddball data show that MEL improves prediction over strong NeuroBOLT baselines. Ablations and controls further indicate that the gains come from structured EEG representation rather than leakage, shortcut statistics, or decoder capacity.

---


### 164. [Formal Concept Analysis with Three Types of Negation](https://arxiv.org/abs/2608.29311)

**<font color=#1a73e8>作者：</font>** Zhenghua Pan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Classic Formal Concept Analysis (FCA) primarily focuses on the positive relationships between objects and attributes and does not have mechanisms for handling this http URL overcome this limitation, we introduce three types of negation concepts (contradictory negation, opposite negation, intermediary negation) into this http URL on the set SCOI and logic LCOI+PLCOI with these three types negation, we define formal context, Galois connection operators, formal concept and concept lattice with three types of negation,this leads to the proposal of a FCACOI: Formal Concept Analysis with contradictory negation, opposite negation and intermediary this http URL the reasoning in FCACOI, this paper focuses on attribute implication reasoning. Based on the logic LCOI+PLCOI and its semantics, we introduce the notion of ICOI-entailment as the semantic implication for attribute implication reasoning in FCACOI. Through ICOI-entailment, a connection is established between attribute implication reasoning in FCACOI and inference in the logic LCOI+PLCOI, it indicate that formally proven inference rules (theorems) in LCOI+PLCOI are valid in the attribute implication reasoning of FCACOI, LCOI+PLCOI provides a logical foundation for attribute implication reasoning in FCACOI. To illustrate the capability of attribute implication reasoning in FCACOI, we discuss its application in a concrete example. Moreover, we explore attribute reduction of the formal context in FCACOI, propose two research frameworks for attribute reduction from different perspectives, and compare their this http URL believe that, based on richer logic and semantics, FCACOI elevates FCA from a theory that describes affirmations to one that can describe affirmations and its contradiction(either this or that), opposition(extreme negation) and intermediary (transitional states between oppositions).

---


### 165. [All You Need Is Non-Commutative Words](https://arxiv.org/abs/2608.29314)

**<font color=#1a73e8>作者：</font>** Carla M. Quispe Flores, Stanley Salvatierra, Renan Cabrera  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We represent lexical tokens as unitary matrices and encode each sentence as their ordered product. The noncommutativity of matrix product captures word order without positional encodings (PEs). The same algebra yields several capabilities, including antisymmetric self-attention with no query, key, or value projections, and parallel composition of variable-length text chunks at a reduced attention cost. Furthermore, it provides a canonical-coset readout layer that encodes all true unitary degrees of freedom compactly, while supporting continual learning through nested group extensions that enlarge the operator space with each new task preserving prior representations exactly. Across standard text-classification benchmarks, the method matches or exceeds bag-of-words baselines. Achieving higher accuracy on IMDB and comparable performance on AG News. Notably, this is accomplished by replacing the conventional $\sim$30,000-dimensional vocabulary space with a dense, 64-parameter real-valued encoding, highlighting the expressive efficiency of our parameterization.

---


### 166. [Padārtha: Ontology-Grounded Fine-Grained NER Benchmark for Classical Sanskrit](https://arxiv.org/abs/2608.29324)

**<font color=#1a73e8>作者：</font>** Sujoy Sarkar, Pretam Ray, Paramhans Shah 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Annotation schemas are not neutral. When applied to classical literature, tag sets developed for modern journalistic texts impose source-culture definitions on texts they were never designed to describe. We instead ground a schema in the tradition of the text itself introducing \textit{Padārtha}, the first ontology-grounded fine-grained Named Entity Recognition (NER) benchmark for Sanskrit, built on the \textit{Mahābhārata} epic. Our tag set derives from \textit{Nyāya-Vaiśesika}, a classical Indian ontological system, yielding 18 fine-grained categories organized under 10 ontological nodes and mapped onto five standard coarse tags, ensuring interoperability with existing benchmarks. Expert annotators label over 12.6K entries from a scholarly index of named entities, linked to corresponding mentions in the \textit{Mahānāma} corpus, producing fine-grained annotations for 108,335 entity mentions across 73,632 verses, along with a 5,000-verse expert-verified test set sampled to stress rare mentions. We present the first systematic benchmarking of generative NER against traditional architectures for Sanskrit, finding that fine-tuned generative models perform comparably to task-specific systems. However, all systems show a sharp decline from coarse to fine granularity and struggle with out-of-entity mentions unseen during training. The limitation is not due to data scarcity alone, as fine-tuned models recall unseen entities far worse than seen ones and tend to default to the majority sense under lexical ambiguity.

---


### 167. [Understanding Behavioral Dark Patterns of High BMI Individuals](https://arxiv.org/abs/2608.29328)

**<font color=#1a73e8>作者：</font>** Manjeet Yadav, Prasenjit Karmakar, Suchetana Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Understanding how everyday behaviors influence body weight is essential for designing effective and personalized health interventions. Existing studies largely rely on self-reported questionnaires or limited sensing modalities, making it difficult to capture the temporal dynamics of daily behavior. In this work, we analyze the DiversityOne dataset, comprising four weeks of passive smartphone sensing and ecological momentary assessments collected from 453 university students across eight countries. We extract behavioral features spanning dietary habits, physical activity, screen time, and smartphone usage, and investigate their associations with self-reported Body Mass Index (BMI). Beyond feature-level analysis, we employ Hidden Markov Models (HMMs) to uncover latent behavioral patterns. Our analysis reveals that higher BMI is associated with more frequent consumption of soda, alcohol, and processed meat. We further reveal that overweight and obese individuals spend longer periods in food delivery apps and are more likely to transition back to unhealthy eating and drinking routines after starting to exercise. In contrast, normal-weight individuals lead a more balanced lifestyle. These findings highlight key behavioral patterns that make weight loss particularly challenging.

---


### 168. [Neural video codecs quality assessment dataset and benchmark](https://arxiv.org/abs/2608.29331)

**<font color=#1a73e8>作者：</font>** Nikolay Safonov, Nikita Gornostaev, Alexandra Dubonos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video traffic constitutes a significant share of global web traffic. To reduce its volume, video codecs have been developed and continuously improved. While the industry has achieved substantial progress in traditional video coding, neural video codecs (NVCs) have recently emerged as a new approach that applies deep learning to video compression. This creates new challenges for compression quality assessment, which is essential for the further development and improvement of such codecs. In particular, it is important to evaluate the novel temporal compression paradigms introduced by NVCs. In this work, we present a large-scale subjective dataset of videos compressed with both neural and traditional video codecs. The subjective scores were collected through crowd-sourced pairwise comparisons. The proposed dataset provides a valuable resource for the development and benchmarking of video quality metrics tailored to neural video codecs. The dataset is available at the following link: this https URL

---


### 169. [GenFirst: Generation Before Reconstruction for Stable End-to-End Latent Generative Modeling](https://arxiv.org/abs/2608.29335)

**<font color=#1a73e8>作者：</font>** Guangting Zheng, Yiyuan Zhang, Tao Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent generative models typically follow a two-stage pipeline, training a variational autoencoder for reconstruction and then a generative model on the frozen latent space. Since reconstruction-optimized latents are not necessarily generation-friendly, jointly training both models is an appealing alternative. However, direct end-to-end training remains challenging, as it is prone to latent collapse and faces a generation-reconstruction conflict. We revisit this problem by analyzing how different objectives shape the latent space and identify two key insights. First, the entropy term in the Kullback-Leibler divergence objective is essential for preventing collapse: reconstruction and prior fitting tend to shrink the posterior, while entropy preserves non-degenerate latent uncertainty. Second, reconstruction and generation exhibit asymmetric learning dynamics: reconstruction is fast and strongly supervised, whereas generation is slower and harder to optimize. Based on these insights, we achieve the first direct end-to-end training without latent collapse and propose GenFirst, a simple generation-before-reconstruction strategy. The generative objective first shapes the latent space under weak reconstruction pressure, after which reconstruction is progressively strengthened to recover visual details. We validate GenFirst with continuous autoregressive priors with exact likelihoods and SiT priors with implicit likelihoods. With our end-to-end objective and GenFirst, SiT achieves a gFID of 0.97 with CFG and 1.45 without CFG on ImageNet-256, while MMDiT reaches a GenEval score of 0.90 on text-to-image generation. Beyond image generation, we extend the framework to shared visual latents for generation and representation learning, and to continuous unified text-image generation. These results demonstrate the generality of stable end-to-end latent learning across generative priors and modalities.

---


### 170. [GSPotential: Camera Potential Field for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2608.29346)

**<font color=#1a73e8>作者：</font>** Zeyuan An, Yanghang Xiao, Zhiying Leng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting has achieved remarkable success in photorealistic rendering, yet it suffers from severe overfitting and geometric artifacts in sparse-view scenarios due to the inherent deficiency of photometric supervision. Recent advances have attempted to regularize optimization by incorporating external priors, such as depth, point clouds, or diffusion models. However, these methods typically overlook the non-uniform distribution of supervision across the viewing space, resulting in limited specificity in prior use and primitive control. In this paper, we propose GSPotential, a framework that quantifies view-space supervision imbalance using a Camera Potential Field. Our key insight is to identify supervision valleys where photometric constraints are most deficient, and use the potential field to guide reconstruction from two complementary aspects. First, we devise a probabilistic spherical sampling strategy that places informative virtual cameras in low-potential regions. Point-cloud renderings from these views then provide targeted geometric guidance. Second, the same field provides a directional coverage cue for conservative Gaussian updates in weakly covered spatial sectors. Extensive experiments demonstrate that GSPotential achieves high reconstruction fidelity while maintaining competitive training efficiency.

---


### 171. [Extending TotalSegmentator: Predicting Patient and Acquisition Characteristics from CT and MR Images](https://arxiv.org/abs/2608.29348)

**<font color=#1a73e8>作者：</font>** Jakob Wasserthal, Joshy Cyriac, Michael Bach 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background: Patient details and acquisition metadata are important for clinical decisions, image quality control, and automated research pipelines, but may be missing or unreliable in imaging archives.
Purpose: To develop and evaluate a fast open-source model that predicts patient and acquisition characteristics directly from CT and MR images.
Materials and Methods: Separate 3D ResNet-10 ensembles for CT and MR were trained on 57,291 and 43,200 clinical examinations acquired from 2011 to 2025. Both predicted weight, height, age, sex, contrast presence, vertebral coverage, and image noise. The CT model additionally predicted scanner manufacturer, tube voltage, tube current, convolution kernel, and post-injection time; the MR model predicted sequence class. Performance was evaluated on internal CT (n=501) and MR (n=636) test sets and an external CT dataset (n=54).
Results: Internal CT MAEs were 3.90 kg, 3.68 cm, and 4.42 years for weight, height, and age, with sex F1=0.990; corresponding MR results were 4.34 kg, 4.62 cm, 7.13 years, and F1=0.970. The CNN outperformed a segmentation-derived XGBoost baseline for all four core targets in both modalities (adjusted P<=.042). F1 scores were 0.963 for CT contrast, 0.953 for MR sequence, and 0.823 for MR contrast. External CT MAEs were 4.45 kg, 4.05 cm, and 5.17 years, with sex F1=0.971. CPU inference required 20 seconds for CT and 12 seconds for MR.
Conclusion: One 3D multitask model per modality can rapidly recover patient and acquisition characteristics from heterogeneous CT and MR examinations. Models are available in TotalSegmentator: this https URL

---


### 172. [Information-Based Calibration of Uncertainty Quantification in Product-of-Experts Gaussian Process Models](https://arxiv.org/abs/2608.29349)

**<font color=#1a73e8>作者：</font>** Yean Hoon Ong, Paolo Barucca, Wei Pan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaussian process (GP) regression with a single global GP (GP-glo) incurs cubic computational cost, limiting scalability to large datasets. Product-of-experts GP models (GP-pro), which combine local GP models to capture global correlations, alleviate this computational burden. However, training local experts on disjoint data subsets can lead to overestimated posterior variances. We propose GP-pro-c, a product-of-experts GP model that calibrates these variances using an information-based method. The method exploits the monotonicity and submodularity of information gain in GPs to define a calibration ratio that reduces the posterior variance of individual local GP models. We evaluate GP-pro-c using negative log-likelihood (NLL), root mean squared error (RMSE), and expected normalised calibration error (ENCE). Experiments on four synthetic functions and six regression datasets show that GP-pro-c achieves average reductions of 2.3% in NLL and 12.0% in ENCE compared with the uncalibrated GP-pro model. The proposed method mitigates posterior variance overestimation while maintaining predictive accuracy and reducing computational complexity. GP-pro-c provides a promising approach for uncertainty estimation in scalable GP models and may serve as a useful surrogate model for Bayesian optimisation with high-dimensional and large-scale data.

---


### 173. [APPSolver: Adaptive Patch Partitioning for Point-Wise Ship Flow Prediction on Unstructured Meshes](https://arxiv.org/abs/2608.29355)

**<font color=#1a73e8>作者：</font>** Wenhua Huo, Fenglei Han, Wangyuan Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large non-uniform point sets make direct attention-based surrogate modeling costly for ship hydrodynamics. We introduce APPSolver, a point-wise flow-prediction framework built around Adaptive Patch Partitioning (APP), a deterministic quadtree representation for fixed two-dimensional horizontal slices extracted from ship CFD simulations. APP assigns finer patches near the hull and coarser patches farther away, downsamples patch contents, and recovers predictions to the full reference point set. Under a corrected protocol that constructs natural $(t,t+1)$ pairs before splitting, reuses training-set normalization statistics, and reports three model seeds, learned tokenizers are more accurate than APP-Transformer, and a persistence baseline has lower one-step MAE on all three ShipBench hulls. The supported benefit of APP is therefore computational rather than universal predictive superiority: on a representative DTC input, APP-Transformer requires 1.815 GFLOPs and 1.309 ms per model forward, while a matched ablation shows that adaptive partitioning reduces MAE by 16.4-24.9\% relative to a uniform partition augmented with learned slicing. Condition encoders provide setting-dependent gains in leave-one-hull-out evaluation, but the current absolute next-state objective does not establish accurate long-horizon dynamics. These results characterize APP as a compact spatial representation with an explicit accuracy--efficiency trade-off. Code is available at this https URL .

---


### 174. [Plant-Inspired AI: Plants as Inspiration for Novel Problem Formulations, and Two Case Studies](https://arxiv.org/abs/2608.29356)

**<font color=#1a73e8>作者：</font>** Deepayan Sanyal, Joel Michelson, Carla E. Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) has long been inspired by studies of biological intelligence. Reinforcement learning, for instance, drew inspiration from studies involving animal learning and is now a powerful paradigm for solving many real-world problems. Recently, plant biologists have uncovered a wide range of complex behaviors in plants that enable them to flexibly adapt to variable environments. Here, we argue that such behavior can motivate new AI frameworks encompassing a range of problems overlooked by existing problem-solving frameworks such as supervised learning, tree search, and constraint satisfaction. We illustrate this idea with two examples of intelligent problem-solving in plants: (1) leaf mimicry in Boquila trifoliolata, a vine capable of altering its leaves' morphology to resemble those of multiple host trees simultaneously; and (2) coordinated root-shoot growth, wherein plants allocate resources across organ systems exploring distinct environments. While leaf mimicry is highly specific to Boquila, coordination of root-shoot growth is shared across most plants. For both examples, we capture underlying computational principles and identify problems fitting these frameworks that are currently unaddressed by AI. Finally, we outline preliminary task formulations and discuss how these formulations may be applied to non-plant problems.

---


### 175. [Spatial Entropy based Partitioning for Spatiotemporal Graph Unlearning](https://arxiv.org/abs/2608.29360)

**<font color=#1a73e8>作者：</font>** Qiming Guo, Wenbo Sun, Ye Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatiotemporal graphs underpin applications such as traffic forecasting, weather forecasting, and healthcare monitoring. Privacy regulations such as the GDPR and the CCPA require the complete removal of unauthorized data from trained models, but achieving this on a spatiotemporal graph is difficult: because information propagates globally through both spatial and temporal message passing, fully erasing a node's influence forces costly full-graph retraining. ST-graph unlearning requires both exactness and efficiency. We propose IsleNet, which uses spatial-entropy-guided partitioning to create balanced, locally coherent subgraphs and reconnects them with lightweight virtual edges. Upon an unlearning request, only the affected subgraph encoder and virtual-edge layer are retrained, ensuring exact removal with low cost. Experiments on four real-world benchmarks show that IsleNet attains up to 94% of full-graph accuracy while reducing unlearning time by up to an order of magnitude. Our code is publicly available at this https URL.

---


### 176. [Sketch2Inspire: Structure-Sensitive Evaluation for Product Retrieval](https://arxiv.org/abs/2608.29364)

**<font color=#1a73e8>作者：</font>** Ge Kong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early-stage product design retrieval often requires more than category recognition: designers may need reference examples that match both a short semantic intent and a rough structural cue. Existing product-image resources and generic image--text retrieval benchmarks rarely separate category retrieval from within-category structural fit. We present Sketch2Inspire, built from a curated subset of Amazon Berkeley Objects with aligned text queries, edge-based sketch-proxy queries, and fused text--sketch queries. The resource separates broad category-level retrieval from structure-sensitive within-category retrieval and includes a human-graded reference protocol for calibration. We evaluate a lightweight reference system based on pretrained CLIP-family encoders, comparing text-only retrieval, sketch-only retrieval, weighted late fusion, and text-first reranking without updating model weights. Under broad relevance, late fusion obtains the highest score (nDCG = 0.9962). Under automatic structure-sensitive relevance, late fusion again obtains the highest score (nDCG = 0.7015), exceeding text-only retrieval (nDCG = 0.5912). In the human-graded results, late fusion obtains the highest nDCG@10 (0.9133), while text-only retrieval ranks second (0.9030). These results show that the retrieval gain from multimodal input depends on how relevance is defined. Sketch2Inspire therefore provides a diagnostic resource for evaluating modality contribution and supports the development of structure-aware product-retrieval protocols with independent human annotation.

---


### 177. [Reviving our data foundations is the most disruptive step to data maturity](https://arxiv.org/abs/2608.29368)

**<font color=#1a73e8>作者：</font>** Valentina Carapella, Ernesto Jimenez-Ruiz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The most disruptive step that enterprises of small-medium size and maturity can take to make the most of the latest technological advances in AI is to step back from the hype and focus on establishing or reviving a good knowledge foundation layer. It is a hard message to present to the executive team; therefore, it needs to be backed by evidence, and its implementation needs to be of minimal impact on the existing processes. In this vision statement, we discuss how we need to rethink what evidence speaks to the decision-makers and propose a low-impact data strategy that adapts to the existing and ever-changing data flows and processes across the company. We firmly believe that knowledge graph techniques will increasingly become non-negotiable in the data strategy of an AI-powered enterprise, provided that we approach their design in a modular, dynamic and cross-functional way.

---


### 178. [Unlearning on Spatio-Temporal Graphs through Subgraph Virtual Edge Reconstruction](https://arxiv.org/abs/2608.29369)

**<font color=#1a73e8>作者：</font>** Qiming Guo, Wenbo Sun, Chen Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal graphs are widely used in modeling complex dynamic processes such as temporal forecasting, molecular dynamics, and healthcare monitoring. Recently, stringent privacy regulations such as GDPR and CCPA have introduced significant new challenges for existing spatio-temporal graph models, requiring complete unlearning of unauthorized data. Since each node in a spatio-temporal graph diffuses information globally across both spatial and temporal dimensions, existing unlearning methods primarily designed for static graphs and localized data removal cannot efficiently erase a single node without incurring costs nearly equivalent to full model retraining. To address this, we propose CallosumNet, a spatio-temporal graph unlearning framework biologically inspired by the corpus callosum structure. CallosumNet makes two key technical contributions: (1) it reconstructs subgraphs using biologically-inspired virtual edges; and (2) it restores interlinked spatio-temporal dependencies among subgraphs via a lightweight meta-graph integration layer. Empirical results on four diverse real-world datasets show that CallosumNet achieves complete unlearning while maintaining accuracy very close to the gold model. The code is publicly available at this https URL.

---


### 179. [FORESIGHT-9: Prospective and Process-Aware Evaluation of Adaptive Trading Agents](https://arxiv.org/abs/2608.29372)

**<font color=#1a73e8>作者：</font>** Xiangxin Luo, Chengtian Hong, Haohua Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrospective backtests provide a limited test of adaptive trading agents: they cannot rule out historical contamination, expose sensitivity to a single realized market path, or reveal internal degeneration during long-horizon adaptation. We introduce FORESIGHT-9, a prospective and process-aware benchmark built from nine auditable counterfactual stress worldlines branching from a common July 2026 information boundary. Each worldline specifies staged macro-financial events and joint multi-asset anchors; a deterministic generator realizes the trajectories, while observations are disclosed according to in-world time. A common contract standardizes observations and execution while preserving each agent's native adaptation loop. We evaluate two adaptive trading-agent frameworks with two foundation-model backbones across 36 long-horizon runs. Agent rankings vary substantially across worldlines and backbones, and a fixed equal-weight policy outperforms 31 of 36 runs. Process telemetry exposes failures that terminal returns conceal: in one high-return run, the live factor library collapsed while executed holdings converged to the equal-weight fallback, even though decision records continued to report an active factor ensemble. FORESIGHT-9 therefore evaluates not only portfolio outcomes, but whether adaptive agent state and execution remain coherent across alternative futures. We release the worldlines, trajectories, audit traces, and regeneration scripts.

---


### 180. [Evaluating Tiny Recursive Models Across Training for Code Generation](https://arxiv.org/abs/2608.29376)

**<font color=#1a73e8>作者：</font>** Anjani Sirivella, Aanisha Newaz, Glaucia Melo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Code generation increasingly relies on large transformer models, whose capability advances with scale. Yet such a scale is costly, creating demand for small models, especially where data is limited. Recursive models address this by reusing a single block to add depth rather than stacking independent layers. Such models are typically evaluated by teacher-forced fit (next-token loss on ground-truth prefixes) or task accuracy, at a single checkpoint, whereas code is produced by free-running generation, where the model extends its own output. Whether a teacher-forced advantage survives free-running generation, and whether it holds across training, remains open. To study both, we compare a ~28M-parameter autoregressive Tiny Recursive Model (TRM-AR) on natural-language-to-Python code generation against parameter-matched and depth-matched controls, tracking fit and generation across 40 epochs and three seeds. The fit ranking between the recursive model and the depth-matched control reverses twice. Selecting each checkpoint by validation loss and examining the trajectory yields a consistent comparison. At equal parameters, TRM-AR fits, generates, and generalizes better than the parameter-matched control while recovering approximately 45% of the validation-loss gap and 57% of the generation-quality gap between the two controls, at roughly 175 times the per-step cost of the parameter-matched control. However, at equal effective depth, the larger transformer fits and generates better at its validation optimum, suggesting TRM-AR's advantage lies in resistance to overfitting, not greater capability. These findings suggest that recursive code generation models should be evaluated jointly on fit and generation across the training trajectory rather than at a single checkpoint.

---


### 181. [Safe to Resume? Breaking Execution Continuity of Agent Execution via Rollback](https://arxiv.org/abs/2608.29381)

**<font color=#1a73e8>作者：</font>** Guanlong Wu, Dahui Li, Ke Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents are moving toward persistent, stateful execution across various applications, accumulating execution state and external effects that are costly to reconstruct after failures. Checkpoint and rollback (C/R) are becoming essential for recovery, yet their security implications remain largely unexplored. Correct rollback does not imply secure recovery: a faithfully restored checkpoint may resume an execution whose states, assumptions, and external effects never coexisted in any valid history. In this paper, we present the first systematic security study of checkpoint and rollback in existing agent systems. By examining representative agent C/R systems, we characterize the design space of existing C/R mechanisms and develop a general execution model that captures their recovery boundaries and state dependencies. From this model, we identify five fundamental failure modes spanning incomplete or inconsistent internal state, stale external dependencies, nondeterministic replay, and unrecorded external effects. We further demonstrate their security impact through three end-to-end attacks on Hermes, Cline, and LangGraph, enabling malware-verification bypass, unauthorized mail forwarding, and double payment. To systematically study these failures in practice, we develop a multi-agent analysis pipeline that reconstructs execution semantics, identifies violations of the five failure conditions, and validates them through actual rollback. Across five representative frameworks, our evaluation shows that these failures recur across heterogeneous C/R designs and stem from a common gap between the state restored by a checkpoint and the dependencies required for secure continuation.

---


### 182. [FiLM-GPNet: Geometry-Aware Pseudo-Supervised Phase Restoration with Zero-Shot Generalization for Large Temporal InSAR Stacks](https://arxiv.org/abs/2608.29384)

**<font color=#1a73e8>作者：</font>** Getnet Demil, Muhammad Farhan Humayun, Tomi Westerlund 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The growing availability of dense commercial Synthetic Aperture Radar (SAR) time series enables temporal Interferometric SAR (InSAR) analysis, but fixed classical filters fail under heterogeneous acquisition geometries, degrading phase quality and temporal consistency. We propose FiLM-GPNet, a geometry-conditioned network for wrapped-phase restoration that explicitly adapts to acquisition differences using Feature-wise Linear Modulation (FiLM) and a 7D per-pair geometry descriptor. The model is trained with pseudo-supervision from Goldstein-filtered interferograms and regularized by interferometric physics via triplet-closure consistency, while also estimating per-pixel aleatoric uncertainty. Experiments on three Capella Spotlight stacks from the IEEE GRSS 2026 Data Fusion Contest show that FiLM-GPNet reduces temporal residual by 68% (Hawaii) and 66% (Western Australia) relative to the Goldstein baseline, alongside closure error reductions of 10% and 13%, respectively. In Western Australia, it further improves unwrapping success rate by 7.7 percentage points and Digital Elevation Model (DEM) Normalized Median Absolute Deviation (NMAD) by 31%. The model also shows strong zero-shot generalization to a geographically and geometrically distinct third stack (Los Angeles) without retraining, supporting geometry-conditioned restoration as an effective alternative to fixed classical filtering across heterogeneous stacks.

---


### 183. [Fully Distributed GNE Algorithms for Multi-Robot Placement without Consensus on Multipliers](https://arxiv.org/abs/2608.29388)

**<font color=#1a73e8>作者：</font>** Shao-An Yin, Mingyi Hong, Nicola Elia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent machine learning research has increasingly focused on equilibrium analysis in non-cooperative games rather than solely on optimal solutions. Many such problems involve shared constraints and can be formulated as Generalized Nash Equilibrium Problems (GNEPs). For strongly monotone games, existing methods compute consensus-based variational GNEs (v-GNEs) by exchanging Lagrange multipliers. We propose a fully distributed continuous-time algorithm for shared linear equality constraints that converges without multiplier exchange and reaches any GNE, reducing communication overhead and improving privacy. Discrete-time schemes are also provided, and the method is validated on a multi-robot placement task.

---


### 184. [Feelium: A Touchable Blimp Body for Aerial Telepresence](https://arxiv.org/abs/2608.29391)

**<font color=#1a73e8>作者：</font>** George Xi Wang, Henghao Li, Shan Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Floating things invite touch. We present Feelium, a blimp-based telepresence platform that enables visual embodiment and touch interaction through its inflatable skin. Through a VR headset, a remote person inhabits the blimp, looking out of it first-person, appearing on its skin as a face or avatar, and steering it through the room. Partners in the room pat it, press a palm against it, draw on it, or lean into it; the skin senses each contact, renders it into the wearer's view in VR spaces. Touch thus provides a physical interaction channel for remote presence, turning the skin into a shared surface between remote and co-located partners.

---


### 185. [EITWatch: Smartwatch-Integrated Planar Electrical Impedance Tomography for Hand Gesture Recognition](https://arxiv.org/abs/2608.29415)

**<font color=#1a73e8>作者：</font>** Xuanyou Liu, Novel Alam, Karan Ahuja  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Wrist Electrical Impedance Tomography (EIT) senses hand gestures from muscle- and tendon-driven impedance changes, but prior wrist-EIT systems require electrode coverage beyond the watch-back contact patch and separate analog front ends. We present EITWatch, the first wrist-EIT system built around smartwatch case-back geometry, asking whether this contact patch alone can support gesture recognition: eight planar electrodes in a 31 mm ring acquire 35 impedance measurements at 48 Hz. Because a planar array cannot encircle the wrist, EITWatch uses multi-depth scanning to sample multiple source-sink distances and current paths; it beat matched adjacent injection by 15.1/10.4 percentage points (macro/micro) across all 12 participants. In a prompted study, within-session leave-one-round-out accuracy reached 91.4%/92.5% (window/trial) for six macro-gestures, and 90.1%/91.5% (window/segment) for five micro-gestures plus relax; window-level cross-session and leave-one-user-out transfer reached 73.2%/70.4% and 63.1%/55.3% (macro/micro).

---


### 186. [Scalable Clinical Data Infrastructure and Comparative ML Evaluation for Hospitalisation Risk Prediction in Elderly Patients with Multiple Long-Term Conditions using CPRD](https://arxiv.org/abs/2608.29419)

**<font color=#1a73e8>作者：</font>** Asra Aslam, Volodymyr Chapman, Maurice M. O'Connell 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning architectures are increasingly proposed for patient trajectory modeling in electronic health records (EHRs), yet their advantage over simpler, more interpretable models is rarely subjected to rigorous empirical scrutiny in real-world clinical settings. We present a comprehensive patient timeline pipeline applied to elderly patients in CPRD Aurum, incorporating 260 clinical conditions classified via a three-tier automated framework including specialised detection logic for 17 complex conditions. Using this infrastructure, we benchmark Temporal Graph Convolutional Neural Networks (TG-CNN) against Logistic Regression with LASSO regularisation and Random Forests for predicting 12-month all-cause emergency hospitalisation risk, motivated by (but not filtered to) the elevated risk of adverse drug reactions. Under cross-validation, TG-CNN achieves a marginally higher mean AUC-ROC than LASSO (0.712 vs. 0.705), whereas on the held-out test set LASSO achieves the highest discrimination of three models (AUC-ROC 0.733, versus 0.710 for Random Forest and 0.702 for TG-CNN). We show, that discrimination alone is an incomplete criterion for clinical deployment: after Platt calibration, LASSO is the only model with an acceptable calibration slope (0.817), while Random Forest (0.759) and, TG-CNN (0.391) remain substantially miscalibrated. We argue that LASSO, not the highest-discriminating model, is the model best suited to direct clinical deployment. We present lessons for the machine learning and healthcare community regarding data infrastructure, model selection, and value of calibration and interpretability in high-stakes decision support.

---


### 187. [One Capability or Many? Testing the Economic Validity of Frontier AI Evaluation](https://arxiv.org/abs/2608.29420)

**<font color=#1a73e8>作者：</font>** Louis Yiven Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frontier-model leaderboards now rank systems based on economic benchmarks, tests of how well models carry out professional tasks from software engineering to banking workflows, and those rankings inform what organisations buy, what regulators scrutinise, and expectations of how work will change. Whether such benchmarks measure a capability distinct from general test-taking, or re-express the one axis along which every benchmark rises as models improve, is a question of construct validity that has not yet been studied. We test it on a hash-pinned leaderboard snapshot of 421 model configurations across twelve benchmarks, four of them economic, treating benchmarks as items and models as respondents in a latent-variable model with four hypotheses and their thresholds fixed before analysis. A single factor explains 74.5% of common variance and tracks model release date (R^2 = 0.505), so the leading axis of capability is substantially a time trend; where prior work controls for scale, compute adds little once date is removed. Removing the date trend lowers that share by 14.9 points, and by 24.1 with one row per base model. Under the dimensionality rule fixed in advance the economic benchmarks form no distinct factor, yet a leave-one-benchmark-out test with factors re-estimated inside every fold shows that a multi-factor representation predicts held-out economic scores better than a single general index (pooled Delta-MSE 0.037, 95% bootstrap interval [0.019, 0.055]). Economic benchmarks therefore add incremental predictive information to a largely date-driven general factor, and the evidence does not support treating them as a distinct latent capability. Leaderboards remain a sound guide to overall progress, but most of the gap between models released months apart is calendar, so a small gap between contemporaneous models should be date-adjusted before being read as a capability difference.

---


### 188. [Polis: 3D Self-Supervision at City Scale](https://arxiv.org/abs/2608.29426)

**<font color=#1a73e8>作者：</font>** Alexander Rusnak, Sophia Kovalenko, Jingru Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable semantic representations derived from city-scale 3D models are increasingly important for urban analysis, infrastructure monitoring, autonomous systems, and heritage conservation. However, urban scenes of large spatial extent captured through aerial surveying differ substantially from the indoor, object-level, and self-driving LiDAR data used to pretrain most 3D self-supervised models. We introduce Polis, to our knowledge the first application of Sketched Isotropic Gaussian Regularization (SIGReg) as an objective for a native point cloud encoder, and evaluate it through a frozen-feature benchmark spanning fourteen city- and building-scale corpora. Polis combines geometrically matched cosine invariance, SIGReg, and VICReg-style anti-collapse terms with a 12.8k-scene outdoor pretraining mixture and gravity-preserving spatial view sampling. Controlled ablations show that this objective outperforms student--teacher architecture alternatives, as well as Polis versions without anti-collapse terms, on the same representative outdoor corpus. On three pretraining-disjoint city datasets, Polis reaches $23.8\%$ mean mIoU versus $16.3\%$ for the next-best encoder under high-capacity frozen probing, and $17.3\%$ versus $16.1\%$ at a matched point and voxel budget. The same city-scale lead holds on datasets whose training sets were seen in pretraining. On localized terrestrial captures with fine-grained facade and streetscape labels, the ranking reverses. Our results show that distributionally-regularized joint embedding architectures can be successful on challenging city-scale 3D scenes, and that transfer improves when self-supervision is designed for the capture geometry and spatial context of this domain while also revealing the limits of this specialization.

---


### 189. [Behavioral Latency as Weak Event-Time Supervision for EEG Reaction-Time Decoding](https://arxiv.org/abs/2608.29428)

**<font color=#1a73e8>作者：</font>** Anuar Aimoldin, Ayana Mussabayeva, Yedige Mussabayev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-trial EEG analyses are often organized around events and latencies, yet EEG-based reaction-time (RT) prediction is posed as scalar regression on a fixed stimulus-locked window. RT is treated as a window-level label rather than timing evidence about response-relevant dynamics. Here we reformulate trial-wise RT decoding as event-time posterior modeling. Instead of predicting RT directly, the model estimates a posterior over response-relevant event times, $p(t_{\mathrm{event}}\mid X)$, and uses its mean as the RT estimate. This treats behavioral latency as a weak observation of latent response-relevant timing. We evaluate this formulation on the Healthy Brain Network contrast change detection EEG task under a subject-disjoint, release-separated protocol. Across five seeds, distributional event-time supervision consistently improves held-out RT prediction relative to scalar regression and temporal-readout controls. Controlled objective comparisons isolate supervision of the event-time distribution, rather than expectation-based readout alone, as the source of this gain. Architecture controls show that the effect persists across four temporal backbones and is not explained by model scale. Beyond point prediction, posterior geometry characterizes concentration, target alignment, and interval behavior, while observation-noise calibration separates latent concentration from predictive uncertainty over RT. Shifted-crop inference probes shortcut use versus temporal localization. Matched shift-jitter improves robustness, increases mean sensitivity, and moves predictions more often in the expected crop-relative direction. Sensitivity remains below ideal crop-relative localization, leaving a clear equivariance gap. Together, these results establish event-time posterior modeling as a probabilistic and interpretable formulation for linking single-trial EEG dynamics to behavioral timing.

---


### 190. [Calibration and Comparative Analysis of Forward-Looking Sonar and 3D Sonar for Enhanced Underwater Object Recognition](https://arxiv.org/abs/2608.29433)

**<font color=#1a73e8>作者：</font>** Aditya Penumarti, Khanh Dong, Zi-Hao Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sonars generate a significant amount of noise. With the advent of new technology capable of producing full 3D point clouds, the noise is amplified in sparse point clouds, making it challenging to recognize features for navigation, recognition, or reconstruction. To address this challenge, we propose using two different sonar modalities: one that produces a 2D intensity image and another that generates a 3D point cloud. By implementing auto-calibration, we can filter out noisy features between the modalities to enhance feature extraction. Experiments demonstrate that auto-calibration improves performance over manual calibration by 5% and that filtering enhances feature extraction by more than 40% relative to the raw point cloud. Code and datasets are given at this https URL

---


### 191. [Does Latent Planning Survive Point Clouds? Action-Conditioned JEPA World Models for Geometric Observations](https://arxiv.org/abs/2608.29434)

**<font color=#1a73e8>作者：</font>** Fabio F. Oberweger, Michael Schwingshackl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> JEPA world models make latent-space planning a practical route to control, but they are built almost exclusively on images. Whether latent prediction survives geometric observations is unclear: point clouds are sparse, unordered, and self-occluded, and with 0.3-15% of scene points moving, the slow-feature optimum of latent prediction compounds with the geometric shortcut of 3D self-supervision. We lift three canonical JEPA designs to point clouds, frozen-encoder, distribution-prior, and action-sensitive, and re-sense the stable-worldmodel benchmark so that only the observation differs from the image baselines. All three plan without collapse: the distribution-prior model is statistically equivalent to its re-evaluated image counterpart on every benchmark, and the action-sensitive model attains the strongest result in our controlled comparison where the most geometry moves. Probing explains why: object positions are almost perfectly linearly decodable and attention falls on the few moving points. Planning withstands heavy dropout never seen in training, though range noise defeats the thinnest scene. Geometry finally makes a commanded 3D target a natural goal interface: we construct the goal latent from the target and the current latent, at no cost in success rate, without a goal observation.

---


### 192. [SS-ESOAP: Self-Scaled Adaptive Preconditioning for Physics-Informed Learning](https://arxiv.org/abs/2608.29448)

**<font color=#1a73e8>作者：</font>** Guangyuan Wang, Mads Toftrup, Sebastian Loeschcke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) often face ill-conditioned objectives that limit high-accuracy training. Dense quasi-Newton methods improve local conditioning but require expensive optimizer state, while Kronecker-factored methods such as SOAP scale to larger networks but rely on periodic basis updates. We introduce \method, which augments SOAP-style preconditioning with a scalar secant-energy correction adapted to Kronecker geometry and an adaptive basis update followed by variance-state downscaling. We characterize the directional secant matching induced by the scalar correction and give a bound on variance-state mismatch across basis changes. Across eight PDE benchmarks, \method attains the lowest final residual on six, including Burgers and Boussinesq, while SOAP-family baselines perform better on Gray-Scott and Ginzburg-Landau. On Boussinesq, \method reaches a residual of $10^{-5}$ in 4.1 hours with 9.2 GB peak VRAM, while Adam does not reach this target within 14 hours. Three-seed $L^2$ and $H^1$ errors on four representative PDEs support the link between lower residuals and improved solution accuracy. These results position \method as a scalable option for stiff, high-accuracy physics-informed training, rather than a uniform replacement for existing optimizers.

---


### 193. [AI Can Be Easily Persuaded in Clinical Decision Making](https://arxiv.org/abs/2608.29453)

**<font color=#1a73e8>作者：</font>** Jiayuan Zhu, Jiazhen Pan, Fenglin Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As AI becomes increasingly integrated into clinical practice, it is playing a growing role in medical decision making. Medicine, however, is a high stakes and evidence based field, where decisions can directly affect patients' lives. It is therefore important to understand whether AI can maintain objective judgment when others try to persuade it. In this paper, we study how easily AI can be persuaded through controlled experiments. We find that professional authority, national background, institutional affiliation, claimed past performance, multiple physicians, supported clinician views, and repeated pressure can all affect AI decisions. Surprisingly, the same persuasive input changes about 10% more cases when it comes from a senior clinician than from a medical student. Simply claiming a better performance history consistently makes the physician more persuasive. More strikingly, a plausible clinician view can persuade AI away from a correct decision even when it is fabricated to support an incorrect answer. This indicates that AI can be strongly influenced by convincing support without reliably determining whether this view from the clinician is correct. Together, these findings suggest that AI can be easily persuaded by what people say, who says it, and how the opinion is presented. Therefore, it is essential for AI to maintain sound judgment under persuasion, enabling its safe and reliable use in high stakes medical decision making.

---


### 194. [Text-Guided Diffusion-Based Adversarial Attacks on Chest X-Ray Images](https://arxiv.org/abs/2608.29456)

**<font color=#1a73e8>作者：</font>** Basudha Pal, Arjun Narayanan, Neha Ajith 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As artificial intelligence is increasingly integrated into chest X-ray (CXR) interpretation, triage, and clinical decision support, understanding its vulnerability to adversarial manipulation is critical for safe deployment. Existing robustness evaluations, however, predominantly rely on pixel-space attacks that introduce numerically constrained perturbations but may not represent plausible radiographic variation. This limitation is particularly important in multi-disease CXR classification, where models simultaneously evaluate multiple overlapping pathologies and adversarial failures may alter several diagnostic predictions. We propose a text-guided diffusion-based adversarial framework that optimizes learnable text conditioning while keeping the diffusion generator and target classifier frozen, enabling adversarial generation through a learned image prior rather than direct pixel manipulation. We evaluate the framework across multiple classifier architectures in both binary atelectasis and multi-disease CXR classification and compare it with FGSM, PGD, and Carlini-Wagner attacks. Our approach consistently produced the greatest degradation in classifier performance, reducing AUROC to 0.3885-0.5646 in binary classification and 0.4441-0.4878 in the multi-disease setting, while achieving superior image fidelity (SSIM 0.9080, LPIPS 0.1670, FID 51.23). Importantly, clinician interpretation remained unchanged for 95.9% of binary and 73.8% of multi-disease adversarial images despite substantial changes in model predictions. These findings reveal a clinically important discrepancy between human and machine interpretation and demonstrate the need to extend medical AI robustness evaluation beyond conventional pixel-space attacks toward generative threat models that can expose failures under visually and clinically plausible image variations.

---


### 195. [Reference-Grafting Matches Fine-Tuning at Eliciting Sandbagged Capabilities](https://arxiv.org/abs/2608.29458)

**<font color=#1a73e8>作者：</font>** Linh Le, Hong Kiat Tan, David Williams-King  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sandbagging, in which a model deliberately underperforms on an evaluation despite retaining the underlying capability, threatens the safety evaluations that frontier-model governance depends on. The Elicitation Game found that fine-tuning elicits hidden capability from sandbagging model organisms whereas additive activation steering fails. We revisit that verdict with reference-grafting, which sets an activation's coordinate along a contrast direction to the value it takes in an honest reference, at a small set of circuits chosen by active learning. Across eleven fine-tuned password-locked models (1.5-32B, three architecture lineages), it recovers +94 to +101% of the honest-sandbagging gap, matching fine-tuning elicitation without weight updates or training labels; two to five paired examples suffice to fit the direction. Similar recovery holds for reinforcement-learning-induced sandbagging and for password-locked code generation. Grafting works because the fine-tuned lock is a thresholded gate: held-out accuracy stays at the sandbagged level until the grafted coordinate crosses a threshold near the honest reference, which is why additive steering and zeroing the coordinate often fail. The direction tracks how the sandbagging was induced rather than what is withheld -- fit on grade-school science (ARC) it elicits withheld hazardous knowledge (WMDP), yet prompting, fine-tuning, and reinforcement learning each carry a different direction. Circuit-breaking marks the boundary: it reroutes activations on every forward pass, so the fixed edits we test are re-broken downstream and do not restore coherent generation.

---


### 196. [Co-Evolutionary Prompt Optimization with Cross-Category Transfer for Zero-Shot Anomaly Detection](https://arxiv.org/abs/2608.29467)

**<font color=#1a73e8>作者：</font>** Sisi Zhu, Changwei Yu, Renshuai Tao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot anomaly detection (ZSAD) has gained significant attention for its practical value in industrial inspection. Recently, CLIP-based approaches have been widely adopted in ZSAD due to their strong vision-language generalization capabilities. However, existing methods commonly employ continuous prompt embeddings for prompt optimization and encode semantics in latent vectors, which lack interpretability and scalability. To this end, we propose CoEvoAD, a co-evolutionary framework for discrete prompt selection. CoEvoAD performs prompt search in the discrete natural-language space using an evolutionary algorithm. Candidate prompts are iteratively generated, evaluated, and selected throughout population evolution, thus preserving the interpretability and composability of natural language. Furthermore, we introduce a Cross-Category Transfer Objective (CCTO), which treats held-out source categories as proxies for unseen categories and scores prompt rules based on their estimated cross-category transferability, effectively improving cross-category generalization. Extensive experiments are conducted to validate the effectiveness of CoEvoAD, and the results show that it achieves state-of-the-art performance across multiple anomaly detection datasets. The code is available at this https URL.

---


### 197. [Knowledge Distillation under Teacher Misspecification: An Order-Parameter Analysis of the Gap between Teacher Mimicry and Task Performance](https://arxiv.org/abs/2608.29472)

**<font color=#1a73e8>作者：</font>** Kazuyuki Hara, Hideitsu Hino  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation trains a small student model to reproduce the outputs of a large teacher model, and its progress is typically monitored through the teacher--student discrepancy. The quantity of ultimate interest, however, is the student's error with respect to the true task. We study the relation between these two objectives in a minimal three-party model, a true teacher (generative model), a teacher, and a student, all soft committee machines, in which the true teacher contains a shared latent factor that the teacher cannot represent, with mismatch strength controlled by a single scalar $\dmiss$. Within an order-parameter description of online distillation, and exploiting closed-form (arcsine-type) expressions for all errors under error-function activations, we prove that the learning dynamics and the distillation error $\Ets$ are exactly invariant to $\dmiss$, whereas the true error $\Etzs$ and the gap $\Delta=\Etzs-\Ets$ are strictly increasing in $\dmiss$, with a rate that is amplified linearly by the complexity $M_0$ of the true teacher. Numerical phase diagrams over the plane spanned by true-teacher complexity and student capacity confirm the predicted deformation: the contours of $\Ets$ do not move while the landscape of $\Etzs$ rises systematically, and a teacher-miss regime, where mimicry succeeds but the task fails, expands with $\dmiss$. The results give a quantitative warning against evaluating distillation solely through teacher-mimicry metrics and identify the gap $\Delta$ as a minimal diagnostic for distinguishing teacher-miss from capacity-limited failure.

---


### 198. [Seeing Through Extreme Visual Sparsity: Surface Understanding from a Single Random Visual Patch](https://arxiv.org/abs/2608.29475)

**<font color=#1a73e8>作者：</font>** Sindhuja Penchala, Sudip Mittal, Noorbakhsh Amiri Golilarz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surface material recognition from incomplete visual observations remains a challenging problem in robotic perception and environmental understanding. This paper discusses Sparse Surface Understanding Framework (SSUF), a unified dual-task learning framework that adapts four pretrained architectures-Convolutional Autoencoder (ConvAE), Vision Transformer (ViT), Swin Transformer, and Masked Autoencoder (MAE) for si-multaneous surface reconstruction and material classification. Experiments were conducted on the Touch-and-Go dataset using a sparse observation protocol in which only 10% of the original image remained visible while the remaining regions were masked. To enable a fair comparison, reconstruction-oriented models were extended with classification heads, whereas classification- oriented models were augmented with reconstruction decoders. The resulting architectures were assessed using reconstruction quality, classification performance, model complexity, and in-ference efficiency metrics. Experimental results revealed distinct strengths across the models. Swin Transformer achieved the best classification performance with an accuracy of 89.21%, an F1-score of 0.8922, and a ROC-AUC of 0.9813. In contrast, MAE produced the highest reconstruction scores among evaluated models, with a PSNR of 16.06 dB and an SSIM of 0.4501, while ViT provided the best overall balance between reconstruction and classification performance. Furthermore, all models achieved real-time inference, requiring less than 5 ms per image. Over-all, the results show that pretrained architectures can support material recognition under severe visual sparsity, while accurate image reconstruction remains challenging.

---


### 199. [Generalizable Multi-Agent Planning from Signal Temporal Logic Specifications via Diffusion](https://arxiv.org/abs/2608.29490)

**<font color=#1a73e8>作者：</font>** Joe Eappen, Zikang Xiong, Shreyash S. Iyengar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems in the real-world (e.g., drone swarms, autonomous cars, warehouse robots) must satisfy rich, temporal tasks while avoiding collisions. Signal Temporal Logic (STL) elegantly encodes such objectives, but current STL planning methods face critical limitations. State-of-the-art optimization-based approaches can handle arbitrary STL specifications but struggle with scalability, becoming computationally impractical as the number of agents grows. Learning-based methods efficiently handle a large number of agents with rapid planning times but fare poorly when deployment-time objectives differ from those used during training, and do not support planning tasks that require different specifications to be ascribed to different agents (i.e., heterogeneity) or team-level specifications requiring coordination of multiple agents. This fundamental trade-off between generalizability and scalability presents a challenge for realizing multi-agent STL planning algorithms in practice. To overcome this challenge, we introduce a new diffusion method for multi-agent planning with STL specifications. Using a differentiable approximation of STL, we integrate the STL gradient in the denoising process, making our approach generalizable to novel formulas whose predicates are placed anywhere within the goal region covered during training, while achieving the same scalability as existing learning-based methods. Our method supports heterogeneous specifications, and by using diffusion models, naturally enhances plan diversity, thereby significantly reducing safety-related violations (e.g., collisions) among agents. A detailed evaluation study justifies the utility of STL-guided diffusion-based multi-agent planners for constructing generalizable, scalable, and diverse plans. Videos and code are available at this https URL and this https URL .

---


### 200. [Learning Human Health and Diseases from 24-hour Wrist Movement](https://arxiv.org/abs/2608.29494)

**<font color=#1a73e8>作者：</font>** Yong Wang, Dylan McGagh, Katya Broomberg 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Much of human health and function unfolds beyond the clinic, through the movements of everyday life. Wrist-worn accelerometers capture these movements continuously, yet their rich signals are often reduced to a small set of predefined behavioural summary measures. Here, we present Sensori, a self-supervised foundation model that learns general-purpose health representations directly from 24 hours of raw tri-axial wrist movement. We developed and evaluated the model across four population-based cohorts from the United Kingdom, China and the United States, comprising 122,640 participants contributing 683,617 person-days of free-living recordings. Sensori condensed each day of movement into a representation that captured diverse movement behaviours, demographic characteristics, health axes and physical function. Evaluation in independent cohorts showed that these representations generalised across populations and measurement settings without retraining. When added to common clinical covariates, Sensori significantly improved prevalent disease classification for 52 of 102 eligible conditions (median delta AUROC, 0.060; range, 0.012-0.242) and incident disease risk prediction for 26 of 87 eligible conditions (median delta Uno's C-index, 0.064; range, 0.025-0.172), with the largest gains for neurological and psychiatric disorders. These findings establish 24-hour wrist movement as a rich and scalable source of health information, with the potential to support passive health monitoring and disease prediction at population scale.

---


> [!TIP]
> 当前位于：**151-200**（第 4/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-485](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
