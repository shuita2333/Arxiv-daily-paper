# 🧠 大模型相关研究 | 2026年05月03日

> 本类共 **123** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-123](./part-03.md)

---

### 51. [Low Rank Adaptation for Adversarial Perturbation](https://arxiv.org/abs/2604.27487)

**<font color=#1a73e8>作者：</font>** Han Liu, Shanghao Shi, Yevgeniy Vorobeychik 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA), which leverages the insight that model updates typically reside in a low-dimensional space, has significantly improved the training efficiency of Large Language Models (LLMs) by updating neural network layers using low-rank matrices. Since the generation of adversarial examples is an optimization process analogous to model training, this naturally raises the question: Do adversarial perturbations exhibit a similar low-rank structure?
In this paper, we provide both theoretical analysis and extensive empirical investigation across various attack methods, model architectures, and datasets to show that adversarial perturbations indeed possess an inherently low-rank structure. This insight opens up new opportunities for improving both adversarial attacks and defenses. We mainly focus on leveraging this low-rank property to improve the efficiency and effectiveness of black-box adversarial attacks, which often suffer from excessive query requirements. Our method follows a two-step approach. First, we use a reference model and auxiliary data to guide the projection of gradients into a low-dimensional subspace. Next, we confine the perturbation search in black-box attacks to this low-rank subspace, significantly improving the efficiency and effectiveness of the adversarial attacks.
We evaluated our approach across a range of attack methods, benchmark models, datasets, and threat models. The results demonstrate substantial and consistent improvements in the performance of our low-rank adversarial attacks compared to conventional methods.

---


### 52. [Skills-Coach: A Self-Evolving Skill Optimizer via Training-Free GRPO](https://arxiv.org/abs/2604.27488)

**<font color=#1a73e8>作者：</font>** Yu Tian, Jiawei Chen, Lifan Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Skills-Coach, a novel automated framework designed to significantly enhance the self-evolution of skills within Large Language Model (LLM)-based agents. Addressing the current fragmentation of the skill ecosystem, Skills-Coach explores the boundaries of skill capabilities, thereby facilitating the comprehensive competency coverage essential for intelligent applications. The framework comprises four core modules: a Diverse Task Generation Module that systematically creates a comprehensive test suite for various skills; a Lightweight Optimization Module dedicated to optimizing skill prompts and their corresponding code; a Comparative Execution Module facilitating the execution and evaluation of both original and optimized skills; and a Traceable Evaluation Module, which rigorously evaluates performance against specified criteria. Skills-Coach offers flexible execution options through its virtual and real modes. To validate its efficacy, we introduce Skill-X, a comprehensive benchmark dataset consisting of 48 diverse skills. Experimental results demonstrate that Skills-Coach achieves significant performance improvements in skill capability across a wide range of categories, highlighting its potential to advance the development of more robust and adaptable LLM-based agents.

---


### 53. [Uni-HOI:A Unified framework for Learning the Joint distribution of Text and Human-Object Interaction](https://arxiv.org/abs/2604.27491)

**<font color=#1a73e8>作者：</font>** Mengfei Zhang, Jinlu Zhang, Zhigang Tu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modeling 4D human-object interaction (HOI) is a compelling challenge in computer vision and an essential technology powering virtual and mixed-reality applications. While existing works have achieved promising results on specific HOI tasks-such as text-conditioned HOI generation and human motion generation from object motion, they typically rely on task-specific architectures and lack a unified framework capable of handling diverse conditional inputs. Building on this, we propose Uni-HOI, a unified framework that learns the joint distribution among text, human motion, and object motion. By leveraging large language models (LLMs) and two motion-specific vector quantized variational autoencoders (VQ-VAEs), we convert heterogeneous motion data into token sequences compatible with LLM inputs, enabling seamless integration and joint modeling of all three modalities. We introduce a two-stage training strategy: the first stage performs multi-task learning on a large-scale HOI dataset to capture the underlying correlations among the three modalities, while the second stage fine-tunes the model on specific tasks to further enhance performance. Extensive experiments demonstrate that Uni-HOI achieves remarkable performances on multiple HOI-related tasks including text-driven HOI generation, object motion-driven human motion generation (optionally with text) and human motion-driven object motion prediction within a unified framework.

---


### 54. [Debiasing Reward Models via Causally Motivated Inference-Time Intervention](https://arxiv.org/abs/2604.27495)

**<font color=#1a73e8>作者：</font>** Kazutoshi Shinoda, Kosuke Nishida, Kyosuke Nishida  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reward models (RMs) play a central role in aligning large language models (LLMs) with human preferences. However, RMs are often sensitive to spurious features such as response length. Existing inference-time approaches for mitigating these biases typically focus exclusively on response length, resulting in performance trade-offs. In this paper, we propose causally motivated intervention for mitigating multiple types of biases in RMs at inference time. Our method first identifies neurons whose activations are strongly correlated with predefined bias attributes, and applies neuron-level intervention that suppresses these signals. We evaluate our method on RM benchmarks and observe reductions in sensitivity to spurious features across diverse bias types, without inducing performance trade-offs. Moreover, when used for preference annotation, small RMs (2B and 7B) with our method, which edits less than 2% of all the neurons in RMs, enable LLMs to improve alignment, achieving performance comparable to that of a state-of-the-art 70B RM on AlpacaEval and MT-Bench. Further analysis reveals that bias signals are primarily encoded by neurons in early layers, shedding light on the internal mechanisms of bias exploitation in RMs.

---


### 55. [Leveraging Verifier-Based Reinforcement Learning in Image Editing](https://arxiv.org/abs/2604.27505)

**<font color=#1a73e8>作者：</font>** Hanzhong Guo, Jie Wu, Jie Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Reinforcement Learning from Human Feedback (RLHF) has become a pivotal paradigm for text-to-image generation, its application to image editing remains largely unexplored. A key bottleneck is the lack of a robust general reward model for all editing tasks. Existing edit reward models usually give overall scores without detailed checks, ignoring different instruction requirements and causing biased rewards. To address this, we argue that the key is to move from a simple scorer to a reasoning verifier. We introduce Edit-R1, a framework that builds a chain-of-thought (CoT) verifier-based reasoning reward model (RRM) and then leverages it for downstream image editing. The Edit-RRM breaks instructions into distinct principles, evaluates the edited image against each principle, and aggregates these checks into an interpretable, fine-grained reward. To build such an RRM, we first apply supervised fine-tuning (SFT) as a ``cold-start'' to generate CoT reward trajectories. Then, we introduce Group Contrastive Preference Optimization (GCPO), a reinforcement learning algorithm that leverages human pairwise preference data to reinforce our pointwise RRM. After building the RRM, we use GRPO to train editing models with this non-differentiable yet powerful reward model. Extensive experiments demonstrate that our Edit-RRM surpasses powerful VLMs such as Seed-1.5-VL and Seed-1.6-VL as an editing-specific reward model, and we observe a clear scaling trend, with performance consistently improving from 3B to 7B parameters. Moreover, Edit-R1 delivers gains to editing models like FLUX.1-kontext, highlighting its effectiveness in enhancing image editing.

---


### 56. [FMCL: Class-Aware Client Clustering with Foundation Model Representations for Heterogeneous Federated Learning](https://arxiv.org/abs/2604.27510)

**<font color=#1a73e8>作者：</font>** Mahad Ali, Laura J. Brattain  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative model training across distributed clients without sharing raw data, yet its performance deteriorates under statistical heterogeneity. Clustered Federated Learning addresses this challenge by grouping similar clients and training separate models per cluster. However, existing clustering strategies often rely on raw data statistics, model parameters, or heuristic similarity measures that fail to capture class-level semantic structure across heterogeneous domains and frequently require iterative coordination. We propose FMCL, a one-shot, class-aware client clustering framework that leverages foundation model representations to construct semantic client signatures. Using a frozen foundation model, FMCL computes class-level embedding prototypes for each client and measures similarity via cosine distance between their class-aware representations. Clustering is performed once prior to training, introducing no additional communication during federated optimization and remaining agnostic to the downstream model architecture. Extensive experiments across heterogeneous benchmarks demonstrate that FMCL improves federated performance and yields more stable clustering behavior compared to existing clustering-based methods under non-identically distributed data partitioning.

---


### 57. [Qualitative Evaluation of Language Model Rescoring in Automatic Speech Recognition](https://arxiv.org/abs/2604.27533)

**<font color=#1a73e8>作者：</font>** Thibault Bañeras-Roux, Mickaël Rouvier, Jane Wottawa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating automatic speech recognition (ASR) systems is a classical but difficult and still open problem, which often boils down to focusing only on the word error rate (WER). However, this metric suffers from many limitations and does not allow an in-depth analysis of automatic transcription errors. In this paper, we propose to study and understand the impact of rescoring using language models in ASR systems by means of several metrics often used in other natural language processing (NLP) tasks in addition to the WER. In particular, we introduce two measures related to morpho-syntactic and semantic aspects of transcribed words: 1) the POSER (Part-of-speech Error Rate), which should highlight the grammatical aspects, and 2) the EmbER (Embedding Error Rate), a measurement that modifies the WER by providing a weighting according to the semantic distance of the wrongly transcribed words. These metrics illustrate the linguistic contributions of the language models that are applied during a posterior rescoring step on transcription hypotheses.

---


### 58. [Belief-Guided Inference Control for Large Language Model Services via Verifiable Observations](https://arxiv.org/abs/2604.27536)

**<font color=#1a73e8>作者：</font>** Wenhao Yuan, Chenchen Lin, Jian Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In black-box large language model (LLM) services, response reliability is often only partially observable at decision time, while stronger inference pathways incur substantial computational cost, inducing a budgeted sequential decision problem: for each request, the system should decide whether the default low-cost response is sufficiently reliable or whether additional computation should be allocated to improve response quality. In this paper, we propose \textbf{Ver}ifiable \textbf{O}bservations for Risk-aware \textbf{I}nference \textbf{C}ontrol (\textsc{Veroic}), a framework for adaptive inference control in black-box LLM settings, which formulates request-time control as a \textit{partially observable Markov decision process} to capture partial observability and sequential budget coupling. It constructs a lightweight verifiable observation channel from the input-output pair by aggregating heterogeneous quality signals into a belief state over latent response reliability, which is then used by a budget-aware policy to decide whether to return the default output or trigger a higher-cost inference pathway. Experiments on diverse tasks show that \textsc{Veroic} achieves improved quality-cost trade-offs, stronger risk estimation and calibration, and more robust long-horizon inference control than competitive baselines.

---


### 59. [In-Context Examples Suppress Scientific Knowledge Recall in LLMs](https://arxiv.org/abs/2604.27540)

**<font color=#1a73e8>作者：</font>** Chaemin Jang, Woojin Park, Hyeok Yun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific reasoning rarely stops at what is directly observable; it often requires uncovering hidden structure from data. From estimating reaction constants in chemistry to inferring demand elasticities in economics, this latent structure recovery is what distinguishes scientific reasoning from curve fitting. Large language models (LLMs) can often recall and apply relevant scientific formulas, but we show that this ability is surprisingly easy to suppress. We show that adding in-context examples makes models rely less on pretrained domain knowledge, even when those examples are generated by the very same formula. Rather than reinforcing knowledge-driven derivation, examples shift computation toward empirical pattern fitting. We document this knowledge displacement on 60 latent structure recovery tasks across five scientific domains, 6,000 trials, and four models. This displacement is consistent across domains, but its accuracy consequences depend on how the displaced strategy compares to the one that replaces it: the same shift can lower accuracy, leave it unchanged, or appear to improve it. In all cases, however, the model shifts away from knowledge-driven reasoning. For practitioners deploying LLMs on scientific tasks, the message is cautionary: in-context examples may displace, rather than reinforce, the knowledge they are intended to support.

---


### 60. [Diagnosing Capability Gaps in Fine-Tuning Data](https://arxiv.org/abs/2604.27547)

**<font color=#1a73e8>作者：</font>** Saeid Asgari Taghanaki, Rakshanda Agarwal, Bruce Sun 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models (LLMs) for domain-specific tasks requires training datasets that comprehensively cover the target capabilities a practitioner needs. Yet identifying which capabilities a dataset fails to support, and doing so before an expensive fine-tuning run, remains a largely unsolved problem. We introduce GoalCover, a framework that helps practitioners systematically detect capability gaps in fine-tuning datasets through interactive goal decomposition and automated coverage assessment. GoalCover guides a practitioner through structured decomposition of a high-level goal into atomic, independently evaluable subgoals; assigns each training sample an LLM-based alignment score against every subgoal; and surfaces missing capabilities through automated analysis of low-scoring sample explanations. We validate the framework along two complementary axes. First, through controlled corruption experiments across three domains (medical QA, legal summarization, code generation), we show that GoalCover reliably distinguishes targeted from non-targeted capability impacts: target subgoals degrade by 25.6% on average versus 2.1% for non-target subgoals (Cohen's d=1.24). Second, we demonstrate downstream utility on a financial-summarization Reinforcement Fine-Tuning (RFT) task with Qwen-3-14B: training on GoalCover-filtered data improves the LLM-judge reward from 3.77 to 4.12 (out of 5) over the unfiltered baseline, and combining filtered data with goal-conditioned synthetic samples yields the strongest result (4.20). The two results together show that GoalCover works as a practical pre-fine-tuning diagnostic: it detects capability gaps and produces concrete signal for closing them.

---


### 61. [APPSI-139: A Parallel Corpus of English Application Privacy Policy Summarization and Interpretation](https://arxiv.org/abs/2604.27550)

**<font color=#1a73e8>作者：</font>** Pengyun Zhu, Qiheng Sun, Long Wen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Privacy policies are essential for users to understand how service providers handle their personal data. However, these documents are often long and complex, as well as filled with technobabble and legalese, causing users to unknowingly accept terms that may even contradict the law. While summarizing and interpreting these privacy policies is crucial, there is a lack of high-quality English parallel corpus optimized for legal clarity and readability. To address this issue, we introduce APPSI-139, a high-quality English privacy policy corpus meticulously annotated by domain experts, specifically designed for summarization and interpretation tasks. The corpus includes 139 English privacy policies, 15,692 rewritten parallel corpora, and 36,351 fine-grained annotation labels across 11 data practice categories. Concurrently, we propose TCSI-pp-V2, a hybrid privacy policy summarization and interpretation framework that employs an alternating training strategy and coordinates multiple expert modules to effectively balance computational efficiency and accuracy. Experimental results show that the hybrid summarization system built on APPSI-139 corpus and the TCSI-pp-V2 framework outperform large language models, such as GPT-4o and LLaMA-3-70B, in terms of readability and reliability. The source code and dataset are available at this https URL.

---


### 62. [Revealing the Impact of Visual Text Style on Attribute-based Descriptions Produced by Large Visual Language Models](https://arxiv.org/abs/2604.27553)

**<font color=#1a73e8>作者：</font>** Xiaomeng Wang, Martha Larson, Zhengyu Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When the visual style of text is considered, a wide variety can be observed in font, color, and size. However, when a word is read, its meaning is independent of the style in which it has been written or rendered. In this paper, we investigate whether, and how, the style in which a word is visualized in an image impacts the description that a Large Visual Language Model (LVLM) provides for the concept to which that word refers. Specifically, we investigate how functional text styles (readability-oriented, e.g., black sans-serif) versus decorative styles (display-oriented, e.g., colored cursive/script) affect LVLMs' descriptions of a concept in terms of the attributes of that concept. Our experiments study the situation in which the LVLM is able to correctly identify the concept referred to by a visual text, i.e., by a word or words rendered as an image, and in which the visual text style should not influence the attribute-based description that the LVLM produces. Our experimental results reveal that even when the concept is correctly identified, text style influences the model's attribute-based descriptions of the concept. Our findings demonstrate non-trivial style leakage from text style into semantic inference and motivate style-aware evaluation and mitigation for LVLM-based multimedia systems.

---


### 63. [SpatialGrammar: A Domain-Specific Language for LLM-Based 3D Indoor Scene Generation](https://arxiv.org/abs/2604.27555)

**<font color=#1a73e8>作者：</font>** Song Tang, Kaiyong Zhao, Yuliang Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatically generating interactive 3D indoor scenes from natural language is crucial for virtual reality, gaming, and embodied AI. However, existing LLM-based approaches often suffer from spatial errors and collisions, in part because common scene representations-raw coordinates or verbose code-are difficult for models to reason about 3D spatial relationships and physical constraints. We propose SpatialGrammar, a domain-specific language that represents gravity-aligned indoor layouts as BEV grid placements with deterministic compilation to valid 3D geometry, enabling verifiable constraint checking. Building on this representation, we develop (1) SG-Agent, a closed-loop system that uses compiler feedback to iteratively refine scenes and enforce collision constraints, and (2) SG-Mini, a 104M-parameter model trained entirely on compiler-validated synthetic data. Across 159 test scenes spanning five scenarios of different complexity, SG-Agent improves spatial fidelity and physical plausibility over prior methods, while SG-Mini performs competitively against larger LLM-based baselines on single-shot generation scenarios.

---


### 64. [RIHA: Report-Image Hierarchical Alignment for Radiology Report Generation](https://arxiv.org/abs/2604.27559)

**<font color=#1a73e8>作者：</font>** Yucheng Chen, Yang Yu, Yufei Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiology report generation (RRG) has emerged as a promising approach to alleviate radiologists' workload and reduce human errors by automatically generating diagnostic reports from medical images. A key challenge in RRG is achieving fine-grained alignment between complex visual features and the hierarchical structure of long-form radiology reports. Although recent methods have improved image-text representation learning, they often treat reports as flat sequences, overlooking their structured sections and semantic hierarchies. This simplification hinders precise cross-modal alignment and weakens RRG accuracy. To address this challenge, we propose RIHA (Report-Image Hierarchical Alignment Transformer), a novel end-to-end framework that performs multi-level alignment between radiological images and their corresponding reports across paragraph, sentence, and word levels. This hierarchical alignment enables more precise cross-modal mapping, essential for capturing the nuanced semantics embedded in clinical narratives. Specifically, RIHA introduces a Visual Feature Pyramid (VFP) to extract multi-scale visual features and a Text Feature Pyramid (TFP) to represent multi-granularity textual structures. These components are integrated through a Cross-modal Hierarchical Alignment (CHA) module, leveraging optimal transport to effectively align visual and textual features across various levels. Furthermore, we incorporate Relative Positional Encoding (RPE) into the decoder to model spatial and semantic relationships among tokens, enhancing the token-level alignment between visual features and generated text. Extensive experiments on two benchmark chest X-ray datasets, IU-Xray and MIMIC-CXR, demonstrate that RIHA outperforms existing state-of-the-art models in both natural language generation and clinical efficacy metrics.

---


### 65. [Decoding Scientific Experimental Images: The SPUR Benchmark for Perception, Understanding, and Reasoning](https://arxiv.org/abs/2604.27604)

**<font color=#1a73e8>作者：</font>** Junpeng Ding, Zichen Tang, Haihong E 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce SPUR, a comprehensive benchmark for scientific experimental image perception, understanding, and reasoning, comprising 4,264 question-answering (QA) pairs derived from 1,084 expert-curated images. SPUR features three key innovations: (1) Panel-Level Fine-Grained Perception: evaluating the visual perception of multimodal large language models (MLLMs) across three dimensions (numerical, morphological, and information localization) on six fine-grained panel types; (2) Cross-Panel Relation Understanding: utilizing complex images with an average of 14.3 panels per sample to evaluate MLLMs' ability to decipher intricate cross-panel relations; (3) Expert-Level Reasoning: assessment of qualitative and quantitative reasoning across five experimental paradigms to determine if models can infer conclusions from evidence as human experts do. Comprehensive evaluation of 20 MLLMs and four multimodal Chain-of-Thought (MCoT) methods reveals that current models fall significantly short of the expert-level requirements for scientific image interpretation, underscoring a critical bottleneck in AI for Science (AI4S) research.

---


### 66. [RoadMapper: A Multi-Agent System for Roadmap Generation of Solving Complex Research Problems](https://arxiv.org/abs/2604.27616)

**<font color=#1a73e8>作者：</font>** Jiacheng Liu, Zichen Tang, Zhongjun Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> People commonly leverage structured content to accelerate knowledge acquisition and research problem solving. Among these, roadmaps guide researchers through hierarchical subtasks to solve complex research problems step by step. Despite progress in structured content generation, the roadmap generation task has remained unexplored. To bridge this gap, we introduce RoadMap, a novel benchmark designed to evaluate the ability of large language models (LLMs) to construct high-quality roadmaps for solving complex research problems. Based on this, we identify three limitations of LLMs: (1) lack of professional knowledge, (2) unreasonable task decomposition, and (3) disordered logical relationships. To address these challenges, we propose RoadMapper, an LLM-based multi-agent system that decomposes the research roadmap generation task into three key stages (i.e., initial generation, knowledge augmentation, and iterative "critique-revise-evaluate"). Extensive experiments demonstrate that RoadMapper can improve LLMs' ability for roadmap generation, while enhancing average performance by more than 8% and saving 84% of the time required by human experts, highlighting its effectiveness and application potential.

---


### 67. [Math Education Digital Shadows for facilitating learning with LLMs: Math performance, anxiety and confidence in simulated students and AIs](https://arxiv.org/abs/2604.27618)

**<font color=#1a73e8>作者：</font>** Naomi Esposito, Anthony Tricarico, Luisa Porzio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To enhance LLMs' impact on math education, we need data on their mathematical prowess and biases across prompts. To fill this gap, we introduce MEDS (Math Education Digital Shadows) as a dataset mapping how large language models reason about and report mathematics across human- and AI-like conditions. MEDS involves 28,000 personas from 14 LLMs (from families like Mistral, Qwen, DeepSeek, Granite, Phi and Grok) shadowing either humans or AI assistants. Each record/shadow includes a set of prompts along with psychological/sociodemographic persona metadata and four types of math tasks: (i) open math interview, (ii) three psychometric tests about math perceptions with explanations, (iii) cognitive networks capturing math attitudes, and (iv) 18 high-school math test questions together with their reasoning and confidence scores. MEDS differs from traditional score-only math benchmarks because it integrates concepts of self-efficacy, math anxiety, and cognitive network science besides math proficiency scores. Data validation shows that the sampled LLMs exhibit schema integrity and consistent personas, together with family-specific peculiarities like human-like negative math attitudes, logical fallacies, and math overconfidence. MEDS will benefit learning analytics experts, cognitive scientists, and developers of safer AI tutors in mathematics.

---


### 68. [Mapping how LLMs debate societal issues when shadowing human personality traits, sociodemographics and social media behavior](https://arxiv.org/abs/2604.27624)

**<font color=#1a73e8>作者：</font>** Ali Aghazadeh Ardebili, Massimo Stella  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can strongly shape social discourse, yet datasets investigating how LLM outputs vary across controlled social and contextual prompting remain sparse. Cognitive Digital Shadows (CDS) is a 190,000-record synthetic corpus supporting analyses of LLM-generated discourse. Each CDS record is generated by one of 19 LLMs, prompted to shadow either a human persona or an AI-assistant role. CDS contains LLM responses on 4 controversial societal topics: vaccines/healthcare, social media disinformation, the gender gap in science, and STEM stereotypes. Persona-conditioned records encode 17 sociodemographic and psychological attributes, providing data linking LLMs' prompts, language, stances and reasoning. Texts are validated for topic anchoring and can support emotional analyses via interpretable NLP (e.g. textual forma mentis networks). CDS is enriched by a pooling platform with user-friendly dashboards, enabling easy, interactive group-level comparisons of emotional and semantic framing across personas, topics and models. The CDS prompting framework supports future audits of LLMs' bias, social sensitivity and alignment.

---


### 69. [WaferSAGE: Large Language Model-Powered Wafer Defect Analysis via Synthetic Data Generation and Rubric-Guided Reinforcement Learning](https://arxiv.org/abs/2604.27629)

**<font color=#1a73e8>作者：</font>** Ke Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present WaferSAGE, a framework for wafer defect visual question answering using small vision-language models. To address data scarcity in semiconductor manufacturing, we propose a three-stage synthesis pipeline incorporating structured rubric generation for precise evaluation. Starting from limited labeled wafer maps, we employ clustering-based cleaning to filter label noise, then generate comprehensive defect descriptions using vision-language models, which are converted into structured evaluation rubrics criteria. These rubrics guide the synthesis of VQA pairs, ensuring coverage across defect type identification, spatial distribution, morphology, and root cause analysis.
Our dual assessment framework aligns rule-based metrics with LLM-Judge scores via Bayesian optimization, enabling reliable automated evaluation. Through curriculum-based reinforcement learning with Group Sequence Policy Optimization (GSPO) and rubric-aligned rewards, our 4B-parameter Qwen3-VL model achieves a 6.493 LLM-Judge score, closely approaching Gemini-3-Flash (7.149) while enabling complete on-premise deployment. We demonstrate that small models with domain-specific training can surpass proprietary large models in specialized industrial visual understanding, offering a viable path for privacy-preserving, cost-effective deployment in semiconductor manufacturing.

---


### 70. [Political Bias Audits of LLMs Capture Sycophancy to the Inferred Auditor](https://arxiv.org/abs/2604.27633)

**<font color=#1a73e8>作者：</font>** Petter Törnberg, Michelle Schimmel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are commonly evaluated for political bias based on their responses to fixed questionnaires, which typically place frontier models on the political left. A parallel literature shows that LLMs are sycophantic: they adapt their answers to the views, identities, and expectations of the user. We show that these findings are linked: standard political-bias audits partly capture sycophantic accommodation to the inferred auditor. We employ a factorial experiment across three major audit instruments--the Political Compass Test, the Pew Political Typology, and 1,540 partisan-benchmarked Pew American Trends Panel items--administered to six frontier LLMs while varying only the asker's stated identity (N = 30,990 responses). At baseline, all six models lean left. When the asker identifies as a conservative Republican, responses shift sharply: the share of items closer to Democrats falls by 28-62 percentage points, and all six models move right of center. A mirror-image progressive-Democrat cue produces little change; rightward accommodation is 8.0$\times$ larger than leftward. When asked who the default asker is, models identify an auditor, researcher, or academic; when asked what answer that asker expects, they select the Democrat-coded option 75% of the time, nearly the rate under an explicit progressive cue. These patterns are inconsistent with a purely fixed model ideology and indicate that single-prompt audits capture an interaction between model and inferred interlocutor. Political bias in LLMs is therefore not a fixed point on an ideological scale but a response profile that must be mapped across realistic interlocutors.

---


### 71. [From Context to Skills: Can Language Models Learn from Context Skillfully?](https://arxiv.org/abs/2604.27660)

**<font color=#1a73e8>作者：</font>** Shuzheng Si, Haozhe Zhao, Yu Lei 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many real-world tasks require language models (LMs) to reason over complex contexts that exceed their parametric knowledge. This calls for context learning, where LMs directly learn relevant knowledge from the given context. An intuitive solution is inference-time skill augmentation: extracting the rules and procedures from context into natural-language skills. However, constructing such skills for context learning scenarios faces two challenges: the prohibitive cost of manual skill annotation for long, technically dense contexts, and the lack of external feedback for automated skill construction, since there is no automatic signal to tell whether a proposed skill is helpful. In this paper, we propose Ctx2Skill, a self-evolving framework that autonomously discovers, refines, and selects context-specific skills without human supervision or external feedback. At its core, a multi-agent self-play loop has a Challenger that generates probing tasks and rubrics, a Reasoner that attempts to solve them guided by an evolving skill set, and a neutral Judge that provides binary feedback. Crucially, both the Challenger and the Reasoner evolve through accumulated skills: dedicated Proposer and Generator agents analyze failure cases and synthesize them into targeted skill updates for both sides, enabling automated skill discovery and refinement. To prevent adversarial collapse caused by increasingly extreme task generation and over-specialized skill accumulation, we further introduce a Cross-time Replay mechanism that identifies the skill set achieving the best balance across representative cases for the Reasoner side, ensuring robust and generalizable skill evolution. The resulting skills can be plugged into any language model to obtain better context learning capability. Evaluated on four context learning tasks from CL-bench, Ctx2Skill consistently improves solving rates across backbone models.

---


### 72. [Language Ideologies in a Multilingual Society: An LLM-based Analysis of Luxembourgish News Comments](https://arxiv.org/abs/2604.27661)

**<font color=#1a73e8>作者：</font>** Emilia Milano, Alistair Plum, Yves Scherrer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting language ideologies is a valuable yet complex task for understanding how identities are constructed through discourse. In Luxembourg's multicultural and multilingual society, language ideologies reflect more than simple preferences: they carry deep cultural and social meanings, shaping identities and social belonging. Following recent developments in applying Natural Language Processing tools to linguistics and social science, this paper explores the potential of large language models to assist in the detection of language ideologies. We manually annotate a corpus of user comments in Luxembourgish with predefined ideological categories and then evaluate the performance of large language models under varying prompt conditions to assess their ability to replicate these human annotations. Since Luxembourgish is a small language and poorly represented in the LLMs' training data, we also investigate whether machine-translating the data to high-resource languages increases performance on the ideology detection task. Our findings suggest that, while LLMs are not yet fully optimized for a multi-class ideological annotation task, they are practical tools to identify language ideological content.

---


### 73. [A generalised pre-training strategy for deep learning networks in semantic segmentation of remotely sensed images](https://arxiv.org/abs/2604.27704)

**<font color=#1a73e8>作者：</font>** Yuan Fang, Yuanzhi Cai, Jagannath Aryal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the segmentation of remotely sensed images, deep learning models are typically pre-trained using large image databases like ImageNet before fine-tuned on domain-specific datasets. However, the performance of these fine-tuned models is often hindered by the large domain gaps (i.e., differences in scenes and modalities) between ImageNet's images and remotely sensed images being processed. Therefore, many researchers have undertaken efforts to establish large-scale domain-specific image datasets for pre-training, aiming to enhance model performance. However, establishing such datasets is often challenging, requiring significant effort, and these datasets often exhibit limited generaliza-bility to other application scenarios. To address these issues, this study introduces a novel yet simple pre-training strategy designed to guide a model away from learning domain-specific features in a pre-training dataset during pre-training, thereby improving the generalisation ability of the pre-trained model. To evaluate the strategy's effectiveness, deep learning models are pre-trained on ImageNet and subsequently fine-tuned on four semantic segmentation datasets with diverse scenes and modalities, including iSAID, MFNet, PST900 and Potsdam. Experimental results show that the proposed pre-training strategy led to state-of-the-art accuracies on all four datasets, namely 67.4% mIoU for iSAID, 56.9% mIoU for MFNet, 84.22% mIoU for PST900, 91.88% mF1 for Potsdam. This research lays the groundwork for developing a unified foundation model applicable to both computer vision and remote sensing applications.

---


### 74. [Contextual Agentic Memory is a Memo, Not True Memory](https://arxiv.org/abs/2604.27707)

**<font color=#1a73e8>作者：</font>** Binyan Xu, Xilin Dai, Kehuan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current agentic memory systems (vector stores, retrieval-augmented generation, scratchpads, and context-window management) do not implement memory: they implement lookup. We argue that treating lookup as memory is a category error with provable consequences for agent capability, long-term learning, and security. Retrieval generalizes by similarity to stored cases; weight-based memory generalizes by applying abstract rules to inputs never seen before. Conflating the two produces agents that accumulate notes indefinitely without developing expertise, face a provable generalization ceiling on compositionally novel tasks that no increase in context size or retrieval quality can overcome, and are structurally vulnerable to persistent memory poisoning as injected content propagates across all future sessions. Drawing on Complementary Learning Systems theory from neuroscience, we show that biological intelligence solved this problem by pairing fast hippocampal exemplar storage with slow neocortical weight consolidation, and that current AI agents implement only the first half. We formalize these limitations, address four alternative views, and close with a co-existence proposal and a call to action for system builders, benchmark designers, and the memory community.

---


### 75. [Linguistically Informed Multimodal Fusion for Vietnamese Scene-Text Image Captioning: Dataset, Graph Framework, and Phonological Attention](https://arxiv.org/abs/2604.27712)

**<font color=#1a73e8>作者：</font>** Nhi Ngoc-Yen Nguyen, Anh-Duc Nguyen, Nghia Hieu Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene-text image captioning requires fusing three information streams -- visual features, OCR-detected text, and linguistic knowledge -- to generate descriptions that faithfully integrate text visible in images. Existing fusion approaches treat text as language-agnostic, which fails for Vietnamese: a tonal language where diacritics alter word meaning, OCR errors are pervasive, and word boundaries are ambiguous. We argue that Vietnamese scene-text captioning demands \textit{linguistically informed multimodal fusion}, where language-specific structural knowledge is explicitly incorporated into the fusion mechanism. Motivated from these insights, we propose \textbf{HSTFG} (Heterogeneous Scene-Text Fusion Graph), a general-purpose graph fusion framework with learned spatial attention bias, and show through topology analysis that cross-modal graph edges are harmful for scene-text fusion. Building on this finding, we design \textbf{PhonoSTFG} (Phonological Scene-Text Fusion Graph) which specializes graph-level fusion for Vietnamese linguistic reasoning. To support evaluation, we introduce \textbf{ViTextCaps}, the first large-scale Vietnamese scene-text captioning dataset (\textbf{15{,}729} images with \textbf{74{,}970} captions), with comprehensive linguistic analysis showing that 52.8\% of the vocabulary is at risk of diacritic collision.

---


### 76. [Knowledge Graph Representations for LLM-Based Policy Compliance Reasoning](https://arxiv.org/abs/2604.27713)

**<font color=#1a73e8>作者：</font>** Wilder Baldwin, Sepideh Ghanavati  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The risks posed by AI features are increasing as they are rapidly integrated into software applications. In response, regulations and standards for safe and secure AI have been proposed. In this paper, we present an agentic framework that constructs knowledge graphs (KGs) from AI policy documents and retrieves policy-relevant information to answer questions. We build KGs from three AI risk-related polices under two ontology schemas, and then evaluate five LLMs on 42 policy QA tasks spanning six reasoning types, from entity lookup to cross-policy inference, using both heuristic scoring and an LLM-as-judge. KG augmentation improves scores for all five models, and an open, LLM-discovered schema matches or exceeds the formal ontology.

---


### 77. [Improving Calibration in Test-Time Prompt Tuning for Vision-Language Models via Data-Free Flatness-Aware Prompt Pretraining](https://arxiv.org/abs/2604.27715)

**<font color=#1a73e8>作者：</font>** Hyeonseo Jang, Jaebyeong Jeon, Joong-Won Hwang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time prompt tuning (TPT) has emerged as a promising technique for enhancing the adaptability of vision-language models by optimizing textual prompts using unlabeled test data. However, prior studies have observed that TPT often produces poorly calibrated models, raising concerns about the reliability of their predictions. Recent works address this issue by incorporating additional regularization terms that constrain model outputs, which improve calibration but often degrade performance. In this work, we reveal that these regularization strategies implicitly encourage optimization toward flatter minima, and that the sharpness of the loss landscape around adapted prompts is a key factor governing calibration quality. Motivated by this observation, we introduce Flatness-aware Prompt Pretraining (FPP), a simple yet effective pretraining framework for TPT that initializes prompts within flatter regions of the loss landscape prior to adaptation. We show that simply replacing the initialization in existing TPT pipelines--without modifying any other components--is sufficient to improve both calibration and performance. Notably, FPP requires no labeled data and incurs no additional computational costs during test-time tuning, making it highly practical for real-world deployment. The code is available at: this https URL.

---


### 78. [Auditing Frontier Vision-Language Models for Trustworthy Medical VQA: Grounding Failures, Format Collapse, and Domain Adaptation](https://arxiv.org/abs/2604.27720)

**<font color=#1a73e8>作者：</font>** Xupeng Chen, Binbin Shi, Chenqian Le 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying vision-language models (VLMs) in clinical settings demands auditable behavior under realistic failure conditions, yet the failure landscape of frontier VLMs on specialized medical inputs is poorly characterized. We audit five recent frontier and grounding-aware VLMs (Gemini~2.5~Pro, GPT-5, o3, GLM-4.5V, Qwen~2.5~VL) on Medical VQA along two trust-relevant axes. Perception: all models localize anatomical and pathological targets poorly -- the best model reaches only 0.23 mean IoU and 19.1% Acc@0.5 -- and exhibit clinically dangerous laterality confusion. Pipeline integration: a self-grounding pipeline, where the same model localizes then answers, degrades VQA accuracy for every model -- driven by both inaccurate localization and format-compliance failures under the two-step prompt (parse failure rises to 70%--99% for Gemini and GPT-5 on VQA-RAD). Replacing predicted boxes with ground-truth annotations recovers and improves VQA accuracy, consistent with the failure residing in the perception module rather than in the decomposition itself. These observational findings identify grounding quality as a primary trustworthiness bottleneck in our SLAKE bounding-box setting. As a complementary fine-tuning follow-up, supervised fine-tuning of Qwen~2.5~VL on combined Med-VQA training data attains the highest reported SLAKE open-ended recall (85.5%) among comparable methods, suggesting that the VQA-level gap is tractable with domain adaptation; whether this also closes the perception/trustworthiness bottleneck is left to future work.

---


### 79. [Optimized Deferral for Imbalanced Settings](https://arxiv.org/abs/2604.27723)

**<font color=#1a73e8>作者：</font>** Corinna Cortes, Anqi Mao, Mehryar Mohri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning algorithms can be significantly improved by routing complex or uncertain inputs to specialized experts, balancing accuracy with computational cost. This approach, known as learning to defer, is essential in domains like natural language generation, medical diagnosis, and computer vision, where an effective deferral can reduce errors at low extra resource consumption. However, the two-stage learning to defer setting, which leverages existing predictors such as a collection of LLMs or other classifiers, often faces challenges due to an expert imbalance problem. This imbalance can lead to suboptimal performance, with deferral algorithms favoring the majority expert. We present a comprehensive study of two-stage learning to defer in expert imbalance settings. We cast the deferral loss optimization as a novel cost-sensitive learning problem over the input-expert domain. We derive new margin-based loss functions and guarantees tailored to this setting, and develop novel algorithms for cost-sensitive learning. Leveraging these results, we design principled deferral algorithms, MILD (Margin-based Imbalanced Learning to Defer), specifically suited for expert imbalance settings. Extensive experiments demonstrate the effectiveness of our approach, showing clear improvements over existing baselines on both image classification and real-world Large Language Model (LLM) routing tasks.

---


### 80. [Iterative Multimodal Retrieval-Augmented Generation for Medical Question Answering](https://arxiv.org/abs/2604.27724)

**<font color=#1a73e8>作者：</font>** Xupeng Chen, Binbin Shi, Chenqian Le 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical retrieval-augmented generation (RAG) systems typically operate on text chunks extracted from biomedical literature, discarding the rich visual content (tables, figures, structured layouts) of original document pages. We propose MED-VRAG, an iterative multimodal RAG framework that retrieves and reasons over PMC document page images instead of OCR'd text. The system pairs ColQwen2.5 patch-level page embeddings with a sharded MapReduce LLM filter, scaling to ~350K pages while keeping Stage-1 retrieval under 30 ms via an offline coarse-to-fine index (C=8 centroids per page, ANN over centroids, exact two-way scoring on the top-R shortlist). A vision-language model (VLM) then iteratively refines its query and accumulates evidence in a memory bank across up to 3 reasoning rounds, with a single iteration costing ~15.9 s and the full three-round pipeline ~47.8 s on 4xA100. Across four medical QA benchmarks (MedQA, MedMCQA, PubMedQA, MMLU-Med), MEDVRAG reaches 78.6% average accuracy. Under controlled comparison with the same Qwen2.5-VL-32B backbone, retrieval contributes a +5.8 point gain over the no-retrieval baseline; we also note a +1.8 point edge over MedRAG + GPT-4 (76.8%), with the caveat that this is a cross-paper rather than head-to-head comparison. Ablations isolate +1.0 from page-image vs text-chunk retrieval, +1.5 from iteration, and +1.0 from the memory bank.

---


### 81. [AgentEconomist: An End-to-end Agentic System Translating Economic Intuitions into Executable Computational Experiments](https://arxiv.org/abs/2604.27725)

**<font color=#1a73e8>作者：</font>** Jiaju Chen, Jinghua Piao, Xia Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A long-standing challenge in economics lies not in the lack of intuition, but in the difficulty of translating intuitive insights into verifiable research. To address this challenge, we introduce AgentEconomist, an end-to-end interactive system designed to translate abstract intuitions into executable computational experiments. Grounded in a domain-specific knowledge base covering over 13,000 high-quality academic papers, the system employs a modular multi-stage architecture. Specifically, the Idea Development Stage generates literature-grounded hypotheses, the Experimental Design Stage configures simulator-aligned experimental parameters and protocols, and the Experimental Execution Stage runs experiments and returns structured analyses. Together, these stages form a human-in-the-loop, iterative workflow that translates economic intuitions into executable computational experiments. Through extensive experiments involving human expert evaluation and large language models (LLMs) as judges, we show that the system generates research ideas with stronger literature grounding and higher novelty and insight than state-of-the-art generic LLMs. Overall, AgentEconomist adopts a human-AI collaboration paradigm that enables researchers to focus on high-level intuitions, while delegating the labor-intensive processes of translation and computational execution to agents.

---


### 82. [Mind the Gap: Structure-Aware Consistency in Preference Learning](https://arxiv.org/abs/2604.27733)

**<font color=#1a73e8>作者：</font>** Mehryar Mohri, Yutao Zhong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference learning has become the foundation of aligning Large Language Models (LLMs) with human intent. Popular methods, such as Direct Preference Optimization (DPO), minimize surrogate losses as proxies for the intractable pairwise ranking loss. However, we demonstrate that for the equicontinuous hypothesis sets typical of neural networks, these standard surrogates are theoretically inconsistent, yielding vacuous generalization guarantees. To resolve this, we formulate LLM alignment within a margin-shifted ranking framework. We derive rigorous $H$-consistency bounds that depend on enforcing a separation margin $\gamma$. Crucially, we extend this to Structure-Aware $H$-consistency, introducing a novel objective (SA-DPO) that adapts the margin based on the semantic distance between responses to handle synonyms and hard pairs. Finally, we analyze the trade-off between consistency and model limitations via the Margin-Capacity Profile, proving that heavy-tailed surrogates (such as the Polynomial Hinge family) offer superior consistency guarantees for capacity-bounded models compared to the standard logistic loss used in DPO.

---


### 83. [Autonomous Traffic Signal Optimization Using Digital Twin and Agentic AI for Real-Time Decision-Making](https://arxiv.org/abs/2604.27753)

**<font color=#1a73e8>作者：</font>** Salman Jan, Toqeer Ali Syed, Shahid Kamal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This article outlines a new framework of traffic light optimization through a digital twin of the transport infrastructure, managed by agentic AI to ensure real-time autonomous decisions. The framework relies on physical sensors and edge computing to measure real-time traffic information and simulate traffic flow in a constantly updated digital twin. The traffic light is automatically controlled through the digital twin according to traffic congestion, travel delay and traffic patterns. This approach is implemented as a three-layer system: perception, conceptualization and action. The perception layer receives data on physical systems; the conceptualization layer uses LangChain to process the data; and the action layer links to the Model Context Protocol (MCP) and traffic management APIs to implement optimised traffic signal control algorithms. The results show that the framework minimizes waiting time at traffic lights and positively affects the effectiveness of the entire traffic flow, which is better than the fixed-time and reinforcement learning-based baselines.

---


### 84. [Intent2Tx: Benchmarking LLMs for Translating Natural Language Intents into Ethereum Transactions](https://arxiv.org/abs/2604.27763)

**<font color=#1a73e8>作者：</font>** Zhuoran Pan, Yue Li, Zhi Guan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The emergence of Large Language Models (LLMs) offers a transformative interface for Web3, yet existing benchmarks fail to capture the complexity of translating high-level user intents into functionally correct, state-dependent on-chain transactions. We present \textsc{Intent2Tx}, a high-fidelity benchmark featuring 29,921 single-step and 1,575 multi-step instances meticulously derived from 300 days of real-world Ethereum mainnet traces. Unlike prior works that rely on synthetic instructions, \textsc{Intent2Tx} grounds natural language intents in real-world protocol interactions across 11 categories, including diverse long-tail Decentralized Finance (DeFi) primitives. To enable rigorous evaluation, we propose an execution-aware framework that transcends surface-level text matching by employing differential state analysis on forked mainnet environments. Our extensive evaluation of 16 state-of-the-art LLMs reveals that while scaling and retrieval-augmentation enhance logical consistency and parameter precision, current models struggle with out-of-distribution generalization and multi-step planning. Crucially, our execution-based analysis demonstrates that syntactically valid outputs often fail to achieve intended state transitions, highlighting a significant gap in current "reasoning-to-execution" capabilities. \textsc{Intent2Tx} serves as a critical foundation for developing autonomous, reliable agents in intent-centric Web3 ecosystems. Code and data: this https URL .

---


### 85. [Instruction-Guided Poetry Generation in Arabic and Its Dialects](https://arxiv.org/abs/2604.27766)

**<font color=#1a73e8>作者：</font>** Abdelrahman Sadallah, Kareem Elozeiri, Mervat Abassy 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Poetry has long been a central art form for Arabic speakers, serving as a powerful medium of expression and cultural identity. While modern Arabic speakers continue to value poetry, existing research on Arabic poetry within Large Language Models (LLMs) has primarily focused on analysis tasks such as interpretation or metadata prediction, e.g., rhyme schemes and titles. In contrast, our work addresses the practical aspect of poetry creation in Arabic by introducing controllable generation capabilities to assist users in writing poetry. Specifically, we present a large-scale, carefully curated instruction-based dataset in Modern Standard Arabic (MSA) and various Arabic dialects. This dataset enables tasks such as writing, revising, and continuing poems based on predefined criteria, including style and rhyme, as well as performing poetry analysis. Our experiments show that fine-tuning LLMs on this dataset yields models that can effectively generate poetry that is aligned with user requirements, based on both automated metrics and human evaluation with native Arabic speakers. The data and the code are available at this https URL

---


### 86. [ObjectGraph: From Document Injection to Knowledge Traversal -- A Native File Format for the Agentic Era](https://arxiv.org/abs/2604.27820)

**<font color=#1a73e8>作者：</font>** Mohit Dubey, Open Gigantic  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every document format in existence was designed for a human reader moving linearly through text. Autonomous LLM agents do not read - they retrieve. This fundamental mismatch forces agents to inject entire documents into their context window, wasting tokens on irrelevant content, compounding state across multi-turn loops, and broadcasting information indiscriminately across agent roles. We argue this is not a prompt engineering problem, not a retrieval problem, and not a compression problem: it is a format problem.
We introduce OBJECTGRAPH (.og), a file format that reconceives the document as a typed, directed knowledge graph to be traversed rather than a string to be injected. OBJECTGRAPH is a strict superset of Markdown - every .md file is a valid .og file - requires no infrastructure beyond a two-primitive query protocol, and is readable by both humans and agents without tooling.
We formalize the Document Consumption Problem, characterise six structural properties no existing format satisfies simultaneously, and prove OBJECTGRAPH satisfies all six. We further introduce the Progressive Disclosure Model, the Role-Scoped Access Protocol, and Executable Assertion Nodes as native format primitives. Empirical evaluation across five document classes and eight agent task types demonstrates up to 95.3 percent token reduction with no statistically significant degradation in task accuracy (p > 0.05). Transpiler fidelity reaches 98.7 percent content preservation on a held-out document benchmark.

---


### 87. [Taming Noise-Induced Prototype Degradation for Privacy-Preserving Personalized Federated Fine-Tuning](https://arxiv.org/abs/2604.27833)

**<font color=#1a73e8>作者：</font>** Yuhua Wang, Qinnan Zhang, Xiaodong Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prototype-based Personalized Federated Learning (ProtoPFL) enables efficient multi-domain adaptation by communicating compact class prototypes, but directly sharing them poses privacy risks. A common defense involves per-example $\ell_2$ clipping before prototype computation to bound sensitivity, followed by isotropic Gaussian noise to enforce Local Differential Privacy (LDP). However, Isotropic Gaussian Prototype Perturbation (IGPP) typically over-perturbs discriminative dimensions and struggles to balance the clipping threshold with representation fidelity. In this paper, we propose VPDR, a client-side privacy plug-in that seamlessly integrates into existing ProtoPFLs. Motivated by the observation that dimension-wise class variance reflects discriminability, we introduce Variance-adaptive Prototype Perturbation (VPP), which allocates less noise to discriminative subspaces, preserving semantic separability while ensuring privacy. We further develop Distillation-guided Clipping Regularization (DCR), which enables feature norms to adaptively concentrate near the predefined clipping threshold while maintaining prediction consistency. Theoretical analysis shows that our groupwise mechanism provides privacy guarantees no weaker than the isotropic baseline under the same privacy constraints. Extensive experiments on multi-domain benchmarks demonstrate that VPDR achieves a superior privacy-utility trade-off, outperforming IGPP in personalized federated fine-tuning without sacrificing robustness against realistic attacks.

---


### 88. [CastFlow: Learning Role-Specialized Agentic Workflows for Time Series Forecasting](https://arxiv.org/abs/2604.27840)

**<font color=#1a73e8>作者：</font>** Bokai Pan, Mingyue Cheng, Zhiding Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, large language models (LLMs) have shown great promise in time series forecasting. However, most existing LLM-based forecasting methods still follow a static generative paradigm that directly maps historical observations to future values in a single pass. Under this paradigm, forecasting is constrained by limited temporal pattern extraction, single-round acquisition of contextual features, one-shot forecast generation, and lack of support from ensemble forecasts. To address these limitations, in this work, we propose CastFlow, a dynamic agentic forecasting framework that enables multi-view temporal pattern extraction, multi-round contextual features acquisition, iterative forecast refinement, and forecasting with ensemble forecasts. First, CastFlow organizes the forecasting process into planning, action, forecasting, and reflection, establishing an agentic workflow. Second, this workflow is supported by a memory module that retrieves prior experience and a multi-view toolkit that constructs diagnostic evidence and provides a reliable ensemble forecast baseline. Third, CastFlow adopts a role-specialized design that combines general-purpose reasoning with specialized numerical forecasting. Under this design, a frozen LLM preserves general-purpose reasoning, while a fine-tuned domain-specific LLM performs evidence-guided numerical forecasting based on the ensemble forecast baseline, rather than from scratch. To optimize a fine-tuned domain-specific LLM, we further develop a two-stage workflow-oriented training that combines supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR). To evaluate the effectiveness of CastFlow, we conduct extensive experiments on diverse datasets and show that it achieves superior overall results against strong baselines. We hope that this work can serve as a step toward more adaptive and accurate time series forecasting.

---


### 89. [Rethinking Agentic Reinforcement Learning In Large Language Models](https://arxiv.org/abs/2604.27859)

**<font color=#1a73e8>作者：</font>** Fangming Cui, Ruixiao Zhu, Cheng Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has traditionally focused on training specialized agents to optimize predefined reward functions within narrowly defined environments. However, the advent of powerful Large Language Models (LLMs) and increasingly complex, open-ended tasks has catalyzed a paradigm shift towards agentic paradigms within RL. This emerging framework extends beyond traditional RL by emphasizing the development of autonomous agents capable of goal-setting, long-term planning, dynamic strategy adaptation, and interactive reasoning in uncertain, real-world environments. Unlike conventional approaches that rely heavily on static objectives and episodic interactions, LLM-based Agentic RL incorporates cognitive-like capabilities such as meta-reasoning, self-reflection, and multi-step decision-making directly into the learning loop. In this paper, we provide a deep insight for looking the conceptual foundations, methodological innovations, and effective designs underlying this trend. Furthermore, we identify critical challenges and outline promising future directions for building LLM-based Agentic RL.

---


### 90. [Modeling Clinical Concern Trajectories in Language Model Agents](https://arxiv.org/abs/2604.27872)

**<font color=#1a73e8>作者：</font>** Sukesh Subaharan, Venkatesan VS, Murugadasan P 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents deployed in clinical settings often exhibit abrupt, threshold-driven behavior, offering little visibility into accumulating risk prior to escalation. In real-world care, however, clinicians act on gradually rising concern rather than instantaneous triggers. We study whether explicit state dynamics can expose such pre-escalation signals without delegating clinical authority to the agent. We introduce a lightweight agent architecture in which a memoryless clinical risk encoder is integrated over time using first- and second-order dynamics to produce a continuous escalation pressure signal. Across synthetic ward scenarios, stateless agents exhibit sharp escalation cliffs, while second-order dynamics produce smooth, anticipatory concern trajectories despite similar escalation timing. These trajectories surface sustained unease prior to escalation, enabling human-in-the-loop monitoring and more informed intervention. Our results suggest that explicit state dynamics can make LLM agents more clinically legible by revealing how long concern has been rising, not just when thresholds are crossed.

---


### 91. [Graph World Models: Concepts, Taxonomy, and Future Directions](https://arxiv.org/abs/2604.27895)

**<font color=#1a73e8>作者：</font>** Jiawei Liu, Senqiao Yang, Mingjun Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As one of the mainstream models of artificial intelligence, world models allow agents to learn the representation of the environment for efficient prediction and planning. However, classical world models based on flat tensors face several key problems, including noise sensitivity, error accumulation and weak reasoning. To address these limitations, many recent studies use graph structure to decompose the environment into entity nodes and interactive edges, and model virtual environments in a structured space. This paper systematically formalizes and unifies these emerging graph-based works under the concept of graph world models (GWMs). To the best of our knowledge, GWMs have not yet been explicitly defined and surveyed as a unified research paradigm. Furthermore, we propose a taxonomy based on relational inductive biases (RIB), categorizing GWMs by the specific structural priors they inject: (1) spatial RIB for topological abstraction; (2) physical RIB for dynamic simulation; and (3) logical RIB for causal and semantic reasoning. For each model category, we outline the key design principles, summarize representative models, and conduct comparative analyses. We further discuss open challenges and future directions, including dynamic graph adaptation, probabilistic relational dynamics, multi-granularity inductive biases, and the need for dedicated benchmarks and evaluation metrics for GWMs.

---


### 92. [Simulating clinical interventions with a generative multimodal model of human physiology](https://arxiv.org/abs/2604.27899)

**<font color=#1a73e8>作者：</font>** Guy Lutsker, Gal Sapir, Jordi Merino 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding how human health changes over time, and why responses to interventions vary between individuals, remains a central challenge in medicine. Here we present HealthFormer, a decoder-only transformer that models the human physiological trajectory generatively, by training on data from the Human Phenotype Project, a multi-visit cohort of over 15,000 deeply phenotyped individuals. We tokenise each participant's health trajectory across 667 measurements spanning seven domains: blood biomarkers, body composition, sleep physiology, continuous glucose monitoring, gut microbiome, wearable-derived physiology, and behaviour and medication exposure. We train HealthFormer to forecast individual physiological trajectories across these domains, and from this single generative objective a range of clinically relevant tasks can be expressed as queries on the model. We show that, without task-specific training, HealthFormer transfers to four independent cohorts and improves prediction for 27 of 30 incident-disease and mortality endpoints, exceeding established clinical risk scores in every comparison. We further show that the model can simulate interventions in silico: in a held-out personalised-nutrition trial, intervention-conditioned predictions recover individual six-month biomarker changes (e.g., Pearson r = 0.78 for diastolic blood pressure). Across 41 randomised intervention-outcome comparisons drawn from published trials, our results show that the predicted direction of effect agrees in every case, and the predicted mean falls within the reported 95% confidence interval in 30 cases. We position HealthFormer as an initial health world model, from which forecasting, risk stratification, and intervention-conditioned simulation arise as queries, providing a basis for clinical digital twins.

---


### 93. [Physical Foundation Models: Fixed hardware implementations of large-scale neural networks](https://arxiv.org/abs/2604.27911)

**<font color=#1a73e8>作者：</font>** Logan G Wright, Tianyu Wang, Tatsuhiro Onodera 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models are deep neural networks (such as GPT-5, Gemini~3, and Opus~4) trained on large datasets that can perform diverse downstream tasks -- text and code generation, question answering, summarization, image classification, and so on. The philosophy of foundation models is to put effort into a single, large (${\sim}10^{12}$-parameter) general-purpose model that can be adapted to many downstream tasks with no or minimal additional training. We argue that the rise of foundation models presents an opportunity for hardware engineers: in contrast to when different models were used for different tasks, it now makes sense to build special-purpose, fixed hardware implementations of neural networks, manufactured and released at the roughly 1-year cadence of major new foundation-model versions.
Beyond conventional digital-electronic inference hardware with read-only weight memory, we advocate a more radical re-thinking: hardware in which the neural network is realized directly at the level of the physical design and operates via the hardware's natural physical dynamics -- \textit{Physical Foundation Models} (PFMs). PFMs could enable orders-of-magnitude advantages in energy efficiency, speed, and parameter density. For ${\sim}10^{12}$-parameter models, this would both reduce the high energy burden of AI in datacenters and enable AI in edge devices that today are power-constrained to far smaller models. PFMs could also enable inference hardware for models much larger than current ones: $10^{15}$- or even $10^{18}$-parameter PFMs seem plausible by some measures. We present back-of-the-envelope calculations illustrating PFM scaling using an optical example -- a 3D nanostructured glass medium -- and discuss prospects in nanoelectronics and other physical platforms. We conclude with the major research challenges that must be resolved for trillion-parameter PFMs and beyond to become reality.

---


### 94. [Geometry-Calibrated Conformal Abstention for Language Models](https://arxiv.org/abs/2604.27914)

**<font color=#1a73e8>作者：</font>** Rui Xu, Yi Chen, Sihong Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When language models lack relevant knowledge for a given query, they frequently generate plausible responses that can be hallucinations, rather than admitting being agnostic about the answer. Retraining models to reward admitting ignorance can lead to overly conservative behaviors and poor generalization due to scarce evaluation benchmarks. We propose a post hoc framework, Conformal Abstention (CA), adapted from conformal prediction (CP) to determine whether to abstain from answering a query. CA provides finite-sample guarantees on both the probability of participation (i.e., not abstaining) and the probability that the generated response is correct. Importantly, the abstention decision relies on prediction confidence rather than the non-conformity scores used in CP, which are intractable for open-ended generation. To better align prediction confidence with the model's ignorance, we introduce a calibration strategy using representation geometry within the model to measure knowledge involvement in shaping the response. Experiments demonstrate that we improve selective answering significantly with 75 percent conditional correctness.

---


### 95. [Beyond Semantics: Measuring Fine-Grained Emotion Preservation in Small Language Model-Based Machine Translation](https://arxiv.org/abs/2604.27920)

**<font color=#1a73e8>作者：</font>** Dawid Wisniewski, Igor Czudy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Preserving affective nuance remains a challenge in Machine Translation (MT), where semantic equivalence often takes precedence over emotional fidelity. This paper evaluates the performance of three state-of-the-art Small Language Models (SLMs) -- EuroLLM, Aya Expanse, and Gemma -- in maintaining fine-grained emotions during backtranslation. Using the GoEmotions dataset, which comprises Reddit comments across 28 distinct categories, we assess emotional preservation across five European languages: German, French, Spanish, Italian, and Polish. Specifically, we investigate (i) the inherent capability of these SLMs to retain emotional sentiment, (ii) the efficacy of emotion-aware prompting in improving preservation, and (iii) the performance of ModernBERT as a contemporary alternative to BERT for emotion classification in MT evaluation.

---


### 96. [Can AI Be a Good Peer Reviewer? A Survey of Peer Review Process, Evaluation, and the Future](https://arxiv.org/abs/2604.27924)

**<font color=#1a73e8>作者：</font>** Sihong Wu, Owen Jiang, Yilun Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Peer review is a multi-stage process involving reviews, rebuttals, meta-reviews, final decisions, and subsequent manuscript revisions. Recent advances in large language models (LLMs) have motivated methods that assist or automate different stages of this pipeline. In this survey, we synthesize techniques for (i) peer review generation, including fine-tuning strategies, agent-based systems, RL-based methods, and emerging paradigms to enhance generation; (ii) after-review tasks including rebuttals, meta-review and revision aligned to reviews; and (iii) evaluation methods spanning human-centered, reference-based, LLM-based and aspect-oriented. We catalog datasets, compare modeling choices, and discuss limitations, ethical concerns, and future directions. The survey aims to provide practical guidance for building, evaluating, and integrating LLM systems across the full peer review workflow.

---


### 97. [DPN-LE: Dual Personality Neuron Localization and Editing for Large Language Models](https://arxiv.org/abs/2604.27929)

**<font color=#1a73e8>作者：</font>** Lifan Zheng, Xue Yang, Jiawei Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the widespread adoption of large language models (LLMs), understanding their personality representation mechanisms has become critical. As a novel paradigm in Personality Editing, most existing methods employ neuron-editing to locate and modify LLM neurons, requiring changes to numerous neurons and leading to significant performance degradation. This raises a fundamental question: Are all modified neurons directly related to personality representation? In this work, we investigate and quantify this specificity through assessments of general capability impact and representation-level patterns. We find that: 1) Current methods can change personalities but reduce overall performance. 2) Neurons are multifunctional, connecting personality traits and general knowledge. 3) Opposing personality traits demonstrate distinctly mutually exclusive representation patterns. Motivated by these findings, we propose DPN-LE (Dual Personality Neuron Localization and Editing), which identifies personality-specific neurons by contrasting MLP activations between high-trait and low-trait samples. DPN-LE constructs layer-wise steering vectors and applies dual-criterion filtering based on Cohen's $d$ effect size and activation magnitude to isolate mutually exclusive neuron subsets. Sparse linear intervention on these neurons enables precise personality control at inference time. Using only 1,000 contrastive sample pairs per trait, DPN-LE intervenes on $\sim$0.5\% of neurons while achieving competitive personality control and substantially better capability preservation across reasoning tasks. Experiments on LLaMA-3-8B-Instruct and Qwen2.5-7B-Instruct demonstrate the effectiveness and generalizability of our approach.

---


### 98. [Dynamic Cluster Data Sampling for Efficient and Long-Tail-Aware Vision-Language Pre-training](https://arxiv.org/abs/2604.27932)

**<font color=#1a73e8>作者：</font>** Mingliang Liang, Zhuoran Liu, Arjen P. de Vries 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The computational cost of training a vision-language model (VLM) can be reduced by sampling the training data. Previous work on efficient VLM pre-training has pointed to the importance of semantic data balance, adjusting the distribution of topics in the data to improve VLM accuracy. However, existing efficient pre-training approaches may disproportionately remove rare concepts from the training corpus. As a result, \emph{long-tail concepts} remain insufficiently represented in the training data and are not effectively captured during training. In this work, we introduce a \emph{dynamic cluster-based sampling approach (DynamiCS)} that downsamples large clusters of data and upsamples small ones. The approach is dynamic in that it applies sampling at each epoch. We first show the importance of dynamic sampling for VLM training. Then, we demonstrate the advantage of our cluster-scaling approach, which maintains the relative order of semantic clusters in the data and emphasizes the long-tail. This approach contrasts with current work, which focuses only on flattening the semantic distribution of the data. Our experiments show that DynamiCS reduces the computational cost of VLM training and provides a performance advantage for long-tail concepts.

---


### 99. [Enhancing multimodal affect recognition in healthcare: the robustness of appraisal dimensions over labels within age groups and in cross-age generalisation](https://arxiv.org/abs/2604.27938)

**<font color=#1a73e8>作者：</font>** Hippolyte Fournier, Sina Alisamir, Safaa Azzakhnini 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The integration of artificial intelligence (AI) into healthcare has advanced significantly, yet affect recognition remains a major challenge, particularly in AI-assisted interventions such as Computerized Cognitive Training (CCT). The THERADIA-WoZ corpus was developed to enable multimodal affect recognition in the context of AI-driven CCT, focusing on an older adult population. This study extends the corpus by introducing a dataset collected from young adults, allowing direct comparison of affect recognition models across age groups. Our objective was to assess whether multimodal models based on dimensions borrowed from appraisal theories outperform those based on categorical labels and to evaluate their generalisation power across age corpora. After comparing both corpora, models were trained and tested using within-corpus, cross-corpus, and mixed-corpus evaluation. Results revealed that appraisal dimensions consistently outperformed categorical labels across all conditions, demonstrating greater predictive accuracy and stability. Notably, categorical labels failed to generalise across age corpora, as performance dropped to chance levels in cross-corpus evaluation. In contrast, appraisal dimensions maintained predictive performance above chance, reinforcing their robustness for cross-age affect recognition. Furthermore, training on both corpora did not improve generalisation beyond within-corpus training. The findings support the theoretical and practical advantages of appraisal dimensions over categorical labels in affective computing. They also highlight the importance of multimodal fusion and deep learning representations for emotion modeling. To facilitate future research, we provide an API for researchers interested in time-continuous emotion prediction, offering valuable tools for behavioral sciences to enhance the measurement of emotional states in various experimental settings.

---


### 100. [The Effects of Visual Priming on Cooperative Behavior in Vision-Language Models](https://arxiv.org/abs/2604.27953)

**<font color=#1a73e8>作者：</font>** Kenneth J. K. Ong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Vision-Language Models (VLMs) become increasingly integrated into decision-making systems, it is essential to understand how visual inputs influence their behavior. This paper investigates the effects of visual priming on VLMs' cooperative behavior using the Iterated Prisoner's Dilemma (IPD) as a test scenario. We examine whether exposure to images depicting behavioral concepts (kindness/helpfulness vs. aggressiveness/selfishness) and color-coded reward matrices alters VLM decision patterns. Experiments were conducted across multiple state-of-the-art VLMs. We further explore mitigation strategies including prompt modifications, Chain of Thought (CoT) reasoning, and visual token reduction. Results show that VLM behavior can be influenced by both image content and color cues, with varying susceptibility and mitigation effectiveness across models. These findings not only underscore the importance of robust evaluation frameworks for VLM deployment in visually rich and safety-critical environments, but also highlight how architectural and training differences among models may lead to distinct behavioral responses-an area worthy of further investigation.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-123](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
