# 📦 其他研究 | 2026年06月17日

> 本类共 **509** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-509](./part-11.md)

---

### 251. [When Correct Edges Cannot Be Verified: A Provenance Gap in Incomplete KGQA and a Provenance-Favoring Completion Policy](https://arxiv.org/abs/2606.15833)

**<font color=#1a73e8>作者：</font>** Yongqi Kang, Yu Fu, Yong Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Incomplete Knowledge Graph Question Answering (IKGQA) requires completing missing edges to continue reasoning. A growing line of work verifies completed edges against retrieved text, treating textual support as a proxy for edge quality. We ask a question that, to our knowledge, has not been systematically tested: does textual verifiability actually track correctness? Exploiting the gold deleted triples provided by the standard random-deletion protocol, we measure both. The finding is counterintuitive: among gold-correct completed edges, 76-96% have no supporting passage even under exhaustive retrieval, robustly across deletion rates (20%/40%), datasets (CWQ/WebQSP), and relation types (structural, commonsense, long-tail). Most Freebase-style facts simply do not occur as head-tail co-mentions in text. Textual faithfulness therefore measures provenance, not correctness -- separated by a paradigm-level gap no in-corpus retrieval closes. This reframes edge completion. Since most completed edges -- correct or not -- are causally redundant for the answer (95-97% of correct answers do not depend on any unsupported edge), the central question shifts from "is the edge correct?" to "admit or abstain under provenance uncertainty?" Within this framing we present TGComplete, a provenance-favoring admission policy that retrieves evidence at a reasoning breakpoint, verifies a candidate through a lightweight loop, and abstains when support is absent. Against the generate-to-complete baseline GoG, it attains higher edge precision against gold (15-21% vs 3-14%), with no statistically detectable EM loss and 3.1-7.4 times higher strict faithfulness of admitted edges -- at the cost of lower recall. We position TGComplete not as uniformly better, but as a principled point on a precision/provenance-recall trade-off, appropriate when auditability matters.

---


### 252. [AIChilles: Automatically Uncovering Hidden Weaknesses in AI-Evolved Systems](https://arxiv.org/abs/2606.15834)

**<font color=#1a73e8>作者：</font>** Yajie Zhou, Ao Li, Ashwin Silla 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The computer systems community has recently seen growing interest in AI-driven system evolution, where AI agents iteratively rewrite systems. Frameworks such as AdaEvolve and Engram report 12-60% score improvements over human-designed algorithms. While these results are promising, there are practical concerns if these AI-evolved programs can perform worse on unseen workloads and exhibit scalability regressions. Given the speed and scale of AI-generated code, we need automated mechanisms to uncover such identify hidden weaknesses in AI-evolved systems programs. To this end, we develop AIChilles that takes as input a baseline program $P$ and an AI-evolved program $P'$, AIChilles searches for valid workloads where $P'$ regresses relative to $P$ in correctness, runtime, memory usage, or output quality. To tackle the diversity in system applications, weakness types and potential bugs, AIChilles combines deterministic workload-parameter extraction, agent-based constraint inference, differential oracles, and code-frequency coverage to discover diverse failures. Across five system applications and 30 AI-evolved programs, AIChilles finds 49 distinct hidden weaknesses. We also show that explicitly including AIChilles in the AI-driven development lifecycle can mitigate several of these weaknesses.

---


### 253. [Wasserstein Convergence of ODE-Based Samplers in Decentralized Diffusion Model via Velocity Field Decomposition](https://arxiv.org/abs/2606.15835)

**<font color=#1a73e8>作者：</font>** Chencheng Tang, Xuanyu Xue, Fangyikang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved impressive empirical success in generative tasks, and their convergence theory is now relatively well understood. Motivated by privacy and scalability, recent decentralized diffusion architectures replace a single global velocity field with multiple local experts and a routing mechanism, yielding a sampling dynamics with stochastic expert switching that falls outside standard diffusion convergence analyses. In this work, We study a decentralized diffusion framework with stochastic velocity fields and ODE-based sampling. We establish a convergence guarantee in Wasserstein-2 distance, showing that the distribution of the $N$-step discretization converges to the analytical solution at rate $\mathcal{O}(N^{-1/2}+\varepsilon)$ in $W_2$, where $\varepsilon$ captures the neural approximation errors. To our knowledge, this is the first $W_2$ convergence result for decentralized diffusion models with an ODE-based sampling scheme.

---


### 254. [Learning a Sampling-Free Variational DNN Plugin from Tiny Training Sets to Refine OOD Segmentation With Uncertainty Estimation](https://arxiv.org/abs/2606.15837)

**<font color=#1a73e8>作者：</font>** Jimut B. Pal, Suyash P. Awate  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks (DNNs) frequently fail to generalize to out-of-distribution (OOD) medical images because of variations in scanners and acquisition protocols. Retraining DNN models to address these distribution shifts is often impractical due to the high cost of acquiring and annotating new medical datasets. To address this, we introduce VarDeepPCA, a novel lightweight variational DNN framework designed to restore/refine degraded segmentation maps by leveraging intrinsic geometric priors. Unlike existing approaches that require target-domain data or extensive pre-training, our VarDeepPCA explicitly learns a distribution of valid anatomical geometries using only small in-distribution (ID) datasets. Theoretically, our novel variational learning framework leverages a reinterpretation of the softmax mapping to implicitly perform exact distribution modeling, thereby enabling computationally efficient, sampling-free learning and inference. This also enables VarDeepPCA to provide uncertainty estimates associated with its restored segmentation maps. We empirically validate our framework across 4 distinct clinical applications, using 14 publicly available datasets, involving segmentation of the myocardium, neuroretinal rim, prostate, and fetal head. Comparisons against 15 existing methods demonstrate that VarDeepPCA consistently restores segmentation maps produced by the existing methods on OOD data to (i) significantly improve anatomical plausibility of geometries and clinical utility of the segmentations, and (ii) significantly reduce errors, without needing any more training data than that used by existing methods.

---


### 255. [EmoZone-Talker: Regional Semantic Control of Audio-Driven 3DGS Talking Heads via Facial Action Units](https://arxiv.org/abs/2606.15848)

**<font color=#1a73e8>作者：</font>** Tingting Chen, Shaojun Wang, Huaye Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has shown strong potential for high-fidelity talking head synthesis. However, enabling fine-grained, interpretable, and editable facial expression control remains fundamentally challenging due to intrinsic conflicts between speech-driven facial dynamics and explicit expression signals. Existing methods rely on implicit multimodal fusion, leading to spatial entanglement and temporal instability. We present EmoZone-Talker, a novel framework that reformulates audio-driven facial animation as a structured spatial-temporal coordination problem under cross-modal conflicts. Our approach introduces an explicit spatial disentanglement and temporal dynamics modeling of facial motion. Specifically, we propose Synergy Zones with Prioritized Attention Bias (SZ-PAB) to explicitly decouple modality contributions via region-wise constraints guided by anatomical priors, and a Channel-Independent Temporal AU Encoder (CIT-AE) to model temporally coherent AU dynamics. By integrating these representations into 3D Gaussian deformation, EmoZone-Talker enables precise and interpretable control over facial expressions. Extensive experiments demonstrate that our method improves expression controllability and realism, with notable gains in upper-face accuracy and temporal coherence, while preserving high rendering quality and accurate lip synchronization. Code will be publicly released to facilitate reproducibility and further research.

---


### 256. [A Dual-Branch Collaborative Framework for Joint Optimization of Underwater Image Enhancement and Object Detection](https://arxiv.org/abs/2606.15857)

**<font color=#1a73e8>作者：</font>** Liyuan Cao, Zheng Liu, Guanghao Liao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Due to wavelength dependent light absorption and scattering, underwater images usually suffer from color distortion and blurred details, which limits underwater object detection performance. Existing underwater image enhancement methods mainly focus on visual quality improvement, while it is still difficult to balance enhancement quality, processing efficiency, and downstream detection performance. Therefore, this paper proposes an efficient dual-branch underwater image enhancement framework for object detection. The detail enhancement branch improves brightness and local contrast to recover texture details in dark regions. The color restoration branch uses adaptive compensation to reduce color distortion and improve color gradation. By combining the complementary outputs of the two branches, the proposed framework provides clearer and more informative images for object detection. On the UIEB and EUVP datasets, the proposed method achieves UIQM scores of 2.249 and 2.576. When applied to the YOLOv8 detection task on the URPC dataset, the proposed method improves mAP50 by 2.1\% compared with the baseline. Extensive experiments show that our method improves object detection in complex underwater scenes, while balancing enhancement quality and processing efficiency.

---


### 257. [Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery](https://arxiv.org/abs/2606.15861)

**<font color=#1a73e8>作者：</font>** Yiping Li, Ronald de Jong, Romy van Jaarsveld 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Question Answering (VQA) in robotic surgery, referred to as surgical VQA, requires high-level understanding of complex surgical scenes and the integration of visual perception with language reasoning, with the potential to support surgical training and intraoperative decision-making. Recent Vision-Language Models (VLMs) have shown promising performance through parameter-efficient fine-tuning; however, most existing approaches rely on coarse visual grounding, typically limited to bounding boxes, which fails to capture the fine-grained spatial structure of surgical objects. In this work, we propose a unified framework that jointly performs pixel-level segmentation and visual question answering within a single framework. Our approach integrates a VLM with a Segment Anything Model (SAM)-based decoder and represents scene elements as object tokens generated by the VLM. These object tokens guide answer prediction and are further projected to the SAM-based decoder to produce segmentation masks. By optimizing the object token embeddings through both segmentation and question answering objectives, the model learns spatially grounded representations that enhance visual reasoning while providing explicit pixel-level grounding. We evaluate the proposed method on the private RAMIE (Robot-Assisted Minimally Invasive Esophagectomy) dataset and the public EndoVis18 dataset, where it consistently outperforms baseline methods for surgical VQA. These results demonstrate that incorporating context-aware object tokens into vision-language models improves fine-grained surgical scene understanding.

---


### 258. [STRIDE: Strategic Trajectory Reasoning via Discriminative Estimation for Verifiable Reinforcement Learning](https://arxiv.org/abs/2606.15866)

**<font color=#1a73e8>作者：</font>** Qinjian Zhao, Zhihao Dou, Dinggen Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has become an effective post-training paradigm for improving the reasoning abilities of large language models. However, existing RLVR methods typically rely on final-answer correctness to assign trajectory-level rewards, providing sparse supervision and treating all tokens uniformly regardless of their actual contribution to reasoning. Although recent studies introduce intermediate signals such as process rewards, high-entropy tokens, and semantic uncertainty, these signals are often not inherently verifiable and may fail to distinguish beneficial strategic patterns from harmful ones. To address this limitation, we propose STRIDE (Strategic Trajectory Reasoning with Discriminative Estimation), a fine-grained RLVR framework that derives strategic reasoning supervision from verifiable outcomes. STRIDE contrasts successful and failed trajectories within each response group to estimate the outcome-discriminative preference of each $n$-gram strategic pattern, and further combines this signal with reasoning saliency entropy to identify decision-relevant strategic patterns. These patterns are assigned differentiated advantage values during RL optimization, enabling more precise credit assignment while preserving the verifiability of RLVR. Extensive experiments demonstrate that STRIDE consistently improves reasoning performance across diverse models, tasks, and extended settings, including VLMs and agent-based systems.

---


### 259. [CogCanvas: A Benchmark for Evaluating Multi-Subject Reference-Based Image Generation](https://arxiv.org/abs/2606.15867)

**<font color=#1a73e8>作者：</font>** Long-Bao Nguyen, Quang-Khai Tran, Tam V. Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-subject reference-based image generation requires jointly preserving multiple human identities, binding per-person objects and fashion items, and respecting a specified background scene, a regime where current diffusion models remain brittle. Existing benchmarks evaluate only one axis at a time and none jointly captures multi-identity composition with human-object interaction, background grounding, and spatial plausibility. We introduce CogCanvas, a benchmark of 1,952 curated reference images spanning 100 celebrity identities, 115 distinctive objects and fashion items, and 29 real-world background scenes including landmarks, from which we construct 1,361 compositional prompts covering 2-5 person group sizes. The curation pipeline combines DINOv2-based deduplication, two-stage aesthetic filtering, and automated derivation of structured interaction and position graphs that serve as ground-truth supervision. CogCanvas supports three tasks, reference-based multi-human-object generation (primary), text-to-image compositional generation, and reference retrieval, under a unified six-axis evaluation protocol. We introduce two metrics tailored to the multi-reference setting: BG-Sim, which scores background fidelity on SAM 3-masked regions via DINOv3 feature similarity, and Attr-VQA, which uses a multimodal LLM to verify per-subject attribute binding and inter-person interactions against the structured graphs. Benchmarking five SOTA methods reveals that every model degrades substantially as group size grows from 2 to 5, with near-complete failure on object/fashion binding beyond three subjects.

---


### 260. [Metis: A Generalizable and Efficient World-Action Model for Autonomous Driving and Urban Navigation](https://arxiv.org/abs/2606.15869)

**<font color=#1a73e8>作者：</font>** Jingyu Li, Zhe Liu, Dongnan Hu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World action models~(WAMs) have shown great promise for autonomous driving and urban navigation. Built upon Vision-Language-Action models or video generation models, existing approaches suffer key limitations: (1) High inference latency due to future observation prediction at test time, and (2) tightly coupled video and action modeling leading to representational mismatch and degraded generalization. To address both issues, we propose Metis, an end-to-end WAM framework that decouples video generation and action prediction. Specifically, Metis employs a Mixture-of-Transformers architecture with dedicated experts for video generation and action prediction, preserving the intrinsic distributional properties of each task. To enhance efficiency, we introduce an asymmetric attention mask that enables joint training of both experts while allowing the action model to bypass explicit video generation during inference. This design ensures training-inference consistency and significantly reduces computational costs without compromising planning performance. Extensive experiments demonstrate state-of-the-art performance on the NAVSIM navhard and navtest benchmarks and the CityWalker navigation benchmark, validating both the generalizability and efficiency across diverse tasks. Real-robot deployments further confirm the practical feasibility of our approach.

---


### 261. [Free Energy Heuristics: Fast-And-Frugal Cognition as Active Inference Under Uncertain Precision](https://arxiv.org/abs/2606.15877)

**<font color=#1a73e8>作者：</font>** Alex Bogdan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) improves large language models' performance in math and symbolic reasoning. But on planning, contested ethics, and tasks where the model cannot check itself, more reasoning makes things worse. Both effects are documented; what has been missing is a principled account of which property decides the outcome. We argue it is meta-uncertainty: how unsure the model is about the reliability of its own evidence. When that uncertainty is high, extra reasoning stops adding signal and starts manufacturing false confidence. We prove that the policy minimizing expected free energy under uncertain precision stops integrating cues after a finite number of high-validity ones when the precision prior is heavy-tailed (Theorem 2.6.1), and under a Descending Dominance condition, is sample-wise identical to take-the-best (Theorem 2.7.4). Fast-and-frugal heuristics and active inference are, then, two descriptions of the same computation. The prediction is that on high-meta-uncertainty items, longer CoT should degrade accuracy. We score the regime per item (simulate-and-recover rho > 0.96), build FEH-79, a benchmark of Knightian frames with matched controls, and run a pre-registered study across seven models (five open-weight 3B-32B, two frontier), five CoT lengths, and 7,875 responses. The gate, fixed before any data, required a negative interaction with posterior probability above 0.95 and an accuracy drop of more than 6 points. It held. The high-regime drop is 17.3 points (95% CI [7.7, 25.5]); matched items with definite answers show no cost. The effect is regime-dependent: decisive in capable mid-to-large models, directional in the two frontier systems, absent-to-reversed in the weakest. The framework answers when CoT helps and unifies the Bayesian and fast-and-frugal traditions: less-is-more effects are evidence about the meta-uncertainty regime, not against Bayesian cognition.

---


### 262. [Koshur Diacritizer: A Byte-Level Sequence-to-Sequence Model for Kashmiri Diacritic Restoration](https://arxiv.org/abs/2606.15883)

**<font color=#1a73e8>作者：</font>** Haq Nawaz Malik, Nahfid Nissar, Faizan Iqbal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Kashmiri, an Indo-Aryan language written in a modified Perso-Arabic script, frequently omits diacritic marks in digital text, creating ambiguity and challenging downstream NLP applications. We present Koshur Diacritizer, a ByT5-small byte-level sequence-to-sequence model for restoring diacritics in Kashmiri text. To support this task, we release a publicly available dataset of 23.7k aligned undiacritized diacritized Kashmiri sentence pairs. The proposed framework combines script-aware normalization, alignment validation, and skeleton-preserving inference to ensure reliable restoration while maintaining the original base-letter sequence. Experimental results on a held-out test set achieve a DERm of 0.2012 and a WER of 0.2159. Additionally, evaluation by a native Kashmiri linguistic expert yields a mean accuracy of 77.5%. The dataset, model, and source code are publicly released to provide a reproducible baseline for Kashmiri diacritic restoration and future low-resource language research.

---


### 263. [Text region detection in historical astronomical diagrams](https://arxiv.org/abs/2606.15886)

**<font color=#1a73e8>作者：</font>** Zeynep Sonat Baltacı, Raphaël Baena, Fei Meng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text detection is a crucial task in the analysis of historical documents. While datasets and benchmarks exist for text detection in manuscripts and maps, the study of text in mathematical diagrams has received little attention. To address this, we introduce a large-scale, diverse, open-access dataset of 948 historical astronomical diagrams containing 10,940 oriented polygonal text regions. Our dataset spans ten centuries (8th to 18th) and seven main linguistic traditions: Arabic and Persian (115), Chinese (332), Byzantine (233), Latin (185), Hebrew (48), and Sanskrit (35). It captures a wide range of diagram styles and textual content, from symbols to multi-line paragraphs. Each text instance is annotated with ordered polygons that precisely delineate text regions and encode the reading direction. In addition, we annotated the 2,293 regions in Latin diagrams with 20 class labels. We evaluated several strong baselines on our dataset, including TESTR, DeepSolo++, and Poly-DETR, a simple extension of DINO-DETR that we design to predict ordered polygon vertices. Poly-DETR achieves state-of-the-art performance on the MTHv2 and cBAD2019 benchmarks and provides a solid, simple baseline on our dataset. Code and dataset available online.

---


### 264. [SiGnature: Explicit Motion Diffusion for Stylized Semantic Gesture](https://arxiv.org/abs/2606.15889)

**<font color=#1a73e8>作者：</font>** Adi Rosenthal, Tomer Koren, Nadav Shaked 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent advances in co-speech gesture generation have achieved impressive rhythmic synchronization, synthesizing gestures that are both semantically meaningful and faithful to a speaker's unique non-verbal style remains an open challenge. Semantic gestures, such as iconic shapes or deictic pointing, are statistically sparse, making them difficult to learn effectively within standard generative models. We present SiGnature, a framework for Stylized and Semantic Gesture generation that reconciles precise semantic control with high-fidelity style preservation. Unlike prevalent methods that rely on entangled latent representations, SiGnature operates in an explicit joint-rotation space. This design enables our core contribution, Joint Motion Integration (JMI), a training-free inference mechanism capable of injecting any external motion sequence, particularly in-the-wild semantic gestures, directly into the diffusion process. JMI automatically identifies the specific ``active joints'' conveying a semantic action and injects them into the generation, while relying on the diffusion backbone to synthesize the remaining body dynamics, including posture and flow, in accordance with the pre-learned style of the target speaker. This allows for the plug-and-play integration of arbitrary motions, including complex semantic gestures, without retraining or introducing the ``Frankenstein'' artifacts typical of cut-and-paste methods. Extensive experiments and perceptual studies demonstrate that SiGnature offers superior semantic motion control while maintaining smooth and natural co-speech gesture generation and preserving the distinct characteristics of the speaker, thereby outperforming state-of-the-art baselines.

---


### 265. [Scalar-pathway fidelity improves physical accuracy in short-range equivariant interatomic potentials](https://arxiv.org/abs/2606.15892)

**<font color=#1a73e8>作者：</font>** Jia Bi, Alin Marin Elena, Samuel Pinilla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate interatomic potentials enable molecular dynamics of materials, molecules, and interfaces beyond density-functional-theory length and time scales. Equivariant neural network potentials have improved the representation of local geometry. However, their deployable energy surfaces ultimately manifest through invariant scalar channels, whose aggregation and spectral resolution remain comparatively underexamined. Here we use Physics-Aware Neighborhood (PAN) pooling and Physics-Guided Spectral (PGS) mixers as controlled scalar-pathway probes: lightweight, symmetry-preserving modifications that act only on \(\ell=0\) channels while leaving the equivariant tensor backbone unchanged. Using MACE as a high-body-order mechanistic scaffold, PAN adds coordination-sensitive amplitude modulation, whereas PGS augments edge and readout scalar features with radial and tapered spectral bases. Across metallic Ag, covalent Si, a short-range ionic LiF/Li--F subset, and MD17/rMD17 molecules, this scalar-pathway correction reduces MACE force errors by 22--27\% and energy errors by 19--22\%; on systems with stress labels, stress errors decrease by 27--28\%, at approximately 5\% additional inference-FLOPs cost. Directionally consistent gains in Allegro and NequIP further indicate that the correction is portable across distinct short-range equivariant backbones, although effect sizes remain architecture-dependent. These results identify scalar-pathway fidelity as a practical design dimension for short-range equivariant interatomic potentials.

---


### 266. [Topological Flow Matching](https://arxiv.org/abs/2606.15897)

**<font color=#1a73e8>作者：</font>** Kacper Wyrwal, İsmail İlkan Ceylan, Alexander Tong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching is a powerful generative modeling framework, valued for its simplicity and strong empirical performance. However, its standard formulation treats signals on structured spaces, such as fMRI data on brain graphs, as points in Euclidean space, overlooking the rich topological features of their domains. To address this, we introduce topological flow matching, a topology-aware generalization of flow matching. We interpret flow matching as a framework for solving a degenerate Schrödinger bridge problem and inject topological information by augmenting the reference process with a Laplacian-derived drift. This principled modification captures the structure of the underlying domain while preserving the desirable properties of flow matching: a stable, simulation-free objective and deterministic sample paths. As a result, our framework serves as a drop-in replacement for standard flow matching. We demonstrate its effectiveness on diverse structured datasets, including brain fMRIs, ocean currents, seismic events, and traffic flows.

---


### 267. [The Missing Layer: Why EdTech Needs Design-Time Generative UI, Not Just Runtime Personalization](https://arxiv.org/abs/2606.15902)

**<font color=#1a73e8>作者：</font>** Seyed Parsa Neshaei, Abhinand Shibu, Fatma Betül Güres  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The dominant paradigm in using generative UI (GenUI) for adaptive EdTech considers the use of AI as a runtime engine: content is authored once in a fixed form, and AI adapts delivery dynamically based on learner needs, behaviors, or profiles. We argue that this paradigm has an issue: it moves the burden of accessibility and representation diversity onto systems that see learners only after content has already been locked into particular details. For learners who might need audio-first, simplified text, interactive, or low-bandwidth representations, runtime adaptation is too late and too costly to be equitable at scale, and might lead to inaccurate learning content due to the inability to conduct verification at scale. We propose an alternative method: accessibility belongs in the authoring layer. Specifically, we advocate for a card-based GenUI paradigm, in which educational content is encoded as modality-agnostic semantic units, and GenAI produces multiple interface representations, such as interactive, audio, text-simplified, or low-bandwidth, at learning design time to be verified by the instructor before it reaches any learner. This shifts the AI intervention from delivery to creation, embeds Universal Design for Learning principles into the authoring workflow, and removed per-learner inference costs. We situate this idea against recent work on GenUI, multimodal content generation, adaptive authoring, and equitable delivery, and argue that realizing this goal requires closer integration of AI, HCI, and learning sciences than what either of those communities has so far provided.

---


### 268. [Control-Plane Placement Shapes Forgetting: An Architectural Study of Agent Memory Across Thirteen System Configurations](https://arxiv.org/abs/2606.15903)

**<font color=#1a73e8>作者：</font>** Dongxu Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Where an LLM sits in an agent memory pipeline -- between the recall plane that retrieves stored facts (extensively benchmarked) and the control plane that mutates them via supersede, release, purge (largely untested) -- shapes which forgetting failure modes the system recovers. Comparing thirteen system configurations on a 385-case adversarial surface, we observe three placement regimes with partly complementary coverage: deterministic primitives suffice for lexical/temporal categories but fail canonicalization (5% on identifier-obfuscation, 0% on cross-lingual); inscribe-time LLM recovers canonicalization (100%) but cannot help intent-aware deletion (0% on prefix-collision and compound-fact); a mutation-time hook recovers intent-aware deletion (78-85%) and brightens nearly all categories simultaneously (91.7-93.2% overall, $0.17 per 385-case run, 2.3s/case mutation latency vs. 64-191ms/case deterministic, recall path unchanged).
We expose the trade-off via ForgetEval, a 1000-case templated suite plus a 385-case adversarial layer (132 hand-crafted + 253 LLM-drafted oracle-validated) scored by deterministic substring match, paired with a six-method Adapter Protocol with honest N/A scoring that lets heterogeneous memory stores enter in 130 lines. Admission is corroborated by 10-annotator IAA (Fleiss' kappa = 0.958) and a 77-case external-authored subset (four blind contributors) that replicates the canonicalization asymmetry and amplifies the joint-placement lift (+27.8 pt). Production failures are predominantly forgetting failures rather than recall failures, yet existing benchmarks measure only recall. ForgetEval and all adapters are released under MIT.

---


### 269. [High-Fidelity 4D Hand-Object Capture via Multi-View Spatiotemporal Tracking and Physics-Aware Gaussians](https://arxiv.org/abs/2606.15908)

**<font color=#1a73e8>作者：</font>** Bo Peng, Xu Chen, Yi Gu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The growing demand for high-fidelity 4D hand-object interaction (HOI) data in embodied AI and spatial computing is currently bottlenecked by the reliance on pre-scanned object templates and physical markers. While recent methods have demonstrated promising results in reconstructing 4D hand-object interaction from videos, they are highly sensitive to initial estimates of hand and object poses. Yet, estimating these poses from images is challenging, in particular under severe occlusion which is inherent in hand-object interaction scenarios. We propose a novel system for the robust and accurate reconstruction of hands and objects from synchronized and calibrated multi-view videos without requiring any templates or markers. Our system consists of two main components with key innovations: (1) a multi-view feed-forward transformer model that aggregates cross-view geometry and temporal cues to provide a reliable, metric-consistent initialization for both poses and dense object geometry, and (2) a hand-object physics-aware Gaussian-based optimization framework to refine the initial estimates, integrating tetrahedral constraints, collision refinement, and appearance decomposition to produce physically plausible and visually accurate reconstruction. Validated on public benchmarks and an extensive internal dataset, our pipeline achieves highly robust, artifact-free reconstruction, providing an efficient foundation for automated 4D asset generation. Our project page are available at this https URL.

---


### 270. [On-Policy Distillation with Curriculum Turn-level Guidance for Multi-turn Agents](https://arxiv.org/abs/2606.15912)

**<font color=#1a73e8>作者：</font>** Gengsheng Li, Mao Zheng, Mingyang Song 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-turn agents that plan, invoke tools, and interact with environments offer a promising paradigm for solving complex tasks, yet their capabilities typically rely on very large models whose inference cost is prohibitive in this http URL-Policy Distillation (OPD) is a natural recipe for transferring such capabilities to smaller students, but we find that it suffers a characteristic failure mode in this setting: small student errors compound across turns and push the trajectory out of the teacher's familiar state distribution, so the teacher's supervision becomes least reliable precisely where the student needs it this http URL propose Guided On-Policy Distillation (Guided-OPD), a simple yet effective algorithm that mixes teacher- and student-generated turns within each rollout and schedules the teacher's intervention probability along a curriculum that decays to this http URL guidance keeps early trajectories close to the teacher distribution and is then gradually withdrawn to recover the purely on-policy regime used at this http URL ALFWorld, ScienceWorld, and WebShop, distilling Qwen3 students from a Qwen3-30B-A3B teacher, Guided-OPD improves Score by 21.1\% and Success Rate by 25.5\% over vanilla OPD on average, with larger gains on smaller students.

---


### 271. [TurboGS: Accelerating 3D Gaussian Splatting via Error-Guided Sparse Pixel Sampling and Optimization](https://arxiv.org/abs/2606.15924)

**<font color=#1a73e8>作者：</font>** Zheng Dong, Daifei Qiu, Pinxuan Dai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Consumer-level applications require fast optimization of 3D Gaussian Splatting (3DGS) with high-fidelity novel view rendering. However, existing 3DGS acceleration approaches still incur substantial computation on redundant pixels while sacrificing fine details. In this paper, we present TurboGS, an error-guided training framework that accelerates 3DGS by concentrating optimization on perceptually informative pixels. TurboGS is built upon four core components: (1) a tile-wise sparse pixel sampling, which, driven by multi-view reconstruction errors during training, prioritizes challenging regions and skips well-reconstructed ones to avoid redundant gradient computation; (2) a tile-wise structure-aware loss with sparse Normalized Cross-Correlation, which provides sparse yet effective supervision to preserve fine details and stabilize training; (3) an error-driven Gaussian density control strategy, which dynamically allocates model capacity and removes redundant primitives; and (4) a tailored hybrid optimizer that couples Hessian-informed updates with Adam moment damping to stabilize and improve convergence under sparse supervision. Experiments on standard benchmarks demonstrate that TurboGS can deliver on par or superior rendering quality within 100 seconds on a single RTX 5090 GPU card (up to 10x training speedup over vanilla 3DGS).

---


### 272. [An Exploratory Study of Blood Glucose Estimation from Photoplethysmography Signals using Machine Learning](https://arxiv.org/abs/2606.15927)

**<font color=#1a73e8>作者：</font>** Ruhani Bhatia, Vijval Ekbote  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diabetes and extreme blood sugar levels are some of the major health problems faced by humans today across the world. While Continuous Glucose Monitoring (CGM) has emerged as an effective technology for management of diabetes as well as for monitoring blood sugar levels, this technology has traditionally been invasive (that is, requiring the piercing of the skin) and carries the risk of irritation, induration, etc. This highlights the need for accurate and non-invasive CGM methods that can be deployed at scale. With the emergence of various sensing technologies and their integration in wearables like the smart-watch, we now have the capability to continuously monitor body signals like the Photoplethysmogram (PPG) in a non-invasive manner. Having the ability to continuously monitor blood glucose through CGMs and continuously monitor PPG signals through a smart-watch offers an opportunity to get dense data on these two, opening the possibility of building machine learning and deep learning based models to estimate blood glucose level from PPG signals. In this work, we first present a paired dataset comprising continuous PPG signals from a smartwatch along with glucose values recorded using a CGM device. We also present the results of some preliminary experimental explorations performed on our dataset. These preliminary results suggest that some predictive signals may exist, though more exploration is needed with more data from a larger number of individuals. The dataset can be accessed at this https URL

---


### 273. [DeepRoot: A KG-Coordinated Multi-Agent System for Therapeutic Reasoning over Historical Medical Texts](https://arxiv.org/abs/2606.15931)

**<font color=#1a73e8>作者：</font>** Zijian Carl Ma, Sean J. Wang, Sijbren Kramer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Historical medical archives and traditional medicines hold immense potential for drug discovery and remain a primary source for current drug development. However, pre-ontological prose and idiosyncratic taxonomies prevent the standardization and medical modernization of the data for use in current biomedical pipelines. Furthermore, no existing LLM agent system, whether tool-calling, retrieval-augmented, or agentic deep-research, can convert such text into verifiable drug-discovery leads at scale. We close this gap with DeepRoot, a multi-agent LLM system that jointly builds and utilizes a verified knowledge graph, showing that grounding and reasoning -- often conflated -- are separable axes the system can compose for therapeutic reasoning. Applied to the Shen Nong Ben Cao Jing, DeepRoot recovers $10$ of $21$ held-out compound-disease treatment pairs at R@$20$ ($47.6\%$ vs $4.8\%$ for a raw corpus LLM and $\sim\!2.4\%$ random) and dominates an LLM-as-judge audit for reasoning quality over baseline LLMs and LLMs with direct tool-call access to the same APIs DeepRoot itself queries. Tool-using LLMs hallucinate evidence on $87\%$ of claims, versus 7-10% for DeepRoot. Graph-only inference hallucinates $0\%$ but ranks lowest on reasoning coherence; DeepRoot KG+LLM is the only condition to win on both axes, pointing toward a route for systematic mining and repurposing of historical medical knowledge.

---


### 274. [GOOSE-M2F: Adapting Mask2Former for High-Fidelity, Long-Tailed Fine-Grained Semantic Segmentation in Unstructured Outdoor Terrain](https://arxiv.org/abs/2606.15937)

**<font color=#1a73e8>作者：</font>** Jyothiraditya Lingam, Nikhileswara Rao Sulake, Sai Manikanta Eswar Machara  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present GOOSE-M2F, a task-specific adaptation of Mask2Former for the GOOSE 2D Fine-Grained Semantic Segmentation (FGSS) Challenge at ICRA~2026. The GOOSE benchmark spans 64 fine-grained classes across unstructured outdoor terrain with a severely long-tailed distribution, where rare classes occupy fewer than 50 pixels per image. We extend the Swin-Large Mask2Former baseline with three targeted contributions: (1)200 Object Queries to eliminate representational saturation; (2)a Feature Refinement Module (FRM) combining ASPP-lite and CBAM dual-attention; and (3)an Auxiliary Supervision Head that delivers direct per-pixel gradients for rare classes. A multi-stage training strategy pairs Distribution-Balanced loss, Rare-Class Copy-Paste augmentation, dynamic IoU-aware re-weighting, and EMA. At inference, a dense sliding-window engine with 2D Gaussian kernel blending and 4-scale TTA adds +10.57\%. GOOSE-M2F achieves 70.08\% Official Composite mIoU (63.55\% fine, 76.61\% coarse), placing 3rd on the GOOSE 2D FGSS leaderboard. Code and trained models are publicly available at: \href{this https URL}{Github GOOSE-M2F Code} and \href{this https URL}{Hugging Face GOOSE-M2F}.

---


### 275. [Learning Directional Semantic Transitions for Longitudinal Chest X-ray Analysis](https://arxiv.org/abs/2606.15938)

**<font color=#1a73e8>作者：</font>** Zhangfeng Hu, Zefan Yang, Ge Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chest X-ray (CXR) interpretation often requires longitudinal comparison to assess disease progression. Existing approaches typically rely on temporal feature fusion or inter-study discrepancy modeling, yet remain limited in capturing subtle progression semantics and overlook the inherently directional nature of disease trajectories. In this paper, we propose ProTrans, a novel vision-language pretraining framework that formulates disease progression as a directional semantic transition between paired CXR studies. ProTrans leverages radiology reports to anchor individual CXR representations within interpretable disease states, and introduces a learnable progression feature map to explicitly encode semantic shifts between states, aligned with report-derived progression descriptions. To enforce direction-aware perception, ProTrans incorporates a reversed temporal modeling process and imposes bidirectional reconstruction consistency across states and transitions, thereby disentangling directional semantics and promoting coherent trajectory modeling. Extensive experiments on longitudinal downstream tasks, including disease progression classification and progression captioning, demonstrate that ProTrans consistently outperforms existing methods, establishing a unified pretraining framework for longitudinal CXR understanding. this https URL

---


### 276. [Causal-Privacy Audit Workflow for Synthetic and Distilled Data in Dropout Support](https://arxiv.org/abs/2606.15940)

**<font color=#1a73e8>作者：</font>** Hanghang Zheng, Xiwei Zhuang, Zhong Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic and distilled student data are increasingly used to enable privacy-conscious learning analytics, yet their suitability for decision-facing institutional support remains uncertain. In dropout support, generated data must preserve not only predictive utility or distributional resemblance, but also the financial-status evidence used to guide advising, payment-plan assistance, and scholarship-related decisions. Method: This study introduces CaP-Eval, a decision-facing causal-privacy audit workflow for evaluating generated student data under a fixed estimand, timing-aware adjustment design, estimator set, and empirical privacy-governance screen. The workflow compares original, distilled, adversarial synthetic, statistical synthetic, and DPGNet privacy-oriented generated data on predictive utility, treatment-effect fidelity, robustness to alternative estimators, and local training-record proximity. Results: DPGNet and distilled data preserved the original financial-status treatment-effect structure more reliably than the adversarial and Gaussian Copula baselines. DPGNet preserved full direction and rank agreement across epsilon levels; epsilon = 10 produced the smallest non-original IPW and DML deviations, while epsilon = 1 and epsilon = 5 amplified several financial-status contrasts. Distilled data remained highly faithful but retained the strongest local training-record proximity signal. TabularGNet preserved qualitative directions with moderate attenuation, and Gaussian Copula compressed effect magnitudes. Conclusions: Predictive utility, privacy orientation, empirical disclosure signals, and causal fidelity diverged; generated student data require joint audits of direction, magnitude, overlap, and release-governance risk before decision use.

---


### 277. [FinBalance: A Multi-Document Accounting Reconciliation Benchmark](https://arxiv.org/abs/2606.15949)

**<font color=#1a73e8>作者：</font>** Sasank Tumpati, Devansh Agarwal, Ayush Kedia 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing financial-NLP benchmarks mostly evaluate prepared artifacts such as filings, tables, or extracted values. Real accounting begins earlier: source documents must be reconciled into cited journal entries, aggregated into a balance sheet, and checked for contradictions. We introduce FinBalance, a multi-document accounting reconciliation benchmark built from source-document bundles across eight industries, three period types, and five difficulty levels. Human-authored business scenarios, accounting policies, tax/FX treatments, document schemas, distractors, and inconsistency templates are composed by a deterministic generator whose ledger produces journal entries,balance sheets, and 23 inconsistency-code labels. On a 710-record evaluation split, six contemporary LLMs reach at most 46% exact final-balance-sheet accuracy. Four models show a 26-41 pp gap between BS_exact, the model's reported balance sheet, and BS_recon, the balance sheet obtained by replaying its entries through our ledger. Models often recover numerically plausible entries but fail to bind them to supporting documents and aggregate them consistently. Citation-pressure prompting barely changes document-linking errors, while ledger-feedback ablations substantially improve reported balance sheets and expose inconsistency-detection trade-offs. Expert finance reviewers validate the benchmark design and labels.

---


### 278. [You Don't Need Strong Assumptions: Visual Representation Learning via Temporal Differences](https://arxiv.org/abs/2606.15956)

**<font color=#1a73e8>作者：</font>** Ninad Daithankar, Alexi Gladstone, Yann LeCun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Progress in AI has largely been driven by methods that assume less. As compute and data increase, approaches with weaker inductive biases generally outperform those with stronger assumptions. This is particularly characteristic of the field of Visual Representation Learning, where approaches have gone from being dominated by Supervised Learning, to Weakly Supervised Learning, to the now widespread success of Self-Supervised Learning without human labels. Yet, even modern Self-Supervised Learning approaches still depend on strong inductive biases such as augmentations, masking, or cropping. If this trend holds, even these remaining biases should become bottlenecks at scale -- and our experiments confirm this: the optimal strength of inductive biases decreases as data grows. This motivates the search for approaches that rely on fewer assumptions. To this end, we introduce Temporal Difference in Vision (TDV), a new paradigm for self-supervised learning from video that avoids existing inductive biases, relying instead on a causal assumption that the past causes the future. TDV functions by jointly training an image encoder and a motion encoder so that the current frame's representation plus the encoded motion equals the next frame's representation. Despite not leveraging any strong inductive biases, TDV matches state-of-the-art recipes on dense spatial tasks, laying the foundation for representation learning without strong assumptions.

---


### 279. [VEPHand: View-Efficient Photometric Hand Performance Capture at Scale](https://arxiv.org/abs/2606.15966)

**<font color=#1a73e8>作者：</font>** Zhengyang Shen, Kai-Hung Chang, Erroll Wood 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust, high-fidelity 3D hand capture, while fundamental to digital human creation, remains challenging with practical multi-view systems that balance rich photometry with the geometric ambiguities of reconstruction arising from limited viewpoint density. This paper presents an end-to-end pipeline for dynamic hand performance capture and registration, specifically designed for view-efficient setups ($\sim$20 views). We address key challenges with two primary innovations. First, to overcome reconstruction difficulties like limited view overlap and background clutter, our mask-free neural method robustly extracts detailed hand geometry and appearance from unmasked images using scene parameterization and scenario-specific density regularization. Second, addressing registration challenges such as accurately capturing non-linear skin deformations and ensuring plausible results during severe self-contact, we propose a physics-inspired framework. It aligns reconstructions to a personalized hand model by optimizing intrinsic volumetric offsets within its canonical tetrahedral mesh, alongside pose parameters. This approach, supported by robust losses and optimization, captures fine surface deformations, ensures plausible results under severe articulation and self-contact, and demonstrates strong tolerance to input noise. We demonstrate the scalability and robustness of our automated pipeline on an extensive dataset of over 12,000 sequences, from which we also derive a large-scale, high-quality synthetic 2D/3D hand dataset for training downstream tasks. This showcases its effectiveness for single hands, intricate two-hand interactions, and natural hand-object manipulations. Our method achieves state-of-the-art reconstruction fidelity in view-efficient, unmasked scenarios and highly accurate registration. Our project page are available at this https URL.

---


### 280. [CRIS: Cross-Plane Self-Supervised Isotropic Restoration for Anisotropic Volumetric Imaging Across Modalities](https://arxiv.org/abs/2606.15967)

**<font color=#1a73e8>作者：</font>** Adi Ahituv, Anat Ilivitzki, Moti Freiman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anisotropic volumetric acquisitions are common in clinical MRI and volume electron microscopy (vEM), where sparse through-plane sampling creates thick slices or sections that degrade orthogonal reformats and downstream analysis. We present CRIS, a cross-plane self-supervised framework for isotropic restoration without paired isotropic ground truth. CRIS casts 3D restoration as 2D stripe completion on orthogonal reformats of an isotropic grid: high-resolution in-plane slices are synthetically degraded and periodically masked for training, while at inference blank slices define the isotropic grid, two orthogonal reformats are restored, and predictions are fused by multi-view averaging. We evaluate CRIS on two MRI cohorts and two microscopy benchmarks up to 8x anisotropy. On brain MRI, CRIS achieves 32.921 +/- 0.436 dB PSNR and 0.9631 +/- 0.0027 SSIM, outperforming interpolation, SMORE4, SIMPLE, SA-INR, and ATME, and gives the best segmentation consistency (Dice 0.940 +/- 0.004, ASSD 0.245 +/- 0.014 mm, HD99 1.275 +/- 0.061 mm). On reference-free abdominal MRI, CRIS reduces FID/KID to 48.714/0.023. On vEM, CRIS outperforms interpolation, NIIV, and vEMINR, reaching 29.133 dB/0.834 3D PSNR/SSIM at 4x, 27.123 dB/0.734 on EPFL at 8x, and 21.915 dB/0.699 on noisy hemibrain data. In a robustness experiment, one variable-gap CRIS model evaluated across gap factors 3--7 and coronal, axial, and sagittal degradations maintained higher PSNR/SSIM than interpolation (36.36--31.14 dB and 0.977--0.932 vs. 33.07--27.85 dB and 0.951--0.853). These results support CRIS as a modality-flexible route to isotropic restoration without paired isotropic targets or configuration-specific retraining. Code is available at this https URL.

---


### 281. [HadBalance: A Plug-and-Play Unified Global Geometric Prior Framework for Generalizable Biomedical Segmentation](https://arxiv.org/abs/2606.15976)

**<font color=#1a73e8>作者：</font>** Zhuangzhi Gao, Feixiang Zhou, He Zhao 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise biomedical image segmentation is crucial for clinical diagnosis. Geometric cues (e.g., boundary, shape, and topology) can improve structural consistency, yet most are task-specific and lack a unified geometric foundation that generalizes across organs and modalities. We are motivated by the observation that several medical segmentation targets can be approximated as globally near-convex shapes. A convex region is one in which any two interior points can be connected by a line segment entirely contained within the region. In practice, medical targets may exhibit small local concavities or boundary irregularities; we refer to such globally convex-like shapes as near-convex. Motivated by this, we derive Hadwiger Shape Priors from Hadwiger's theorem as an interpretable global regularizer using three 2D measures: area A, perimeter P, and Euler characteristic chi, enabling transfer across organs and modalities. However, because medical datasets are shape-heterogeneous, enforcing near-convex priors uniformly can over-regularize non-convex anatomy with significant concavities, washing out concavities and fine details and degrading segmentation accuracy. To address this challenge, we propose Conflict-Aware Objective Balancing (CAOB), which integrates shape priors with segmentation in a gradient-aware manner. For each prior, CAOB removes only the gradient component that conflicts with segmentation while preserving the remaining aligned component, and adaptively regulates objective influences to prevent prior dominance. This enables stable use of shape priors on shape-heterogeneous data without erasing genuine concavities or fine structural details. We call this plug-and-play framework HadBalance.

---


### 282. [Scalar-Stepsize Nonuniform Monte Carlo Optimistic Policy Iteration: A Certified Counterexample](https://arxiv.org/abs/2606.15978)

**<font color=#1a73e8>作者：</font>** Yuanlong Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tsitsiklis proved convergence of Monte Carlo optimistic policy iteration under a uniform update structure and identified nonuniform update frequencies as a delicate obstruction. We give a certified negative answer for the natural scalar-stepsize, unnormalized asynchronous state-value recursion with fixed nonuniform state-selection probabilities. In a three-state, two-action discounted MDP, the nonuniform update frequencies induce a diagonally scaled greedy-policy mean field with a certified nonconstant attracting hybrid periodic orbit. With a bounded unbiased geometric-horizon estimator and Robbins--Monro stepsizes, the original stochastic recursion remains trapped near the cycle with positive probability and therefore fails to converge. The example pinpoints a geometric obstruction: uniform sampling gives radial residual contraction, whereas scalar nonuniform sampling anisotropically distorts the residual dynamics and can generate switched attracting cycles.

---


### 283. [Do Safety Monitors Stay Reliable After an Update? Benchmarking and Predicting Activation-Monitor Staleness](https://arxiv.org/abs/2606.15980)

**<font color=#1a73e8>作者：</font>** Evan Duan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation monitors-lightweight probes trained on a language model's internal representations-are an increasingly common layer in deployment safety stacks. Deployed models however are rarely static: they are quantized, fine-tuned, adapted with LoRA, or served with merged adapters while the monitor remains frozen. We present the first systematic test of whether this implicit contract holds: whether activation monitors trained on a base model remain reliable after these routine model updates. Across multiple safety-relevant monitors, model depths, update families, and open-weight models, we find a sharp split: quantization-style updates largely preserve frozen probe performance, while fine-tuning-style updates frequently make probes stale. Fragility is highly monitor-dependent, with privacy/PII probes most affected and refusal-compliance probes comparatively stable, showing that retraining a behavior need not stale its corresponding monitor. QLoRA is especially damaging despite NF4 quantization alone being relatively benign, suggesting that quantization becomes riskier when combined with adaptation. We further show that degradation is predictable from pre-deployment features, enabling revalidation budgets to be triaged toward the monitors most likely to fail. These results suggest that fine-tuning should trigger activation-monitor revalidation by default, while prediction can help prioritize which monitors to check first.

---


### 284. [Mind the Gap: Diagnosing Constraint Discovery Failures in Text-in-Image Editing](https://arxiv.org/abs/2606.15982)

**<font color=#1a73e8>作者：</font>** Rui Gui  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A key challenge in multimodal reasoning is determining which visual dependencies become relevant under a specific task, rather than merely recognizing visible content. We study this through edit-induced constraint discovery in text-in-image editing, a controlled diagnostic setting where a local text change can activate secondary consistency constraints: given a valid editing instruction and an image, can a model identify the secondary regions that must also change? Across 461 diagnostic cases, four MLLMs, and 19 constraint subtypes, models recover only 46% case-level macro recall under unguided prompting versus 94% when constraints are explicitly provided, suggesting that a substantial portion of the failure arises when models must decide which unstated dependencies to surface. Oracle-field decomposition shows that case-specific causal explanations are the most effective partial guidance (0.782 recall), above region names (0.610) or type labels (0.646), suggesting that edit-specific causal cues account for much of the oracle gain. A downstream experiment further shows that higher self-discovery recall does not necessarily improve task performance: unverified self-discovery introduces false positives that offset recall gains, motivating precision-aware constraint elicitation.

---


### 285. [ROMPAR: Morphological Completion and Demographic Unlearning for Romanian-Accented Speech Recognition](https://arxiv.org/abs/2606.15984)

**<font color=#1a73e8>作者：</font>** Andrei-Marius Avram, Aureliu-Valentin Antonie, Ştefan-Bogdan Badea 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated transcription of parliamentary proceedings faces significant hurdles due to demographic bias, dialectal variation, and technical artifacts such as utterance truncation during segmentation. This paper introduces the ROManian PARliamentary Speech Corpus (ROMPAR) dataset, a 17.80-hour corpus of Romanian and Moldavian parliamentary speech, featuring double-annotated ground truth and explicit labels for reconstructed word fragments. To build a robust ASR system, we propose a multi-task adversarial training framework that enforces demographic invariance across age, gender, and dialect. We address the inherent instability of adversarial objectives in generative architectures by introducing an exponential decay mechanism for the adversarial coefficients. Furthermore, we implement an LLM-guided decoding strategy with position-dependent weighting to facilitate morphological completion of truncated terminal words. Our results demonstrate that the proposed framework significantly reduces WER and achieves an F1-score of 96.6% in morphological reconstruction.

---


### 286. [A Text Recognition Dataset from Sahidic Coptic Ancient Manuscripts](https://arxiv.org/abs/2606.15987)

**<font color=#1a73e8>作者：</font>** Fabio Quattrini, Carmine Zaccagnino, Costanza Bianchi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we target Handwritten Text Recognition (HTR) in low-resource scenarios, which arise from underrepresented languages, rare scripts, and degraded visual conditions typical of historical documents. We introduce SCAM (Sahidic Coptic Ancient Manuscripts), a new line-level dataset built from digitized ancient manuscripts written in the extinct Sahidic Coptic dialect. The dataset reflects a realistic and challenging setting, as it combines heterogeneous acquisition conditions across libraries with typical manuscript degradations such as ink fading, bleed-through, and material deterioration. In addition to visual complexity, SCAM poses significant linguistic challenges due to the scarcity of resources for Sahidic Coptic, its uncommon alphabet, and dialect-specific diacritics. To support research in low-resource HTR, we benchmark several state-of-the-art approaches based on different paradigms, highlighting their limitations and strengths in this setting. Our results underline the gap between current HTR performance on well-resourced modern scripts and historically grounded, low-resource scenarios, thus providing a reference point for future developments.

---


### 287. [Multi-Task Tennis Stroke Biomechanics Analysis Using MediaPipe Pose](https://arxiv.org/abs/2606.15992)

**<font color=#1a73e8>作者：</font>** Jigyashman Hazarika  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We built a multi-task pipeline for tennis stroke biomechanics from plain RGB video. On top of pose-based stroke recognition, it adds two new tasks, predicting shot direction and grading posture quality, plus a rule-based feedback layer that suggests coaching tips. Strokes are found automatically using a weighted joint velocity score, s(t) = 0.5 v_wrist + 0.3 m_elbow + 0.2 m_shoulder, removing the need for manual annotation. Pose comes from MediaPipe Pose Landmarker (33 landmarks, metric world coordinates), with each stroke turned into a 30-frame by 39-feature sequence for TennisTransformerGPU, a compact 564,103-parameter transformer (4 layers, 4 heads, d=128) with three parallel output heads. Trained on 1,281 labeled strokes from 7 pros and 1 amateur across 11 videos, it hits 83.7% stroke-type accuracy, 61.9% on direction, and 62.6% on posture under a random 80/20 split. The interesting test is cross-player: train on pros, evaluate on the amateur. Stroke type barely budges, 82.9%, a 0.8% drop. Direction prediction does not transfer; it just falls back to the majority class. An ablation shows why world coordinates matter so much here: switching to image-space landmarks tanks cross-player stroke-type accuracy from 83% to 47% and direction from 68% to 21%. Everything runs on Kaggle's free T4 GPU tier and is fully reproducible.

---


### 288. [GRACE-DS: a Guarded Reward-guided Agent Correction Environment in Data Science](https://arxiv.org/abs/2606.16000)

**<font color=#1a73e8>作者：</font>** Aleksandr Tsymbalov, Danis Zaripov, Artem Epifanov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce GRACE-DS, a Guarded Reward-guided Agent Correction Environment in Data Science for pre-deployment evaluation of LLM-powered AutoML agents. GRACE-DS is a set of evaluation metrics in an isolated environment that can be applied to tabular ML tasks specific to a particular organization. It exposes agents to realistic workflow stages, from planning and data inspection through feature engineering, model development, validation, and code repair to final submission, while hidden executable validators measure not only final predictive performance but also leakage avoidance, reproducibility, protocol validity, correction behavior, and reward alignment. The strongest structured regime, flexible iterative interaction (our approach), achieves higher end-to-end normalized hidden-test quality than single-shot generation, unstructured interaction, and restart-based baselines, while also improving protocol-valid completion. Validated across more than 7,000 episodes, these results establish GRACE-DS as a robust platform for assessing the capacity of LLM-based AutoML agents to execute machine learning workflows under production-like conditions and in accordance with organization-specific requirements.

---


### 289. [Decomposing one-class support vector machine into an ensemble of one-data support vector machines](https://arxiv.org/abs/2606.16002)

**<font color=#1a73e8>作者：</font>** Toshitaka Hayashi, Dalibor Cimr, Hamido Fujita 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One-class classification (OCC) is a classification problem in which the training data contains only one class. The one-class support vector machine (OCSVM) is one of the most competitive OCC algorithms. However, OCSVM has scalability issues with large-scale datasets. This paper proposes the acceleration strategy of OCSVM. The idea is to decompose the dataset into samples and train OCSVM models for single data points. Subsequently, ensemble learning is applied to combine all models to compute the OCSVM model for the dataset. In addition, further acceleration is achieved through a data-reduction strategy with an OCSVM model trained on the average of the training samples. The experiment compared the proposal and traditional OCSVM using the Python package. The proposed strategy is faster than traditional OCSVM, while achieving similar classification results. Moreover, the proposed strategy can create one-to-one correspondence between samples and models. Source code is uploaded at this https URL

---


### 290. [Bridging the Usability Gap: Lessons from Interpreting Studies for Machine Interpreting Design](https://arxiv.org/abs/2606.16009)

**<font color=#1a73e8>作者：</font>** Claudio Fantinuoli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine interpreting (MI), the live, real-time branch of speech translation, has achieved remarkable progress on standard benchmarks, with some systems approaching human parity on textual fidelity. Yet the user experience remains far inferior to interpreter-mediated communication, revealing what we term the \emph{accuracy illusion}: systems that appear accurate on paper but fail in practice to support smooth, goal-oriented interaction. This paper defines MI as a distinct subfield of speech translation, with its own characteristics and the need for evaluation methods grounded in communicative effectiveness rather than isolated fidelity metrics. Drawing on insights from interpreting studies, we identify critical dimensions of professional interpreting practice that are overlooked by current systems, and consolidate them into three interdependent design priorities for future MI: \emph{agency} (context-sensitive initiative and repair), \emph{grounding} (multimodal and discourse-level situational awareness), and \emph{experience} (adaptive improvement through real interaction). Together, these priorities chart a path toward closing the usability gap and enabling systems that can sustain authentic multilingual communication in real time.

---


### 291. [Stringalign: Moving beyond summary statistics with a transparent Unicode-aware tool for evaluating automatic transcription models](https://arxiv.org/abs/2606.16015)

**<font color=#1a73e8>作者：</font>** Yngve Mardal Moe, Marie Roald  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Comparing text strings is crucial when evaluating and understanding the performance of various text processing tasks such as document recognition and audio transcription. With an increasingly complex landscape of AI-based handwritten text recognition (HTR), optical character recognition (OCR) and automatic speech recognition (ASR) models, there is a need for tools that facilitate evaluation in a flexible and reproducible way. This paper presents Stringalign, a Python library designed to simplify the evaluation process for automatic transcription projects and facilitate transparent evaluation. Stringalign's tools to examine and visualise both the rate of errors and the types of errors a model makes, give insights into possible improvements and help inform model selection for a particular task. Widely used string comparison metrics, such as the character and word error rates (CER and WER), although useful, can be ambiguous due to varying definitions of what constitutes a character and a word. Stringalign addresses this challenge by ensuring all preprocessing (i.e. normalisation and tokenisation) is transparent and easily replicable, and by providing tools to move beyond summary statistics and analyse common model errors. Moreover, Stringalign adheres to FAIR (Findable, Accessible, Interoperable, and Reusable) principles for research software while staying lightweight and easy to adapt into researchers existing workflows. In this paper, we discuss challenges with character and word level string comparisons and show through examples that where existing tools can yield opaque and sometimes confusing results, Stringalign provides an easy-to-use and unambiguous alternative.

---


### 292. [Scaling Human and G2P Supervision for Robust Phonetic Transcription](https://arxiv.org/abs/2606.16019)

**<font color=#1a73e8>作者：</font>** Alexander Metzger, Aruna Srivastava, Ruslan Mukhamedvaleev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Expert phonetic annotation is costly, especially for non-standard dialects and atypical speech. A common alternative is using Grapheme-to-Phoneme (G2P) models to auto-generate phonetic labels from text transcripts at scale. We study how automatic phonetic transcription performance scales with human and G2P supervision in English. Using a curated 80-hour benchmark spanning native, non-native and post-stroke speech, we identify a supervision quality threshold: G2P supervision helps only when fewer than 20-30 hours of human annotation are available. Beyond this threshold, it provides no significant benefit and can reduce cross-dialect robustness. What is effective after this threshold is ASR pretraining which we use to achieve a 2.3x reduction in weighted phone feature error rate over prior systems, with strong gains on non-native and aphasic speech. These results suggest that quantity-driven G2P scaling may yield diminishing returns for robust generalization.

---


### 293. [AI as a Sparring Partner -- an HCAI Approach to Promote Human Capabilities](https://arxiv.org/abs/2606.16020)

**<font color=#1a73e8>作者：</font>** Thomas Herrmann  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A systematic literature reveals that the role of AI as a sparring partner (SP) is often proposed but not systematically analyzed or defined. We propose the definition: An AI sparring partner (AI SP) interacts with users in a combination of a cooperative as well as a challenging, competitive mode, where AI is selected, customized or self-adapting to meet a level of skills that neither over- nor under-challenges the users. They can have the experience that they become better or are better than AI. AI as a SP can support creativity, extend viewpoints or foster learning and critical thinking either towards ideas and decisions or towards the AI itself. Sparring with AI can either be explicit, e.g. when AI simulates certain roles, or implicit, when AI is used to find out whether or how to perform better.

---


### 294. [Stickel-type key exchange with hidden subspaces](https://arxiv.org/abs/2606.16021)

**<font color=#1a73e8>作者：</font>** Fintan Costello, Paul Watts  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We give a witness-finding cryptanalysis of Stickel-type key exchange schemes, which involve two-sided multiplication of $n \times n$ matrices over $\mathbb{F}_p$, where these matrices are drawn from public subspaces with a particular commuting structure. This analysis covers Stickel's original proposal , Shpilrain's polynomial extension of that scheme, Nager's algebraic extension of that scheme, and more generally all Stickel-type approaches using public subspaces over matrix algebra in finite fields: all such schemes can be broken in polynomial time. We also describe a new key establishment scheme using two-sided matrix multiplication in which the commuting subspaces used to form the key are hidden via conjugation by private terms, blocking this specific public-subspace analysis; the witness-finding problem in this new scheme has a direct reduction from a standard NP-hard problem (Edmonds' problem).

---


### 295. [IBAD: Interpretable Behavioral Anomaly Detection on Human Mobility Data](https://arxiv.org/abs/2606.16023)

**<font color=#1a73e8>作者：</font>** Bita Azarijoo, John Krumm, Cyrus Shahabi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human mobility appears highly diverse, yet much of a person's daily mobility can be explained by a small set of recurring behavioral templates, such as commuting, school-centered activities, caregiving, nightlife, or errand patterns. We present \texttt{IBAD} (\underline{I}nterpretable \underline{B}ehavioral \underline{A}nomaly \underline{D}etection), a framework that learns interpretable daily mobility templates and represents each individual as a distribution over mixtures of these templates. Rather than focusing on specific locations, IBAD characterizes activities that individuals perform across locations. This approach first discovers global behavioral templates using Latent Dirichlet Allocation (LDA), then employs a hierarchical self-supervised model to learn normal behavior of individuals from their soft behavioral templates. We also introduce a \emph{splicing benchmark} that creates controlled behavioral mismatches between an individual's historical profile and injected mobility patterns. Experiments on real-world and synthetic datasets show that daily behavior can be effectively decomposed into a small number of interpretable templates. Crucially, we show that the learned behavioral archetypes \emph{transfer} across distinct geographic and demographic contexts. Furthermore, IBAD maintains a robust competitive performance across all settings. For reproducibility purposes, the code is accessible at ~\href{this https URL}{this https URL}.

---


### 296. [In-Domain Supervised Pathology Report Classification: A Reproducible Pipeline from Data Curation to Production-Matched Evaluation](https://arxiv.org/abs/2606.16026)

**<font color=#1a73e8>作者：</font>** Isaac Hands, Bin Huang, Adam Spannaus 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce an in-domain supervised pipeline designed to counter the out-of-distribution performance drop that hampers supervised biomedical NLP models, a problem observed when models trained on pathology reports are moved across cancer registries. Our contribution is a reproducible recipe for training a supervised classifier from routinely collected cancer registry data. It describes how to build the in-domain training set and a production-matched holdout, and to choose operating points that keep the false-negative rate (FNR) very low while keeping reviewer workload manageable. The pipeline standardizes data curation with facility-stratified sampling and separate handling of reports linked to registry cases, and includes a blinded manual audit to estimate positive-case prevalence and label noise. On a 418k-report holdout set, the Kentucky model achieved FNR 0.003 and false-positive rate (FPR) 0.097, improving over the Seattle-trained MOSSAIC OncoID baseline (FNR 0.010, FPR 0.183) and raising F1 from 0.860 to 0.922. In a blinded manual review of 600 reports, estimated positive prevalence declined from 0.500 to 0.398, indicating substantial label noise with errors concentrated in rare primary sites.

---


### 297. [The Information-Theoretic Benefit of Shared Representations under Orthogonality Constraints](https://arxiv.org/abs/2606.16028)

**<font color=#1a73e8>作者：</font>** Thomas Dittrich, Oliver Potocki, Philipp Grohs  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern deep learning architectures are increasingly multi-task and multi-modal, using a pretrained foundation model combined with task-specific, fine-tuned models. Empirically, exploiting similarity across different problems, instead of solving them individually, can significantly improve overall performance. While the generalization and sample complexity properties of multitask learning have been widely studied, the parametric complexity of joint approximation in comparison to separate approximation remains less well understood. The question is particularly relevant in modern deep learning, where models are increasingly required to satisfy structural constraints such as equivariance, conservation laws, or orthogonality. We prove lower and upper bounds on the description-length for separate and joint approximation classes, respectively, in uniform norm. We build a class of orthogonal functions by composing a shared hard feature, realized by a Rademacher-Haar wavelet series, with Sawtooth-Walsh readouts to enforce orthogonality of output coordinates. The dyadic tree structure of the Rademacher-Haar wavelet concentrates the approximation hardness in the common feature component, while the readouts act as task-specific heads. Using an information-theoretic framework, we obtain a sharp gap between the optimal approximation rates achievable by joint and separate coding. Finally, we realize this separation in a neural network model using Heaviside activations via reduction to triangle-wave approximation. Our results show that even under an orthogonality constraint joint approximation requires strictly fewer bits in compositional architectures, provided the tasks share a latent hard feature. This provides theoretical insight into the description-length-efficiency of compositional multi-output architectures and clarifies how neural networks can retain expressivity under geometric constraints.

---


### 298. [The Third Challenge on Image Denoising at NTIRE 2026: Methods and Results](https://arxiv.org/abs/2606.16031)

**<font color=#1a73e8>作者：</font>** Lei Sun, Hang Guo, Bin Ren 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper reports on the NTIRE 2026 Challenge on Image Denoising, specifically focusing on the high-noise regime ($\sigma = 50$). The competition investigates advanced neural architectures designed to restore high-fidelity details from images corrupted by additive white Gaussian noise (AWGN). Unlike constrained benchmarks, this track emphasizes peak quantitative performance, measured by Peak Signal-to-Noise Ratio (PSNR), without limitations on parameter count or computational overhead. By synthesizing contributions from 20 finalist teams out of 116 registrants, this report benchmarks the latest technical innovations and provides a comprehensive snapshot of the current state-of-the-art in unconstrained image restoration.

---


### 299. [Inference-Time Decision Calibration for Temporal Classification](https://arxiv.org/abs/2606.16034)

**<font color=#1a73e8>作者：</font>** Arthur Chagas, Arthur Buzelin, Yan Aquino 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal classification errors are often treated as representation failures, but they can also arise from how available evidence is converted into decisions. This paper proposes a representation--calibration decomposition for temporal classification. We keep a trained native classifier frozen and separate two inference-time interventions: a conservative residual multi-scale branch that adds auxiliary logits to the native prediction, and a post-hoc branch-aware calibrator that recombines native and residual evidence at decision time. This design distinguishes missing temporal evidence from underused decision-level evidence without retraining the backbone. Across FI-2010, PTB-XL, UCI-HAR, MHEALTH, and HARTH, we find that gains are strongly regime-dependent. Residual multi-scale evidence is most useful in noisy or representation-limited settings, especially short-horizon FI-2010 and weaker recurrent backbones, while branch-aware calibration helps when native and auxiliary logits contain complementary evidence not fully exploited by the raw decision rule. Near-saturated settings show limited gains from either intervention. These results suggest that temporal classification should be understood not only as representation learning, but also as the problem of trusting, combining, and calibrating evidence from multiple views.

---


### 300. [Trusting Right Predictions for Wrong Reasons: A LIME Based Analysis of Deep Learning Interpretability in Lung Cancer Diagnosis](https://arxiv.org/abs/2606.16036)

**<font color=#1a73e8>作者：</font>** Samarpan Poudel, Vladislav D Veksler  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lung cancer is the leading cause of cancer-related mortality, with approximately 2.5 million new cases and 1.8 million deaths annually, making reliable diagnosis a clinical priority. Although deep learning models have achieved strong performance in lung cancer classification, evaluation has largely focused on predictive accuracy, leaving their decision-making processes insufficiently examined. This study compares three architecturally distinct models: a Convolutional Neural Network (CNN), a pretrained ResNet50, and a Vision Transformer (ViT), trained on the IQ-OTH/NCCD lung cancer CT dataset. Local Interpretable Model-Agnostic Explanations (LIME) were applied to investigate model reasoning. In addition to standard performance metrics, a dual-correlation framework was introduced to measure both prediction agreement and explanation agreement across model pairs. All three models achieved strong classification performance, with ResNet50 attaining 98.61% accuracy, CNN 97.91%, and ViT 93.75%, while all achieved ROC-AUC scores of 0.99. Prediction correlations exceeded 0.99 across all model pairs, indicating highly consistent outputs. However, LIME explanation correlations remained below 0.26, revealing substantial differences in the image regions used to reach those predictions. Analysis of misclassified samples further identified a consistent spatial pattern: incorrect predictions were associated with attention outside the lung parenchyma, whereas correct predictions focused primarily within lung regions. These findings demonstrate that prediction agreement is a poor proxy for reasoning consistency, and that interpretability evaluation must be treated as an independent validation criterion alongside predictive performance in clinical AI systems.

---


> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-509](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
