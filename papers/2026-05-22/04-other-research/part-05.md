# 📦 其他研究 | 2026年05月22日

> 本类共 **352** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-352](./part-08.md)

---

### 201. [VISTA: Technical Report for the Ego4D Short-Term Object Interaction Anticipation at EgoVis 2026](https://arxiv.org/abs/2605.20901)

**<font color=#1a73e8>作者：</font>** Qiaohui Chu, Haoyu Zhang, Yisen Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose VISTA, a V-JEPA Integrated StillFast Temporal Anticipator for the Ego4D Short-Term Object Interaction Anticipation (STA) Challenge at EgoVis 2026. Given an egocentric video timestamp, the task requires anticipating the next human-object interaction, including the future active object's bounding box, noun category, verb category, time-to-contact, and confidence score. VISTA follows a StillFast-style design that combines object-centric spatial detection with short-horizon temporal context. Specifically, a COCO-pretrained Faster R-CNN ResNet-50 FPN detector generates object proposals from the last observed high-resolution frame, while a frozen V-JEPA 2.1 temporal branch extracts clip-level egocentric context from the observed video. The temporal representation is injected into the detection pathway through feature modulation and ROI-level context fusion. The fused proposal features are then passed to multi-head STA predictors for box refinement, noun classification, verb classification, time-to-contact regression, and interaction confidence estimation. For the final submission, we further ensemble complementary predictions to improve robustness. Experimental results on the official challenge server show that VISTA achieves first place in the EgoVis 2026 Ego4D STA Challenge. Our code will be released at this https URL.

---


### 202. [JFAA: Technical Report for the EPIC-KITCHENS-100 Action Anticipation Challenge at EgoVis 2026](https://arxiv.org/abs/2605.20904)

**<font color=#1a73e8>作者：</font>** Qiaohui Chu, Haoyu Zhang, Yisen Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose JFAA, a JEPA-based Future Action Anticipation method for the EPIC-KITCHENS-100 (EK-100) Action Anticipation task. Inspired by the representation learning and future prediction ability of V-JEPA 2.1, JFAA uses a frozen encoder and predictor to extract observed context features and near-future latent tokens. A lightweight attentive probe is then trained to predict verb, noun, and action logits with separate task queries. To improve robustness, we further build a field-aware ensemble over selected epoch-level predictions, allowing each output field to benefit from its most reliable candidates. Experimental results on the official challenge server show that JFAA achieves first place in the EgoVis 2026 EK-100 Action Anticipation Challenge. Our code will be released at this https URL.

---


### 203. [SynCB: A Synergy Concept-Based Model with Dynamic Routing Between Concepts and Complementary Neural Branches](https://arxiv.org/abs/2605.20908)

**<font color=#1a73e8>作者：</font>** Tores Julie, Sun Rémy, Sassatelli Lucile 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept-based (CB) models provide interpretability and support test-time human intervention, while standard neural networks (NN) offer strong task performance but little transparency. Prior work has explored hybrid formulations that integrate concepts and additional representations to improve accuracy, often at the cost of human interventions. We introduce the \emph{Synergy Concept-Based Model (SynCB)} framework, that combines a CB branch with a complementary neural branch, and a trainable routing module that dynamically selects which branch to use for each input. Unlike prior models, which fuse residual and concept-based predictions, SynCB keeps the two branches distinct and coordinates them through the routing module. Moreover, both branches are learned jointly, allowing information sharing between the complementary neural branch and CB branches through their common backbone. To improve responsiveness to interventions, we further introduce a test-time intervention policy and a corresponding loss. Across five datasets and CB benchmarks, SynCB consistently achieves higher task accuracy while remaining more responsive to human interventions, surpassing the full neural baseline by up to 3.9 percentage points and exceeding the strongest competitor in intervention performance by up to 6.43 percentage points.

---


### 204. [FlowLong: Inference-time Long Video Generation via Manifold-constrained Tweedie Matching](https://arxiv.org/abs/2605.20910)

**<font color=#1a73e8>作者：</font>** Jangho Park, Geon Yeong Park, Gihyun Kwon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extending the generation horizon of video diffusion models to long sequences remains a long-standing and important challenge. Existing training-free approaches fall into two categories: extensions of bidirectional models, which are tightly coupled to specific architectures and suffer from quality degradation over long horizons, and autoregressive models, which accumulate drift errors due to exposure bias and tend to produce repetitive motion patterns. To address these issues, we propose a novel but simple inference-time approach for long video generation that is architecture-agnostic and requires no additional training. Our method generates long videos via overlapping sliding windows, where predicted clean samples from adjacent windows are blended via \emph{Tweedie matching} to enforce both \textbf{manifold constraint and temporal consistency} across overlap regions. \emph{Stochastic early-phase sampling} then synchronizes per-window trajectories by injecting fresh noise after each Tweedie matching correction in the high-noise phase, before transitioning to deterministic ODE sampling to preserve fine-grained visual fidelity. Applied to various video generation models, our method generates videos several times longer than the native window length while outperforming both training-free and autoregressive baselines in temporal consistency and visual quality, and further extends to audio-video joint generation and text-to-3DGS without any fine-tuning.

---


### 205. [For How Long Should We Be Punching? Learning Action Duration in Fighting Games](https://arxiv.org/abs/2605.20911)

**<font color=#1a73e8>作者：</font>** Hoang Hai Nguyen, Kurt Driessens, Dennis J.N.J. Soemers  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fighting games such as Street Fighter II present unique challenges to reinforcement learning (RL) agents due to their fast-paced, real-time nature. In most RL frameworks, agents are hard-coded to make decisions at a fixed interval, typically every frame or every N frames. Although this design ensures timely responses, it restricts the agent's ability to adjust its reaction timing. Acting every frame grants frame-perfect reflexes, which are unrealistic compared to human players, whereas longer fixed intervals reduce computational cost but hinder responsiveness. We consider an alternative decision-making framework in which the agent learns not only what action to take but also for how long to execute it. By jointly predicting both action and duration, the agent can dynamically adapt its responsiveness to different situations in the game. We implement this method using the open-source FightLadder environment with agents trained against scripted built-in bots, systematically testing different frame skip configurations to analyze their influence on performance, responsiveness, and learned behavior. Experiments show that learned timing can match the performance of well-chosen fixed frame skips and encourages repeatable action patterns, but does not ensure robustness on its own. In most cases, we see agents performing best with consistently high frame skip values (i.e., low responsiveness). This strategy makes it easier to learn exploitative strategies where the same action is repeated over and over, which the scripted bots appear to be susceptible to.

---


### 206. [Enhancing Scientific Discourse: Machine Translation for the Scientific Domain](https://arxiv.org/abs/2605.20912)

**<font color=#1a73e8>作者：</font>** Dimitris Roussis, Sokratis Sofianopoulos, Stelios Piperidis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The increasing volume of scientific research necessitates effective communication across language barriers. Machine translation (MT) offers a promising solution for accessing international publications. However, the scientific domain presents unique challenges due to its specialized vocabulary and complex sentence structures. In this paper, we present the development of a collection of parallel and monolingual corpora for the scientific domain. The corpora target the language pairs Spanish-English, French-English, and Portuguese-English. For each language pair, we create a large general scientific corpus as well as four smaller corpora focused on the domains of: Cancer Research, Energy Research, Neuroscience, and Transportation research. To evaluate the quality of these corpora, we utilize them for fine-tuning general-purpose neural machine translation (NMT) systems. We provide details regarding the corpus creation process, the fine-tuning strategies employed, and we conclude with the evaluation results.

---


### 207. [Task-Routed Mixture-of-Experts with Cognitive Appraisal for Implicit Sentiment Analysis](https://arxiv.org/abs/2605.20916)

**<font color=#1a73e8>作者：</font>** Yaping Chai, Haoran Xie, Joe S. Qin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Implicit sentiment analysis is challenging because sentiment toward an aspect is often inferred from events rather than expressed through explicit opinion words. Existing models typically learn from the final polarity label, which provides limited guidance for reasoning about sentiment from the context. Motivated by cognitive appraisal theory, we propose an appraisal-aware multi-task learning (MTL) framework for implicit sentiment analysis that provides polarity prediction with two complementary auxiliary tasks: implicit sentiment detection and cognitive rationale generation. However, training several objectives with different targets and sharing a single backbone across tasks in MTL limits flexibility and can lead to task interference. To reduce interference among these related but distinct objectives, we adopt task-level mixture-of-experts models in which all tasks share a common set of experts, and task identity controls the sparse combination of these experts. Our method builds on an encoder-decoder architecture and replaces a subset of encoder and decoder blocks with these sparse mixtures. We use a task-conditioned router to select sparse expert mixtures for each task, and a task-separated routing objective to encourage different tasks to learn distinct expert-selection patterns. Experimental results show that our model outperforms recently proposed approaches, with strong gains on the implicit sentiment subset. Our code is available at this https URL.

---


### 208. [Sutra: Tensor-Op RNNs as a Compilation Target for Vector Symbolic Architectures](https://arxiv.org/abs/2605.20919)

**<font color=#1a73e8>作者：</font>** Emma Leonhart  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sutra is a typed, purely functional programming language whose compiled forward pass is a PyTorch neural network. The compiler beta-reduces the whole program -- primitives, control flow, string I/O -- to one fused tensor-op graph over a frozen embedding substrate. Rotation binding, unbind, bundle, polynomial Kleene three-valued logic, and tail-recursive loops all lower to tensor operations; the Kleene connectives are Lagrange-interpolated polynomials exact on the {-1, 0, +1} truth grid. Validation is one fact tested two ways. (1) The same program runs on four frozen embeddings spanning two modalities -- three text encoders (nomic-embed-text, all-minilm, mxbai-embed-large) and one protein language model (ESM-2) -- and decodes bundles at 100% accuracy through width k=8 on every substrate, where the textbook Hadamard product has already collapsed (2.5% on mxbai-embed-large, 7.5% on all-minilm). (2) PyTorch autograd flows through the actually compiled graph: a fuzzy-rule classifier written in .su trains from random init (18.7 +/- 9.5%; chance = 20%, five classes) to 100.0 +/- 0.0% (three seeds) by backpropagating through the emitted graph, the symbolic source unmodified. A weighted variant additionally trains a scalar cosine gain and writes it back into the .su source as a numeric literal; recompiling reproduces the trained behaviour to ~2e-7 per logit, so the trained model is itself legible, recompilable code. The same artifact is therefore both a logic program and a trainable neural network.

---


### 209. [Evaluating Speech Articulation Synthesis with Articulatory Phoneme Recognition](https://arxiv.org/abs/2605.20920)

**<font color=#1a73e8>作者：</font>** Vinicius Ribeiro, Yves Laprie  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in machine learning and the availability of articulatory datasets allow vocal tract synthesis to be conditioned on phonetic sequences, a primary task of articulatory speech synthesis. However, quality assessment needs a better definition. Generally, ranking generative models is tricky due to subjectivity. However, articulatory synthesis has the additional difficulty of requiring specialized knowledge in vocal tract anatomy and acoustics. To address this problem, this paper proposes to evaluate speech articulation synthesis using phoneme recognition as a proxy.
Our hypothesis is that phoneme recognition using articulatory features better captures nuances in phoneme production, such as correct places of articulation, which traditional metrics (e.g., point-wise distance metrics) do not. We train a neural network with acoustic and articulatory features extracted from a single-speaker RT-MRI dataset. Then, we compare the recognition performance when testing the model with different synthetic articulatory features. Our results show that our articulatory feature set is phonetically rich and helps exploring additional dimensions on speech articulation synthesis.

---


### 210. [Winfree Oscillatory Neural Network](https://arxiv.org/abs/2605.20922)

**<font color=#1a73e8>作者：</font>** Jiawen Dai, Yue Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Oscillations and synchronization are widely believed to play a fundamental role in representation and computation. However, existing machine learning approaches based on synchronization dynamics have largely been confined to specialized settings such as object discovery, with limited evidence of scalability to standard vision benchmarks or logic reasoning tasks. We propose the Winfree Oscillatory Neural Network (WONN), a dynamical neural architecture based on generalized Winfree dynamics. WONN evolves representations on the torus $(S^1)^d$ through structured oscillatory interactions, combining phase-based inductive biases with flexible and hierarchical interaction mechanisms instantiated as either fixed trigonometric mappings or learnable neural networks. We evaluate WONN on image recognition and complex reasoning tasks, including CIFAR, ImageNet, Maze-hard, and Sudoku. Across these domains, WONN achieves competitive or superior performance with strong parameter efficiency. In particular, WONN is, to our knowledge, the first synchronization-based oscillatory architecture to scale competitively to ImageNet-1K. Furthermore, on Maze-hard, WONN achieves 80.1% accuracy using only 1% of the parameters of prior state-of-the-art models. These results suggest that structured oscillatory dynamics provide a scalable and parameter-efficient alternative to conventional neural architectures.

---


### 211. [DASH: Fast Differentiable Architecture Search for Hybrid Attention in Minutes on a Single GPU](https://arxiv.org/abs/2605.20936)

**<font color=#1a73e8>作者：</font>** Weizhe Chen, Miao Zhang, Junpeng Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid attention architectures are becoming an increasingly important paradigm for improving LLM inference efficiency while preserving model quality, making hybrid architecture design a central problem. Existing designs often rely on manual empirical rules or proxy-based selector signals for layer-wise operator allocation. Recent NAS-style systems such as Jet-Nemotron demonstrate the promise of automated hybrid architecture search. However, Jet-Nemotron's PostNAS search stages alone use 200B tokens, making such search pipelines difficult to use as routine methods for hybrid architecture design. We introduce DASH, a fast differentiable search framework for hybrid attention architecture design, which relaxes discrete layer-wise attention operator placement into continuous architecture logits, prepares reusable teacher-aligned linear candidates, and performs architecture-only search with model and operator weights frozen to significantly enhance search efficiency. On Qwen2.5-3B-Instruct, DASH consistently outperforms a comprehensive suite of existing selector-style hybrid attention design baselines, showing that direct differentiable search can discover stronger hybrid architectures. Moreover, DASH achieves stronger RULER performance than released Jet-Nemotron models while remaining competitive on overlapping short-context and general benchmarks. Notably, each DASH search run uses only 12.3M tokens and takes about 20 minutes on a single RTX Pro 6000 GPU, corresponding to merely 0.006% of the PostNAS search tokens reported by Jet-Nemotron. These results suggest that high-quality hybrid attention architectures can be obtained through minutes-level differentiable search, providing a promising direction for hybrid architecture design.

---


### 212. [Toward 6G-enabled Brain Computer Interfaces: Technical Requirements, Use Cases, Challenges, and Future Trends](https://arxiv.org/abs/2605.20939)

**<font color=#1a73e8>作者：</font>** Houda Hafi, Bouziane Brik, Nuraini Jamil 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Brain computer interface (BCI) enables the brain to directly control an external device by converting neural signals into actionable outputs. However, effective real-time translation of brain activity strongly depends on the quality of neural communication between the brain and the external device. 6G is the next generation of wireless communication, expected to provide unprecedented levels of data rates, data security, and automation capabilities. In this context, integrating 6G into BCI systems would not only enhance the performance of brain-device communication, but would also create new opportunities for innovative applications. This work provides a comprehensive study on how BCI technology can be built effectively on top of 6G wireless networks by introducing several technical aspects and use cases. We first provide an overview of BCI and 6G, following their progression from early development to convergence through cognitive communication and advanced neural interfaces. We then highlight the need for the upcoming 6G systems toward BCI technology in every aspect, including 6G technologies such as intelligent edge and zero-touch networks, and 6G use cases such as digital twin, immersive communication, and internet of minds. Furthermore, we identify key technical challenges, open issues, and future research directions related to the 6G-enabled BCI paradigm.

---


### 213. [3D Reconstruction and Knowledge Distillation to Improve Multi-View Image Models to Explore Spike Volume Estimation in Wheat](https://arxiv.org/abs/2605.20940)

**<font color=#1a73e8>作者：</font>** Olivia Zumsteg, Jannis Widmer, Yann Bourdé 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate estimation of wheat spike volume is important for yield component analysis and stress resilience assessment, yet field-based measurement remains challenging. Active 3D sensing methods such as Light Detection and Ranging (LiDAR) or time-of-flight (ToF) are sensitive to plant motion or poorly suited to outdoor conditions, while 3D reconstructions are computationally expensive. Direct 2D image processing would offer computational advantages, but image-based models lack explicit geometric information. We therefore propose a hybrid 2D-3D approach with knowledge distillation during training while enabling efficient image-only inference. First, we train a rigid-invariant point cloud network using distance-based histogram features to obtain pose-robust geometric representations. We then combine the 3D model with a proposed multi-view image-based regulated Transformer (RT) in an ensemble architecture. Finally, we distill the ensemble knowledge into a purely image-based student model using either feature-based or label-based distillation. The two distilled RTs reduce the mean absolute error (MAE) from 654.31 mm$^3$ of the non-distilled RT to 639.93 mm$^3$ and 644.62 mm$^3$, and increase correlation from 0.76 to 0.77 and 0.82, respectively. At the same time, inference time is reduced from 160 ms to 1.4 ms per spike. Distillation further mitigates volume-dependent bias and reshapes the latent representation of the image model toward a geometry-aware shape. Our results demonstrate that 3D-informed training of a 2D Transformer allows for scalable and efficient spike volume estimation for high-throughput field phenotyping.

---


### 214. [PaintCopilot: Modeling Painting as Autonomous Artistic Continuation](https://arxiv.org/abs/2605.20941)

**<font color=#1a73e8>作者：</font>** Yunge Wen, Yuancheng Shen, Paul Pu Liang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PaintCopilot, a co-creative neural painting assistant that models painting as an open-ended autoregressive artistic behavior conditioned on evolving canvas states and prior brushstroke history, without requiring a target image. Unlike existing neural painting methods that frame painting as pixel reconstruction toward a predefined reference, PaintCopilot predicts future strokes directly from learned artistic dynamics, analogous to how large language models continue text sequences from prior context.
The framework proposes three complementary models: a ViT-based Target Predictor that infers artist intent from partial canvas observations, an autoregressive Next Stroke Predictor that generates temporally coherent brushstrokes via flow matching, and a VAE-based Region Sampler that synthesizes semantically localized stroke sequences on demand. Built on three differentiable brush representations (Hard Round, Brush Tip, and 2D Gaussian), the system supports four interactive workflows: Optimize History, Stroke Completion, Region Inpainting, and Dynamic Brush. Through case studies with professional artists, we demonstrate that PaintCopilot enables fluid co-creative painting workflows in which artists and AI continuously alternate control throughout the creative process.

---


### 215. [Bridging Structure and Language: Graph-Based Visual Reasoning for Autonomous Road Understanding](https://arxiv.org/abs/2605.20942)

**<font color=#1a73e8>作者：</font>** Lena Wild, Katie Z Luo, Marco Pavone  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structured road understanding of lane geometry, topology, and traffic element relationships is foundational to safe autonomous driving. While vision-language models (VLMs) offer promising semantic flexibility, they lack the geometric and relational grounding required for precise road reasoning. Conversely, traditional modular systems, e.g., HD maps and topological road graphs, provide structural precision but remain semantically rigid. To bridge this gap, we introduce the Combined Road Substrate (CRS), a graph-grounded framework that makes geometric road structure and open-vocabulary semantics jointly executable in a single representation. CRS enables the automatic generation of compositionally complex and linguistically varied question-answer pairs via recursive graph queries, augmented with a "grounding for free" mechanism that ensures logical traceability to specific map elements, and procedurally extracted chain-of-thought supervision traces. We demonstrate that state-of-the-art VLMs - including large, closed-source models - struggle significantly with structured road reasoning, yet training a small 2- or 4-billion-parameter model with as few as 20 to 80 CRS-enriched scenes yields stable gains in compositional reasoning tasks of varying depth. Analysis of model behavior via verifiable reasoning traces reveals a systematic shift in failure modes: whereas baseline models fail at relational scene understanding, CRS-trained models reduce failures to attribute recognition, suggesting that the primary bottleneck in road understanding is not model scale, but the absence of structured supervision.

---


### 216. [Thinking-while-speaking: A Controlled, Interleaved Reasoning Method for Real-Time Speech Generation](https://arxiv.org/abs/2605.20946)

**<font color=#1a73e8>作者：</font>** Xuan Du, Qiangyu Yan, Wenshuo Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The thinking-while-speaking paradigm aims to make AI communication more human. A key challenge is maintaining fluent speech while performing deep reasoning. Our method, InterRS, tackles this by inserting reasoning steps only during natural speech generation. This requires high-quality data where reasoning and speech are precisely aligned, and the length ratio are under controlled. We introduce a novel pipeline to generate such seamlessly interleaved audio data. To train our model, we combine interleaved SFT with refined data and reinforcement learning with two new rewards: a TA-Balance Reward to manage timing and thinking-answer ratio, and a Linguistic Quality Reward to refine expression. Experiments show our approach achieves 13% better performance on mathmatical and logic benchmarks while generating instant response like a spoken-language instruct model which outputs fast CoT response. Furthermore, our method generates more natural and fluent answers than prior methods.

---


### 217. [DrawMotion: Generating 3D Human Motions by Freehand Drawing](https://arxiv.org/abs/2605.20955)

**<font color=#1a73e8>作者：</font>** Tao Wang, Lei Jin, Zhihua Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-motion generation, which translates textual descriptions into human motions, faces the challenge that users often struggle to precisely convey their intended motions through text alone. To address this issue, this paper introduces DrawMotion, an efficient diffusion-based framework designed for multi-condition scenarios. DrawMotion generates motions based on both a conventional text condition and a novel hand-drawing condition, which provide semantic and spatial control over the generated motions, respectively. Specifically, we tackle the fine-grained motion generation task from three perspectives: 1) freehand drawing condition. To accurately capture users' intended motions without requiring tedious textual input, we develop an algorithm to automatically generate hand-drawn stickman sketches across different dataset formats; 2) multi-condition fusion. We propose a Multi-Condition Module (MCM) that is integrated into the diffusion process, enabling the model to exploit all possible condition combinations while reducing computational complexity compared to conventional approaches; and 3) training-free guidance. Notably, the MCM in DrawMotion ensures that its intermediate features lie in a continuous space, allowing classifier-guidance gradients to update the features and thereby aligning the generated motions with user intentions while preserving fidelity. Quantitative experiments and user studies demonstrate that the freehand drawing approach reduces user time by approximately 46.7% when generating motions aligned with their imagination. The code, demos, and relevant data are publicly available at this https URL.

---


### 218. [A Deployment Audit of Release-Side Risk in Conformal Triage under Prevalence Shift](https://arxiv.org/abs/2605.20956)

**<font color=#1a73e8>作者：</font>** Chengze Li, Xiao Liu, Hanrong Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal triage converts predictive scores into deployment actions that either release a case, flag it for urgent attention, or defer it to human review. Under prevalence shift, however, the usual summaries of marginal coverage and human-review rate can miss the safety-critical question of whether patients who truly experience the target event are released without review. To address this gap, we introduce a leakage-aware deployment audit for release-side conformal triage. It first assigns target subjects to three non-overlapping roles: prevalence correction, conformal calibration, and held-out release-safety evaluation. This separation then lets the audit evaluate release directly: how many event-positive patients are cleared without review, whether the pilot has enough event labels for calibration, and how the safety-review trade-off shifts. Applying this audit to a retrospective NSCLC pilot shows why lower review can be misleading: after prevalence correction, the pooled conformal branch lowers review by releasing more patients, some of whom are event-positive. Within the audit, the classwise branch acts as a scarcity diagnostic: the pilot has too few event labels to certify safe low-review release.

---


### 219. [JobArabi: An Arabic Corpus and Analysis of Job Announcements from Social Media](https://arxiv.org/abs/2605.20960)

**<font color=#1a73e8>作者：</font>** Wajdi Zaghouani, Shimaa Amer Ibrahim, Mabrouka Bessghaier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces JobArabi, a large-scale corpus of Arabic job announcements collected from social media between January 2024 and October 2025. The dataset contains 20,528 public posts from X and captures more than two years of employment-related discourse across Arabic-speaking online communities. The corpus was compiled using a linguistically informed query framework covering 21 Arabic keyword families that reflect gendered, plural, formal, and dialectal expressions of recruitment language. The resulting dataset includes posts from institutional, commercial, and individual accounts and provides metadata such as timestamps, engagement indicators, and geolocation when available, enabling temporal and regional analysis of employment discourse. Quantitative analysis reveals several sociolinguistic patterns in online recruitment, including the persistence of gendered hiring language, regional variation in occupational demand, and the emotional framing of recruitment messages. These findings highlight the potential of Arabic social media as a resource for studying labor market communication and linguistic change. The JobArabi corpus, together with documentation and collection scripts, will be released to support research in Arabic NLP, computational social science, and digital labor studies.

---


### 220. [Preserve, Reveal, Expand: Faithful 4D Video Editing with Region-Aware Conditioning](https://arxiv.org/abs/2605.20961)

**<font color=#1a73e8>作者：</font>** Zhangchi Hu, Wenzhang Sun, Xiangchen Yin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 4D-driven video diffusion models primarily target plausible generation, but faithful 4D editing requires preserving source-observed regions while synthesizing disoccluded or out-of-view content. We identify Evidence-Role Mismatch: reliable source-backed evidence, unreliable rendered cues, and unsupported regions are entangled in a single conditioning signal, causing preservation drift, ghosting, and unstable extrapolation. We propose PREX (Preserve, Reveal, Expand), a region-aware framework that decomposes the target spatiotemporal volume into Preserve, Reveal, and Expand roles according to observation support and scene extent. PREX builds observation-backed appearance cues with calibrated confidence and injects them into a frozen video diffusion backbone through a region-aware adapter, trained with proxy tasks without requiring paired edited videos. We further introduce PREBench, a diagnostic benchmark with curated edits, region-role masks, and human-aligned metrics that complement global video-quality and 4D-control evaluations. Experiments show that PREX reduces region-structured failures while maintaining strong visual quality and 4D edit control capability. Project Page: this https URL

---


### 221. [Towards UAV Detection in the Real World: A New Multispectral Dataset UAVNet-MS and a New Method](https://arxiv.org/abs/2605.20963)

**<font color=#1a73e8>作者：</font>** Yihang Luo, Jun Chen, Chao Xiao 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The proliferation of unmanned aerial vehicles (UAVs) has created urgent demand for precise UAV monitoring. Existing RGB-based systems rely on spatial cues that degrade at small scales, particularly with high inter-type similarity, target-clutter ambiguity, and low contrast. Multispectral imaging (MSI) encodes material-aware spectral signatures, yet MSI-based fine-grained small-UAV detection remains underexplored due to lack of dedicated datasets. We introduce UAVNet-MS, the first multispectral dataset for fine-grained small-UAV detection, comprising 15,618 temporally synchronized RGB-MSI data cubes (1440x1080) with bounding box annotations. The dataset features challenging small objects (93.7% <= 32^2 pixels, average 18^2 pixels, ~0.02% image area) under low contrast. We propose MFDNet, a dual-stream baseline addressing array-induced parallax and spatial-spectral fusion. Extensive evaluation under RGB-only, MSI-only, and RGB+MSI protocols against 20 detectors shows MFDNet achieves +6.2% AP50 improvement over best RGB-only methods, demonstrating spectral cues provide complementary material evidence beyond spatial cues. This work provides foundational dataset, strong baseline, and benchmark for multispectral UAV monitoring research.

---


### 222. [Comparative Evaluation of Deep Learning Models for Fake Image Detection](https://arxiv.org/abs/2605.20971)

**<font color=#1a73e8>作者：</font>** Akhitha Pakala, Mohammed Mahir Rahman, Shahzad Memon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The growing sophistication of GAN-based image manipulation presents significant challenges for digital forensics. This study compares the performance of four pretrained CNN architectures including VGG16, ResNet50, EfficientNetB0, and XceptionNet for fake image detection using a unified preprocessing and training pipeline. A dataset of real and manipulated images was processed through resizing, normalization, and augmentation to address class imbalance and improve generalization. Models were evaluated using Accuracy, Precision, Recall, F1-score, and ROC-AUC. VGG16 achieved the highest accuracy at 91%, with XceptionNet, ResNet50, and EfficientNetB0 each reaching 90%. EfficientNetB0 showed stronger sensitivity to fake images but reduced reliability on real samples, reflecting imbalance-driven bias. Limitations include dataset imbalance, overfitting, and limited interpretability, which affect cross-domain robustness. The study provides a reproducible baseline and underscores the need for balanced datasets, advanced augmentation, and fairness-aware training to develop reliable fake image detection systems.

---


### 223. [Towards Integrated Rock Support Visualisation in 3D Point Cloud of Underground Mines](https://arxiv.org/abs/2605.20973)

**<font color=#1a73e8>作者：</font>** Dibyayan Patra, Simit Raval, Pasindu Ranasinghe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The effectiveness of rock support in underground mines depends on the interaction between installed rock bolts and the structural fabric of the surrounding rock mass. However, discontinuity characterisation and rock bolt identification are commonly treated as separate tasks, limiting their value for integrated support assessment. This study presents an automated framework for integrated rock support visualisation using 3D point clouds of underground mine excavations. The framework integrates structure mapping, rock bolt identification, discontinuity plane fitting, and bolt orientation estimation into a unified workflow optimised for accuracy and computational efficiency. The outputs are used to generate an integrated 3D visualisation of fitted discontinuity planes and bolt vectors, enabling direct assessment of their spatial intersections and geometric relationships. A complementary stereographic analysis of discontinuity poles and bolt orientations is also performed to evaluate overall bolting geometric effectiveness relative to the mapped structural fabric. Additionally, bolt-level quality metrics, including exposed protrusion length and deviation from the local roof normal, are visualised to support assessment of installation quality. The proposed framework is demonstrated on real underground metal mine scans, producing accurate structure mapping and rock bolt identification results in medium-scale point clouds. Overall, the study provides a practical step towards automated, integrated geotechnical assessment of rock support effectiveness without requiring manual measurements or additional in-situ data acquisition.

---


### 224. [Choose Wisely and Privately: Proactive Client Selection for Fair and Efficient Federated Learning](https://arxiv.org/abs/2605.20975)

**<font color=#1a73e8>作者：</font>** Adda Akram Bendoukha, Heber Hwang Arcolezi, Nesrine Kaaniche 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning enables collaborative model training across decentralized data sources without data transfer. Averaging-based FL is limited by the presence of non-IID data, which negatively impacts convergence speed and final model accuracy. Conventional alternatives suffer from significant inefficiency. Clients with noisy or highly heterogeneous data contribute expensive gradient computations that are either discarded or heavily down-weighted before aggregation. These reactive approaches waste computational resources, require more communication rounds and result in unnecessary privacy exposure. In this paper, we propose a proactive client selection framework that aims to find an optimal federation of clients whose combined data match utility and fairness requirements before training begins. Our method relies on mutual information computed from differentially private contingency tables to quantify the relevance of cross-feature correlations in the union dataset. We introduce a Potential Federation Loss (PFL) over the set of fixed-size federations, which balances two objectives. Maximizing collective data utility while ensuring fair cross-features correlations to prevent group unfairness. Client selection is expressed as an optimal subset search problem over the PFL objective, which we solve using simulated annealing under strong differential privacy guarantees for clients' local statistics. Experimental results on four benchmarks show faster, fairer, and more accurate models trained on optimally found federations, compared to uniform sampling, even when state-of-the-art adaptive aggregation or sampling strategies are employed.

---


### 225. [Point Cloud Sequence Encoding for Material-conditioned Graph Network Simulators](https://arxiv.org/abs/2605.20978)

**<font color=#1a73e8>作者：</font>** Philipp Dahlinger, Balázs Gyenes, Niklas Freymuth 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Network Simulators (GNSs) have emerged as powerful surrogates for complex physics-based simulation, offering inherent differentiability and orders-of-magnitude speedups over traditional solvers. However, GNSs typically assume access to the underlying material parameters, such as stiffness or viscosity, severely limiting their utility in realistic experimental settings. While recent meta-learning approaches address the parameter dependency by inferring properties from mesh trajectories, reconstructing a mesh from an observed scene is challenging. In this work, we introduce Point Cloud Encoding for Accurate Context Handling (PEACH), a novel framework that applies in-context learning on point clouds to adapt a learned simulator to unseen physical properties during inference. Our approach relies on a novel spatio-temporal point cloud sequence encoder, as well as two forms of auxiliary supervision to help improve simulation fidelity. We demonstrate that PEACH is capable of accurate zero-shot sim-to-real transfer on a challenging, dynamic scene. Experiments on simulation scenes show that PEACH even outperforms mesh-based baselines on prediction accuracy, while being much more practical for real-world deployment.

---


### 226. [An IoT-Enabled Smart Home Automation System for Energy Efficiency with Web-Based Control](https://arxiv.org/abs/2605.20981)

**<font color=#1a73e8>作者：</font>** Amaan Ahmed, Mohammed Mahir Rahman, Shahzad Memon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper illustrates the design and implementation of a smart home automation system for the conservation of energy and user control with the help of environmental sensors and Raspberry Pi 5. It monitors real-time conditions like motion, temperature, humidity, light and smoke to automatically control the device's behavior and save energy. A prototype single two-room was developed which uses GPIO/I2C interfaces to integrate sensors and actuators. The fan speed and LED brightness was dynamically controlled using PWM. Manual control and real-time monitoring are made possible through a web dashboard that was developed using Flask and graphical displays, and CSV logs of the energy are taken every 30 seconds. It was designed in an iterative model of sprints and the energy savings during testing was more than 46% over an always-on model. The results prove that with the help of these low-cost, modular devices it is possible to improve sustainability and usability in the home as part of the IoT.

---


### 227. [Domijn: The Security of Domain Registrars and the Risk of a Domain Name Takeover](https://arxiv.org/abs/2605.20984)

**<font color=#1a73e8>作者：</font>** Koen van Hove, Jeroen van der Ham-de Vos, Roland van Rijswijk-Deij  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Domain names are key assets for organisation. They anchor an organisation's online presence and reputation, and serve as linking pin for web services and, e.g., email. Consequently, a malicious takeover of a domain can lead to significant damages. Organisations register domain names through so-called registrars, a type of business that plays a key role in the domain name industry. This implies that registrars play an important part in safeguarding against malicious takeovers of domains. In this paper we empirically study how registrars implement security controls to prevent against such takeovers. We focus on the top 10 most popular registrars for the .nl ccTLD. We present the results of this study in light of a model for the impact of domain takeovers, that analyses the possible consequence of a takeover. We contrast this against the impact of two other well-known threats: ransomware and DDoS attacks. We find that all registrars in our study implement relatively effective security measures, but that they fall short in more advanced security controls, such as the proper implementation of two-factor authentication. We also find that a domain takeover can have significant impact, potentially equalling that of a ransomware attack.

---


### 228. [A Sharper Picture of Generalization in Transformers](https://arxiv.org/abs/2605.20988)

**<font color=#1a73e8>作者：</font>** Paul Lintilhac, Sair Shaikh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study transformers' generalization behavior on boolean domains from the perspective of the Fourier Spectra of their target functions. In contrast to prior work (Edelman et al., 2022; Trauger and Tewari, 2024), which derived generalization bounds from Rademacher complexity, we investigate the feasibility of obtaining generalization bounds via PAC-Bayes theory. We show that sparse spectra concentrated on low-degree components enable low-sharpness constructions with good generalization properties. Our idea is to show the existence of flat minima implementing any boolean function of sparsity no greater than the context length, and then apply a PAC-Bayes bound to an idealized low-sharpness learner, resulting in a non-vacuous generalization bound. We evaluate predictions empirically and conduct a mechanistic interpretability study to support the realism of our theoretical construction in real transformers.

---


### 229. [Modeling Temporal scRNA-seq Data with Latent Gaussian Process and Optimal Transport](https://arxiv.org/abs/2605.20989)

**<font color=#1a73e8>作者：</font>** Mehmet Yigit Balik, Harri Lähdesmäki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-cell RNA sequencing provides insights into gene expression at single-cell resolution, yet inferring temporal processes from these static snapshot measurements remains a fundamental challenge. Current approaches utilizing neural differential equations and flows are sensitive to overfitting and lack careful considerations of biological variability. In this work, we propose a generative framework that models population trends using a latent heteroscedastic Gaussian process (GP) approximated by Hilbert space methods. To address the absence of genuine cell trajectories, we leverage an optimal transport (OT) objective that aligns generated and observed population distributions. Our method explicitly captures biological heterogeneity by incorporating cell-specific latent time and cell type conditioning to disentangle temporal asynchrony and trajectories to different cell types. We demonstrate state-of-the-art performance on complex interpolation and extrapolation benchmarks and introduce a novel gradient-based strategy for inferring perturbation trajectories.

---


### 230. [CHOIR: Contact-aware 4D Hand-Object Interaction Reconstruction](https://arxiv.org/abs/2605.20992)

**<font color=#1a73e8>作者：</font>** Hao Xu, Yilin Liu, Yinqiao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We ask whether everyday open-world monocular videos can be turned into reusable 4D interaction primitives: articulated hand motion, object shape with 6D pose over time, and the when/where of contact. Such a capability would enable scalable mining of real interactions and, beyond reconstruction, support scene-aware synthesis and planning. However, reconstructing hand-object interaction (HOI) from challenging monocular videos remains difficult: methods often assume known objects or curated scenes, and separately estimated hands and objects easily become misaligned under clutter, occlusion, and unseen object geometries. Targeting this setting, we present CHOIR, a Contact-aware HOI Reconstruction framework for a monocular camera, using contact as an explicit coupling signal between hands and objects. CHOIR first initializes a coarse, contact-agnostic 4D HOI sequence from open-world visual priors. It then introduces a generative HOI spatial rectification module to predict ray-depth corrections and rectify hand-object relative placement, then derive initial per-frame contact correspondences on the rectified geometry. Last, a contact-aware joint optimization with dynamically updated contact constraints enforces geometric, temporal, and contact consistency. Experiments on controlled and challenging videos show that CHOIR improves object reconstruction, physical plausibility, and temporal consistency over state-of-the-art methods.

---


### 231. [Hybrid Machine Learning Model for Forest Height Estimation from TanDEM-X and Landsat Data](https://arxiv.org/abs/2605.20997)

**<font color=#1a73e8>作者：</font>** Islam Mansour, Ronny Haensch, Irena Hajnsek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Integrating machine learning (ML) with physical models (PM) has emerged as a promising way of retrieving geophysical parameters from remote sensing data. In this context, a ML model for estimating forest height from TanDEM-X interferometric coherence measurements has recently been proposed, that constrains the learning process through a PM. While the features used for training and inversion where selected to ensure the physical consistency of the solutions, they could not resolve all height / structure and baseline / terrain slope ambiguities in the data. To improve this, the extension of the feature space with optical Landsat data is proposed able to provide complementary information on forest type or structure. The extended model is applied and validated on several TanDEM-X acquisitions over the Gabonese Lopé national park site and assessed against airborne LiDAR measurements. Results show a 13.5% reduction in RMSE and a 16.6% reduction in MAE compared to the original hybrid model, confirming the added value of multispectral inputs.

---


### 232. [Single-Pass, Depth-Selective Reading for Multi-Aspect Sentiment Analysis](https://arxiv.org/abs/2605.20998)

**<font color=#1a73e8>作者：</font>** Yan Xia, Zhuangzhuang Pan, Amirrudin Kamsin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aspect-Term Sentiment Analysis (ATSA) in multi-aspect sentences faces a fundamental tradeoff between efficiency and expressiveness. Existing models either re-encode the sentence for each aspect or rely on static use of deep representations, leading to redundant computation and limited adaptivity. We argue that Transformer depth is a costly, queryable resource, and propose DABS, a single-pass inference framework that encodes each sentence once to construct a reusable, depth-ordered substrate. Each aspect then queries this shared representation to selectively read relevant tokens and abstraction levels, without re-encoding. This decouples shared sentence encoding from lightweight, aspect-conditioned readout. Experiments on four ATSA benchmarks show that DABS achieves competitive performance while reducing end-to-end computation by up to 60% in multi-aspect settings (M >= 2). Further analyses indicate that adaptive depth querying is most beneficial for linguistically complex cases such as negation and contrast. Code is publicly available at this https URL

---


### 233. [DAMA: Disentangled Body-Anchored Gaussians for Controllable Multi-Layered Avatars](https://arxiv.org/abs/2605.21001)

**<font color=#1a73e8>作者：</font>** Daniel Eskandar, Berna Kabadayi, Garvita Tiwari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D clothed avatar reconstruction methods achieve high visual fidelity but ignore geometric structure and physical plausibility. They either model clothed humans as a single deformable surface or attempt garment disentanglement without enforcing geometric constraints, resulting in ambiguous garment boundaries and no control over stacking or layer ordering. To address these limitations, we introduce DAMA (Disentangled body-Anchored Gaussians for Controllable Multi-layered Avatars), a 3D avatar reconstruction method that produces physically plausible clothed avatars through a dedicated representation and reconstruction method. At the representation level, we bind Gaussians to SMPL-X faces using barycentric in-plane coordinates and a positive normal offset. Based on this parameterization, the reconstruction method lifts 2D segmentations to body-anchored Gaussians, refines layers using topology-guided correction, and jointly optimizes geometry and appearance. DAMA is the first Gaussian avatar reconstruction method from multi-view images to achieve physically plausible layering, clean garment separation, and explicit stacking control. On the full 4D-DRESS dataset (82 scans), it achieves state-of-the-art performance in geometry reconstruction, garment separation, penetration rate, and penetration depth. The representation further supports user-defined garment reordering and fast conversion of body-conforming garments to simulation-ready meshes. Project Page: this https URL

---


### 234. [Verifiable Provenance and Watermarking for Generative AI: An Evidentiary Framework for International Operational Law and Domestic Courts](https://arxiv.org/abs/2605.21002)

**<font color=#1a73e8>作者：</font>** Gustav Olaf Yunus Laitinen-Fredriksson Lundström-Imanov, Nurana Abdullayeva  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence now synthesizes photorealistic imagery, audio, and video at a cost that defeats traditional forensic intuition. The legal consequences span three regimes studied so far in isolation: international operational law, domestic procedure, and product regulation. This article presents a unified evidentiary framework that maps cryptographic content provenance, robust statistical watermarking, and zero knowledge attestation to the proof requirements of each regime. We define a five tier threat model spanning naive regeneration, adversarial laundering, cross model regeneration, active watermark removal, and insider provenance forgery. We release a public benchmark of 12000 generated items across image, audio, and video modalities under six laundering pipelines for 72000 evaluation samples. We evaluate four representative schemes and report true positive rate at fixed false positive rate, robustness area under the curve, computational overhead, and a regime conditioned legal sufficiency score. We translate empirical detection bounds into legal sufficiency thresholds for command decisions under the law of armed conflict, for criminal and civil admissibility under domestic procedure, and for persistence audits under the European Union Artificial Intelligence Act and analogous regimes. The result is a reproducible reference pipeline, a public benchmark, and model annexes that lawyers, engineers, and operators can deploy together.

---


### 235. [Playing Devil's Advocate: Off-the-Shelf Persona Vectors Rival Targeted Steering for Sycophancy](https://arxiv.org/abs/2605.21006)

**<font color=#1a73e8>作者：</font>** Ishaan Kelkar, Nebras Alam, Vikram Kakaria 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study the effect of different persona on \textbf{sycophancy}: model's agreement with users even when the user is incorrect. The standard mitigation, Contrastive Activation Addition (CAA), derives a steering direction from labelled pairs of sycophantic and honest responses. This study evaluates whether off-the-shelf persona steering vectors, originally developed for general role-playing and not trained on sycophancy data, can serve as an alternative. In two instruction-tuned models, steering toward personas characterised by doubt or scrutiny reduces sycophancy to approximately $68\%$ and $98\%$ of CAA's effect, and, unlike CAA, maintains accuracy when the user is correct. The effect is also asymmetric: steering toward agreeable personas does not produce a mirror increase in sycophancy. Geometrically, the persona vector is largely independent of the direction of sycophancy in activation space. Collectively, these findings suggest that sycophancy is better understood as a persona-level property rather than a single steerable direction. We release our code here: this https URL.

---


### 236. [LiteViLNet: Lightweight Vision-LiDAR Fusion Network for Efficient Road Segmentation](https://arxiv.org/abs/2605.21007)

**<font color=#1a73e8>作者：</font>** Daojie Peng, Bingtao Wang, Fulong Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Road segmentation is a fundamental perception task for autonomous driving and intelligent robotic systems, requiring both high accuracy and real-time inference, especially for deployment on resource-constrained edge devices. Existing multi-modal road segmentation methods often rely on heavy transformer-based encoders to achieve state-of-the-art performance, but their enormous computational cost prohibits real-time deployment on embedded platforms. To address this dilemma, we propose \textbf{LiteViLNet}, a lightweight multi-modal network that fuses RGB texture information and LiDAR geometric information for efficient road segmentation. Specifically, we design a dual-stream lightweight encoder and depth-wise separable convolutions to extract hierarchical features from both modalities with minimal parameters. We further propose a Multi-Scale Feature Fusion Module (MSFM) to facilitate cross-modal interaction at different levels, and a large-kernel-bridge module to capture long-range dependencies with linear complexity. Extensive experiments on the KITTI Road dataset and real-world applications demonstrate that LiteViLNet achieves a promising balance between accuracy and efficiency. Notably, with only 14.04M parameters, our model attains a 96.36\% MaxF score, ranking the best among all CNN-based methods and being comparable to larger transformer-based models, and runs at 163.79 FPS in model-only inference on RTX 4060 Ti (22.18 FPS on Jetson Orin NX). It outperforms numerous heavy-weight methods in inference speed while maintaining highly competitive accuracy, fully validating the potential of LiteViLNet for real-time embedded deployment in autonomous driving and intelligent robotics.

---


### 237. [DySink: Dynamic Frame Sinks for Autoregressive Long Video Generation](https://arxiv.org/abs/2605.21028)

**<font color=#1a73e8>作者：</font>** Bo Ye, Xinyu Cui, Jian Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive long video generation often adopts bounded-memory streaming for efficiency, typically combining local windows for short-term continuity with static early-frame sinks as long-range anchors. However, this fixed allocation keeps early frames cached even when the current visual state has substantially diverged from them, while discarding potentially more relevant intermediate history. As a result, the retained long-range context may become less adaptive and bias generation toward outdated cues; in severe cases, RoPE-induced phase re-alignment can homogenize inter-head attention and cause sink collapse, where content regresses toward sink frames. We propose DySink, a retrieval-based framework that maintains a compact memory bank and selects visually relevant historical frames as dynamic frame sinks. DySink couples adaptive retrieval with a sink anomaly gate, which detects excessive inter-head consensus over retrieved context and suppresses collapse-prone context. Experiments on minute-long videos show that DySink consistently improves dynamic degree over strong baselines while also achieving higher temporal quality. The code and model weights will be released at this https URL.

---


### 238. [Building a Custom Taxonomy of AI Skills and Tasks from the Ground Up with Job Postings](https://arxiv.org/abs/2605.21029)

**<font color=#1a73e8>作者：</font>** Stephen Meisenbacher, Peter Norlander  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Utilizing LLMs for automated taxonomy construction presents a clear opportunity for the comprehensive, yet efficient mapping of potentially complex domains. When contending with high volumes of rapidly growing corpora, however, it becomes unclear how to best leverage such data for optimal taxonomy construction. Taking the case of systematizing AI skills in the workplace, we use two large-scale job postings corpora to investigate key design decisions for the inclusion (or exclusion) of data points for taxonomy construction. We propose TaxonomyBuilder as a blueprint for our systematic study, with which we evaluate various configurations of custom, data-informed, and hierarchical taxonomies. We demonstrate that less data can provide more clarity: filtering inputs to TaxonomyBuilder provides better domain-specific coverage than offering unfiltered inputs to clustering and LLM-enhanced hierarchical taxonomy labeling tools.

---


### 239. [Towards Physically Consistent 4D Scene Reconstruction for Closed-loop Autonomous Driving Simulation](https://arxiv.org/abs/2605.21032)

**<font color=#1a73e8>作者：</font>** Bowyn Tan, Yutong Xie, Bai Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity street scene reconstruction is pivotal for end-to-end autonomous driving simulation, where novel-view synthesis (NVS) and time-varying information modeling are two fundamental capabilities to facilitate closed-loop training. However, existing 3DGS methods and their 4D extensions fail to simultaneously achieve both. To bridge this gap, we establish an information-geometric diagnostic framework, revealing that this limitation stems from a credit assignment dilemma between spatial and temporal parameters. Specifically, the deterministic coupling between viewpoint and time in single-source observation creates a low-rank structure that induces massive null-space ambiguity between static view-dependent and dynamic time-varying components. Temporal information overshadows spatial cues, causing the estimation variance of spatial parameters to diverge. To address this issue, we propose Orthogonal Projected Gradient (OPG), a hierarchical training method designed to restore spatial identifiability. OPG prioritizes the integrity of spatial representations by securing them in an initial stage, then restricts temporal updates to the spatial null space, enabling proactive credit assignment. While OPG isolates temporal updates algebraically, Temporal Regularization Strategy is proposed to further refine the temporal solution space by imposing a smoothness constraint based on the physical prior of consistent appearance evolution, ensuring that the reconstructed scene remains physically consistent in closed-loop simulation. Extensive experiments demonstrate that our method not only maintains stable NVS capabilities but also demonstrates superior performance in traditional observation-reproducing metrics, which indirectly reflect the capability of modeling temporal dynamics.

---


### 240. [Efficient Banzhaf-Based Data Valuation for $k$-Nearest Neighbors Classification](https://arxiv.org/abs/2605.21033)

**<font color=#1a73e8>作者：</font>** Guangyi Zhang, Lutz Oettershagen, Lixu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data valuation, the task of quantifying the contribution of individual data points to model performance, has emerged as a fundamental challenge in machine learning. Game-theoretic approaches, such as the Banzhaf value, offer principled frameworks for fair data valuation; however, they suffer from exponential computational complexity. We address this challenge by developing efficient algorithms specifically tailored for computing Banzhaf values in $k$-nearest neighbor ($k$NN) classifiers. We first establish the theoretical hardness of the problem by proving that it is \#P-hard. Despite this intractability, we exploit the locality properties of $k$NN classifiers to develop practical exact algorithms. Our main contribution is a dynamic programming framework that achieves significant computational improvements: we present a pseudo-polynomial algorithm with $O(Wkn^2)$ time complexity for weighted $k$NN classifiers, where $W$ is the maximum sum of top-$k$ weights, and a specialized algorithm for unweighted $k$NN that achieves $O(nk^2)$ time complexity, that is, linear in the number of data points. We also offer efficient Monte Carlo estimation methods. Extensive experiments on real-world datasets demonstrate the practical efficiency of our approach and its effectiveness in data valuation applications.

---


### 241. [Dynamic Video Generation: Shaping Video Generation Across Time and Space](https://arxiv.org/abs/2605.21042)

**<font color=#1a73e8>作者：</font>** Shikang Zheng, Jingkai Huang, Jiacheng Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved impressive performance in video generation, but their iterative denoising process remains computationally expensive due to the large number of tokens processed at each timestep. Recently, progressive resolution sampling has emerged as a promising acceleration approach by reducing latent resolution in early stages. However, scaling this idea to video generation remains challenging, as the additional temporal dimension introduces diverse spatio-temporal demands across different videos, and compressing only a single dimension often leads to limited acceleration or degraded quality. Therefore, we propose DVG, a Dynamic Video Generation framework that jointly allocates computation across time and space, automatically selecting content-aware acceleration strategies without manual tuning or retraining. DVG achieves near-lossless acceleration across models and tasks, reaching up to 7 times speedup on HunyuanVideo and HunyuanVideo-1.5, and 18 times when combined with distillation, demonstrating its potential as a key component in today's large-scale efficient video generation systems. Our code is in supplementary material and will be released on Github.

---


### 242. [A Dialogue between Causal and Traditional Representation Learning: Toward Mutual Benefits in a Unified Formulation](https://arxiv.org/abs/2605.21058)

**<font color=#1a73e8>作者：</font>** Yan Li, Yuewen Sun, Shaoan Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal representation learning (CRL) and traditional representation learning have largely developed along different trajectories. Traditional representation learning has been driven mainly by applications and empirical objectives, whereas CRL has focused more on theoretical questions, particularly identifiability. This difference in emphasis has created a gap between the two fields in terminology, problem formulation, and evaluation, limiting communication and sometimes leading to disconnected or redundant efforts. In this paper, we argue that these two fields should be brought into dialogue rather than treated as separate paradigms. To this end, we introduce a unified formulation in which the representation learning is characterized by two components: a task component, which specifies what information the learned representation is required to preserve, and a constraint component, which specifies what structure is imposed on the latent space. Under this formulation, the benefits run in both directions. CRL provides theoretical tools for understanding when structured latent constraints are useful or necessary, while traditional representation learning offers practical insights on task design and objective choice that can improve the development of CRL methods. To illustrate this interaction, we experimentally study how different task components affect the behavior of CRL methods under different structured constraints. Results on CausalVerse show that the effectiveness of causal constraints depends strongly on the tasks with which they are paired.

---


### 243. [Divide et Calibra: Multiclass Local Calibration via Vector Quantization](https://arxiv.org/abs/2605.21060)

**<font color=#1a73e8>作者：</font>** Cesare Barbera, Lorenzo Perini, Giovanni De Toni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate and well-calibrated Machine Learning (ML) models are mandatory in high-stakes settings, yet effective multiclass calibration remains challenging: global approaches assume calibration errors are homogeneous across the latent space, while local methods often rely on latent-space dimensionality reduction, which leads to information loss. To address these issues, we propose a compositional approach to multiclass calibration, where region-specific calibration maps are constructed from shared codeword-dependent factors. We instantiate this idea via Vector Quantization (VQ), which induces a structured partition of the representation space, and an indexed parameterization of Dirichlet concentrations that enables parameter sharing across regions. Our approach learns heterogeneous calibration maps that generalize well even to sparse regions of the latent space. Experiments on benchmark datasets show significant improvements in local calibration while maintaining competitive global calibration and predictive performance.

---


### 244. [Grounding Driving VLA via Inverse Kinematics](https://arxiv.org/abs/2605.21061)

**<font color=#1a73e8>作者：</font>** Junsung Park, Hyunjung Shim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing Driving VLAs predict trajectories while largely ignoring their visual tokens -- a phenomenon we trace not to insufficient training but to a structurally ill-posed task formulation. We show that trajectory recovery, when viewed through the lens of inverse kinematics, requires both a current and a future visual state as boundary conditions; existing VLAs supply only the former, which encourages the model to shortcut through ego status and text commands alone. To address this, we re-design Driving VLA in the style of an inverse kinematics solver. First, a next visual state prediction objective that requires the LLM to predict the future visual scene provides dense visual supervision and suppresses shortcut paths. Second, a separate Inverse Kinematics Network (a cross-attention-based conditional diffusion model) that takes only the current and future visual states as input is designed to suppress reliance on ego status and textual shortcuts during trajectory decoding. With this simple prescription alone, our 0.5B-scale model recovers visual grounding and reaches trajectory planning performance comparable to 7B--8B VLAs more than an order of magnitude larger, on both the closed-loop NAVSIM-v2 and the nuScenes benchmarks. Extensive analysis further shows that this improvement stems from a recovered ability to exploit visual features, with the effect being most pronounced in dynamic driving situations such as turning.

---


### 245. [Robust Personalized Recommendation under Hidden Confounding in MNAR](https://arxiv.org/abs/2605.21066)

**<font color=#1a73e8>作者：</font>** Zongyu Li, Wanting Su, Tianyu Xia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recommender systems often rely on observational user--item interaction data, which is prone to selection bias due to users' selective interactions with items. Inverse propensity weighting and doubly robust estimators effectively mitigate selection bias under observed confounding, but are unreliable in the presence of hidden confounders. Existing approaches relying on randomized controlled trials (RCTs) or global sensitivity bounds are constrained in practice: RCTs demand costly experimental data, while global sensitivity bounds presume a uniformly bounded effect of unmeasured confounders on propensities through sensitivity analysis, thereby neglecting heterogeneity across user--item interactions. To overcome this limitation, we propose a novel framework, which estimates user--item level sensitivity bounds, thereby substantially relaxing the homogeneity assumption inherent in global sensitivity bounds named Personalized Unobserved-Confounding-aware Interaction Deconfounder (PUID). To ensure both robustness and predictive accuracy, we further develop an adversarial optimization strategy and propose a benchmark-guided variant (BPUID) that incorporates pre-trained models as stabilizing references. Extensive experiments on three real-world datasets demonstrate that our approach significantly outperforms global methods under hidden confounding, without requiring RCT data.

---


### 246. [Towards Understanding Self-Pretraining for Sequence Classification](https://arxiv.org/abs/2605.21070)

**<font color=#1a73e8>作者：</font>** Omar Coser, Loredana Zollo, Paolo Soda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Amos et al. (2024) showed that the accuracy of Transformer models in sequence classification can be significantly improved by first pretraining with a masked token prediction objective without external data or augmentation, a procedure referred to as self-pretraining (SPT). While the primary objective of Amos et al. (2024) was to showcase that Transformers can achieve strong performance on the Long-Range Arena (LRA), their pipeline raises more fundamental questions: How does SPT drive optimization to better solutions? Why can standard supervised training fail in Transformers? To better understand this, we replicate and systematically ablate the findings of Amos et al. (2024). Our ablations suggest that a central bottleneck in the studied settings is not depth or generalization alone, but the ability of label supervision to learn useful query-key Attention patterns from random initialization. With a minimal setup, we identify learning proximity interactions - turning absolute positional encodings into proximity-biased Attention scores - as a key source of the improvements brought by SPT. Finally, in a simplified theoretical setup, we show that label supervision can be locally blind to certain Attention-score directions that are instead detectable through masked reconstruction.

---


### 247. [Q-ARVD: Quantizing Autoregressive Video Diffusion Models](https://arxiv.org/abs/2605.21072)

**<font color=#1a73e8>作者：</font>** Siao Tang, Xinyin Ma, Gongfan Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion models (ARVDs) have emerged as a promising architecture for streaming video generation, paving the way for real-time interactive video generation and world modeling. Despite their potential, the substantial inference cost of ARVDs remains a major obstacle to practical deployment, making model quantization a natural direction for improving efficiency. However, quantization for ARVDs remains largely unexplored. Our empirical analysis shows that directly applying existing quantization schemes developed for standard diffusion transformers to ARVDs leads to suboptimal performance, revealing quantization behaviors that differ from those observed in bidirectional diffusion models. In this paper, we identify two critical challenges in quantizing ARVDs: (C1) Highly unbalanced frame-wise quantization sensitivity. Error accumulation during autoregressive generation can induce severely skewed quantization sensitivity across frames, following an exponential-like decay pattern. (C2) Prominent and heterogeneous outlier patterns in weights. Weight distributions exhibit pronounced outlier channels, whose patterns vary substantially across layer types and block depths. To address these issues, we propose Q-ARVD, a novel framework for accurate ARVD quantization. (S1) To tackle the highly unbalanced frame-wise sensitivity, Q-ARVD incorporates a final-quality aware frame-weighting mechanism into the quantization objective. (S2) To prevent heterogeneous outliers from degrading performance, Q-ARVD introduces an outlier-aware adaptive dual-scale quantization, which automatically detects the presence and quantity of outlier channels for an arbitrary layer, and isolates them to protect normal channels. Extensive experiments demonstrate the superiority of Q-ARVD.

---


### 248. [GradeLegal: Automated Grading for German Legal Cases](https://arxiv.org/abs/2605.21076)

**<font color=#1a73e8>作者：</font>** Abdullah Al Zubaer, Lorenz Wendlinger, Simon Alexander Nonn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grading German legal exam solutions faces growing volumes and a shortage of qualified graders, delaying feedback and creating a bottleneck. At the same time, it is a high-stakes expert task, since state exam grades strongly influence career outcomes in Germany. Despite this practical relevance, literature lacks systematic studies on effective methods for grading legal exams. To address this gap, we investigate whether large language models (LLMs) can support the automated grading of German legal case solutions in criminal and public law, thereby enabling scalable feedback and student self-testing. We present a systematic evaluation of 27 proprietary and open-source LLMs, benchmarking prompting strategies that incrementally add task-related information, such as a sample solution and a grading rubric. Using quadratic weighted kappa (QWK), reasoning-oriented LLMs can approximate expert grading in public law when given a sample solution and a grading rubric (up to 0.91), compared to 0.60 in criminal law, suggesting a harder grading task in criminal law. Beyond single-model grading, ensembling improves agreement by up to 0.15 over its best member and can offer an alternative to stronger closed-source single models. In addition, our findings suggest that effective prompt design and model selection are necessary for reliable LLM-based grading of legal exams.

---


### 249. [VDFP: Video Deflickering with Flicker-banding Priors](https://arxiv.org/abs/2605.21079)

**<font color=#1a73e8>作者：</font>** Zhiyi Zhou, Libo Zhu, Zihan Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Capturing digital screens with smartphones frequently induces severe banding due to hardware synchronization mismatches. Existing video restoration methods struggle with these structured, periodic luminance fluctuations, often resulting in residual artifacts or over-smoothed textures. We firstly construct DeViD, a real-world dataset in various scenes to deal with the lack of available this http URL we propose VDFP (Video Deflickering with Flicker-banding Priors), a novel perception-guided generation framework. First, we introduce a Degradation Field Modeling Based on Rolling Shutter Mechanism (DFM) capable of synthesizing complex multi-banding scenarios. Second, we present a spatial-temporal continuous prior perception (CPP). Unlike traditional binary segmentation, this module is optimized via a Flicker-Aware Mean Squared Error (FA-MSE) to capture the luminance transitions. By zero-initializing an augmented input layer, our model preserves pre-trained generative priors as well as spatial-temporal prior perception. Extensive experiments demonstrate that VDFP significantly outperforms other methods, eliminating complex banding with high-fidelity spatial details and temporal consistency. Our dataset and code will be released at~ this https URL.

---


### 250. [Decoupling Communication from Policy: Robust MARL under Bandwidth Constraints](https://arxiv.org/abs/2605.21085)

**<font color=#1a73e8>作者：</font>** Alexi Canesse, Benoît Goupil, Jesse Read 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Communication enables coordination in multi-agent reinforcement learning (MARL), but many real-world applications, e.g., search-and-rescue with drone swarms, operate under severe bandwidth constraints. Many communication architectures still expose a coupled bottleneck in which a shared latent representation is used for both policy execution and inter-agent communication. Consequently, reducing message size directly limits the policy's latent space, often leading to significant performance degradation. We address this with two contributions. First, we introduce $\beta$, a normalised per-agent bandwidth budget that unifies sparsity, rounds, and message dimension into a single comparable constraint. Second, we provide SLIM, a minimal architecture that decouples the communication pathway from the policy's latent representation, allowing us to isolate the effect of bandwidth from the effect of policy capacity while benefiting from in-step communication. We evaluate our method on several partially-observable MARL benchmarks, where communication is essential. Our approach achieves state-of-the-art performance and exhibits scalability and robustness under limited communication, with only marginal degradation as bandwidth is reduced.

---


> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-352](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
