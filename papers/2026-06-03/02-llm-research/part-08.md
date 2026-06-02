# 🧠 大模型相关研究 | 2026年06月03日

> 本类共 **376** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**351-376**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-376**

---

### 351. [Investigating and Alleviating Harm Amplification in LLM Interactions](https://arxiv.org/abs/2606.02423)

**<font color=#1a73e8>作者：</font>** Ruohao Guo, Wei Xu, Alan Ritter  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can serve as helpful assistants, yet they can equally function as harm amplifiers that enable malicious users to achieve harmful outcomes beyond their capabilities through extended interactions. This risk manifests along two axes, i.e., democratizing domain expertise that allows novices to produce specialized harmful content, and scaling harmful operations at volumes that manual effort cannot match. Existing works, however, often overlook how LLMs compound harm across multi-turn conversations. We introduce HarmAmp, a new benchmark for multi-turn harm amplification scenarios spanning twelve risk categories. Each scenario is grounded in real-world threats and satisfies rigorous criteria, i.e., substantive amplification, operational specificity, and multi-turn necessity. We further propose TrajSafe, a proactive monitor that anticipates harmful trajectories and intervenes through actions such as probing users' genuine intents and steering the models towards safer completion. Our extensive experiments demonstrate that TrajSafe significantly reduces the harmfulness incurred in multi-turn interactions while preserving a low over-refusal rate and the target model's general capabilities. Our work offers a promising paradigm to alleviate the nuanced safety risks in LLM interactions.

---


### 352. [GC-MoE: Genomics-Guided Cell-Type-Specific Mixture of Experts for Histology-Based Single-Cell Spatial Transcriptomics](https://arxiv.org/abs/2606.02424)

**<font color=#1a73e8>作者：</font>** Kaito Shiku, Ahtisham Fazeel Abbasi, Ryoma Bise 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Histology-based single-cell spatial transcriptomics (ST) estimation aims to predict gene expression for individual cells from histopathological images and cell locations, reducing the need for costly single-cell ST measurements. Unlike existing histology-to-ST methods that mainly predict spot-level profiles for local regions containing multiple cells, this task requires modeling cell-to-cell expression variability, which is strongly structured by cell type. We propose Genomics-Guided Cell-Type-Specific Mixture-of-Experts (GC-MoE), which estimates cell-type probabilities with a routing network and softly combines cell-type-specific experts for gene expression prediction. To further encode cell-type-dependent gene programs, we introduce the Cell-Type-Specific Co-Expression-Aware Predictor (CAP), together with a lightweight Cell-to-Cell Interaction Attention (C2CA) module for neighboring-cell context. Experiments and ablations on public single-cell ST datasets show consistent improvements over existing single-cell and adapted spot-level baselines.

---


### 353. [Geometry-Aware Implicit Memory for Video World Models](https://arxiv.org/abs/2606.02436)

**<font color=#1a73e8>作者：</font>** Zhengxuan Wei, Xu Guo, Xinghui Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models aim to simulate controllable visual environments, but long-horizon rollouts depend on what the model remembers after observations leave its native context window. Explicit memories retain frames or online 3D reconstructions, which can suffer from heuristic retrieval errors, redundant appearance storage, or reconstruction artifacts. Implicit memories compress history into a compact state, but existing designs are not explicitly constrained to encode cross-view scene geometry. We propose GIM-World, a geometry-aware implicit memory framework for video world models. A lightweight transformer encoder compresses variable-length history into fixed-size memory tokens, a camera-queryable geometry head distills 3D scene structure from a frozen foundation model into the memory during training, and an information-guided pruning rule keeps encoding cost bounded as history grows. The geometry teacher is discarded at inference, leaving a lightweight memory module. Experiments on MIND show that GIM-World better preserves long-horizon geometric and visual consistency than both explicit- and implicit-memory baselines.

---


### 354. [LLM-Evolved Pattern Generators for Optimal Classical Planning](https://arxiv.org/abs/2606.02438)

**<font color=#1a73e8>作者：</font>** Windy Phung, Dominik Drexler, Arnaud Lequen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learned heuristics have recently become a competitive alternative to traditional domain-independent heuristics for satisficing planning. Existing approaches, however, focus on improving search guidance rather than guaranteeing admissibility, which makes them unsuitable for optimal classical planning. We present the first method for learning domain-dependent heuristics that are admissible by design and thus preserve the optimality guarantees of A* search. Instead of learning a direct mapping from states to heuristic values, we learn to construct abstractions that induce admissible heuristics. We use an LLM-driven evolutionary program-synthesis framework to obtain, for each domain, a program that produces a pattern collection for any task in that domain, and we combine the resulting patterns admissibly via saturated cost partitioning. Empirically, the learned programs encode interpretable domain-specific insights, run with negligible overhead at test time and yield heuristics that match the coverage of state-of-the-art domain-independent baselines on several domains while evaluating each state substantially faster.

---


### 355. [PaSBench-Video: A Streaming Video Benchmark for Proactive Safety Warning](https://arxiv.org/abs/2606.02443)

**<font color=#1a73e8>作者：</font>** Yusong Zhao, Yuejin Xie, Youliang Yuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Between the first visible sign of danger and the moment an accident occurs, there is often a window where intervention remains possible. Video-capable multimodal large language models (MLLMs) could serve as always-on safety monitors that issue warnings during this window. Yet current benchmarks do not test this ability: they rely on static inputs, ignore timing precision, and omit false-positive measurement on safe scenes. We present PaSBench-Video, a 740-video benchmark with 481 risk and 259 no-risk videos across four domains: driving, healthcare, daily life, and industrial production. Risk videos are annotated with frame-level risk onset and accident boundaries. A model must observe the video causally and produce a warning that is both temporally calibrated and content-correct. Testing 13 MLLMs, we find that no model exceeds 20.0% on our strictest metric, and recall is tightly coupled with false-positive rate, with Pearson correlation 0.64: higher detection comes only at the cost of triggering warnings on the majority of safe clips. Performance splits sharply by domain: models achieve moderate recall at low false-positive rates in daily life, where risks are inherently anomalous, yet fire indiscriminately in driving, where routine and hazardous scenes look alike. These results indicate that current models rely on scene-level activity cues rather than reasoning about emerging harm.

---


### 356. [Food Noise & False Safety: A Systematic Evaluation of How LLMs Fail to Adapt to Eating Disorder Queries with Clinician Feedback](https://arxiv.org/abs/2606.02444)

**<font color=#1a73e8>作者：</font>** Giulia Pucci, Emily Hemendinger, Ruizhe Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent evidence shows that people with eating disorders (EDs) are increasingly seeking guidance, advice, and emotional support from Large Language Model (LLM)-based chat systems. Although these systems are not designed to provide clinical advice, their perceived expertise, neutrality and accessibility make them a frequent, albeit risky, source of support. This paper investigates potential patterns of interaction between users with EDs and LLMs, focusing on the potential harms arising from models that uncritically adapt to, and facilitate unsafe or self-harming user requests. We find, in consultation with clinical ED experts, that specific linguistic cues in prompts increase the likelihood of unsafe responses and, through systematically varying the degree of potential risk present in the user prompt, report the extent to which LLMs uncritically adapt to problematic, and potentially dangerous user inputs.

---


### 357. [Active Exploring like a Pigeon: Reinforcing Spatial Reasoning via Agentic Vision-Language Models](https://arxiv.org/abs/2606.02459)

**<font color=#1a73e8>作者：</font>** Wei Deng, Xianlin Zhang, Mengshi Qi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Enabling Vision-Language Models (VLMs) to perform spatial reasoning remains challenging. Existing approaches treat VLMs as passive observers, which is difficult for real-world applications. Moreover, reinforcement learning methods rely on sparse rewards, limiting their effectiveness for complex reasoning tasks. Inspired by pigeons' building and exploiting cognitive maps for navigation, we propose a novel agentic pipeline for spatial reasoning. First, we introduce a new \emph{dynamic cognitive map} parameterizing scene layout as object positions and orientations, serving as persistent memory for new observations. Second, we propose a novel \emph{Spatial Assertion Codes (SAC)}, Python expressions programmatically describing spatial relationships. By collaborating with the dynamic cognitive map, SAC enables verification of intermediate reasoning steps, providing dense reward signals. We optimize the model via supervised and reinforcement finetuning. Experiments on the MindCube benchmark demonstrate state-of-the-art performance with \emph{80.5\%} overall accuracy, outperforming the best current method by \emph{29.5} accuracy points (a relative improvement of \emph{53.2\%}) on the challenging \textsc{Rotation} subset. Our code and data are open-sourced at this https URL.

---


### 358. [MCP-Persona: Benchmarking LLM Agents on Real-World Personal Applications via Environment Simulation](https://arxiv.org/abs/2606.02470)

**<font color=#1a73e8>作者：</font>** Wenhao Wang, Peizhi Niu, Gongyi Zou 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) has emerged as a transformative standard for connecting large language models (LLMs) with external data sources and tools, and has been rapidly adopted across personal applications and development platforms. However, existing benchmarks predominantly focus on generic information-seeking tools and fail to capture the practical challenges posed by personal social applications, where tools interact with individual accounts or local databases. To bridge this critical gap, we introduce MCP-Persona, the first benchmark specifically designed for evaluating agent performance on real-world, personalized MCP tools. MCP-Persona encompasses a diverse set of widely-used applications, ranging from social media platforms like Reddit and Xiaohongshu (Rednote) to enterprise collaboration suites such as Lark (Feishu) and Slack. Our extensive experiments on various state-of-the-art (SOTA) agents demonstrate their significant struggles with personalized tool use, thereby highlighting the benchmark's crucial role in identifying and addressing these limitations. MCP-Persona is publicly available at this https URL}{this https URL.

---


### 359. [Retrieve What's Missing: Coverage-Maximizing Retrieval for Consistent Long Video Generation](https://arxiv.org/abs/2606.02479)

**<font color=#1a73e8>作者：</font>** Minseok Joo, Dogyun Park, Taehoon Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Maintaining long-term geometric consistency remains challenging for long-horizon autoregressive video generation. Memory-augmented generative models address this by retrieving historical frames, but their effectiveness depends on two key design choices: what 3D-geometric evidence should represent past observations, and how memory frames should be selected from this evidence. Existing methods often rely on camera poses or field-of-view overlap, which are lightweight but too coarse to reason about pixel-wise visibility, or use explicit 3D reconstruction, which provides fine-grained evidence but is costly to maintain over long rollouts. We propose Coverage-Maximizing Retrieval-Augmented Generation (COVRAG), a depth-based memory retrieval framework that uses pretrained 3D priors to construct a target-view coverage map as lightweight 3D memory evidence. For frame selection, COVRAG maximizes residual coverage gain, iteratively retrieving frames that explain target-view regions not covered by the current context or previously selected memories. To improve scalability in long-video generation, we introduce sliding-window depth caching for efficient geometry estimation. Experiments on RealEstate10K and DL3DV10K show that COVRAG improves long-horizon geometric consistency while maintaining low latency compared to baselines.

---


### 360. [X-Stream: Exploring MLLMs as Multiplexers for Multi-Stream Understanding](https://arxiv.org/abs/2606.02482)

**<font color=#1a73e8>作者：</font>** Peiwen Sun, Xudong Lu, Huadai Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While video streaming understanding has made significant strides, real-world applications, such as live sports broadcasting, autonomous driving, and multi-screen collaboration, inherently demand continuous, multi-stream interactions. However, existing benchmarks are confined to single-stream paradigms, leaving a critical gap in evaluating online, cross-stream reasoning. To bridge this, we introduce X-Stream, the first benchmark dedicated to multi-stream streaming understanding. Comprising 4,220 rigorously curated QA pairs across 932 videos, X-Stream evaluates 11 subtasks across multi-window, multi-view, and multi-device scenarios. Crucially, our dataset is constructed using a novel dual-verification pipeline that prevents over-reliance on a single stream. Furthermore, we pioneer the conceptualization of multi-modal large language models (MLLMs) as naive multiplexers, systematically evaluating their performance through the lens of Signal Multiplexing Theory. Our extensive online inference experiments reveal a stark reality: state-of-the-art MLLMs struggle significantly with concurrent streams, achieving only about 50% score and exhibiting poor proactive ability. Ultimately, X-Stream exposes the trade-off of current multiplexing schemes, providing both a practical evaluation protocol and empirical guidance for next-generation multi-stream agents.

---


### 361. [Iteris: Agentic Research Loops for Computational Mathematics](https://arxiv.org/abs/2606.02484)

**<font color=#1a73e8>作者：</font>** Leheng Chen, Zihao Liu, Wanyi He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models and agentic AI systems have enabled significant progress in mathematical discovery, from solving competition problems to tackling research-level conjectures. However, open problems in computational mathematics have received comparatively less attention: research in this area often requires not only proofs but also numerical experimentation, adversarial constructions, and algorithm design. In this paper, we introduce an agentic research system, Iteris, designed for open problems in computational mathematics. We apply Iteris to two open problems from a recent Simons Workshop collection (arXiv:2602.05394). In these case studies, Iteris generated numerical evidence, constructions, and proof drafts that led, after expert review and correction, to verified results. The first result is a phase diagram for the asymptotic comparison between conjugate gradient and randomized coordinate descent on power-law spectra; the second is a counterexample showing that QR factorization with column pivoting can fail to select well-conditioned submatrices even under low coherence. These case studies suggest that agentic AI systems can participate meaningfully in research workflows for open problems in computational mathematics, while human validation remains essential.

---


### 362. [Towards Multidisciplinary Summarization of Hospital Stays: Efficient Sentence-Level Clinical Provenance Categorization](https://arxiv.org/abs/2606.02487)

**<font color=#1a73e8>作者：</font>** Baris Karacan, Vaibhav Bhargava, Barbara Di Eugenio 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective "all-team" summarization in high-complexity settings like the Neonatal Intensive Care Unit (NICU) requires aggregating insights from diverse disciplines (physicians, nurses, therapists) spread across hundreds of clinical free-text notes. Simply pooling heterogeneous text often leads to incoherent outputs. Structured summarization therefore first requires accurate categorization of sentence-level provenance across multi-source notes. This pilot study introduces a clinical provenance categorization pipeline using supervised fine-tuning (SFT) of large language models (LLMs). We adapted two Llama-3 models (8B and 70B) to MedSecId, a corpus of 2,002 MIMIC-III (Adult ICU) notes annotated with clinical provenance headers, achieving in-domain Macro F1 scores above 92% for both models. To evaluate cross-domain generalization, we assessed model capacity (8B vs. 70B) and quantization on a gold-standard dataset of 227 sentence-level spans derived from three multi-disciplinary NICU summaries. Experimental results demonstrate a scale-dependent transfer effect: while SFT produced only marginal changes for the 8B model, it substantially improved the 70B model, increasing Macro F1 by 7%. Notably, the quantized fine-tuned 70B model outperformed its full-precision baseline while substantially reducing computational requirements. These findings suggest that sufficient model capacity is critical for preserving semantic flexibility during cross-domain clinical transfer and that efficient quantized adaptation can enable structured provenance modeling for downstream summarization.

---


### 363. [Not What, But How: A Communicative Audit of LLM Response Framing](https://arxiv.org/abs/2606.02493)

**<font color=#1a73e8>作者：</font>** Siddhesh Milind Pawar, Sarah Masud, Haneul Yoo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are being increasingly used to answer subjective, information-seeking questions, where users are sensitive to how responses are communicated, not just whether the answers are correct. Existing LLM evaluations for subjective cultural queries largely focus on factual correctness, ignoring how the response is framed. To this end, we introduce FRANZ, an automated FRAmework for respoNse characteriZation to conduct communicative audit of LLM responses along four dimensions: cultural positioning, use of generalizing language, anthropomorphic cues, and adherence to conversational maxims. To enable this evaluation, we contribute SQUARE - a corpus of 376k subjective questions sourced from 57 subreddits, and mapped to 7 countries and 19 question categories. We demonstrate FRANZ's applicability by scoring responses from three open-weight LLMs. We observe that LLMs show statistically significant differences in the frequency with which they employ each response characteristic. Unlike single-dimensional audits, FRANZ reveals that insider positioning and anthropomorphism are positively coupled, with the degree of coupling varying by country, providing a diagnostic lens for identifying framing divergences.

---


### 364. [Bridging the Last Mile of Time Series Forecasting with LLM Agents](https://arxiv.org/abs/2606.02497)

**<font color=#1a73e8>作者：</font>** Yuhua Liao, Zetian Wang, Qiangqiang Nie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series forecasting has advanced rapidly, especially with the emergence of foundation models that show strong zero-shot performance on numerical extrapolation. However, in real-world forecasting settings, a statistically plausible baseline is rarely the final forecast used in practice. Before a forecast becomes decision-ready, it often needs to be revised using weakly structured business context such as holiday effects, campaign plans, external events, historical analogs, and expert feedback. This practical stage remains underexplored in the forecasting literature. In this paper, we formulate this stage as the \textbf{last-mile forecasting} problem and present an LLM-agent framework that sits on top of a forecasting backbone. Our system maintains a unified forecast workspace, invokes tools to retrieve contextual evidence, and converts reasoning trajectories into explicit forecast revision actions under structural safety constraints. It also supports long-horizon forecasting through map-reduce-style decomposition and post-hoc reflection through a memory bank. The resulting system is designed to be controllable and auditable. Through real-world case studies, we show how LLM agents can bridge the gap between statistical prediction and business-ready forecasting.

---


### 365. [CRAM: Centroid-Routing and Adaptive MoE for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2606.02502)

**<font color=#1a73e8>作者：</font>** Jun-Tao Tang, Zhen-Hao Xie, Yu-Cheng Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) unify heterogeneous vision-language tasks under a shared generative framework via instruction tuning, yet real-world deployment demands continuous capability expansion, making Multimodal Continual Instruction Tuning (MCIT) essential. Existing methods either update all tasks with a shared parameter set or allocate dedicated modules for each new task. Shared updates force heterogeneous tasks to compete, causing forgetting of learned capabilities. Conversely, isolated expansion prevents interference but severely limits parameter efficiency over long task streams. To address this dilemma, we propose CRAM. Specifically, by isolating task-specific patterns into independent modules, CRAM mitigates catastrophic forgetting across tasks. To further boost parameter efficiency, we utilize adaptive-rank instantiation to identify the capability gap between existing expert capability and new task demands, and dynamically allocate only the necessary parameters. To ensure stable reuse among tasks, centroid-guided routing recognizes and activates existing experts' capabilities, while an orthogonality penalty confines new updates to task-specific directions, preventing re-learning general capability. Extensive experiments across diverse benchmarks consistently demonstrate its superiority over existing methods.

---


### 366. [When Rating Scales Fall Short: LLM-Assisted Discovery of ADHD Signals in Turkish Teacher Narratives](https://arxiv.org/abs/2606.02509)

**<font color=#1a73e8>作者：</font>** Baris Karacan, Irem Aktar Songur, Ahmet Ozaslan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Attention Deficit Hyperactivity Disorder (ADHD) is one of the most common neurodevelopmental disorders in childhood, and its diagnosis relies on assessments combining clinician judgment with standardized rating scales and reports from parents and teachers. While structured instruments such as the Conners' Teacher Rating Scale-Revised Short Form (CTRS-R:S) quantify ADHD-related behaviors, teachers also provide open-ended narratives that may contain complementary signals not captured by structured assessments. However, it remains unclear to what extent teacher narratives encode signals overlooked by rating scales. In this study, we analyze de-identified Turkish teacher evaluation forms collected during clinical ADHD assessments, including both CTRS-R:S scores and open-ended teacher narratives. We compare predictive signals from structured scores and narrative text and identify cases where structured assessments fail to clearly distinguish ADHD from non-ADHD students while narrative-based models capture distinct behavioral patterns. Notably, these cases show minimal overlap with those missed by the narrative model, suggesting that structured and narrative information encode complementary signals. To interpret these differences, we apply a large language model (LLM)-assisted theme discovery pipeline that reveals distinct attention, behavioral, and family-related patterns, highlighting the potential of natural language processing (NLP) to uncover clinically relevant signals from teacher narratives and to complement traditional ADHD screening tools.

---


### 367. [Moment-Video: Diagnosing Temporal Fidelity of Video MLLMs on Momentary Visual Events](https://arxiv.org/abs/2606.02522)

**<font color=#1a73e8>作者：</font>** Xiaolin Liu, Yilun Zhu, Xiangyu Zhao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video multimodal large language models (MLLMs) have made rapid progress on general and long-form video understanding, yet their ability to preserve brief answer-critical visual evidence remains underexplored. Many practical questions are determined by momentary visual events: localized actions or state transitions that may last only a few frames. Such evidence can be skipped by sparse frame sampling, suppressed by visual-token compression, or diluted by coarse temporal aggregation, causing failures that language-side reasoning cannot reliably recover. We introduce Moment-Video, a benchmark for diagnosing the temporal fidelity of video MLLMs through momentary visual event understanding. Each question is grounded in a localized, visually observable, and sampling-sensitive event, requiring models to notice, count, describe, or reason about transient evidence rather than rely on persistent objects, global scene context, or language priors. Moment-Video contains 1,000 human-verified video-QA pairs across 7 domains and 25 fine-grained subcategories, covering four task types: Temporal Occurrence, Temporal Counting, Action Description, and Temporal Reasoning. We evaluate 33 proprietary and open-source MLLMs on Moment-Video. The best-performing model, Seed-2.0-Pro, achieves only 39.6% overall accuracy, while most open-source models remain below 25%, revealing a substantial gap in momentary visual event understanding. Diagnostic analyses show that denser frame sampling improves some models but does not eliminate the bottleneck, and longer videos introduce stronger temporal-localization challenges. These findings suggest that current video MLLMs still lack temporally faithful representations for capturing, preserving, and using brief but decisive visual evidence.

---


### 368. [SafeSteer: Localized On-Policy Distillation for Efficient Safety Alignment](https://arxiv.org/abs/2606.02530)

**<font color=#1a73e8>作者：</font>** Hao Li, Jingkun An, Zijun Song 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aligning Large Language Models (LLMs) with human values often degrades their general capabilities, termed the alignment tax. Existing methods mitigate this by balancing dual objectives, which heavily rely on massive general-purpose data or auxiliary reward models.
In this paper, we argue that, because safety features are inherently sparse within the output distribution, alignment requires localized modifications rather than global trade-offs. To this end, we propose SafeSteer, which performs on-policy distillation confined to safety tokens. First, we construct a safety teacher via activation steering. Based on this teacher, we develop a safety token selection algorithm. Consequently, SafeSteer restricts the reverse KL penalty to these tokens during training to preserve general capabilities.
Experimental results across diverse models show that our SafeSteer achieves a superior trade-off between safety and general capability compared with existing methods, attaining strong safety performance on seven safety benchmarks with only minimal degradation on five general capability benchmarks. Notably, SafeSteer requires only 100 harmful samples without using any general-purpose data, less than 1% of what previous baselines used, considerably reducing alignment cost. More details are on our project page at this https URL.

---


### 369. [SimSD: Simple Speculative Decoding in Diffusion Language Models](https://arxiv.org/abs/2606.02544)

**<font color=#1a73e8>作者：</font>** Junxia Cui, Haotian Ye, Runchu Tian 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) have recently emerged as a promising alternative to autoregressive (AR) LLMs, offering faster inference through parallel or blockwise decoding. However, their masked language modeling formulation remains incompatible with standard token-level speculative decoding, one of the most effective acceleration techniques for AR models. In AR decoding, the causal mask preserves temporally valid token-level contexts, enabling a target model to verify multiple drafted tokens in a single forward pass. In contrast, dLLMs rely on mask tokens and bidirectional attention, causing the effective context to change across denoising steps and preventing direct token-level speculative verification. To bridge this gap, we propose a simple but effective speculative decoding algorithm for diffusion language models, named SimSD, which mainly adopts a plug-and-play masking strategy that equips dLLMs with temporally valid token-level contexts for speculative decoding. Our method explicitly introduces reference tokens from draft-model predictions and designs an attention mask that regulates their interaction with current-step tokens, allowing dLLMs to compute valid logits for drafted tokens in a single forward pass. This restores the key verification ability provided by causal masking in AR models while preserving the parallel decoding advantages of dLLMs. The proposed method is training-free and can be flexibly integrated with other acceleration techniques such as KV cache and blockwise decoding. Experiments on SDAR-family dLLMs across four benchmarks show that our method achieves up to 7.46x higher decoding throughput while maintaining and even improving average generation quality.

---


### 370. [LongLive-RAG: A General Retrieval-Augmented Framework for Long Video Generation](https://arxiv.org/abs/2606.02553)

**<font color=#1a73e8>作者：</font>** Qixin Hu, Shuai Yang, Wei Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) video diffusion enables variable-length synthesis, but long-horizon generation often suffers from accumulated errors and identity drift. For efficiency, existing methods commonly adopt sliding-window attention during generation. This creates an irreversible generation trajectory: once the active window accumulates appearance errors, subsequent generations can only condition on this degraded trajectory and drift further away. We address this limitation by formulating long video generation as a retrieval-augmented generation (RAG) problem. Rather than relying solely on the recent window, we treat previously generated latents as a dynamic, searchable history. We propose LongLive-RAG, a general retrieval framework for AR video generation. At each new block, LongLive-RAG uses a query embedding to retrieve relevant historical latents. This lightweight retrieval step adds only a small overhead relative to generation and lets the generator condition on non-local context instead of only the recent window. To make retrieval more discriminative, we introduce the Window Temporal Delta Loss that suppresses redundant local similarity and encourages embeddings to capture meaningful temporal changes. Together, these components help reduce error accumulation caused by sliding-window attention. Experiments across multiple AR backbones and generation lengths show improved long-video quality and the best average VBench-Long rank. To our knowledge, among open-ended AR long video generation methods, LongLive-RAG is the first to formulate self-generated latent history as content-addressable retrieval memory. Code is available at this https URL.

---


### 371. [From Layers to Submodules: Rethinking Granularity in Replacement-Based LLM Compression](https://arxiv.org/abs/2606.02559)

**<font color=#1a73e8>作者：</font>** Elia Cunegatti, Marcus Vukojevic, Erik Nielsen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training compression of Large Language Models (LLMs) removes entire architectural components, either deleting them or replacing them with fitted modules. Existing replacement-based methods share two design constraints: full-layer granularity and contiguous selection. We argue that this is overly restrictive: in fact, redundancy in pretrained transformers is not confined to contiguous regions, nor does it evenly distribute between Attention and FeedForward outputs, implying that different strategies best approximate different submodule types and that removable components need not cluster within contiguous depth ranges. Based on this intuition, we introduce SubFit (Submodule-level Fitted residual replacement), which compresses LLMs at the submodule level: Attention and FeedForward submodules are selected non-contiguously, and each receives its own lightweight fitted residual bypass. SubFit operates post-training and requires only calibration data. Across ten LLMs (five base, five instruction-tuned), five sparsity levels from 12.5% to 37.5%, and four replacement-based baselines, SubFit achieves the best aggregate perplexity-accuracy trade-off across the evaluated sparsity levels, with larger gains under aggressive compression. At 25% sparsity, it retains 84.6% of dense downstream accuracy and incurs 2.42x perplexity degradation, against 81.6% and 4.34x for the strongest baselines, while delivering measurable inference speedup and KV-cache savings. Code is available at this https URL.

---


### 372. [AdaCodec: A Predictive Visual Code for Video MLLMs](https://arxiv.org/abs/2606.02569)

**<font color=#1a73e8>作者：</font>** Haowen Hou, Zhen Huang, Zheming Liang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video is temporally redundant: adjacent frames usually share most objects, background, and layout. Yet existing video multimodal large language models (video MLLMs) usually encode each sampled frame as an independent RGB image, causing visual tokens to repeat content already present in earlier frames. This suggests a more direct video interface: send a full reference frame only when the scene cannot be predicted well from prior context, and otherwise transmit a compact description of inter-frame changes. We call this interface a \emph{predictive visual code}, and instantiate it for video MLLMs as \textbf{AdaCodec}. AdaCodec spends full visual tokens on a reference frame only when its conditional predictive cost is high; otherwise, it encodes inter-frame changes, including motion and prediction residuals, as compact P-tokens. Across all eleven benchmarks, AdaCodec improves over the Qwen3-VL-8B per-frame RGB baseline at a matched visual-token budget. Even at $1/7$ the budget, AdaCodec with 32k tokens surpasses the 224k baseline on all long-video benchmarks; on five general-video benchmarks, it raises the average score while substantially cutting time-to-first-token from 9.26s to 1.62s.

---


### 373. [From Zero to Hero: Training-Free Custom Concept Spawning in World Models](https://arxiv.org/abs/2606.02575)

**<font color=#1a73e8>作者：</font>** Kiymet Akdemir, Pinar Yanardag  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive world models have emerged as a powerful paradigm for interactive video generation, allowing users to navigate dynamically generated environments through actions. These models are typically conditioned on a text prompt and/or a single reference frame, from which the entire world is generated. Yet the moment the user navigates beyond what is visible in that frame, the unseen regions are populated by the base model's priors, with no mechanism for the user to specify what should appear and where. This is a fundamental limitation for applications such as gaming, interactive storytelling, and simulation, where controllable scene composition is essential. We refer to this missing capability as concept spawning; introducing a user-specified visual concept into a world model, analogous to spawning in a game engine. We introduce SPAWN (Swapping Pinned Anchor with Windowed iNjection), a training-free method for concept spawning. SPAWN exploits a structural property of image-to-video backbones: the first slot of the context memory is pinned to the reference frame and acts as a foundational anchor for every generated chunk. By swapping this anchor with an external concept latent over a short injection window and letting the original anchor return, we cause the concept to propagate naturally through the rollout via the model's own memory. SPAWN supports concepts from fine-grained entities such as characters and props to large-scale elements such as buildings and landmarks, and accepts either a concept image or a text description as input. Experiments show that SPAWN integrates concepts with consistent lighting, scale, and perspective while preserving identity and temporal coherence, demonstrating that controllable concept spawning is achievable in existing autoregressive world models without any training.

---


### 374. [ProtoAda: Prototype-Guided Adaptive Adapter Expansion and Geometric Consolidation for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2606.02576)

**<font color=#1a73e8>作者：</font>** Yu-Cheng Shi, Zhen-Hao Xie, Jun-Tao Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) achieve strong performance through instruction tuning, but real-world deployment requires them to continually acquire new vision-language capabilities, making Multimodal Continual Instruction Tuning (MCIT) essential. To reduce inter-task interference and promote collaboration, recent methods often employ sparse architectures like Mixture of LoRA Experts with image-text similarity routing. However, tasks with distinct response structures could share highly similar visual-linguistic semantics and thus be wrongly routed to the same expert; image-text similarity alone is insufficient for reliable task assignment. For example, an expert in a grounding task requiring coordinate prediction may be biased toward producing short textual answers after learning semantically similar VQA tasks. This format-blind task assignment integrates heterogeneous response types into shared parameters, inducing gradient interference and ineffective expert collaboration. To address this problem, we propose ProtoAda, a prototype-guided adaptive tuning framework. ProtoAda introduces format-aware task prototypes to align task assignment and routing with both task semantics and output structure, and further consolidates format-compatible updates in a geometry-aware manner to effectively reuse and progressively refine existing parameters. Extensive experiments on multiple benchmarks demonstrate that ProtoAda achieves superior performance, especially on tasks whose answer structures are easily corrupted by sequential tuning.

---


### 375. [Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling](https://arxiv.org/abs/2606.02578)

**<font color=#1a73e8>作者：</font>** Seojeong Park, Jiho Choi, Junyong Kang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models have demonstrated strong reasoning ability, yet their reliability as automated evaluators remains limited by a critical weakness: when visual evidence conflicts with textual cues, MLLM judges tend to reward plausible narratives over perceptually correct answers. We identify and systematically analyze this phenomenon, which we term Perceptual Judgment Bias. Through controlled visual perturbations, existing multimodal judges frequently anchor on the response text instead of their own visual perception, leading to inconsistent and non-verifiable evaluations. To address this issue, we introduce the Perceptually Perturbed Judgment Dataset, which constructs minimally edited counterfactual responses that isolate perceptual errors and enable verifiable supervision. Building on this dataset, we develop a unified training framework that combines a structured GRPO-based reward with a batch-ranking objective, achieving coherent global ordering without explicit pairwise labels. Experiments across diverse MLLM-as-a-Judge benchmarks show that our approach substantially improves perceptual fidelity, ranking coherence, and alignment with human evaluation. Our results establish a scalable and generalizable pathway for training multimodal judges that are perceptually grounded, interpretable, and robust to visual-reasoning conflicts.

---


### 376. [Thinking in Blender: Staged Executable Inverse Graphics with Vision-Language Models](https://arxiv.org/abs/2606.02580)

**<font color=#1a73e8>作者：</font>** Guangzhao He, Rundong Luo, Wei-Chiu Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inverse graphics is a longstanding and highly underconstrained problem that seeks to reconstruct images as editable 3D scenes which can be rendered, relit, and manipulated. In this work, we investigate whether pretrained vision-language models (VLMs) can perform executable inverse graphics directly from a single image by reconstructing a scene as an editable Blender program, without relying on specialized 2D or 3D foundation models, differentiable rendering, or multi-view supervision. We introduce Staged Executable Inverse Graphics (SEIG), an agentic framework that reconstructs a 3D scene from a single image by progressively refining scene factors including geometry, materials, composition, and lighting directly in executable Blender code space. We evaluate our framework across diverse scenes using a range of reconstruction metrics spanning pixel-level, perceptual, and semantic fidelity. Our experiments show that staged reconstruction substantially improves reconstruction fidelity, highlighting the importance of task decomposition for executable inverse graphics with general-purpose VLMs. Finally, we showcase various downstream applications enabled by the reconstructed editable Blender scenes.

---


> [!TIP]
> 当前位于：**351-376**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-376**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
