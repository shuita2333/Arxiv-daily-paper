# 📦 其他研究 | 2026年04月30日

> 本类共 **190** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-190**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-190**

---

### 151. [ClayScape: A GenAI-Supported Workflow for Designing Chinese Style Ceramics with Clay 3D Printing](https://arxiv.org/abs/2604.25657)

**<font color=#1a73e8>作者：</font>** Sijia Liu, Hoi Ching Silvester Mok, Long Ling 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Chinese ceramic-making involves complex and interdependent steps, making it technically demanding. Digital fabrication methods attempt to make the process more accessible, but for craft-creators, technical challenges such as CAD and CAM skills remain major obstacles. To address this, we designed a hybrid workflow that integrates Generative AI with clay 3D printing to support new creative possibilities. We evaluated the workflow through ClayScape, a design tool that operationalizes this approach, with four ceramic creators. Our findings show that the workflow supports accessible ceramic creation while revealing both expanded opportunities for creative exploration and challenges in balancing agency and control. This work demonstrates how hybrid workflows can lower barriers to digital fabrication while supporting creative possibilities in culturally grounded ceramic practices.

---


### 152. [Modeling Human-Like Color Naming Behavior in Context](https://arxiv.org/abs/2604.25674)

**<font color=#1a73e8>作者：</font>** Yuqing Zhang, Ecesu Ürker, Tessa Verhoef 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modeling the emergence of human-like lexicons in computational systems has advanced through the use of interacting neural agents, which simulate both learning and communicative pressures. The NeLLCom-Lex framework (Zhang et al., 2025) allows neural agents to develop pragmatic color naming behavior and human-like lexicons through supervised learning (SL) from human data and reinforcement learning (RL) in referential games. Despite these successes, the lexicons that emerge diverge systematically from human color categories, producing highly non-convex regions in color space, which contrast with the convexity typical of human categories. To address this, we introduce two factors, upsampling rare color terms during SL and multi-listener RL interactions, and adopt a convexity measure to quantify geometric coherence. We find that upsampling improves lexical diversity and system-level informativeness of the color lexicon, while many-listener setups promote more convex color categories. The combination of moderate upsampling and multiple listeners produces lexicons most similar to human systems.

---


### 153. [Exploring Remote Photoplethysmography for Neonatal Pain Detection from Facial Videos](https://arxiv.org/abs/2604.25680)

**<font color=#1a73e8>作者：</font>** Ashutosh Dhamaniya, Anup Kumar Gupta, Trishna Saikia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unaddressed pain in neonates can lead to adverse effects, including delayed development and slower weight gain, emphasising the need for more objective and reliable pain assessment methods. Hence, automated methods using behavioural and physiological pain indicators have been developed to aid healthcare professionals in the Neonatal ICU. Traditional contact-based methods for physiological parameter estimation are unsuitable for long-term monitoring and increase the risk of spreading diseases like COVID-19. We introduce a novel approach using remote photoplethysmography (rPPG) to estimate pulse signals in a non-contact manner and employ them for neonatal pain detection. The temporal signals acquired from regions-of-interest (ROIs) affected by skin deformations may exhibit lower quality and provide erroneous rPPG signals. Therefore, we incorporated a quality parameter to select the temporal signals obtained from ROIs that are least affected by skin deformations. Further, we employed signal-to-noise ratio as a fitness parameter to extract the rPPG signal corresponding to the clip that is least affected by noise. Experimental findings demonstrate that the rPPG signals provide useful information for neonatal pain detection, and signals extracted from the blue colour channel outperform those extracted from other colour channels. We also show that combining rPPG and audio features provides better results than individual modalities.

---


### 154. [QB-LIF: Learnable-Scale Quantized Burst Neurons for Efficient SNNs](https://arxiv.org/abs/2604.25688)

**<font color=#1a73e8>作者：</font>** Dewei Bai, Hongxiang Peng, Jiajun Mei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Binary spike coding enables sparse and event-driven computation in spiking neural networks (SNNs), yet its 1-bit-per-timestep representation fundamentally limits information throughput. This bottleneck becomes increasingly restrictive in deep architectures under short simulation horizons. We propose the Quantized Burst-LIF (QB-LIF) neuron, which reformulates burst spiking as a saturated uniform quantization of membrane potentials with a learnable scale. Instead of relying on predefined multi-threshold structures, QB-LIF treats the quantization scale as a trainable parameter, allowing each layer to autonomously adapt its spiking resolution to the underlying membrane-potential statistics. To preserve hardware efficiency, we introduce an absorbable scale strategy that folds the learned quantized scale into synaptic weights during inference, maintaining a strict accumulate-only (AC) execution paradigm. To enable stable optimization in the discrete multi-level space, we further design ReLSG-ET, a rectified-linear surrogate gradient with exponential tails that sustains gradient flow across burst intervals. Extensive experiments on static (CIFAR-10/100, ImageNet) and event-driven (CIFAR10-DVS, DVS128-Gesture) benchmarks demonstrate that QB-LIF consistently outperforms binary and fixed-burst SNNs, achieving higher accuracy under ultra-low latency while preserving neuromorphic compatibility.

---


### 155. [RADD: Retrieval-Augmented Discrete Diffusion for Multi-Modal Knowledge Graph Completion](https://arxiv.org/abs/2604.25693)

**<font color=#1a73e8>作者：</font>** Guanglin Niu, Bo Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most multi-modal knowledge graph completion (MMKGC) models use one embedding scorer to do both retrieval over the full entity set and final decision making. We argue that this coupling is a core bottleneck: global high-recall search and local fine-grained disambiguation require different inductive biases. Therefore, we propose a Retrieval-Augmented Discrete Diffusion (RADD) framework to decouple retrieve and reranking for MMKGC. A relation-aware multimodal KGE retriever serves as both global retriever and distillation teacher, while a conditional discrete denoiser performs shortlist-level entity-identity generation for reranking. Training combines KGE supervision, denoising cross-entropy, and temperature-scaled distillation from the retriever to the denoiser. At inference, the designed Diff-Rerank first forms a top-$K$ shortlist with the retriever and then reranks it with the denoiser, ensuring that recall is a strict prerequisite for precision. Experiments on three MMKGC benchmarks show that RADD achieves the best performance and consistent gains over strong unimodal, multimodal, and LLM-based baselines, while ablations further verify the contribution of each component.

---


### 156. [Backtranslation Augmented Direct Preference Optimization for Neural Machine Translation](https://arxiv.org/abs/2604.25702)

**<font color=#1a73e8>作者：</font>** Mehrdad Ghassabi, Spehr Rajabi, Hamidreza Baradaran Kashani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contemporary neural machine translation (NMT) systems are almost exclusively built by training on supervised parallel data. Despite the tremendous progress achieved, these systems still exhibit persistent translation errors. This paper proposes that a post-training paradigm based on reinforcement learning (RL) can effectively rectify such mistakes. We introduce a novel framework that requires only a general text corpus and an expert translator which can be either human or an AI system to provide iterative feedback. In our experiments, we focus specifically on English-to-German translation as a representative high-resource language pair. Crucially, we implement this RL-based post-training using Direct Preference Optimization (DPO). Applying our DPO-driven framework to the gemma3-1b model yields a significant improvement in translation quality, elevating it's COMET score from 0.703 to 0.747 on the English to German task. The results demonstrate that DPO offers an efficient and stable pathway for enhancing pre-trained NMT models through preference-based post-training.

---


### 157. [Designing and Evaluating Next-Generation Learning Interfaces: Linking AI, HCI, and the Learning Sciences](https://arxiv.org/abs/2604.25721)

**<font color=#1a73e8>作者：</font>** Meng Xia, Yan Chen, Qiao Jin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This workshop addresses this gap by bringing together researchers and practitioners from AI, HCI, and the learning sciences to explore how interactive systems can better support learning. We focus on the design and evaluation of human-AI collaborative learning interfaces that are technically robust, human-centered, and pedagogically grounded. By fostering interdisciplinary dialogue, the workshop aims to identify shared challenges, design principles, and research directions for next-generation learning technologies.

---


### 158. [Scalable Inference Architectures for Compound AI Systems: A Production Deployment Study](https://arxiv.org/abs/2604.25724)

**<font color=#1a73e8>作者：</font>** Srikanta Prasad S V, Utkarsh Arora  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern enterprise AI applications increasingly rely on compound AI systems - architectures that compose multiple models, retrievers, and tools to accomplish complex tasks. Deploying such systems in production demands inference infrastructure that can efficiently serve concurrent, heterogeneous model invocations while maintaining cost-effectiveness and low latency. This paper presents a production deployment study of a modular, platform-agnostic inference architecture developed at Salesforce to support compound AI use cases including Agentforce (autonomous AI agents) and ApexGuru (AI-powered code analysis). The system integrates serverless execution, dynamic autoscaling, and MLOps pipelines to deliver consistent low-latency inference across multi-component agent workflows. We report production results demonstrating over 50% reduction in tail latency (P95), up to 3.9x throughput improvement, and 30 to 40% cost savings compared to prior static deployments. We further present a novel analysis of compound-system-specific challenges including multi-model fan-out overhead, cascading cold-start propagation, and heterogeneous scaling dynamics that emerge uniquely when serving agentic workloads. Through detailed case studies and operational lessons, we illustrate how the architecture enables compound AI systems to scale model invocations in parallel, handle bursty multi-agent workloads, and support rapid model iteration - capabilities essential for operationalizing agentic AI at enterprise scale.

---


### 159. [Toward Scalable Terminal Task Synthesis via Skill Graphs](https://arxiv.org/abs/2604.25727)

**<font color=#1a73e8>作者：</font>** Zhiyuan Fan, Tinghao Yu, Yuanjun Cai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Terminal agents have demonstrated strong potential for autonomous command-line execution, yet their training remains constrained by the scarcity of high-quality and diverse execution trajectories. Existing approaches mitigate this bottleneck by synthesizing large-scale terminal task instances for trajectory sampling. However, they primarily focus on scaling the number of tasks while providing limited control over the diversity of execution trajectories that agents actually experience during training. In this paper, we present SkillSynth, an automated framework for terminal task synthesis built on a scenario-mediated skill graph. SkillSynth first constructs a large-scale skill graph, where scenarios serve as intermediate transition nodes that connect diverse command-line skills. It then samples paths from this graph as abstractions of real-world workflows, and uses a multi-agent harness to instantiate them into executable task instances. By grounding task synthesis in graph-sampled workflow paths, SkillSynth explicitly controls the diversity of minimal execution trajectories required to solve the synthesized tasks. Experiments on Terminal-Bench demonstrate the effectiveness of SkillSynth. Moreover, task instances synthesized by SkillSynth have been adopted to train Hy3 Preview, contributing to its enhanced agentic capabilities in terminal-based settings.

---


### 160. [QAROO: AI-Driven Online Task Offloading for Energy-Efficient and Sustainable MEC Networks](https://arxiv.org/abs/2604.25740)

**<font color=#1a73e8>作者：</font>** Yongtao Yao, Yao Yang, Haorui Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of artificial intelligence (AI) and intelligent science, intelligent edge computing has been widely adopted. However, the limitations of traditional methods, such as poor adaptability and the slow convergence of heuristic algorithms, are becoming increasingly evident. To enable sustainable and resource-efficient edge applications, this paper proposes an online task offloading framework for wireless powered mobile edge computing (MEC) networks, called Quantum Attention-based Reinforcement learning for Online Offloading (QAROO). The system employs a binary offloading strategy with the aim of co-optimizing computing and energy resources in dynamic channel environments. In response to the issues of poor adaptability in traditional approaches and the slow convergence of heuristic algorithms, the framework integrates quantum neural networks and attention mechanisms, introducing three key improvements: using recurrent neural networks to enhance temporal modeling capability, proposing an uncertainty-guided quantization method to improve exploration efficiency, and incorporating attention mechanisms into quantum networks to strengthen feature representation. Experiments demonstrate that the proposed method outperforms comparative schemes in terms of normalized computation speed and processing time, offering an efficient and stable solution for online task offloading in large-scale Internet of Things (IoT) dynamic environments.

---


### 161. [Threat-Oriented Digital Twinning for Security Evaluation of Autonomous Platforms](https://arxiv.org/abs/2604.25757)

**<font color=#1a73e8>作者：</font>** Thomas J. Neubert, Laxima Niure Kandel, Berker Peköz  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open, unclassified research on secure autonomy is constrained by limited access to operational platforms, contested communications infrastructure, and representative adversarial test conditions. This paper presents a threat-oriented digital twinning methodology for cybersecurity evaluation of learning-enabled autonomous platforms. The approach is instantiated as an open-source, modular twin of a representative autonomy stack with separated sensing, autonomy, and supervisory-control functions; confidence-gated multi-modal perception; explicit command and telemetry trust boundaries; and runtime hold-safe behavior. The contribution is methodological: a reproducible design pattern that translates threat analysis into observable, controllable tests for spoofing, replay, malformed-input injection, degraded sensing, and adversarial ML stress. Although the implemented proxy is ground based, the architecture is intentionally framed around stack elements shared with UAV and space systems, including constrained onboard compute, intermittent or high-latency links, probabilistic perception, and mission-critical recovery behavior. The result is an implementable research scaffold for dependable and secure autonomy studies across UAV and space domains.

---


### 162. [Measuring the Sensitivity of Classification Models with the Error Sensitivity Profile](https://arxiv.org/abs/2604.25765)

**<font color=#1a73e8>作者：</font>** Andrea Maurino  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The quality of training data is critical to the performance of machine learning models. In this paper, the Error Sensitivity Profile (ESP) is proposed. It quantifies the sensitivity of model performance to errors in a single feature or in multiple features. By leveraging ESP, data-cleaning efforts can be prioritized based on error types and features most likely to affect model performance. To support the computation of this metric, an integrated suite of tools, called \dirty, is created. We conduct an extensive experimental study on two widely used datasets using 14 classification models, revealing that performance degradation is not always predictable from simple correlations with the target variable.

---


### 163. [Unrequited Emotions: Investigating the Gaps in Motivation and Practice in Speech Emotion Recognition Research](https://arxiv.org/abs/2604.25776)

**<font color=#1a73e8>作者：</font>** Taryn Wong, Zeerak Talat, Hanan Aldarmaki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Critical analyses of emotion recognition technology have raised ethical concerns around task validity and potential downstream impacts, urging researchers to ensure alignment between their stated motivations and practice. However, these discussions have not adequately influenced or drawn from research on speech emotion recognition (SER). We address this gap by conducting a systematic survey of SER research to uncover what stated motivations drive this work and if they align with the datasets and emotions studied. We find that while SER research identifies appealing goals, such as well-situated voice-activated systems or healthcare applications, commonly-used datasets do not reflect these proposed deployment contexts, thus presenting a gap between motivations and research practices. We argue that such gaps engender ethical concerns, and that SER research should reassert itself with concrete use-cases to prevent misinterpretations, misuse, and downstream harms.

---


### 164. [Sketch2Arti: Sketch-based Articulation Modeling of CAD Objects](https://arxiv.org/abs/2604.25781)

**<font color=#1a73e8>作者：</font>** Yi Yang, Hao Pan, Yijing Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Articulation modeling aims to infer movable parts and their motion parameters for a 3D object, enabling interactive animation, simulation, and shape editing. In this paper, we present Sketch2Arti, the first sketch-based articulation modeling system for CAD objects. Our key observation is that designers naturally communicate articulation intent through lightweight sketches (e.g., arrows and strokes) that indicate how parts should move, yet translating such sketches into articulated 3D models remains largely manual. Sketch2Arti bridges this gap by enabling users to specify articulation through simple 2D sketches drawn from a chosen viewpoint. Given a CAD model and user sketches, our approach automatically discovers the corresponding movable parts and predicts their motion parameters, allowing iterative modeling of multiple articulations on complex objects with fine-grained control. Importantly, Sketch2Arti is trained in a category-agnostic manner without requiring object category information, leading to strong generalization to diverse objects beyond existing articulation datasets. Moreover, for shell models lacking interior structures, Sketch2Arti supports controllable internal completion guided by user sketches, generating plausible internal components consistent with the existing geometry and predicted motion constraints. Comprehensive experiments and user evaluations demonstrate the effectiveness, controllability, and generalization of Sketch2Arti. The code, dataset, and the prototype system are at this https URL.

---


### 165. [Subliminal Steering: Stronger Encoding of Hidden Signals](https://arxiv.org/abs/2604.25783)

**<font color=#1a73e8>作者：</font>** George Morgulis, John Hewitt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Subliminal learning describes a student language model inheriting a behavioral bias by fine-tuning on seemingly innocuous data generated by a biased teacher model. Prior work has begun to characterize this phenomenon but leaves open questions about the scope of signals it can transfer, the mechanisms that explain it, and the precision with which a bias can be encoded by seemingly unrelated data. We tackle all three problems by introducing subliminal steering, a variant of subliminal learning in which the teacher's bias is implemented not via a system prompt, as in prior work, but through a steering vector trained to maximize the likelihood of a set of target samples. First, we show that subliminal steering transfers complex multi-word biases, whereas prior work focused on single-word preferences, demonstrating a large scope of subliminally transferrable signals. Second, we provide mechanistic evidence that subliminal learning transfers not only the target behavioral bias, but also the steering vector itself, localized to the layers at which the teacher was steered. Finally, we show that the bias is encoded with surprising precision. We train a new steering vector directly on the subliminally-laden dataset and find that it attains high cosine similarity with the original vector.

---


### 166. [Diverse Image Priors for Black-box Data-free Knowledge Distillation](https://arxiv.org/abs/2604.25794)

**<font color=#1a73e8>作者：</font>** Tri-Nhan Vo, Dang Nguyen, Trung Le 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) represents a vital mechanism to transfer expertise from complex teacher networks to efficient student models. However, in decentralized or secure AI ecosystems, privacy regulations and proprietary interests often restrict access to the teacher's interface and original datasets. These constraints define a challenging black-box data-free KD scenario where only top-1 predictions and no training data are available. While recent approaches utilize synthetic data, they still face limitations in data diversity and distillation signals. We propose Diverse Image Priors Knowledge Distillation (DIP-KD), a framework that addresses these challenges through a three-phase collaborative pipeline: (1) Synthesis of image priors to capture diverse visual patterns and semantics; (2) Contrast to enhance the collective distinction between synthetic samples via contrastive learning; and (3) Distillation via a novel primer student that enables soft-probability KD. Our evaluation across 12 benchmarks shows that DIP-KD achieves state-of-the-art performance, with ablations confirming data diversity as critical for knowledge acquisition in restricted AI environments.

---


### 167. [Improving Diversity in Black-box Few-shot Knowledge Distillation](https://arxiv.org/abs/2604.25795)

**<font color=#1a73e8>作者：</font>** Tri-Nhan Vo, Dang Nguyen, Kien Do 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) is a well-known technique to effectively compress a large network (teacher) to a smaller network (student) with little sacrifice in performance. However, most KD methods require a large training set and internal access to the teacher, which are rarely available due to various restrictions. These challenges have originated a more practical setting known as black-box few-shot KD, where the student is trained with few images and a black-box teacher. Recent approaches typically generate additional synthetic images but lack an active strategy to promote their diversity, a crucial factor for student learning. To address these problems, we propose a novel training scheme for generative adversarial networks, where we adaptively select high-confidence images under the teacher's supervision and introduce them to the adversarial learning on-the-fly. Our approach helps expand and improve the diversity of the distillation set, significantly boosting student accuracy. Through extensive experiments, we achieve state-of-the-art results among other few-shot KD methods on seven image datasets. The code is available at this https URL.

---


### 168. [StratFormer: Adaptive Opponent Modeling and Exploitation in Imperfect-Information Games](https://arxiv.org/abs/2604.25796)

**<font color=#1a73e8>作者：</font>** Andy Caen, Mark H.M. Winands, Dennis J.N.J. Soemers  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present StratFormer, a transformer-based meta-agent that learns to simultaneously model and exploit opponents in imperfect-information games through a two-phase curriculum. The first phase trains an opponent modeling head to identify behavioral patterns from action histories while the agent plays a game-theoretic optimal (GTO) policy. The second phase progressively shifts the policy toward best-response (BR) exploitation, guided by a per-opponent regularization schedule tied to exploitability. Our architecture introduces dual-turn tokens -- feature vectors constructed at both agent and opponent decision points -- coupled with bucket-rate features that encode opponent tendencies across five strategic contexts. On Leduc Hold'em, a small poker variant with six cards and two betting rounds, we test against six opponent archetypes at two strength levels each, with exploitability ranging from 0.15 to 1.26 Big Blinds (BB) per hand. StratFormer achieves an average exploitation gain of +0.106 BB per hand over GTO, with peak gains of +0.821 against highly exploitable opponents, while maintaining near-equilibrium safety.

---


### 169. [Barriers to Universal Reasoning With Transformers (And How to Overcome Them)](https://arxiv.org/abs/2604.25800)

**<font color=#1a73e8>作者：</font>** Oliver Kraus, Yash Sarrof, Yuekun Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) has been shown to empirically improve Transformers' performance, and theoretically increase their expressivity to Turing completeness. However, whether Transformers can learn to generalize to CoT traces longer than those seen during training is understudied. We use recent theoretical frameworks for Transformer length generalization and find that -- under standard positional encodings and a finite alphabet -- Transformers with CoT cannot solve problems beyond $TC^0$, i.e. the expressivity benefits do not hold under the stricter requirement of length-generalizable learnability. However, if we allow the vocabulary to grow with problem size, we attain a length-generalizable simulation of Turing machines where the CoT trace length is linear in the simulated runtime up to a constant. Our construction overcomes two core obstacles to reliable length generalization: repeated copying and last-occurrence retrieval. We assign each tape position a unique signpost token, and log only value changes to enable recovery of the current tape symbol through counts circumventing both barriers. Further, we empirically show that the use of such signpost tokens and value change encodings provide actionable guidance to improve length generalization on hard problems.

---


### 170. [MAIC-UI: Making Interactive Courseware with Generative UI](https://arxiv.org/abs/2604.25806)

**<font color=#1a73e8>作者：</font>** Shangqing Tu, Yanjia Li, Keyu Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Creating interactive STEM courseware traditionally requires HTML/CSS/JavaScript expertise, leaving barriers for educators. While generative AI can produce HTML codes, existing tools generate static presentations rather than interactive simulations, struggle with long documents, and lack pedagogical accuracy mechanisms. Furthermore, full regeneration for modifications requires 200--600 seconds, disrupting creative flow. We present MAIC-UI, a zero-code authoring system that enables educators to create and rapidly edit interactive courseware from textbooks, PPTs, and PDFs. MAIC-UI employs: (1) structured knowledge analysis with multi-modal understanding to ensure pedagogical rigor; (2) a two-stage generate-verify-optimize pipeline separating content alignment from visual refinement; and (3) Click-to-Locate editing with Unified Diff-based incremental generation achieving sub-10-second iteration cycles. A controlled lab study with 40 participants shows MAIC-UI reduces editing iterations (4.9 vs. 7.0) and significantly improves learnability and controllability compared to direct Text-to-HTML generation. A three-month classroom deployment with 53 high school students demonstrates that MAIC-UI fosters learning agency and reduces outcome disparities -- the pilot class achieved 9.21-point gains in STEM subjects compared to -2.32 points in control classes. Our code is available at this https URL.

---


### 171. [Instruction-Evidence Contrastive Dual-Stream Decoding for Grounded Vision-Language Reasoning](https://arxiv.org/abs/2604.25809)

**<font color=#1a73e8>作者：</font>** Yashwant Pravinrao Bangde, Debaditya Roy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) exhibit strong performance in instruction following and open-ended vision-language reasoning, yet they frequently generate fluent outputs that are weakly grounded in visual evidence. Prior works have shown that instruction prompting further worsens this issue by amplifying language priors, especially when the visual signal is uncertain or ambiguous. To address this challenge, we propose a decoding framework that explicitly balances linguistic informativeness and visual faithfulness during generation. Our method, Instruction-Evidence Contrastive Dual-Stream Decoding (IECD2), maintains two parallel probability distributions of tokens at each decoding step: an instruction-driven stream that promotes expressive and informative responses, and an evidence-driven stream that enforces strict grounding in the image. These two streams are adaptively fused using a symmetric KL-based contrast-based gate, which suppresses tokens favored by language priors but unsupported by visual evidence, while preserving them when both distributions agree. We evaluate IECD2 on multiple datasets spanning various generative vision-language reasoning tasks such as captioning and visual question answering, including POPE, MME, VQAv2, AMBER, MS-COCO, and LLaVA-Bench. IECD2 demonstrates consistent improvements in task accuracy and reasoning performance, alongside a substantial reduction in hallucination across all evaluation metrics compared to state-of-the-art decoding approaches.

---


### 172. [Lexical Anthropomorphization Influences on Moral Judgments of AI Bad Behavior](https://arxiv.org/abs/2604.25814)

**<font color=#1a73e8>作者：</font>** Jaime Banks, Nicholas David Bowman, Roman Saladino  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Anthropomorphic language describing artificial intelligence (AI) is widespread in media, policy, and everyday discourse; so too are discussions of AI bad behavior, from hallucinations to inappropriate comments. How does humanizing language about AI shape moral judgments when AI behaves badly? Across four experiments (total N = 1,020), we tested whether lexical anthropomorphism (LA) primes shape judgments of AI moral character, behavior morality, and behavioral responsibility. Studies 1-3 tested interactions between anthropomorphic language and humanizing design cues (icons, names, self-referencing) in the context of amoral errors. Study 4 extended this to genuinely immoral AI behavior across seven moral-violation types. Results indicate humanizing language and design cues have little influence on moral judgments of misbehaving AI. Where effects emerged, high-anthropomorphic primes elevated perceptions of an AI's capacity for dishonesty. The type of moral violation observed was the strongest predictor of moral judgments, with harm and degradation violations producing the broadest negative character assessments. Prime drift, horn effects, and egoistic value orientations emerged as potentially important predictors of AI moral judgments.

---


### 173. [Magnification-Invariant Image Classification via Domain Generalization and Stable Sparse Embedding Signatures](https://arxiv.org/abs/2604.25817)

**<font color=#1a73e8>作者：</font>** Ifeanyi Ezuma, Olusiji Medaiyese  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Magnification shift is a major obstacle to robust histopathology classification, because models trained on one imaging scale often generalize poorly to another. Here, we evaluated this problem on the BreaKHis dataset using a strict patient-disjoint leave-one-magnification-out protocol, comparing supervised baseline, baseline augmented with DCGAN-generated patches, and a gradient-reversal domain-general model designed to preserve discriminative information while suppressing magnification-specific variation. Across held-out magnifications, the domain-general model achieved the strongest overall discrimination and its clearest gain was observed when 200X was held out. By contrast, GAN augmentation produced inconsistent effects, improving some folds but degrading others, particularly at 400X. The domain-general model also yielded the lowest Brier score at 0.063 vs 0.089 at baseline. Sparse embedding analysis further revealed that domain-general training reduced average signature size more than three-fold (306 versus 1,074 dimensions) while preserving equivalent predictive performance (AUC: 0.967 vs 0.965; F1: 0.930 vs 0.931). It also increased cross-fold signature reproducibility from near-zero Jaccard overlap in the baseline to 0.99 between the 100X and 200X folds. These findings show that calibrated, compact, and transferable representations can be learned without added architectural complexity, with clear implications for the reliable deployment of computational pathology models across heterogeneous acquisition settings.

---


### 174. ["The Worst Weather In America": Augmenting the Information Design of Extreme Cold Weather Forecasts](https://arxiv.org/abs/2604.25818)

**<font color=#1a73e8>作者：</font>** Michael Correll, Jay Broccolo, Drew Bush  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mount Washington is home to extreme, and extremely volatile, weather conditions. Consulting a weather forecast of conditions at the summit is vital for making one's visit as safe as possible. Using the discussion and suggestions arising from a participatory workshop as input, we test a design intervention employing color-coded hazard icons to function as visual summaries of Mount Washington Observatory's current text-heavy forecast through a crowd-sourced study. We find that the use of icons increases the perceived risk of activities involving visiting the mountain. However, we highlight remaining questions around visualization design and design ethics that warrant further study in the domain of how best to communicate cold weather hazards in ways that are mindful of the diversity of literacies and experiences of visitors.

---


### 175. [Mutual Forcing: Dual-Mode Self-Evolution for Fast Autoregressive Audio-Video Character Generation](https://arxiv.org/abs/2604.25819)

**<font color=#1a73e8>作者：</font>** Yupeng Zhou, Lianghua Huang, Zhifan Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we propose Mutual Forcing, a framework for fast autoregressive audio-video generation with long-horizon audio-video synchronization. Our approach addresses two key challenges: joint audio-video modeling and fast autoregressive generation. To ease joint audio-video optimization, we adopt a two-stage training strategy: we first train uni-modal generators and then couple them into a unified audio-video model for joint training on paired data. For streaming generation, we ask whether a native fast causal audio-video model can be trained directly, instead of following existing streaming distillation pipelines that typically train a bidirectional model first and then convert it into a causal generator through multiple distillation stages. Our answer is Mutual Forcing, which builds directly on native autoregressive model and integrates few-step and multi-step generation within a single weight-shared model, enabling self-distillation and improved training-inference consistency. The multi-step mode improves the few-step mode via self-distillation, while the few-step mode generates historical context during training to improve training-inference consistency; because the two modes share parameters, these two effects reinforce each other within a single model. Compared with prior approaches such as Self-Forcing, Mutual Forcing removes the need for an additional bidirectional teacher model, supports more flexible training sequence lengths, reduces training overhead, and allows the model to improve directly from real paired data rather than a fixed teacher. Experiments show that Mutual Forcing matches or surpasses strong baselines that require around 50 sampling steps while using only 4 to 8 steps, demonstrating substantial advantages in both efficiency and quality. The project page is available at this https URL.

---


### 176. [TrialCalibre: A Fully Automated Causal Engine for RCT Benchmarking and Observational Trial Calibration](https://arxiv.org/abs/2604.25832)

**<font color=#1a73e8>作者：</font>** Amir Habibdoust, Xing Song  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world evidence (RWE) studies that emulate target trials increasingly inform regulatory and clinical decisions, yet residual, hard-to-quantify biases still limit their credibility. The recently proposed BenchExCal framework addresses this challenge via a two-stage Benchmark, Expand, Calibrate process, which first compares an observational emulation against an existing randomized controlled trial (RCT), then uses observed divergence to calibrate a second emulation for a new indication causal effect estimation. While methodologically powerful, BenchExCal is resource intensive and difficult to scale. We introduce TrialCalibre, a conceptualized multiagent system designed to automate and scale the BenchExCal workflow. Our framework features specialized agents such as the Orchestrator, Protocol Design, Data Synthesis, Clinical Validation, and Quantitative Calibration Agents that coordi-nate the the overall process. TrialCalibre incorpo-rates agent learning (e.g., RLHF) and knowledge blackboards to support adaptive, auditable, and transparent causal effect estimation.

---


### 177. [Action-Aware Generative Sequence Modeling for Short Video Recommendation](https://arxiv.org/abs/2604.25834)

**<font color=#1a73e8>作者：</font>** Wenhao Li, Zihan Lin, Zhengxiao Guo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the rapid development of the Internet, users have increasingly higher expectations for the recommendation accuracy of online content consumption platforms. However, short videos often contain diverse segments, and users may not hold the same attitude toward all of them. Traditional binary-classification recommendation models, which treat a video as a single holistic entity, face limitations in accurately capturing such nuanced preferences. Considering that user consumption is a temporal process, this paper demonstrates that the timing of user actions can represent diverse intentions through statistical analysis and examination of action patterns. Based on this insight, we propose a novel modeling paradigm: Action-Aware Generative Sequence Network (A2Gen), which refines user actions along the temporal dimension and chains them into sequences for unified processing and prediction. First, we introduce the Context-aware Attention Module (CAM) to model action sequences enriched with item-specific contextual features. Building upon this, we develop the Hierarchical Sequence Encoder (HSE) to learn temporal action patterns from users' historical actions. Finally, through leveraging CAM, we design a module for action sequence generation: the Action-seq Autoregressive Generator (AAG). Extensive offline experiments on the Kuaishou's dataset and the Tmall public dataset demonstrate the superiority of our proposed model. Furthermore, through large-scale online A/B testing deployed on Kuaishou's platform, our model achieves significant improvements over baseline methods in multi-task prediction by leveraging sequential information. Specifically, it yields increases of 0.34% in user watch time, 8.1% in interaction rate, and 0.162% in overall user retention (LifeTime-7), leading to successful deployment across all traffic, serving over 400 million users every day.

---


### 178. [PSI-Bench: Towards Clinically Grounded and Interpretable Evaluation of Depression Patient Simulators](https://arxiv.org/abs/2604.25840)

**<font color=#1a73e8>作者：</font>** Nguyen Khoi Hoang, Shuhaib Mehri, Tse-An Hsu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Patient simulators are gaining traction in mental health training by providing scalable exposure to complex and sensitive patient interactions. Simulating depressed patients is particularly challenging, as safety constraints and high patient variability complicate simulations and underscore the need for simulators that capture diverse and realistic patient behaviors. However, existing evaluations heavily rely on LLM-judges with poorly specified prompts and do not assess behavioral diversity. We introduce PSI-Bench, an automatic evaluation framework that provides interpretable, clinically grounded diagnostics of depression patient simulator behavior across turn-, dialogue-, and population-level dimensions. Using PSI-Bench, we benchmark seven LLMs across two simulator frameworks and find that simulators produce overly long, lexically diverse responses, show reduced variability, resolve emotions too quickly, and follow a uniform negative-to-positive trajectory. We also show that the simulation framework has a larger impact on fidelity than the model scale. Results from a human study demonstrate that our benchmark is strongly aligned with expert judgments. Our work reveals key limitations of current depression patient simulators and provides an interpretable, extensible benchmark to guide future simulator design and evaluation.

---


### 179. [Semi-Markov Reinforcement Learning for City-Scale EV Ride-Hailing with Feasibility-Guaranteed Actions](https://arxiv.org/abs/2604.25848)

**<font color=#1a73e8>作者：</font>** An Nguyen, Hoang Nguyen, Phuong Le 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study city-scale control of electric-vehicle (EV) ride-hailing fleets where dispatch, repositioning, and charging decisions must respect charger and feeder limits under uncertain, spatially correlated demand and travel times. We formulate the problem as a hex-grid semi-Markov decision process (semi-MDP) with mixed actions -- discrete actions for serving, repositioning, and charging, together with continuous charging power -- and variable action durations. To guarantee physical feasibility during both training and deployment, the policy learns over high-level intentions produced by a masked, temperature-annealed actor. These intentions are projected at every decision step through a time-limited rolling mixed-integer linear program (MILP) that strictly enforces state-of-charge, port, and feeder constraints. To mitigate distributional shifts, we optimize a Soft Actor--Critic (SAC) agent against a Wasserstein-1 ambiguity set with a graph-aligned Mahalanobis ground metric that captures spatial correlations. The robust backup uses the Kantorovich--Rubinstein dual, a projected subgradient inner loop, and a primal--dual risk-budget update. Our architecture combines a two-layer Graph Convolutional Network (GCN) encoder, twin critics, and a value network that drives the adversary. Experiments on a large-scale EV fleet simulator built from NYC taxi data show that PD--RSAC achieves the highest net profit, reaching \$1.22M, compared with \$0.58M--\$0.70M for strong heuristic, single-agent RL, and multi-agent RL baselines, including Greedy, SAC, MAPPO, and MADDPG, while maintaining zero feeder-limit violations.

---


### 180. [Luminol-AIDetect: Fast Zero-shot Machine-Generated Text Detection based on Perplexity under Text Shuffling](https://arxiv.org/abs/2604.25860)

**<font color=#1a73e8>作者：</font>** Lucio La Cava, Andrea Tagarelli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine-generated text (MGT) detection requires identifying structurally invariant signals across generation models, rather than relying on model-specific fingerprints. In this respect, we hypothesize that while large language models excel at local semantic consistency, their autoregressive nature results in a specific kind of structural fragility compared to human writing. We propose Luminol-AIDetect, a novel, zero-shot statistical approach that exposes this fragility through coherence disruption. By applying a simple randomized text-shuffling procedure, we demonstrate that the resulting shift in perplexity serves as a principled, model-agnostic discriminant, as MGT displays a characteristic dispersion in perplexity-under-shuffling that differs markedly from the more stable structural variability of human-written text. Luminol-AIDetect leverages this distinction to inform its decision process, where a handful of perplexity-based scalar features are extracted from an input text and its shuffled version, then detection is performed via density estimation and ensemble-based prediction. Evaluated across 8 content domains, 11 adversarial attack types, and 18 languages, Luminol-AIDetect demonstrates state-of-the-art performance, with gains up to 17x lower FPR while being cheaper than prior methods.

---


### 181. [When Errors Can Be Beneficial: A Categorization of Imperfect Rewards for Policy Gradient](https://arxiv.org/abs/2604.25872)

**<font color=#1a73e8>作者：</font>** Shuning Shang, Hubert Strauss, Stanley Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training language models via reinforcement learning often relies on imperfect proxy rewards, since ground truth rewards that precisely define the intended behavior are rarely available. Standard metrics for assessing the quality of proxy rewards, such as ranking accuracy, treat incorrect rewards as strictly harmful. In this work, however, we highlight that not all deviations from the ground truth are equal. By theoretically analyzing which outputs attract probability during policy gradient optimization, we categorize reward errors according to their effect on the increase in ground truth reward. The analysis establishes that reward errors, though conventionally viewed as harmful, can also be benign or even beneficial by preventing the policy from stalling around outputs with mediocre ground truth reward. We then present two practical implications of our theory. First, for reinforcement learning from human feedback (RLHF), we develop reward model evaluation metrics that account for the harmfulness of reward errors. Compared to standard ranking accuracy, these metrics typically correlate better with the performance of a language model after RLHF, yet gaps remain in robustly evaluating reward models. Second, we provide insights for reward design in settings with verifiable rewards. A key theme underlying our results is that the effectiveness of a proxy reward function depends heavily on its interaction with the initial policy and learning algorithm.

---


### 182. [Prime-Field PINI: Machine-Checked Composition Theorems for Post-Quantum NTT Masking](https://arxiv.org/abs/2604.25878)

**<font color=#1a73e8>作者：</font>** Ray Iskander, Khaled Kirah  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This is Paper 6 of a series of formally-verified analyses of masked NTT hardware for post-quantum cryptography; Paper 1 [1] established structural dependency analysis of the QANARY platform, and Paper 2 [2] quantified security margins under partial NTT masking. Boolean masking composition is well-understood through NI, SNI, and PINI. Arithmetic masking over $\mathbb{Z}_q$ for prime $q$, the foundation of NTT-based post-quantum cryptography, has lacked an analogous theory. We prove, to our knowledge, the first machine-checked composition theorems for arithmetic masking over prime fields. Our key insight is the renewal argument: when a fresh random mask is applied between two pipeline stages, the intermediate wire becomes perfectly uniform regardless of Stage 1's security parameter. For two PF-PINI gadgets with parameters $k_1$ and $k_2$, the composed two-stage pipeline with fresh masking satisfies PF-PINI($k_2$), Stage 1's multiplicity is completely erased from the composed output. Without fresh masking, intermediate wires have multiplicity up to $k_1$, creating a necessary condition for differential power analysis. We formalize both theorems in Lean 4 with 18 machine-checked proofs and zero sorry stubs. We formally bridge the algebraic and hardware-faithful arithmetic models of Barrett reduction, and instantiate the theorems to formally diagnose Microsoft's Adams Bridge PQC accelerator: its absence of fresh inter-stage masking leaves Barrett output wires non-uniform under the first-order probing model, the same architectural flaw that two independent empirical analyses [3, 4] and our own prior structural analysis [1] identified. Computational evidence further suggests the 1-Bit Barrier is universal across Barrett and Montgomery reductions.

---


### 183. [No Pedestrian Left Behind: Real-Time Detection and Tracking of Vulnerable Road Users for Adaptive Traffic Signal Control](https://arxiv.org/abs/2604.25887)

**<font color=#1a73e8>作者：</font>** Anas Gamal Aly, Hala ElAarag  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current pedestrian crossing signals operate on fixed timing without adjustment to pedestrian behavior, which can leave vulnerable road users (VRUs) such as the elderly, disabled, or distracted pedestrians stranded when the light changes. We introduce No Pedestrian Left Behind (NPLB), a real-time adaptive traffic signal system that monitors VRUs in crosswalks and automatically extends signal timing when needed. We evaluated five state-of-the-art object detection models on the BGVP dataset, with YOLOv12 achieving the highest mean Average Precision at 50% (mAP@0.5) of 0.756. NPLB integrates our fine-tuned YOLOv12 with ByteTrack multi-object tracking and an adaptive controller that extends pedestrian phases when remaining time falls below a critical threshold. Through 10,000 Monte Carlo simulations, we demonstrate that NPLB improves VRU safety by 71.4%, reducing stranding rates from 9.10% to 2.60%, while requiring signal extensions in only 12.1% of crossing cycles.

---


### 184. [Robust Deepfake Detection: Mitigating Spatial Attention Drift via Calibrated Complementary Ensembles](https://arxiv.org/abs/2604.25889)

**<font color=#1a73e8>作者：</font>** Minh-Khoa Le-Phan, Minh-Hoang Le, Trong-Le Do 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current deepfake detection models achieve state-of-the-art performance on pristine academic datasets but suffer severe spatial attention drift under real-world compound degradations, such as blurring and severe lossy compression. To address this vulnerability, we propose a foundation-driven forensic framework that integrates an extreme compound degradation engine with a structurally constrained, multi-stream architecture. During training, our degradation pipeline systematically destroys high-frequency artifacts, optimizing the DINOv2-Giant backbone to extract invariant geometric and semantic priors. We then process images through three specialized pathways: a Global Texture stream, a Localized Facial stream, and a Hybrid Semantic Fusion stream incorporating CLIP. Through analyzing spatial attribution via Score-CAM and feature stability using Cosine Similarity, we quantitatively demonstrate that these streams extract non-redundant, complementary feature representations and stabilize attention entropy. By aggregating these predictions via a calibrated, discretized voting mechanism, our ensemble successfully suppresses background attention drift while acting as a robust geometric anchor. Our approach yields highly stable zero-shot generalization, achieving Fourth Place in the NTIRE 2026 Robust Deepfake Detection Challenge at CVPR. Code is available at this https URL.

---


### 185. [TSN-Affinity: Similarity-Driven Parameter Reuse for Continual Offline Reinforcement Learning](https://arxiv.org/abs/2604.25898)

**<font color=#1a73e8>作者：</font>** Dominik Żurek, Kamil Faber, Marcin Pietron 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual offline reinforcement learning (CORL) aims to learn a sequence of tasks from datasets collected over time while preserving performance on previously learned tasks. This setting corresponds to domains where new tasks arise over time, but adapting the model in live environment interactions is expensive, risky, or impossible. However, CORL inherits the dual difficulty of offline reinforcement learning and adapting while preventing catastrophic forgetting. Replay-based continual learning approaches remain a strong baseline but incur memory overhead and suffer from a distribution mismatch between replayed samples and newly learned policies. At the same time, architectural continual learning methods have shown strong potential in supervised learning but remain underexplored in CORL. In this work, we propose TSN-Affinity, a novel CORL method based on TinySubNetworks and Decision Transformer. The method enables task-specific parameterization and controlled knowledge sharing through a RL-aware reuse strategy that routes tasks according to action compatibility and latent similarity. We evaluate the approach on benchmarks based on Atari games and simulations of manipulation tasks with the Franka Emika Panda robotic arm, covering both discrete and continuous control. Results show strong retention from sparse SubNetworks, with routing further improving multi-task performance. Our findings suggest that similarity-guided architectural reuse is a strong and viable alternative to replay-based strategies in a CORL setting. Our code is available at: this https URL.

---


### 186. [Toward a Functional Geometric Algebra for Natural Language Semantics](https://arxiv.org/abs/2604.25902)

**<font color=#1a73e8>作者：</font>** James Pustejovsky  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Distributional and neural approaches to natural language semantics have been built almost exclusively on conventional linear algebra: vectors, matrices, tensors, and the operations that accompany them. These methods have achieved remarkable empirical success, yet they face persistent structural limitations in compositional semantics, type sensitivity, and interpretability. I argue in this paper that geometric algebra (GA) -- specifically, Clifford algebras -- provides a mathematically superior foundation for semantic representation, and that a Functional Geometric Algebra (FGA) framework extends GA toward a typed, compositional semantics capable of supporting inference, transformation, and interpretability while retaining full compatibility with distributional learning and modern neural architectures. I develop the formal foundations, identify three core capabilities that GA provides and linear algebra does not, present a detailed worked example illustrating operator-level semantic contrasts, and show how GA-based operations already implicit in current transformer architectures can be made explicit and extended. The central claim is not merely increased dimensionality but increased structural organization: GA expands an $n$-dimensional embedding space into a $2^n$ multivector algebra where base semantic concepts and their higher-order interactions are represented within a single, principled algebraic framework.

---


### 187. [Teacher Forcing as Generalized Bayes: Optimization Geometry Mismatch in Switching Surrogates for Chaotic Dynamics](https://arxiv.org/abs/2604.25904)

**<font color=#1a73e8>作者：</font>** Andre Herz, Daniel Durstewitz, Georgia Koppe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identity teacher forcing (ITF) enables stable training of deterministic recurrent surrogates for chaotic dynamical systems and has been highly effective for dynamical systems reconstruction (DSR) with recurrent neural networks (RNNs), including interpretable almost-linear RNNs (AL-RNNs). However, as an intervention-based prediction loss (and thus a generalized Bayes update), teacher forcing need not match the free-running model's marginal likelihood geometry. We compare the objective-induced curvatures of ITF and marginal likelihood in a probabilistic switching augmentation of AL-RNNs, estimating ambiguity-aware observed information via Louis' identity. In the switching setting studied here, conditioning on a single forced regime path (as ITF does) inflates curvature, while marginal likelihood curvature is reduced by a missing-information correction when multiple switching explanations remain plausible. In Lorenz-63 experiments, windowed evidence fine-tuning improves held-out evidence but can degrade dynamical quantities of interest (QoIs) relative to ITF-pretrained models.

---


### 188. [A paradox of AI fluency](https://arxiv.org/abs/2604.25905)

**<font color=#1a73e8>作者：</font>** Christopher Potts, Moritz Sudhof  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How much does a user's skill with AI shape what AI actually delivers for them? This question is critical for users, AI product builders, and society at large, but it remains underexplored. Using a richly annotated sample of 27K transcripts from WildChat-4.8M, we show that fluent users take on more complex tasks than novices and adopt a fundamentally different interactional mode: they iterate collaboratively with the AI, refining goals and critically assessing outputs, whereas novices take a passive stance. These differences lead to a paradox of AI fluency: fluent users experience more failures than novices -- but their failures tend to be visible (a direct consequence of their engagement), they are more likely to lead to partial recovery, and they occur alongside greater success on complex tasks. Novices, by contrast, more often experience invisible failures: conversations that appear to end successfully but in fact miss the mark. Taken together, these results reframe what success with AI depends on. Individuals should adopt a stance of active engagement rather than passive acceptance. AI product builders should recognize that they are designing not just model behavior but user behavior; encouraging deep engagement, rather than friction-free experiences, will lead to more success overall. Our code and data are available at this https URL

---


### 189. [DV-World: Benchmarking Data Visualization Agents in Real-World Scenarios](https://arxiv.org/abs/2604.25914)

**<font color=#1a73e8>作者：</font>** Jinxiang Meng, Shaoping Huang, Fangyu Lei 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-world data visualization (DV) requires native environmental grounding, cross-platform evolution, and proactive intent alignment. Yet, existing benchmarks often suffer from code-sandbox confinement, single-language creation-only tasks, and assumption of perfect intent. To bridge these gaps, we introduce DV-World, a benchmark of 260 tasks designed to evaluate DV agents across real-world professional lifecycles. DV-World spans three domains: DV-Sheet for native spreadsheet manipulation including chart and dashboard creation as well as diagnostic repair; DV-Evolution for adapting and restructuring reference visual artifacts to fit new data across diverse programming paradigms and DV-Interact for proactive intent alignment with a user simulator that mimics real-world ambiguous requirements. Our hybrid evaluation framework integrates Table-value Alignment for numerical precision and MLLM-as-a-Judge with rubrics for semantic-visual assessment. Experiments reveal that state-of-the-art models achieve less than 50% overall performance, exposing critical deficits in handling the complex challenges of real-world data visualization. DV-World provides a realistic testbed to steer development toward the versatile expertise required in enterprise workflows. Our data and code are available at \href{this https URL}{this project page}.

---


### 190. [Recursive Multi-Agent Systems](https://arxiv.org/abs/2604.25917)

**<font color=#1a73e8>作者：</font>** Xiyuan Yang, Jiaru Zou, Rui Pan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive or looped language models have recently emerged as a new scaling axis by iteratively refining the same model computation over latent states to deepen reasoning. We extend such scaling principle from a single model to multi-agent systems, and ask: Can agent collaboration itself be scaled through recursion? To this end, we introduce RecursiveMAS, a recursive multi-agent framework that casts the entire system as a unified latent-space recursive computation. RecursiveMAS connects heterogeneous agents as a collaboration loop through the lightweight RecursiveLink module, enabling in-distribution latent thoughts generation and cross-agent latent state transfer. To optimize our framework, we develop an inner-outer loop learning algorithm for iterative whole-system co-optimization through shared gradient-based credit assignment across recursion rounds. Theoretical analyses of runtime complexity and learning dynamics establish that RecursiveMAS is more efficient than standard text-based MAS and maintains stable gradients during recursive training. Empirically, we instantiate RecursiveMAS under 4 representative agent collaboration patterns and evaluate across 9 benchmarks spanning mathematics, science, medicine, search, and code generation. In comparison with advanced single/multi-agent and recursive computation baselines, RecursiveMAS consistently delivers an average accuracy improvement of 8.3%, together with 1.2$\times$-2.4$\times$ end-to-end inference speedup, and 34.6%-75.6% token usage reduction. Code and Data are provided in this https URL.

---


> [!TIP]
> 当前位于：**151-190**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-190**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
