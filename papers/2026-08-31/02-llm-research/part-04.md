# 🧠 大模型相关研究 | 2026年08月31日

> 本类共 **231** 篇论文：已确认 **221** 篇，待复核 **10** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-231](./part-05.md)

---

### 151. [AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations](https://arxiv.org/abs/2608.26921)

**<font color=#1a73e8>作者：</font>** Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce AraMS-28k, the largest publicly released line-level dataset of genuine historical Arabic manuscripts, comprising 14 books, 3,043 pages, and 28,600 annotated text lines (27,971 main-text, 629 margin). Thirteen books are hand-copied manuscripts spanning three script traditions -- Naskh, Ruq'ah, and Maghrebi -- and one is a lithographed printed edition included to broaden format diversity. Each line is labelled as main-text or margin, and margin lines that have an unambiguous attachment point in the main text are further annotated with an insertion anchor, recovering the manuscript's true non-linear reading order at line-level granularity -- to our knowledge the first such annotation released for a historical Arabic manuscript corpus. Because reference transcriptions are fully vocalised while manuscript hands are typically undiacritised, we release both the raw diacritised transcription and a diacritic-normalised counterpart for every line. The dataset was constructed with RefLAM, a reference-grounded annotation pipeline that aligns multimodal-LLM OCR against independently sourced clean transcriptions and routes every line through human review, combining automatic verification with expert oversight. We describe the construction and quality-control process, present the annotation schema, report dataset statistics at both the corpus and per-book level, and provide baseline HTR results using Kraken and HATFormer, including a cross-script generalisation gradient from in-distribution pages to fully unseen books. AraMS-28k is released with page images, line-level annotations, and fixed train/val/test splits under CC BY-NC-SA 4.0 to support reproducible research on Arabic manuscript recognition, layout analysis, and reading-order recovery.

---


### 152. [TabuLM: Morphology-Aware Tabular Pre-training for Low-Resource Languages](https://arxiv.org/abs/2608.26923)

**<font color=#1a73e8>作者：</font>** Ireddi Rakshitha, Devavarapu Yashwanth, Ntakirutimana Pierre  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present TabuLM, the first language model pre-trained on Kinyarwanda tabular data. Kinyarwanda is a morphologically rich Bantu language spoken by over 12 million people in Rwanda, yet lacks any dedicated tabular representation learning resource. TabuLM extends KinyaBERT-large, a two-tier morphological transformer, with additive row, column, and cell-type embeddings and a learned table-structure attention bias that sharpens same-row and same-column attention. Pre-training uses two new objectives: Masked Cell Recovery (MCR), which masks entire cells and forces reconstruction from row and column context, and Column Type Prediction (CTP), which predicts column semantic types from observed cell values. We pre-train on 172 Rwandan government tables (~35,000 cells) from NISR, RAB, REB, and MoH open-data portals, and introduce TabQA-kin, the first native Kinyarwanda table question-answering benchmark comprising 526 QA pairs across 31 tables and four question types. TabuLM achieves 62.0% exact match on TabQA-kin, outperforming KinyaBERT-large by 5.7 EM points and all multilingual baselines (mBERT 49.3%, XLM-R 50.0%) by 11.7-12.7 points. Analysis shows that structural table embeddings are most decisive for comparison and lookup questions, while morphological awareness provides complementary gains. Our code, data, and pre-trained checkpoint are publicly available.

---


### 153. [A Layer Importance Metric for Quantization Accounting for the Speed-Quality Trade-off in Autoregressive Models](https://arxiv.org/abs/2608.26926)

**<font color=#1a73e8>作者：</font>** Artem Safronov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small language models (sLLMs) are nowadays hosted on devices with limited memory and computational budget. In an autoregressive setup, inference is memory-bandwidth bound: uniform quantization is often detrimental to such models, since their architecture has limited redundancies and only a few layers are not very sensitive to lower precision. We propose a composite metric that combines two orthogonal criteria: information retention (measured in terms of a normalized SQNR-based coefficient) and throughput gains (modeled using a roofline-based latency analysis). By profiling Gemma 3 1B, we find that Feed-Forward Network blocks and the embedding matrix are the most promising targets for acceleration. For each candidate, we estimate a normalized quality score based on simulated quantization and a normalized speed score based on roofline modeling with no actual execution needed. We combine the two scores in a composite priority coefficient, allowing us to tune the trade-off between speed and quality as needed. Our metric is general and can be used to prioritize individual blocks, their projection sublayers, or transformer layers as a whole. We evaluate our approach on several model architectures, showing that our estimates have at around 4% prediction error for the accelerated speedup. We find that our method generally allocates more resources to the most expressive layers compared to evolutionary search, specialized accelerators, or Shapley-value-based approaches that require expensive approximate inference. Our analytical approach makes sLLM quantization a predictable engineering task.

---


### 154. [A Table Is Worth 64 Tokens: Pixel-level Compression for Multi-Table Document Question Answering](https://arxiv.org/abs/2608.26949)

**<font color=#1a73e8>作者：</font>** Iñigo Alonso, Mirella Lapata  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Answering questions over real-world documents requires processing long inputs that interleave text with tables. Optical context compression, which represents context as images, promises to reduce token cost, but its effect on table understanding remains unclear. We study pixel-level table compression for question answering over documents with multiple tables, evaluating five VLMs across two benchmarks and five visual-token budgets. Representing tables as images at native resolution matches text in both performance and efficiency, but downscaling them makes models compensate the loss in readability with longer, less effective reasoning traces that cancel the expected savings. Highly downscaled tables, however, preserve enough signal to identify whether they are relevant to a question. We exploit this asymmetry with a training-free, two-step method: the model first identifies the tables needed to answer a question from a pixel-compressed context, and then reasons over those at native resolution. On long documents, our method saves 41% of total tokens and gains 7 accuracy points over single-step QA with native resolution tables. It also uses 15% fewer tokens than the most efficient single-step compressed configuration, with no accuracy loss.

---


### 155. [From Atomic to Agentic: Towards Interpretable Evaluation of LLMs' Agentic Mathematical Capabilities](https://arxiv.org/abs/2608.26950)

**<font color=#1a73e8>作者：</font>** Jiayi Kuang, Yinghui Li, Yunze Song 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are evolving from performing end-to-end mathematical reasoning to integrating agentic intelligence. However, most existing math benchmarks evaluate only final answers. This outcome-oriented evaluation provides limited diagnostic value for identifying process-level failures or rigorous logic, failing to guide the transformation of LLMs into robust agents. To bridge this gap, we present a process-level benchmark designed to evaluate the inherent agentic mathematical reasoning abilities of LLMs. Our framework aligns problem-solving agentic behaviors with a structured taxonomy of reusable mathematical atomic capabilities. We design a comprehensive suite of planning, action, and feedback tasks across both textual and multimodal contexts, supported by an automated pipeline that synthesizes high-quality trajectories and produces fine-grained annotations via controlled LLM rewriting. Experiments reveal that models with similar end-to-end accuracy can exhibit markedly different agentic capability profiles. This demonstrates that process-level evaluation is crucial for interpreting the true potential of LLMs and guiding the development of next-generation mathematical agents.

---


### 156. [RubricRM: Generative Reward Modeling via Dynamic Rubrics for Image Generation and Editing](https://arxiv.org/abs/2608.26956)

**<font color=#1a73e8>作者：</font>** Zijian Kan, Wei Wang, Long Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reward models play an essential role in aligning visual generative models, yet most existing visual reward models use a single scalar score or rely on fixed criteria that cannot adapt to different instructions. This limits both interpretability and task sensitivity, especially for text-to-image generation and instruction-based image editing, where different inputs require different evaluation dimensions. We propose RubricRM, a pairwise generative reward modeling framework that first produces an input-specific rubric with evaluation dimensions, weights, and scoring criteria, and then applies the rubric to score candidate images. We train dedicated RubricRM models for text-to-image generation and image editing using a two-stage training pipeline: supervised fine-tuning teaches the model the rubric-based scoring paradigm, while GRPO further improves scoring through fine-grained dimension-level rewards. Experiments on multiple generation and editing benchmarks show that RubricRM outperforms existing specialized reward models and remains competitive with strong proprietary MLLM judges despite using smaller backbones. Our models, data, and code are available at this https URL.

---


### 157. [JudgeStealer: Extracting LLM Judging Capabilities across Evaluation Protocols](https://arxiv.org/abs/2608.26982)

**<font color=#1a73e8>作者：</font>** Chen Chen, Yaolin Chen, Xuehan Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) judges are increasingly used across various evaluation scenarios, making their judgment capabilities valuable intellectual property. However, black-box access exposes these capabilities to model extraction attacks. Existing extraction methods do not specifically target LLM judges and provide limited support for multiple evaluation protocols under restricted query budgets. In this study, we propose JUDGESTEALER, the first query-efficient model extraction framework for replicating judging capabilities across pointwise scoring, pairwise comparison, and listwise ranking protocols. JUDGESTEALER exploits the strong cross-protocol agreement to acquire pointwise scores and transform them into pairwise and listwise supervisions without additional victim queries. To capture informative judge patterns and improve query efficiency, JUDGESTEALER dynamically selects pointwise inputs based on semantic diversity, predictive uncertainty, and potential judge biases. It further applies score smoothing and multi-protocol review to preserve the ordinal structure of scores and mitigate catastrophic forgetting during surrogate adaptation. Extensive experiments on state-of-the-art LLM-as-a-judge and reward models show that JUDGESTEALER consistently outperforms existing extraction baselines, achieving up to 73.3%, 87.0%, and 71.6% accuracy for pointwise, pairwise, and listwise evaluation, respectively. JUDGESTEALER also remains effective across different sur- rogate model scales, adaptation strategies, and reasoning settings. Moreover, JUDGESTEALER demonstrates robustness against representative extraction defenses.

---


### 158. [GraphMemix: Query-Aware Evidence Forests for Long-Term Multimodal Agent Memory](https://arxiv.org/abs/2608.26983)

**<font color=#1a73e8>作者：</font>** Geng Li, Yuhao Wang, Dong Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Organizing long-term memory for multimodal agents remains challenging because existing methods either suffer from expensive question-agnostic offline summaries or naive embedding similarity matching that introduces incomplete and redundant context. To address these issues, we propose GraphMemix, a combinatorial-optimization graph memory framework that models memory organization as query-aware evidence-forest construction. Specifically, our method consists of three key components:(1) candidate graph construction, which expands multi-view seed memories through schema and semantic relations to acquire query-aware original context; (2) evidence utility and activation costs, which decouples direct memory support from anchor-conditioned relation verification to suppress redundant or conflicting information; and (3) forest optimization, which jointly selects a forest-format memory context under a maximum evidence budget and its reliable relational structure. By organizing memory into a query-relevant subgraph, the method avoids substantial lifecycle cost and recovers low-similarity complementary evidence. Experimental results across four long-term multimodal memory benchmarks demonstrate significant improvements with different foundation models and establish a new Pareto frontier between accuracy and lifecycle cost.

---


### 159. [DSA: Evidence-Aware LLM-Agent Orchestration for Multi-Market Stock Research](https://arxiv.org/abs/2608.26990)

**<font color=#1a73e8>作者：</font>** Linsen Zhu, Yi Shi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can summarize financial information, but an operational stock-research system must first assemble heterogeneous evidence, expose unavailable data and model capabilities, and control how generated opinions affect a final report. We present DSA, an evidence-aware orchestration framework for multi-market stock research with large language model (LLM) agents. DSA organizes the workflow into evidence acquisition, structured context construction, model-routed analysis, optional role and Strategy Skill reasoning, and report generation with selected context and diagnostics. A default report profile and an optional agentic profile share evidence and model-routing services but use profile-specific output validation and risk safeguards. In the agentic profile, core role outputs are processed by role-specific parsers, whereas Strategy Skill opinions undergo an additional signal-eligibility partition before synthesis; disagreement is supplied explicitly to the decision agent, followed by a conservative risk override. The reference implementation includes six regional market paths, fifteen bundled Strategy Skills, hosted and local model routes, and multiple execution and delivery surfaces. At a frozen software snapshot, a selected manifest of 1,457 portable offline backend contract tests passed; 596 cases were retrospectively mapped to six contract families central to the reported LLM-agent architecture. This evidence establishes implementation conformance for the tested software contracts, not superior report quality, forecasting accuracy, or investment returns.

---


### 160. [ASIL: Replacing Screenshot-and-Click with Structured State and Semantic Actions](https://arxiv.org/abs/2608.26991)

**<font color=#1a73e8>作者：</font>** Rui Xie, Lu Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Powerful code agents can execute scripts, call tools, and manage files, yet many important applications remain accessible primarily through graphical user interfaces. We argue that screenshot-and-click is an inefficient interface for software-operating agents: screenshots are state-incomplete, and GUI actions are brittle, semantically weak, and poorly matched to long-horizon planning. We introduce ASIL (Agent-Software Interaction Layer), an agent-native interface that exposes software through structured JSON observations and code-executable semantic actions, realized through the deepest feasible access path for each application. We instantiate ASIL across 15 applications and a benchmark of 300 single-application and 80 multi-application tasks. ASIL reaches above 80 with closed models while executing fewer than five actions per task. Under a repaired runtime and a 50-step screenshot budget, the same tasks yield 6.6 and 26.6 strict success under screenshot-and-click control, rising to 15.0 and 53.3 on an easier OSWorld-comparable band. Against application-native interfaces on matched tasks, ASIL exceeds LibreOffice's UNO API by 28-38 strict points but only matches this http URL's MCP content contract. The structured modality also suits training: small-scale SFT raises Qwen3.5-2B from 58.0 to 72.1 and Qwen3.5-9B from 66.6 to 80.4, and resource-limited on-policy RL further raises them to 74.4 and 82.2.

---


### 161. [Aphanta: Diagnosing Task-Aligned Image-Edited Intermediates for Multimodal Reasoning](https://arxiv.org/abs/2608.26993)

**<font color=#1a73e8>作者：</font>** Hengyuan Xu, Wei Cheng, Yumeng Ji 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Explicit visual intermediates can help multimodal large language models (MLLMs) externalize spatial evidence and updated visual states, but their utility depends on whether an image editor can faithfully realize the required transformation. We introduce \textbf{Aphanta}, an automated task-discovery and closed-loop diagnostic framework for the MLLM -> image editor -> MLLM pipeline. Aphanta evaluates three conditions---direct reasoning, reasoning with an editor-generated intermediate, and reasoning with an idealized reference intermediate---to separate potential visual headroom from the practical utility of current editors. Across 20 candidate tasks and multiple editor--MLLM combinations, we find that utility is strongly task-conditioned. Gains concentrate in visual cue injection, grounding, and counterfactual state realization, whereas intermediates requiring symbol-sensitive construction or structural extrapolation are substantially less reliable. On the selected positive-task subset, our consolidated Qwen pipeline improves the mean task score from 0.343 to 0.445 ($+10.2$ points; $+29.7\%$ relative), while the full study also retains filtered and unsuccessful tasks to expose the boundary. These results position image editing as a specialized visual workspace rather than a universal reasoning mechanism, and establish Aphanta as a reusable protocol for measuring task--representation alignment, editor realization, and downstream pipeline utility.

---


### 162. [MVC-Bench: Benchmarking Calibration of Medical Vision-Language Models](https://arxiv.org/abs/2608.27004)

**<font color=#1a73e8>作者：</font>** Ashshak Sharifdeen, Shihab Aaqil Ahamed, Ufaq Khan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable evaluation of vision-language models (VLMs) and medical vision-language models (Medical-VLMs) requires calibrated confidence, particularly under realistic clinical conditions. However, existing efforts mainly focused on improving accuracy, leaving calibration in the medical domain underexplored. To this end, we propose MVC-Bench, a calibration-centric benchmark for medical image classification with VLMs and Medical-VLMs. MVC-Bench assesses the calibration across three axes: (i) robustness to modality, backbone, and domain shift (ii) effectiveness of calibration strategies and prompt-tuning methods (iii) stability under prompt-template and random-seed variations. The benchmark covers eight different backbones, three medical modalities, including fundus imaging, histopathology, and chest X-ray under in-domain and domain shift settings. It compares post-hoc calibration, train-time calibration, and zero-shot inference methods, together with six prompt-tuning methods. Across more than 1638 controlled experiments, we report accuracy and Expected Calibration Error (ECE) as primary metrics, and further report results with complementary calibration measures, including Maximum Calibration Error (MCE) and Adaptive Calibration Error (ACE). We further investigate the underlying causes of miscalibration in VLMs and Medical-VLMs and propose a simple train-time calibration method, Multi-Class Margin (MCM) regularization, which achieves lowest ECE on 10 out of 12 settings in in-domain and remains competitive under domain shifts. Collectively, MVC-Bench provides a structured evaluation framework and actionable guidance for improving calibration in safety-critical medical workflows.

---


### 163. [Disentangling Optimization Scale from Preference Scale in DPO](https://arxiv.org/abs/2608.27032)

**<font color=#1a73e8>作者：</font>** Ivan Kruzhilov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) is a widely used objective for aligning language models from preference data, with the coefficient $\beta$ commonly interpreted as controlling the KL constraint to a reference policy. We show that $\beta$ entangles two distinct roles: it governs the effective inverse preference-noise scale and simultaneously rescales the optimization dynamics, coupling this scale with the effective step size. As a consequence, at a fixed learning rate the achieved policy deviation is non-monotone in $\beta$: it vanishes in a dead zone at small $\beta$, reaches a peak at an intermediate value, and decreases again for larger $\beta$. Moreover, standard DPO loss values are not comparable across $\beta$: runs with nearly identical loss curves can differ several-fold in KL divergence from the reference model. This entanglement obscures the role of $\beta$, increases sensitivity to hyperparameter choices, and complicates learning-rate scheduling. We propose a centered-softplus reformulation that is argmin-equivalent to DPO for $\beta>0$, while making the inverse preference-noise-scale and learning-rate effects explicit and independently tunable. The normalized centered-softplus objective also admits a continuous $\beta\to0$ endpoint that reduces to a linear preference-margin objective.

---


### 164. [Reasoning about In-Context Samples for Machine-Translation](https://arxiv.org/abs/2608.27036)

**<font color=#1a73e8>作者：</font>** Maxime Bouthors, Josep Crego, François Yvon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can be trained to perform chain-of-thoughts reasoning in order to improve the reliability of their responses. In this work, we investigate how explicit reasoning can be leveraged for LLM-Based Machine Translation (MT) with in-context samples. We introduce a novel fragment-based reasoning framework in which the model first extracts parallel source-target fragments from retrieved similar exemplars, and uses these fragments as intermediate reasoning traces to produce the final translation. To train our model, we distill silver fragments and drafts from a large teacher model. Our experiments with the Qwen3 model family, over 6 languages, including up to 5 domains per language, demonstrate that fragment-based MT significantly outperforms alternative methods like standard k-shot or basic drafting.

---


### 165. [Cascaded Batch Prompting](https://arxiv.org/abs/2608.27038)

**<font color=#1a73e8>作者：</font>** Sho Hoshino, Peinan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although batch prompting makes large language model inference more efficient by processing multiple instances simultaneously, it suffers from unpredictable downstream task performance. We propose cascaded batch prompting, a two-stage approach designed to resolve the unpredictability of conventional batch prompting by disentangling complex reasoning from symbol grounding. Experiments on multiple-choice question answering and natural language inference demonstrate that the proposed method outperforms the standard single prompting baseline while achieving a speedup proportional to batch size, establishing a new state of the art on the Pareto frontier.

---


### 166. [Omni-Interactive Universal Embedder](https://arxiv.org/abs/2608.27044)

**<font color=#1a73e8>作者：</font>** Wei-Yao Wang, Kazuya Tateishi, Shuyang Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal representation learning has been shifting from traditional two-tower architectures to large language model (LLM)-based embedders due to their strong instruction-following capabilities. Despite this progress, existing approaches primarily focus on language and image modalities, which also remain the dominant modalities for user-conditioned interactions in current embedders. In this paper, we propose the first Omni-Interactive Universal Embedder (OmniUE), which not only learns a unified embedding space across text, video, and audio by leveraging intermediate-layer representations from dedicated learnable tokens, but also supports omni-interactive querying, enabling users to provide inputs in the form of text, visual regions of interest, and audio spans. Within OmniUE, visual and audio segmenters process diverse user interactions and integrate them with an omni-LLM to produce user-conditioned any-to-any embeddings via context aggregation. To evaluate OmniUE's omni-interactive capabilities, we introduce OmniCHOIR, benchmarking models for omni-interactive compositional audio retrieval based on the given text, video, and audio as well as unimodal or multimodal interaction prompts. OmniUE consistently surpasses state-of-the-art baselines across diverse modalities, with average improvements of 10.5% on textual-interactive video benchmarks (MMEB-v2-video), 1.1% on audio tasks (MAEB), 83.7% on visual-interactive benchmarks (SCaR), and 24.1% on our omni-interactive OmniCHOIR benchmark. We believe that jointly advancing omni-modal representation learning and omni-interactive querying paves the way toward universal embedders.

---


### 167. [Performance Foundations of Parallel & Distributed Reasoning Language Models](https://arxiv.org/abs/2608.27046)

**<font color=#1a73e8>作者：</font>** Maciej Besta, Leonard Schmidt, Lara Nonino 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) and other RL-style post-training paradigms have been used for aligning large language models (LLMs) with reasoning standards. The resulting recent Reasoning Language Models (RLMs) such as DeepSeek-R1, o3, and Kimi k1.5 show that such RL-style post-training ("RL-for-LLMs") can substantially improve chain-of-thought reasoning, long-horizon planning, and self-correction. However, the computational footprint of these systems is massive: state-of-the-art RLM training requires millions of GPU-hours and tightly coupled multi-model pipelines that stress modern hardware far beyond classical supervised LLM training. This makes RLM training as much a parallel and distributed systems problem as an algorithmic one. In this work, to facilitate developing RLMs that are simultaneously high-performance, scalable, and cost-effective, we first systematize the RL-for-LLM paradigm and provide a compute-centric analysis of prominent post-training algorithmic frameworks: Proximal Policy Optimization (PPO), Group Relative Policy Optimization (GRPO), as well as their variants. Second, we develop a taxonomy of intra- and inter-model parallelism strategies for RL-for-LLMs, covering both traditional techniques (data, tensor, pipeline, sequence, context, and expert parallelism) as well as novel forms of parallelism and optimization techniques for multi-model RLM training, for example disaggregated placement, stage fusion, hybrid parallelism, and asynchronous execution. We harness the work-depth model of parallel computing to make our taxonomy and its insights rigorous and portable. Finally, we analyze existing RLM frameworks and we distill practical guidelines and outline open research directions for building scalable, fast, and cost-effective RLMs.

---


### 168. [Research Design Tracking and Assessment for the Social Sciences](https://arxiv.org/abs/2608.27049)

**<font color=#1a73e8>作者：</font>** Marco Rovera, Sergiu Burlacu, Dominique Cappelletti 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable assessment of causal research designs in the social sciences is critical for evidence-based policy-making, yet has so far relied entirely on manual expert analysis. We introduce Automated Research Design Tracking and Assessment (ARDTrA), a task that involves detecting the research design used in a paper and assessing the quality of its application. We create an expert-annotated dataset of papers covering six families of counterfactual research designs and evaluate the task using a multi-turn RAG-based conversational pipeline. Across four retrieval strategies, four LLMs and six embedding models, we find that passage length is the main driver of performance, explaining 52-66% of the variance. A per-research-design analysis also shows that human and machine difficulty do not align: the designs that prove hardest for the system are not those on which expert annotators disagree most, pointing to two independent sources of task difficulty.

---


### 169. [Video-OPSD: Exploiting Privileged Visual Evidence for On-Policy Self-Distillation in Video Large Language Models](https://arxiv.org/abs/2608.27065)

**<font color=#1a73e8>作者：</font>** Ziyue Wang, Shiqi Huang, Weiwen Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) has recently emerged as an effective post-training paradigm that improves policy optimization through dense token-level supervision from a privileged self-teacher. Despite its promise, OPSD remains largely underexplored for Video Large Language Models (Video-LLMs). Existing methods typically construct privileged teachers by augmenting their context with additional information while keeping the primary input unchanged for both teacher and student. Video reasoning, however, offers a distinct source of privileged supervision within the primary input itself: long videos contain substantial temporal redundancy, and only a small subset of frames provides the evidence necessary to answer a question. Building on this observation, we present $\textbf{Video-OPSD}$, an OPSD framework that exploits privileged visual evidence for both self-teacher construction and knowledge transfer. First, our Evidence-Grounded Self-Teacher conditions the teacher exclusively on annotated evidence frames while the student continues to reason over the complete video. This focused visual input enables the teacher to provide more informative supervision. Second, our Evidence-Guided Token Optimization adaptively weights token-level distillation according to each reasoning token's reliance on privileged visual evidence, thereby emphasizing perceptually grounded reasoning. Experiments across video understanding and reasoning benchmarks show that $\textbf{Video-OPSD}$ consistently improves upon Standard OPSD across multiple backbones and achieves performance comparable to GRPO while requiring substantially less training time, establishing an effective and efficient post-training approach for Video-LLMs.

---


### 170. [Unifying Detection and Adaptation in Task-Free Continual Learning](https://arxiv.org/abs/2608.27070)

**<font color=#1a73e8>作者：</font>** Dezheng Han, Anbang Zhang, Zhihao Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To mitigate catastrophic forgetting in downstream continual learning (CL) for large language models (LLMs), existing methods typically constrain parameter updates or introduce task-specific adaptation modules. However, these methods often rely on explicit task boundaries during training, limiting their applicability to realistic task-free scenarios. In this paper, we propose a \textbf{Fi}sher-guided \textbf{uni}fied (\textbf{FiUni}) framework for batch-level task detection and parameter-efficient continual adaptation. FiUni is motivated by a key observation about the Fisher information matrix (FIM) of pre-trained models: the orthogonality among the principal subspaces of its Kronecker-Factored Approximate Curvature (K-FAC) approximation, estimated from a small number of downstream task samples, can reflect the similarity between different tasks. Based on this observation, FiUni constructs FIM-derived frozen subspaces to guide low-rank adaptation (LoRA), while matching the Fisher principal subspace of each incoming batch window with historical subspaces. This enables FiUni to adaptively determine whether to reuse existing knowledge, expand a related subspace, or create a new subspace, dynamically balancing knowledge sharing and task isolation. Experiments show that FiUni can effectively infer latent batch-level task affiliations and achieve competitive performance against advanced task-aware CL methods with fewer trainable parameters.

---


### 171. [pro-team at LLMs4OL 2026 Tasks Flagship and Reuse: Retrieval-Augmented Generation and Vocabulary-Constrained Filtering for Ontology Learning](https://arxiv.org/abs/2608.27101)

**<font color=#1a73e8>作者：</font>** Shivam Mishra, Dhannu Ram Meena, Muneendra Ojha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ontology learning from text remains challenging despite significant progress in Large Language Models (LLMs), which can hallucinate domain terms, produce inconsistent formats, and favor hierarchical over associative relations. In the LLMs4OL 2026 Challenge, we address both the End-to-End Flagship Task (Task A) and Ontology Extension Reuse Task (Task B) using an offline retrieval-augmented few-shot prompting pipeline. Our system employs Qwen2.5-14B-Instruct with all-MiniLM-L6-v2 for demonstration retrieval, selecting the top-5 examples for Task A and top-2 for Task B. A left-truncated context-windowing strategy preserves task instructions within long prompts. For Task B, generated triples undergo deterministic vocabulary-constrained filtering, retaining triples when at least one endpoint belongs to the sample's closed term/type vocabulary and removing duplicates of the initial ontology. The approach achieves Semantic Graph Similarity of 0.8692, Term-Typing F1 of 0.9200, and Taxonomy Discovery F1 of 0.8540 on Task B, while Task A achieves 0.7416 Semantic Graph Similarity. However, no non-taxonomic relations are extracted, highlighting limitations of closed, taxonomy-oriented relation vocabularies.

---


### 172. [LAAF: A Layered Accountability Architecture Framework for LLM Applications](https://arxiv.org/abs/2608.27102)

**<font color=#1a73e8>作者：</font>** Prachi Chaturvedi, Shahnawaz Ahmad, Ehsan Nowroozi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) operate in hospitals, courtrooms, banks, and public service desks, where fluent, confident outputs are treated as authoritative even when ungrounded or incorrect. When such an output contributes to harm, who is answerable, and through what mechanisms can responsibility be traced, explained, and acted upon? Following PRISMA guidance, five databases were searched from January 2022 to March 2026 against four review questions; of 4,512 records identified, 122 primary studies were included, together with 12 regulatory and standards documents analysed as primary sources. The review consolidates a sociotechnical account of accountability as an actor-forum relation resolved into five dimensions, and synthesises mechanisms across four families: technical controls, human oversight, organisational governance, and documentation and traceability, each with a maturity assessment. The corpus is read through a four-layer classification device spanning provenance, application logic, human oversight, and governance and redress, cross-cut by traceability, role clarity, and continuous monitoring. Both are mapped onto the EU AI Act, whose high-risk obligations have applied since 2 August 2026, the NIST AI RMF with its Generative AI Profile, ISO/IEC 42001, and sectoral guidance in healthcare, consumer finance, education, and the public sector. Four persistent gaps emerge: under-specification of human oversight, absence of shared accountability metrics, disciplinary disconnection, and limited empirical evaluation, alongside five structural tensions that no surveyed instrument resolves. The review closes by consolidating the classification device into an integrated accountability architecture, LAAF, with cybersecurity aligned to the OWASP LLM Top 10 (2025); it is a synthesis of the surveyed evidence rather than a validated artefact.

---


### 173. [DocTalkBN: A Novel Dataset of Expert Telemedicine Conversations in Bengali](https://arxiv.org/abs/2608.27110)

**<font color=#1a73e8>作者：</font>** Anik Saha, Fahmida Sultana Naznin, Sadatul Islam Sadi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable medical conversational AI requires authentic expert--patient interaction data, yet such datasets remain scarce, especially for low-resource languages such as Bengali. We present DocTalkBN, a large-scale multimodal dataset of real-world expert telemedicine conversations in Bengali, collected from nationally broadcast telemedicine programs featuring board-certified physicians. DocTalkBN contains 557.63 hours of paired audio and text, 1,515 multi-turn patient calls, 10,274 host--doctor question--answer exchanges, totaling 1.7M tokens, spanning 26 medical specialties. Unlike prior resources derived from medical forums, written health content, or synthetic data, our dataset preserves the spontaneity, contextual richness, and spoken characteristics of authentic medical interactions in a low-resource setting. To support benchmark-driven research, we further construct three downstream tasks from the corpus, medical triage classification, advice safety evaluation, and medical named entity recognition, and benchmark a diverse set of large language models and encoder-based baselines. Our results show that DocTalkBN is a practically useful resource, particularly for clinically grounded reasoning tasks. We release this resource to facilitate future research on reliable medical NLP and safer, more culturally grounded healthcare systems for low-resource languages. Our source codes and dataset are publicly available at this https URL.

---


### 174. [Cross-Lingual Alignment Without Joint Training: Do Monolingual Language Models Converge on Universal Representations?](https://arxiv.org/abs/2608.27115)

**<font color=#1a73e8>作者：</font>** Ej Zhou, Suchir Salhan, Catherine Arnett 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual alignment in multilingual language models is typically attributed to joint training: shared parameters, mixed-language batches, or explicit alignment objectives. We ask whether monolingual models trained on non-parallel data learn alignable representations without joint training. By testing on strictly monolingual language models, such as the Goldfish model families and independently developed models from different research labs, we find three results. Correlation: these models develop alignable representational geometry across layers, with alignment strengthening as data scale, model scale, or linguistic proximity increases. Construction: a single Procrustes rotation fit on parallel sentences maps hidden states between models. Causation: the same rotation transfers functional content; patching a rotated English residual into a German model on a factual cloze flips the prediction to the donor's capital in most cases. We confirm that cross-lingual alignment can emerge from the structure of language and the information it carries rather than from joint training, and this points to practical future directions including model stitching, merging, and modular multilingual systems built from monolingual components.

---


### 175. [TransMeme: A Multi-Agent Framework for Cross-Cultural Meme Transcreation](https://arxiv.org/abs/2608.27127)

**<font color=#1a73e8>作者：</font>** Jingyi Zheng, Yule Liu, Zifan Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Internet memes are a pervasive form of multimodal online communication; however, such communication often involves users from diverse linguistic and cultural backgrounds. Therefore, adapting memes across cultures and languages is a central challenge for enabling mutual understanding in online communication. Unlike ordinary translation or standalone text rewriting, cross-cultural meme transcreation must jointly preserve communicative intent, adapt culture-dependent meaning for the target audience, and maintain coherence between text and image. In this work, we first provide an explicit task analysis of cross-cultural meme transcreation and identify three core challenges: culture-specific knowledge understanding, intent and tone preservation, and multimodal consistency. Based on this analysis, we propose a multi-agent framework with specialized agents that are coordinated to address these challenges through cultural adaptation, target text rewriting, revision, and conditional visual adjustment. The framework strengthens target text adaptation with coordinated feedback to handle difficult cases that require deeper cultural or visual intervention. We evaluate the framework on bidirectional Chinese-English meme transcreation using both human evaluation and LLM-as-a-Judge. Our method consistently outperforms all baselines across both evaluation settings. In human evaluation, it achieves the best performance on all four dimensions and delivers a 33.1% average improvement over the strongest baseline, while in LLM-as-a-Judge, it attains the highest Top-1 ranking rate (60% versus 26% for the second-best baseline). Further analysis indicates that each component contributes to the performance. Our error analysis suggests that the remaining bottlenecks lie in humor reconstruction and image-text alignment rather than simple cultural knowledge gaps, pointing to future work on humor transfer.

---


### 176. [TwinKV: A Composable Repair Pass for KV Cache Eviction via Pairwise Key Redundancy](https://arxiv.org/abs/2608.27128)

**<font color=#1a73e8>作者：</font>** Hong Chen, Yudong Zeng, Yongwei Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context inference is bottlenecked by the memory footprint of the key-value (KV) cache, especially for small models under tight resource budgets. Existing KV cache eviction methods score tokens using the model's attention distribution or, in attention-free variants, each key's distance from a global reference point. Using a controlled leave-one-out probe, we find that attention magnitude is unrelated to a token's causal contribution to the answer (Spearman $\rho=-0.004$), challenging the premise behind dominant eviction methods. We introduce TwinKV, a training-free, attention-free redundancy signal that detects whether a token's key has a near-duplicate elsewhere in context. Rather than replacing existing policies, TwinKV acts as a composable repair pass: given a policy's fixed retained set, it identifies evicted tokens with no surviving duplicate (\emph{orphans}) and retained tokens whose information is duplicated elsewhere (\emph{redundant donors}), then swaps them while preserving the original budget and scoring rule. We compose TwinKV with four recent eviction policies across LongBench, LooGLE, RULER, and a short-context MMLU-Pro no-harm control at compression ratios ${0.3,0.5,0.7}$. On Qwen3-4B, TwinKV improves a majority of configurations for two policies, is near-even for a third, and helps only a minority for a fourth adaptive baseline already near a performance ceiling; gains across the three non-ceiling policies are smallest at the loosest ratio. On RULER with Llama-3.2-1B, however, that fourth policy improves in every evaluated cell because its Alone score leaves substantial room to improve. More broadly, Llama-3.2-1B shows a smaller average LongBench gain but a higher fraction of improved cells on LongBench and LooGLE than Qwen3-4B, plus a clean RULER win. We also identify few-shot classification exemplars as a task structure where TwinKV does not help on either model.

---


### 177. [Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents](https://arxiv.org/abs/2608.27141)

**<font color=#1a73e8>作者：</font>** Chenhao Wu, Haoxuan Jia, Yang Liu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model agents are increasingly deployed as autonomous loops. Starting from one human goal, such a system repeatedly discovers work, plans, executes tool calls, verifies outcomes and persists state across many unattended iterations. The agent safeguards in wide use, however, are defined over a single trajectory, and their safety state is re-initialized when the next trajectory begins. We show that this is a failure of composition rather than an implementation detail. Our central result is a separation: against an attack whose evidence is fragmented across several iterations, every trajectory-scoped monitor has a true-positive rate equal to its false-positive rate, however expressive it is, because the evidence it would need never appears in the window it sees, whereas a monitor retaining cross-iteration state separates the two perfectly. We further show that the obvious repair of carrying a geometrically decaying risk score is insufficient, because the cooling-off period a patient adversary must wait is a constant that does not grow with the horizon $N$. We then present LoopHarness, which restores a persistent, non-decaying safety state at the loop level. Under mediated commits and an arbiter detection floor $\delta_M$, it bounds the expected number of unauthorized irreversible actions by $B+m-1+m/\delta_M$, a constant in $N$, of which the $B+m-1$ term is decided by a model-free rule and therefore survives a fully colluding verifier. We give a complete evaluation protocol on native Agent-SafetyBench tasks with paired clean and attacked episodes, an outer-state attack suite whose decisive evidence exists only across iterations, per-module ablations, and an adaptive white-box red team.

---


### 178. [GRAIN: Bridging Name and Narrative Shifts in Real-World Graph Reasoning through Invariance-Rewarded Agentic RL](https://arxiv.org/abs/2608.27142)

**<font color=#1a73e8>作者：</font>** Zike Yuan, Han Zhang, Jianzhi Yan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite their potential in standardized graph tasks, Large Language Models (LLMs) remain brittle to real-world shifts in node identifiers and task formulation. While deterministic graph tools are invariant to such shifts, extracting topological structures from noisy text is highly fragile for LLMs, which often overfit to surface patterns. Moreover, mitigating these parsing failures via multi-agent systems incurs prohibitive latency. To address this, we propose GRAIN, a single-agent framework optimized via reinforcement learning. GRAIN models reasoning as a semantic parsing and tool-execution pipeline, guided by a Structure Invariance Reward. By validating extracted intermediate graphs against ground-truth topologies, this reward forces the LLM to learn robust text-to-structure mappings rather than memorizing linguistic artifacts. We also introduce GRIT, a benchmark evaluating sensitivity to such linguistic shifts. GRAIN outperforms multi-agent baselines by 16.45\% in accuracy with approximately 24\% lower latency. Furthermore, it demonstrates superior structural generalization, halving the out-of-distribution (OOD) gap of SFT models (from 15.77\% to 7.80\%) and maintaining robustness on large-scale graphs beyond the training distribution.

---


### 179. [When Tool Outputs Become Commands: Separating Action Induction from Runtime Authorization in Tool-Augmented LLM Agents](https://arxiv.org/abs/2608.27146)

**<font color=#1a73e8>作者：</font>** Xiaokun Guo, Zhen Xu, Dongdong Huo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented LLM agents must rely on untrusted runtime Observations to complete open-ended tasks; however, when tool outputs no longer merely provide data but begin to specify concrete actions, they effectively become ``commands'' that can drive real-world side effects beyond user intent. We argue that this risk arises from conflating action induction with execution authorization. To address this distinction, we propose SARA, which treats action induction and execution authorization as distinct runtime roles and separates action provenance from execution authority. On the Observation side, a context-isolated Action Probe exposes action-inducing semantics and persistently records action-origin provenance across steps as a review signal; on the execution side, actual tool calls are authorized only against the user objective and audited evidence from authorized successful executions, while satisfying goal, execution-chain, and argument-level support. To preserve this separation across multi-step execution, SARA applies No-History-Promotion to prevent historical recurrence from laundering action origins into execution authority. Across AgentDojo and AgentDyn, SARA limits ASR to no more than \(0.63\%\) across four primary evaluation settings while maintaining competitive task utility, and consistently reduces ASR across additional Agent backbones.

---


### 180. [ReViCo: Unveiling the Limitations of VLMs in Visual Text Understanding via Error Correction](https://arxiv.org/abs/2608.27154)

**<font color=#1a73e8>作者：</font>** Bojun Zhang, Junhong Liang, Feifei Zhai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) have shown great success in general visual tasks, yet they still struggle to deeply understand text within images. In this paper, we introduce ReViCo (Real Visual Correction), a benchmark designed to evaluate VLM text understanding through a novel task of visual text error correction. ReViCo challenges models to identify and fix text errors in real-world images, which requires a profound understanding of the interplay between visual text and its surrounding visual context. We benchmark various VLMs using two distinct paradigms: prompt-based strategy and targeted model training, both aimed at pushing the limits of current models. Our experiments reveal a striking performance gap between even the best VLMs and human, and further analysis also shows that most models struggle to accurately perceive the visual text, resulting in frequent correction errors. By highlighting these gaps, ReViCo provides a new benchmark foundation for developing more robust and text-aware VLMs.

---


### 181. [STAR : Sentence Translation Alignment Rate for Document-to-Document Machine Translation](https://arxiv.org/abs/2608.27161)

**<font color=#1a73e8>作者：</font>** Yichen Dong, Hao Wang, Junhui Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have enabled a shift from sentence-level to document-to-document (Doc2Doc) machine translation, promising improved global coherence. However, document-to-document generation in a single pass frequently suffers from structural misalignment, manifesting as sentence omissions or hallucinations that violate the core requirement of source-target correspondence. To address this, we introduce Sentence Translation Alignment Rate (STAR), an auxiliary metric that explicitly quantifies sentence-level structural fidelity. Building on this, we propose STAR-masked Preference Optimization (StarPO), a framework that ranks document-level hypotheses by structural quality and utilizes a dynamic alignment mask to focus optimization on misaligned segments. Experimental results across news and literary domains demonstrate that StarPO significantly enhances translation quality and structural integrity. Notably, StarPO allows compact models to surpass the performance of massive proprietary systems like GPT-4o while maintaining superior token efficiency.

---


### 182. [Prediction of Prediction (PoP): Inter-Layer Activation Fusion for Single-Pass Hallucination Detection in Large Language Models](https://arxiv.org/abs/2608.27165)

**<font color=#1a73e8>作者：</font>** Himal Badu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive large language models (LLMs) routinely generate factually incorrect outputs with high decoding confidence, limiting their deployment in high-stakes workflows. Existing output-stage uncertainty metrics can fail when models are overconfident on false assertions, while multi-sample verification pipelines introduce substantial memory and latency overhead. This work evaluates whether internal hidden-state transition dynamics during generation can signal factual errors without auxiliary decoding calls. We introduce Prediction of Prediction (PoP), a mechanism that captures layer-transition uncertainty by fusing intermediate hidden representations across depth during a single forward pass. Evaluated on the TruthfulQA benchmark using autoregressive transformer backbones, PoP achieves an area under the receiver operating characteristic curve (AUROC) of 75.5% for factual-correctness classification. The mechanism operates within the base forward pass, adding less than 1.2% runtime latency and requiring zero additional generation passes. The numerical results are reported from the author-verified experimental implementation and are bounded by the evaluation scope described below.

---


### 183. [Calibrated Enough to Know, Not Calibrated to Act: Fabricated Evidence Makes LLM Agents Commit to the Unknowable](https://arxiv.org/abs/2608.27167)

**<font color=#1a73e8>作者：</font>** Pranav Aggarwal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An LLM agent shown a professional-looking market panel commits to a directional call on a provably unpredictable question far more often than one asked the bare question: across 12 frontier models, commitment rises from 6.5% to 54.0% as evidence is escalated. It commits just as readily when every number on the panel is invented: fabricating the entire display, so nothing the model can see is true except the question itself, still lifts commitment from 24.5% to 36.8%, statistically indistinguishable from the 37.6% produced by genuine market data. What unlocks confident action is not information but the authority of its packaging. The failure is narrow and locatable. Incapacity is not the answer: on matched answerable questions attached to the same panels, the same models answer essentially always, at near-perfect accuracy. Nor is it belief - stated probabilities barely move across the gradient that swings action by 48 points, and score worse than a climatological baseline. Missing judgment isn't it either: asked to classify a question's knowability before acting, models call it irreducible 90% of the time and then commit on just 0.4% of those. The act/don't-act gate is what fails, and the effect is concentrated in a few models rather than universal. Because the gate is separable, it can be trained. Supervised fine-tuning of a 3B model on 540 synthetic cases, predominantly dice, coins, jars and timers, drives commitment to 0.0% on the original cases and transfers to three unseen domains. It does not survive everything: the gate holds exactly when the response format leaves room to reason, and rigid formats that remove that room leave the model confident and wrong on questions it otherwise answers correctly. The gate is trainable and context-fragile, and deployment needs both halves of that sentence.

---


### 184. [Ancient-Bench: A Comprehensive Multi-millennial, Multi-medium, and Multi-script Benchmark for Ancient Chinese Artifact Text Recognition](https://arxiv.org/abs/2608.27169)

**<font color=#1a73e8>作者：</font>** Hiuyi Cheng, Nuo Xu, Yuyi Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ancient Chinese artifact text recognition is fundamental to heritage digitization, and benchmarks for ancient texts are essential for evaluating current model capabilities. However, existing benchmarks suffer from ''fragmentation'', manifested in limited temporal coverage, limited medium diversity, and incomplete script types. Therefore, we present Ancient-Bench, a comprehensive benchmark of 2,700 images for ancient Chinese artifact text recognition, featuring three dimensions: Multi-millennial (spanning 3,000 years of character evolution), Multi-medium (covering nine artifact categories), and Multi-script (encompassing seven historical script forms). To enable consistent and fair evaluation across heterogeneous media, we further define three annotation standards tailored to the medium-specific characteristics of ancient texts: symbol standardization, character standardization, and parsing standardization. Extensive experiments on Ancient-Bench covering general Vision-Language Models (VLMs) and OCR-specialist models reveal that ancient Chinese artifact text recognition remains fundamentally unsolved, with persistent challenges in variant characters, specialized symbols, and hallucination. The dataset is available at this https URL.

---


### 185. [X-WAD: eXplainable Web Anomaly Detection](https://arxiv.org/abs/2608.27172)

**<font color=#1a73e8>作者：</font>** Matteo Bitussi, Roberto Doriguzzi-Corin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid growth of web-based services, particularly API-driven architectures, reflects an increasing reliance on distributed systems, exposing sensitive data to security risks and making the adoption of automated defensive mechanisms essential. In this context, where benign traffic predominates in real-world settings, modern defenses increasingly model normal behavior, relying on semi-supervised approaches trained on only normal data. However, ensuring the complete absence of anomalous instances in such training data is inherently difficult in practice, and mislabeled or contaminated attack samples can introduce backdoors into the learned defense, causing the model to silently misclassify certain attack patterns as normal behavior. This paper investigates the effectiveness of Transformer-based Language Models (TLMs) in the detection of anomalies in HTTP requests, focussing on providing detailed explanations for the detected anomalies. The study employs token-level logit-based surprisal mapping to provide both an anomaly score and a direct, detailed explanation via heatmap-like highlighting. The effectiveness of the proposed explainability approach is demonstrated by the discovery of labelling inconsistencies in a popular public dataset, revealing how anomalous contamination in the training data had induced backdoor-like failures in the detection models.

---


### 186. [When Text Misleads: Inconsistent-Aware Reasoning for Audio-Grounded Dialogue](https://arxiv.org/abs/2608.27176)

**<font color=#1a73e8>作者：</font>** Yen-Ju Lu, Yuzhe Wang, Yaohan Guan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding spoken dialogue requires joint reasoning over lexical content and paralinguistic acoustic signals such as emotion and conversational intent. However, existing evaluations often allow shortcuts based on transcripts or single-modality solutions, obscuring whether models genuinely ground predictions in speech. We formalize this failure mode as cross-modal disagreement, where transcripts suggest plausible but incorrect surface interpretations while acoustic cues such as prosody or speaking style support different answers. We develop a scalable framework that identifies text-biased surface interpretations and converts disagreement regions into conflict QA examples. We also include consistent cases where transcript-based and speech-grounded interpretations agree, enabling evaluation beyond adversarial audio dependence. This results in ContraTalk, a controlled benchmark containing 501 questions across five discourse dimensions: interaction behavior, emotion state, dialogue act, social stance, and conversational intent. We further develop an agentic-style reasoning framework that converts speech into an Audio Twin, a text-readable representation of localized acoustic cues that exposes acoustic evidence to the reasoning model. Experiments show that strong text-only LLMs exceed 90% accuracy in consistent cases but drop to 33-48% in conflict cases. Direct AudioLLMs provide only partial grounding, still selecting the transcript-biased trap in roughly 30-40% of conflict cases. Our Audio Twin framework improves conflict-case accuracy while reducing trap selection, but its consistent-case behavior remains backbone-dependent. These results identify transcript-based shortcuts as an important failure mode in spoken dialogue understanding and show that explicit acoustic evidence aggregation provides a more controllable interface for diagnosing and improving speech-grounded reasoning.

---


### 187. [TraceBench: Controlled Evaluation of LLM Agents for Time-Series Root-Cause Attribution](https://arxiv.org/abs/2608.27182)

**<font color=#1a73e8>作者：</font>** Tommaso Bendinelli, Artur Dox, Christian Holz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly applied to anomaly detection and root-cause analysis in time-series observations collected from real-world systems; however, their performance on these tasks has not been systematically evaluated under controlled conditions. We introduce TraceBench, a simulation-based framework for generating controlled root-cause attribution tasks. In each generated task, an agent receives time-series observations produced by simulating a physical dynamical system and must determine whether a system parameter was altered during the simulation and, if so, which one. Using TraceBench, we generate tasks from three interpretable mechanical systems and systematically evaluate four LLM agents across controlled experimental conditions, yielding new insights into how these agents analyze time-series observations from dynamical systems. Our results show that agents benefit substantially from domain context and explore data primarily through numerical console output rather than visualizations. We also find that agents generally perform worse when required to produce a Python script that maps each time-series sample to a predicted root-cause label than when they submit predictions directly. We release our datasets, agent trajectories, experimental results, and a leaderboard on our website, this http URL.

---


### 188. [Vision-centric generative AI models: A software-hardware perspective](https://arxiv.org/abs/2608.27199)

**<font color=#1a73e8>作者：</font>** Eleni Tselepi, Cristian Sestito, Shady Agwa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision generative artificial intelligence (AI) has emerged as one of the most rapidly advancing areas of deep learning. The explosion of multimodal models has made them widely associated with text-to-image applications running on large datacentres. However, vision generative models are equally needed in applications that operate under strict hardware constraints at the edge, including autonomous vehicles, agricultural sensors, and mobile devices. In this Perspective, we argue that progress in vision generative AI has been driven by output quality, with hardware evolving reactively to accommodate growing model demands. We quantify the parameter cost and energy efficiency of these models across a range of accelerator platforms, and map four generative model families against seven real-world application domains. Finally, we advocate a software-hardware co-design approach, where deployment constraints are considered from the start of the design process, ensuring that the "right model" runs on the "right hardware" to serve the "right application", making generative AI deployment sustainable and accessible across a much broader range of platforms.

---


### 189. [PACE: A Unified Condense-and-Extract Paradigm for Fast VLM Inference](https://arxiv.org/abs/2608.27206)

**<font color=#1a73e8>作者：</font>** Junjie Liu, Shengyuan Ye, Xu Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) demonstrate exceptional visual reasoning capabilities, yet their inference costs escalate rapidly with the proliferation of visual tokens. Existing visual token pruning methods exhibit two fundamental limitations. First, most approaches operate exclusively post-vision encoder, leaving the substantial latency of the visual encoding phase unoptimized. Second, under strict token budgets, these methods often fail to jointly preserve holistic visual contexts and fine-grained details, leading to performance degradation. To address these bottlenecks, we propose PACE (Pixel-Adaptive Condense and Extract), a training-free inference framework that accelerates both the vision encoder and the Large Language Model (LLM) via a unified Condense-and-Extract paradigm. During the Condense stage, an Adaptive Pixel Compressor (APC) evaluates visual information density prior to encoding, adaptively downsampling redundant inputs, curtailing encoder computation while preserving global context and essential visual cues. In the Extract stage, a Dynamic Dual-Attention Extractor (DDAE) selectively retains visual tokens via a fusion of internal visual signals from the encoder and semantic signals from the LLM, safeguarding task-critical details. By integrating PACE into Qwen2.5-VL-7B, the model retains 93.8% of its original performance while utilizing only 10% of the visual tokens, yielding a 3.1x speedup in time to first token (TTFT). Our code is available at this https URL.

---


### 190. [BALMS: Benchmarking Agentic LLMs for Longitudinal Mental Health Sensing](https://arxiv.org/abs/2608.27219)

**<font color=#1a73e8>作者：</font>** Yu Yvonne Wu, Arvind Pillai, Yuliang Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mental health assessment relies on episodic self-report scales, which convert subjective states such as stress into numerical scores but provide only sparse snapshots of wellbeing. Wearable devices offer longitudinal behavioral and physiological signals for continuous, low-burden monitoring. Recent LLM-driven personal-health agents enable natural language queries over wearable signals, but mainly handle short-term, retrieval-based lookups (e.g., highest step count over a week). They do not evaluate whether agents can reason over long-term signals to predict wellbeing scores paired with evidence-grounded rationales. To address this gap, we introduce BALMS, the first systematic benchmark of LLM-based agentic systems for longitudinal mental health sensing. BALMS spans 3 real-world longitudinal datasets, 2 task families (closed-form wellbeing-score prediction and rationale generation auto-graded by an LLM-as-Judge), 3 agentic paradigms evaluated across 5 open- and closed-source LLM backbones. We find that zero-shot agents rarely outperform a simple mean baseline, except with stronger backbones or compact, semantically meaningful features. Chain-of-thought prompting improves reasoning-oriented backbones, but does not guarantee temporal grounding or numerical correctness. Together with more analysis on efficiency and temporal scaling, BALMS highlights the need for longitudinal mental health agents that selectively retrieve history, ground temporal evidence, and reason over interpretable behavioral features.

---


### 191. [SPA: Securing Persistent LLM Agents Across Queries with Plan-First Information-Flow Control](https://arxiv.org/abs/2608.27234)

**<font color=#1a73e8>作者：</font>** Dylan Girrens, Guangjing Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly operate over untrusted webpages, documents, tools, and persistent states while exercising authority over security-sensitive resources. Existing defenses typically protect either planning or individual tool interactions, but persistent agents face a broader threat: attacker-controlled data can alter control flow, enter security-sensitive tool arguments, or compromise later queries. We present SPA, a plan-first architecture that secures planning, execution, and cross-query state reuse. SPA invokes the planner once per query to generate a complete executable plan in a declarative domain-specific language, then applies dual-lattice information-flow control to track confidentiality and integrity across explicit data flows and control dependencies. To support persistence without re-exposing untrusted payloads to the planner, SPA stores execution results as labeled artifacts and reveals only semantic metadata during later planning. We evaluate SPA on AgentDojo and AgentDojo-MQ, which is our multi-query extension for measuring secure state reuse and delayed attacks. Under the 'tool_knowledge' attack, SPA with information-flow control reduces attack success to zero on AgentDojo and 0.2% on AgentDojo-MQ. Our results show that plan-first execution combined with label-preserving persistence can substantially strengthen persistent LLM agents, while revealing an important security-utility tradeoff introduced by strict integrity enforcement.

---


### 192. [What Makes Good Agentic Data? An ACE Lens on Data Generation for LLM Agents](https://arxiv.org/abs/2608.27260)

**<font color=#1a73e8>作者：</font>** Xingshan Zeng, Zishan Xu, Boju Zhang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on generated interaction data to learn how to interact with external environments. Agentic data generation must maintain consistency among environments, tasks, interactions, and success signals while producing experience that is useful rather than merely abundant. Existing work spans many agent domains, but domain-centered organization and heterogeneous evaluation often obscure common generation mechanisms and conflate candidate construction with verification and selection. This work develops a two-level framework for the field. First, we represent agentic data as a common factorized object $(E,q,\tau,v)$, comprising an environment specification, task signal, interaction realization, and optional verifier. We organize generation paradigms by their primary anchor and dependency structure. Second, we formulate generation as constrained distribution design through the Accuracy-Complexity-divErsity (ACE) lens. Accuracy establishes the feasible support of grounded and internally consistent data. Within this support, Complexity places learning mass relative to the capability of a declared learner and execution configuration, while divErsity controls coverage and redundancy of data. Using this framework, we explore how prior work verifies generated experience, constructs and calibrates difficulty, and expands behavioral coverage. The literature reveals a shift toward execution-grounded accuracy, learner-relative complexity, and diversity beyond surface variation or dataset size. We further discuss broader directions and emerging trends in agentic data generation through the ACE lens, including their implications for scaling, data sources, training regimes and adaptive learning. Overall, the central challenge is not simply to generate more data, but to continually allocate valid, informative, and non-redundant experience as agents and environments evolve.

---


### 193. [SCIT: Testing Causal Cache Carriers in Latent Chain-of-Thought Models](https://arxiv.org/abs/2608.27265)

**<font color=#1a73e8>作者：</font>** Yi Ding, Lijun Huang, Menglin Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Latent chain-of-thought models move intermediate reasoning from emitted text into continuous states, improving compactness but hiding the causal object. We introduce SCIT, the Suffix Cache Interchange Test, a causal protocol that constructs exact source-recipient counterfactuals, patches declared cache segments, and identifies which transformer object carries the counterfactual computation. SCIT combines sufficiency tests with K/V component splits, hidden-state controls, semantic source controls, decoded validation, and matched corruption. On CODI-GPT2 and a Sim-CoT-style GPT-2 reproduction, counterfactual arithmetic transfers primarily through value-cache suffix trajectories rather than hidden states, keys, reusable answer slots, or single-token triggers. Complete sufficiency-and-necessity evidence for the late-value-suffix mechanism holds for the main CODI-GPT2 checkpoint; the Sim-CoT-style checkpoint shows the same sufficiency and decoded-control pattern but insufficient matched-corruption evidence for a necessity call. Beyond these local arithmetic cells, SCIT reveals carrier-regime shifts: arithmetic-like GPT-2/1B cells preserve latent-tail value/KV transfer, whereas competent 8B and repaired non-arithmetic cells route through prompt-prefix or full-cache K/V; boundary cells receive no mechanism call. SCIT therefore contributes a cache-level diagnostic, a checkpoint-specific GPT-2 arithmetic mechanism, and a competence-gated carrier map rather than a universal latent-tail claim.

---


### 194. [BrailleBench: Investigating Multi-Criteria Braille Comprehension in Large Language Models](https://arxiv.org/abs/2608.27268)

**<font color=#1a73e8>作者：</font>** Jinghan Zhang, Fengran Mo, Zhiyu Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although Large language models (LLMs) mediate access to knowledge and computational assistance, their capabilities should benefit vulnerable groups in the same way. However, it is unclear whether existing AI systems are inclusive enough for blind and deafblind users to access the same functionality through Braille, whose indicators, contractions, and digital representations introduce distinct requirements for model comprehension. To this end, we introduce BrailleBench, a benchmark for evaluating LLMs in Braille comprehension from different Criteria. BrailleBench aligns 5,570 instances from five datasets, including mathematics, commonsense, and multi-hop question answering across English and Braille Grades 1 and 2. Different configurations are designed to understand whether the systems can comprehend Braille-authored content, express answers in Braille, and complete end-to-end Braille interaction. To ensure the quality and prevent evaluation bias, the benchmark is built through a deterministic, expert-reviewed pipeline via a self-created Braille Toolkit without using any data instances generated by LLMs. We evaluate six representative LLMs from various aspects. The results reveal a persistent gap between print-English capability and Braille accessibility. Braille understanding and expression are asymmetric, where Grade 2 is especially fragile on the input side compared to Grade 1, and fully Braille requests further reduce performance. The experimental observations provide valuable guidance for the development of future Braille AI systems. All related resources in BrailleBench are publicly available for future research.

---


### 195. [MM-Spectrum: Multimodal Multi-spectral Molecular Structural Elucidation with a Stable MoE Framework](https://arxiv.org/abs/2608.27286)

**<font color=#1a73e8>作者：</font>** Hai-tao Yu, Nan Min, Zheng Fang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring molecular structures from multimodal spectroscopic measurements requires integrating complementary yet highly heterogeneous signals. However, the common paradigm of directly concatenating multispectral sequences can exhibit anomalous performance degradation, primarily due to pronounced heterogeneity and the resulting multimodal imbalance across modalities. As a remedy, we propose MM-Spectrum, a sparse Mixture-of-Experts framework tailored for multimodal multispectral spectra-to-structure elucidation. To better match the information characteristics under multispectral imbalance, MM-Spectrum introduces an explicit modality-aware routing mechanism that exposes spectral identity to the router in addition to token content representations. Moreover, it incorporates shared and interaction experts, together with heterogeneous expert capacities, to extract multispectral modality-unique and cross-modal synergistic information while suppressing noise-induced interference. Across full-modality, bimodal, and missing-modality settings on molecular structural elucidation, MM-Spectrum achieves consistent and substantial improvements, supported by ablation studies and interpretability analyses.

---


### 196. [LLMs Can Design Near-Optimal OR Algorithms](https://arxiv.org/abs/2608.27296)

**<font color=#1a73e8>作者：</font>** Jackie Baek  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We ask whether large language models (LLMs) can design effective algorithms for well-specified operations research (OR) problems. We study inventory control, queueing network control, and assortment optimization. We evaluate two levels of LLM use: at level 1, the model receives one problem instance and returns a solution for that instance; at level 2, it receives only the problem class description and broad parameter ranges, and returns an algorithm that maps instance parameters to solutions. Human input is minimal: we give one untuned prompt that describes the problem, and the model has access to a Python sandbox tool with a fixed compute budget.
The strongest model we test, gpt-5.6-sol, matches or outperforms the best existing method on almost all evaluated instances. This holds even at level 2, where the returned algorithm is fixed before seeing the evaluation instances. Performance also improves sharply across models released less than eight months apart, suggesting that this capability is moving quickly. Thus, for the well-specified operations problems we study, a single untuned LLM query can already produce algorithms competitive with specialized methods. These results suggest that frontier LLMs can be a serious empirical baseline for algorithm design in well-specified OR problems.

---


### 197. [When Context Gets Root: Privilege Escalation in LLM Harnesses](https://arxiv.org/abs/2608.27299)

**<font color=#1a73e8>作者：</font>** Xingbang He, Yuanwei Chen, Yi Qian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Instruction hierarchy is a model-side defense that assigns instructions different levels of privilege according to their sources. These levels constrain which content may direct model behavior. During agent execution, however, agent harnesses construct context for each model invocation. This construction can elevate low-level content to a higher instruction level and grant it greater model-facing privilege. We introduce instruction privilege escalation. In this attack, an attacker induces an agent to elevate low-level malicious content to a higher instruction level. The elevated content then causes the agent to execute instructions it would not follow at their original level. We evaluate this threat by using multi-agent mechanisms to achieve 13 attack objectives across six coding-agent harnesses. These objectives span confidentiality, integrity, availability, and remote code execution. With unrestricted action execution, the attacks achieve all 13 objectives on all six harnesses. Under automatic permission review, the attacks achieve all 13 objectives on all three harnesses that provide this mode. We further reproduce the vulnerability using harness-provided persistent goals and scheduled tasks. These results demonstrate the generality of instruction privilege escalation.

---


### 198. [Difference-in-Differences on a Censored Rating Scale Can Manufacture an Effect: Evidence from a Pre-Registered LLM-Judge Audit](https://arxiv.org/abs/2608.27309)

**<font color=#1a73e8>作者：</font>** Shuyi Fan, Boyuan Deng, Mengyu Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audits of LLM judges certify a bias by contrasting matched conditions, and the strongest designs difference twice: a within-item contrast between two candidate responses, differenced again across a manipulated attribute, read off a bounded rating scale. We show that this endpoint is not identified on the scale that reports it. Each term of the double difference is censored by its own share, so the observed statistic confounds differential preference with differential attenuation: a severity shift common to both responses manufactures an interaction whenever the two censor it unequally, as unequal distances from the bounds make them, exactly where good stimuli place them. We exhibit the failure inside a pre-registered audit of a frozen pedagogy judge, sealed before the first of its 990 calls. The registered primary endpoint, the effect of a stated learner profile on the judge's scaffolding preference, is null: $+0.085$ points (95\% BCa $[-0.167, +0.353]$, $p = 0.684$). The audit's one nominally significant interaction, $+0.378$ ($p = 0.002$), is not identified as preference: a construction containing zero differential preference reproduces 79 to 85\% of it from the observed severity shift and the scale floor alone. We derive the mechanism in closed form and show that its contribution is measurable from an audit's own ratings.

---


### 199. [Verify Smarter, Evolve Further: Efficient Harness Evolution through Behavior-Aware Verification](https://arxiv.org/abs/2608.27311)

**<font color=#1a73e8>作者：</font>** Jinghan Xu, Yikai Zhang, Aili Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent harnesses shape how language-model agents use instructions, tools, and runtime components, but adapting these harnesses requires costly verification. Existing propose-and-verify methods typically score every candidate on a fixed task set, wasting rollouts on unrelated behaviors and allowing aggregate scores to obscure specific regressions. We introduce HarnessLens, a budget-aware framework for automated harness evolution. HarnessLens jointly explores the task space and user-configurable components, derives candidate modifications from execution trajectories, and selectively verifies each candidate on behavior-relevant tasks using an attributable-evidence gate. Across three agent harnesses and four benchmarks, HarnessLens improves average held-out performance by 7.6-13.6% while consuming substantially less evaluation budget than competing baselines. These results demonstrate that behavior-aware verification with explicit attribution enables more reliable and sample-efficient harness evolution under constrained interaction budgets. Our code is available at this https URL.

---


### 200. [BTS-AgentBench: A Deterministic, Replayable Pipeline from Read-Only Telemetry Logs to Agent Benchmarks](https://arxiv.org/abs/2608.27334)

**<font color=#1a73e8>作者：</font>** Jeong-Yoon Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Industrial sites contain large volumes of read-only telemetry, but few benchmarks specify how to compile these records into executable multi-turn agent tasks. We present a telemetry-to-episode construction method instantiated as BTS-AgentBench. The pipeline normalizes BTS metadata and raw histories into a read-only tool store, compiles static tasks with tool-derived gold answers and evidence, and lifts retained tasks into typed, bounded operator-facing episodes. The 532-row release adds clarification, goal revision, timestamp policy, quality-gated reporting, and evidence attribution while preserving the source computation and split. Coded contract preflight reports zero findings, and the construction-exclusion controller completes 0/532 rows. Two independent raw-to-episode builds match all 11 logical tool-store exports and reproduce the released 356/87/89 train/dev/test artifact exactly. Applying the shared construction path to XAI4HEAT produces 204 episodes; on its 41-row held-out test split, the controller completes 0 rows and the retained GPT-5.5 execution completes all 41. Code, artifacts, and replay reports are available at this https URL.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-231](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
