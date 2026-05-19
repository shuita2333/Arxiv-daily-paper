# 📦 其他研究 | 2026年05月20日

> 本类共 **619** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**601-619**（第 13/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | **601-619**

---

### 601. [AI for Auto-Research: Roadmap & User Guide](https://arxiv.org/abs/2605.18661)

**<font color=#1a73e8>作者：</font>** Lingdong Kong, Xian Sun, Wei Chow 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-assisted research is crossing a threshold: fully automated systems can now generate research papers for as little as $15, while long-horizon agents can execute experiments, draft manuscripts, and simulate critique with minimal human input. Yet this productivity frontier exposes a deeper integrity problem: under scientific pressure, even frontier LLMs still fabricate results, miss hidden errors, and fail to judge novelty reliably. Studying developments through April 2026, we present an end-to-end analysis of AI across the complete research lifecycle, organized into four epistemological phases: Creation (idea generation, literature review, coding & experiments, tables & figures), Writing (paper writing), Validation (peer review, rebuttal & revision), and Dissemination (posters, slides, videos, social media, project pages, and interactive agents). We identify a sharp, stage-dependent boundary between reliable assistance and unreliable autonomy: AI excels at structured, retrieval-grounded, and tool-mediated tasks, but remains fragile for genuinely novel ideas, research-level experiments, and scientific judgment. Generated ideas often degrade after implementation, research code lags far behind pattern-matching benchmarks, and end-to-end autonomous systems have not yet consistently reached major-venue acceptance standards. We further show that greater automation can obscure rather than eliminate failure modes, making human-governed collaboration the most credible deployment paradigm. Finally, we provide a structured taxonomy, benchmark suite, and tool inventory, cross-stage design principles, and a practitioner-oriented playbook, with resources maintained at our project page.

---


### 602. [Efficient and Noise-Tolerant PAC Learning of Multiclass Linear Classifiers](https://arxiv.org/abs/2605.18662)

**<font color=#1a73e8>作者：</font>** Rita Adhikari, Shiwei Zeng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Noise-tolerant PAC learning of linear models has been of central interests in machine learning community since the last century. In recent years, many computationally-efficient algorithms have been proposed for the problem of learning linear threshold functions under multiple noise models. Yet, when the problem is considered under multiclass learning settings, i.e. when the number of classes $k$ is at least $3$, it is unknown whether there exist computationally-efficient PAC learning algorithms when the data sets are maliciously corrupted. In this paper, we consider that the marginal distribution is a mixture of bounded variance distributions and the data sets satisfy a margin condition at the same time. We show that there exists a computationally-efficient algorithm that PAC learns multiclass linear classifiers $\{h_w:x\mapsto \arg\max_{y\in[k]}w_y\cdot x, x\in \mathbb{R}^d, w\in\mathbb{R}^{kd}\}$ using at most $O(k^2\cdot (d\log d+\log k))$ samples even under a constant rate of nasty noise. Our algorithm consists of two main ingredients: a cluster-based pruning scheme and a standard multiclass hinge loss minimization program. Even in the special case of binary setting, i.e. $k=2$, our result is strictly stronger than all prior works.

---


### 603. [GIM: Evaluating models via tasks that integrate multiple cognitive domains](https://arxiv.org/abs/2605.18663)

**<font color=#1a73e8>作者：</font>** Rohit Patel, Alexandre Rezende, Steven McClain  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM benchmarks saturate, the evaluation community has pursued two strategies to increase difficulty: escalating knowledge demands (GPQA, HLE) or removing knowledge entirely in favor of abstract reasoning (ARC-AGI). The first conflates memorization with capability; the second divorces reasoning from the practical contexts in which it matters. We take a different approach. The Grounded Integration Measure (GIM) is a benchmark of 820 original problems (615 public, 205 private) where difficulty comes from integration; individual problems require coordinating multiple cognitive operations (constraint satisfaction, state tracking, epistemic vigilance, audience calibration) over broadly accessible knowledge, so that reasoning stays grounded in realistic tasks without being gated on specialized expertise. Each problem is an original expert-authored composition, majority with rubric-decomposed scoring (median 6 independently judged criteria). A balanced public--private split provides built-in contamination diagnostic. We calibrate a continuous response 2-parameter logistic (2PL) IRT model over >200k prompt-response pairs across 28 models, producing robust ability estimates that correctly order test-configurations even when raw accuracy is distorted by errors or missing data, addressing a common challenge in benchmark reporting. Using this framework, we present a comprehensive leaderboard spanning 22 models and 47 test-configurations (unique model, thinking-level pairs), and conduct what is to our knowledge the most extensive published study of how test-time compute trades off against model capability on a fixed benchmark: 11 models swept across 35 test-configurations. We observe that within-family configuration choices, such as thinking budget and quantization, matter as much as model selection. We release the evaluation framework, calibrated IRT parameters, and all public problems.

---


### 604. [A No-Defense Defense Against Gradient-Based Adversarial Attacks on ML-NIDS: Is Less More?](https://arxiv.org/abs/2605.18666)

**<font color=#1a73e8>作者：</font>** Mohamed elShehaby, Ashraf Matrawy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient-based adversarial attacks subtly manipulate inputs of Machine Learning (ML) models to induce incorrect predictions. This paper investigates whether careful architectural choices alone can yield an inherently robust Deep Neural Network (DNN)-based Network Intrusion Detection Systems (NIDS), without any additional explicit defenses. Through thousands of experiments, around 2200, varying network depth, feature dimensionality, activation functions, and dropout across FGSM, PGD, and BIM attacks, we show that shallower networks, reduced feature sets, and ReLU activation consistently and jointly reduce adversarial vulnerability. Moreover, a simple model following this recipe outperforms deeper, fully-featured adversarially trained models, while maintaining near-perfect clean-traffic detection and lower training times. Nevertheless, while less is more, the selection of the right less is what truly matters.

---


### 605. [Better Together: Evaluating the Complementarity of Earth Embedding Models](https://arxiv.org/abs/2605.18667)

**<font color=#1a73e8>作者：</font>** Thijs L van der Plas, Jacob JW Bakermans, Vishal Nedungadi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth embedding models transform Earth observation data into embeddings uniquely tied to locations on the Earth's surface. These models are typically evaluated in isolation, comparing the downstream task performance across different Earth embeddings. However, spatially aligned embeddings can naturally be fused, providing richer information per location, a capability that isolated evaluations fail to capture. We therefore propose assessing Earth embeddings by their complementarity: the performance gain of fused embeddings over the best single-model baseline. To operationalise this, we introduce an embedding complementarity index applicable to any embedding and task, and evaluate four Earth embedding models (AlphaEarth, Tessera, GeoCLIP, SatCLIP) in isolation, in all pairs, and jointly across six downstream tasks. Fused embeddings outperform the best single model in four out of six tasks, confirming that single-embedding evaluations often underestimate Earth embedding capabilities. Complementarity proves both task- and location-dependent. Further, for a land cover regression task, we find that complementarity is partially determined by the spatial scale of land cover classes. Complementarity reframes Earth embeddings: the greatest future gains may come not from any single Earth embedding model, but from combinations that are better together.

---


### 606. [Sublinear Risk-Limiting Audits from Direct Ballot Selection and Statistical Ballot Manifests](https://arxiv.org/abs/2605.18670)

**<font color=#1a73e8>作者：</font>** Benjamin Fuller, Abigail Harrison, Alexander Russell  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Risk-limiting audits (RLAs) are post-election auditing procedures that rigorously guarantee a specified maximum probability that an incorrect electoral outcome will not be detected. Aside from ready access to physical ballots, known RLAs require a software-independent accounting of the sizes of each ballot batch, called a ballot manifest. While typical electoral procedures automatically provide rough estimates for batch sizes, even slight inaccuracies (commensurate with the margin of the contest under audit) completely invalidate conventional RLAs (Lindeman et al., EVT 2012). Thus, establishing a sufficiently accurate manifest often requires handling every ballot and can be the dominant cost of conducting the RLA.
We propose two new risk-limiting techniques: 1) A statistical mechanism for ensuring that the batch sizes reported by an untrusted tabulation are, in fact, an accurate manifest; this effectively bootstraps from a rough manifest to an accurate one with sublinear effort. 2) We propose a new class of RLAs called direct ballot selection. This method reverses the traditional comparison procedure and compares uniformly selected ballots against their cast vote records, requiring a new statistical test for identifier duplication but efficiently supporting elections without in order identifiers.
These techniques reduce the complexity of RLAs across many elections. Our two main findings are as follows: 1) The time to create a manifest can be drastically reduced with a modest increase in the number of ballots sampled in the audit. At a 3% margin and a large population, there is a reduction in the overall audit time of at least an order of magnitude across methods. 2) Direct ballot selection improves over state-of-the-art polling for small margins. For Connecticut (29th in population) at a 1% margin, it beats Minerva (Security 2022) by 55% in ballot sample complexity.

---


### 607. [Efficient Lookahead Encoding and Abstracted Width for Learning General Policies in Classical Planning](https://arxiv.org/abs/2605.18674)

**<font color=#1a73e8>作者：</font>** Michael Aichmüller, Simon Ståhlberg, Martin Funkquist 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generalized planning aims to learn policies that generalize across collections of instances within a classical planning domain. Recent Graph Neural Network (GNN) approaches have learned nearly perfect policies for several domains. This work improves on the recently published idea of Iterated Width (IW) policies. Therein, the policy broadens its successor scope through an IW-lookahead search that can "jump" over multiple transitions, simplifying the problem structure. Yet, each transition is evaluated individually, leading to unscalable compute costs and expressivity limitations. Furthermore, although IW(1) is attractive because it scales linearly with the number of atoms, it becomes inefficient once thousands of objects are considered, as in the International Planning Competition (IPC) 2023 benchmark. We address both limitations. First, we introduce a vastly more efficient holistic encoding of the entire search tree. It jointly represents IW(1)-reachable states only by their relational differences to the current state, enabling Relational GNNs (R-GNNs) to score all transitions in a single forward pass. Second, we define Abstracted IW(1) to improve scaling through relational abstraction during novelty checks. Rather than testing fully instantiated atoms, it abstracts each atom by replacing all but one argument with its type. The original atom is novel if any of its abstracted forms is novel. This structural compression shifts novelty search scaling from atoms to objects, while preserving meaningful subgoal structure. We evaluate our contributions on the hyperscaling IPC 2023 benchmark and across diverse domains, including domains requiring features beyond the $C_2$ logic fragment. Our policies achieve new state-of-the-art performance, significantly surpassing prior work, including the classical planner LAMA.

---


### 608. [COOPO: Cyclic Offline-Online Policy Optimization Algorithm](https://arxiv.org/abs/2605.18675)

**<font color=#1a73e8>作者：</font>** Qisai Liu, Zhanhong Jiang, Joshua Russell Waite 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning struggles with distributional shift and constrained performance due to static dataset limitations, while online RL demands prohibitive environment interactions. The recent advent of hybrid offline-to-online methods bridges these domains but suffers from distribution drift during transitions and catastrophic forgetting of offline knowledge. We introduce COOPO (Cyclic Offline-Online Policy Optimization), a generalized framework that repeatedly cycles between constrained offline training and online fine-tuning. Each cycle first anchors the policy to the dataset via KL-regularized advantage-weighted offline updates to minimize distributional shift and then fine-tunes it online using any policy optimization for stable exploration. Crucially, periodically returning to offline training eliminates forgetting and drift while maximizing dataset reuse. The cyclic behavior also helps reduce the online environment interactions. Theoretically, COOPO achieves better online sample efficiency, surpassing pure online RL, with guaranteed monotonic improvement under standard coverage assumptions. Extensive D4RL benchmarks demonstrate COOPO reduces online interactions versus state-of-the-art hybrids while improving final returns, maintaining robustness across diverse offline algorithms and online optimizers. This looped synergy sets new efficiency and performance standards for adaptive RL.

---


### 609. [CMAG: Concept-Scaffolded Retrieval for Marketplace Avatar Generation](https://arxiv.org/abs/2605.18680)

**<font color=#1a73e8>作者：</font>** Rajeev Goel, Jason Ding, Phani Harish Wajjala 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Metaverse platforms rely on creator-driven marketplaces where avatars are assembled from discrete, taxonomy-labeled 3D assets (e.g., tops, bottoms, shoes, accessories) under strict category and topology constraints. While users increasingly expect free-form text control, text-only retrieval is brittle: natural language is ambiguous with respect to platform taxonomies, metadata is often noisy or informal, and independently retrieved components can be stylistically inconsistent or geometrically incompatible. We propose \textbf{CMAG}, a concept-scaffolded retrieval and verified composition framework for marketplace avatar generation. Given a prompt, CMAG first synthesizes an intermediate 3D concept scaffold that disambiguates intent beyond text by providing global spatial and stylistic context. In parallel, a view-aware part discovery module extracts localized visual evidence via prompt decomposition and text-grounded segmentation. A prompt-conditioned taxonomy router enforces category coverage and resolves semantic-to-taxonomic mismatch, after which a hybrid category-wise retriever combines part-based fusion with a concept-residual fallback using feature suppression. Finally, an agentic vision--language model filters and re-ranks candidates across categories and drives an iterative verification loop to assemble prompt-faithful, topologically consistent avatars from catalog assets. We evaluate CMAG on diverse compositional prompts and demonstrate improved retrieval robustness and compositional correctness compared to strong baselines, highlighting the importance of 3D concept scaffolding under prompt ambiguity.

---


### 610. [Learning Quantifiable Visual Explanations Without Ground-Truth](https://arxiv.org/abs/2605.18681)

**<font color=#1a73e8>作者：</font>** Amritpal Singh, Andrey Barsky, Mohamed Ali Souibgui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explainable AI (XAI) techniques are increasingly important for the validation and responsible use of modern deep learning models, but are difficult to evaluate due to the lack of good ground-truth to compare against. We propose a framework that serves as a quantifiable metric for the quality of XAI methods, based on continuous input perturbation. Our metric formally considers the sufficiency and necessity of the attributed information to the model's decision-making, and we illustrate a range of cases where it aligns better with human intuitions of explanation quality than do existing metrics.
To exploit the properties of this metric, we also propose a novel XAI method, considering the case where we fine-tune a model using a differentiable approximation of the metric as a supervision signal. The result is an adapter module that can be trained on top of any black-box model to output causal explanations of the model's decision process, without degrading model performance. We show that the explanations generated by this method outperform those of competing XAI techniques according to a number of quantifiable metrics.

---


### 611. [Contextualized Dynamic Explanations: A Vision](https://arxiv.org/abs/2605.18698)

**<font color=#1a73e8>作者：</font>** Zhicheng Liu, Jason H Li, Greg Briskin  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Asynchronous data-driven explanations often fail because the content and presentation are not tailored to the target audience, and they provide limited opportunities for active audience engagement. We present a vision for Contextualized Dynamic Explanations (CODEX), an agentic approach to dynamically generating contextualized multi-modal information interfaces for effective data-driven explanations based on an evolving audience model and a predefined communication intent. The premise underlying CODEX is that it is impossible for communicators to anticipate the full range of interactive scenarios involving the target audience. This observation motivates a set of research challenges focused on developing autonomous agents capable of evaluating communication progress, making context-sensitive decisions, and producing effective information representations.

---


### 612. [A Large-Scale Study on the Accuracy vs Cost Trade-offs of Training and Evaluation Settings in Fine-Grained Image Recognition](https://arxiv.org/abs/2605.18700)

**<font color=#1a73e8>作者：</font>** Edwin Arkel Rios, Augusto Christian Surya, Oswin Gosal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prior work on fine-grained image recognition (FGIR) has established the importance of the backbone selection, but has neglected the accuracy-vs-cost trade-offs under different training and evaluation settings. In this work we conduct a large-scale study with over 2000 experiments across 6 training and evaluation settings, 9 pretrained backbones, and 17 datasets. Preliminary observations on the effectiveness of data augmentation for fine-grained training motivate us to extend Counterfactual Attention Learning (CAL), a state-of-the-art method based on data-aware cropping and masking augmentations, with cross-image discriminative region mixing augmentation. We also propose an efficient evaluation-only variant that maintains competitive accuracy while reducing inference costs by forfeiting the forward pass on discriminative crops that is normally used by CAL and similar FGIR methods. Our results show that data-aware augmentations during training only can enable a model to achieve excellent accuracy even without crops, significantly reducing inference costs. To support future research we share our code and checkpoints at: \url{this https URL}

---


### 613. [Learning Normal Representations for Blood Biomarkers](https://arxiv.org/abs/2605.18701)

**<font color=#1a73e8>作者：</font>** Aashna P. Shah, Michelle M. Li, Yash Lal 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Blood-based biomarkers underpin clinical diagnosis and management, yet their interpretation relies largely on fixed population reference intervals that ignore stable, intra-patient variability. As such, population-based interpretation can mask meaningful deviation from an individual's baseline, risking delayed disease detection. To remedy this, there have been increasing efforts to personalize blood biomarker interpretation using individual testing histories. However, these methods may overfit to sparse data, inflating false-positive rates and unnecessary follow-up, and can also unwittingly include unrecognized or subclinical disease. Here, we leverage nearly 2 billion longitudinal laboratory measurements from over 1.6 million individuals across North America, the Middle East, and East Asia, to show that while laboratory values are highly individual, purely personalized intervals routinely overfit, classifying up to 68% of measurements as abnormal, without corresponding associations with adverse clinical outcomes. We then introduce NORMA, a conditional transformer-based framework that generates reference intervals by conditioning on both a patient's history and population-level data about "normal" variation. NORMA-derived intervals achieve higher precision for predicting outcomes, including mortality, acute kidney injury, and chronic disease. These findings caution against over-personalization in laboratory medicine and demonstrate that anchoring individual trajectories to population-level priors outperforms either approach alone. To promote transparency, we publicly release the model, code, and an interactive user interface for accessible, individualized laboratory interpretation.

---


### 614. [EgoExoMem: Cross-View Memory Reasoning over Synchronized Egocentric and Exocentric Videos](https://arxiv.org/abs/2605.18734)

**<font color=#1a73e8>作者：</font>** Ruiping Liu, Junwei Zheng, Yufan Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric memory is widely used in embodied intelligence, but it may be insufficient for comprehensive spatial-temporal reasoning. Inspired by human recall from both field and observer perspectives, we introduce EgoExoMem, the first benchmark for cross-view memory reasoning over synchronized egocentric and exocentric videos. EgoExoMem contains $2.6K$ high-quality MCQs across eight temporal, spatial, and cross-view QA types. To support dual-view retrieval, we propose E$^2$-Select, a training-free frame selection method for synchronized ego-exo videos. It combines relevance-based budget allocation with per-view k-DPP sampling to handle view asymmetry and cross-view temporal consistency. Experiments show that ego and exo views provide complementary memory cues, while existing MLLMs remain far from solving the benchmark: the best model reaches only $55.3\%$. E$^2$-Select achieves state-of-the-art performance of $58.2\%$ over frame-selection and RAG-based memory baselines. Further analysis reveals systematic view-preference conflicts between question framing and answer grounding, underscoring the novelty and challenge of cross-view memory reasoning.

---


### 615. [PIXLRelight: Controllable Relighting via Intrinsic Conditioning](https://arxiv.org/abs/2605.18735)

**<font color=#1a73e8>作者：</font>** Miguel Farinha, Ronald Clark  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PIXLRelight, a feed-forward approach for physically controllable single-image relighting. Existing methods either provide limited lighting control (e.g. through text or environment maps), accumulate errors when chaining inverse and forward rendering, or require costly per-image optimization. Our key idea is to bridge physically based rendering (PBR) and learned image synthesis through a shared intrinsic conditioning that can be obtained from either real photographs or PBR renders. At training time, paired multi-illumination photographs are decomposed into albedo, diffuse shading, and non-diffuse residuals, which condition the model. At inference time, the same conditioning is computed from a path-traced render of a coarse 3D reconstruction of the input under user-specified PBR lights. A transformer-based neural renderer then applies the target illumination to the source photograph, preserving fine image detail through a per-pixel affine modulation. PIXLRelight enables arbitrary PBR-style lighting control, achieves state-of-the-art relighting quality, and runs in under a tenth of a second per image. Code and models are available at this https URL.

---


### 616. [Spectral Progressive Diffusion for Efficient Image and Video Generation](https://arxiv.org/abs/2605.18736)

**<font color=#1a73e8>作者：</font>** Howard Xiao, Brian Chao, Lior Yariv 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have been shown to implicitly generate visual content autoregressively in the frequency domain, where low-frequency components are generated earlier in the denoising process while high-frequency details emerge only in later timesteps. This structure offers a natural opportunity for efficient generation, as high-resolution computation on noise-dominated frequencies is largely redundant. We propose Spectral Progressive Diffusion, a general framework that progressively grows resolution along the denoising trajectory of pretrained diffusion models. To this end, we develop a spectral noise expansion mechanism and derive an optimal resolution schedule from the model's power spectrum. Our framework supports training-free acceleration and a novel fine-tuning recipe that further improves efficiency and quality. We demonstrate significant speedups on state-of-the-art pretrained image and video generation models while preserving visual quality.

---


### 617. [LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation](https://arxiv.org/abs/2605.18739)

**<font color=#1a73e8>作者：</font>** Yukang Chen, Luozhou Wang, Wei Huang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present LongLive-2.0, an NVFP4-based parallel infrastructure throughout the full training and inference workflow of long video generation, addressing speed and memory bottlenecks. For training, we introduce sequence-parallel autoregressive (AR) training, instantiated as Balanced SP, which co-designs the efficient teacher-forcing layout with SP execution by pairing clean-history and noisy-target temporal chunks on each rank, enabling a natural teacher-forcing mask with SP-aware chunked VAE encoding. Combined with NVFP4 precision, it reduces GPU memory cost and accelerates GEMM computation during training, the proportion of which increases as video length grows. Moreover, we show that a high-quality infrastructure and dataset enable a remarkably clean training pipeline. Unlike existing Self-Forcing series methods that rely on ODE initialization and subsequent distribution matching distillation (DMD), LongLive-2.0 directly tunes a diffusion model into a long, multi-shot, interactive auto-regressive (AR) diffusion model. It can be further converted to real-time generation (4 to 2 denoising steps) with standalone LoRA weights. For inference on Blackwell GPUs, we enable W4A4 NVFP4 inference, quantize KV cache into NVFP4 for memory savings, and boost end-to-end throughput with asynchronous streaming VAE decoding. On non-Blackwell GPU architectures, we deploy SP inference to match the speed on Blackwell GPUs, while the quantized KV cache can lower inter-GPU communication of SP. Experiments show up to 2.15x speedup in training, and 1.84x in inference. LongLive-2.0-5B achieves 45.7 FPS inference while attaining strong performance on benchmarks. To our knowledge, LongLive-2.0 is the first NVFP4 training and inference system for long video generation.

---


### 618. [Actionable World Representation](https://arxiv.org/abs/2605.18743)

**<font color=#1a73e8>作者：</font>** Kunqi Xu, Jitao Li, Jianglong Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inspired by the emergent behaviors in large language models that generalized human intelligence, the research community is pursuing similar emergent capabilities within world models, with a emphasis on modeling the physical world. Within the scope of physical world model, objects are the fundamental primitives that constitute physical reality. From humans to computers, nearly everything we interact with is an object. These objects are rarely static; they are actionable entities with varying states determined by their intrinsic properties. While current methods approach object action states either via video generation or dynamic scene reconstruction, none explicitly model this basic element in a unified, principled way to build an actionable object representation. We propose WorldString, a neural architecture capable of modeling the state manifold of real-world objects by learning directly from point clouds or RGB-D video streams. Serving as a versatile digital twin, it acts as a foundational building block for physical world models; thus, we name it WorldString. Sweetly, its fully differentiable structure seamlessly enables future integration with policy learning and neural dynamics.

---


### 619. [ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop](https://arxiv.org/abs/2605.18746)

**<font color=#1a73e8>作者：</font>** Yining Hong, Jiageng Liu, Han Yin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence unfolds through a perception-action loop: agents act to acquire observations, and reason about how observations vary as a function of action. Rather than passively processing what is seen, they actively uncover what is unseen - occluded structure, dynamics, containment, and functionality that cannot be resolved from passive sensing alone. We move beyond prior formulations of spatial intelligence that assume oracle observations by recasting the observer as an actor. We introduce ESI-BENCH, a comprehensive benchmark for embodied spatial intelligence spanning 10 task categories and 29 subcategories built on OmniGibson, grounded in Spelke's core knowledge systems. Agents must decide what abilities to deploy - perception, locomotion, and manipulation - and how to sequence them to actively accumulate task-relevant evidence. We conduct extensive experiments on state-of-the-art MLLMs and find that active exploration substantially outperforms passive counterparts, with agents spontaneously discovering emergent spatial strategies without explicit instructions, while random multi-view often adds noise rather than signal despite consuming far more images. Most failures stem not from weak perception but from action blindness: poor action choices lead to poor observations, which in turn drive cascading errors. While explicit 3D grounding stabilizes reasoning on depth-sensitive tasks, imperfect 3D representation proves more harmful than 2D baselines by distorting spatial relations. Human studies further reveal that unlike humans who seek falsifying viewpoints and revise beliefs under contradiction, models commit prematurely with high confidence regardless of evidence quality, exposing a metacognitive gap that neither better perception nor more embodied interaction alone can close.

---


> [!TIP]
> 当前位于：**601-619**（第 13/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | **601-619**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
