# 🧠 大模型相关研究 | 2026年09月04日

> 本类共 **177** 篇论文：已确认 **170** 篇，待复核 **7** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-177**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-177**

---

### 151. [LoRA-TSD: Tangent-Space Spectral Descent for LoRA via Muon-Style Updates](https://arxiv.org/abs/2609.02734)

**<font color=#1a73e8>作者：</font>** Dmitrii Andriianov, Andrey Veprikov, Aleksandr Beznosikov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) is the standard way to fine-tune large models, yet when its two factors are trained independently, the update ignores the geometry of the low-rank weight change it induces. We introduce LoRA-TSD, an optimizer that treats every LoRA step as a tangent vector of the fixed-rank matrix manifold and takes the spectral-norm steepest-descent step of Muon inside that tangent space, mapping the result back to the factors through a retraction native to the LoRA parametrization. The step avoids expensive operations on full weight matrices, and its retraction is up to $2.8\times$ cheaper than the truncated-SVD retraction used by prior manifold methods. We prove that the Frobenius-norm version of our surrogate recovers LoRA-Pro, and we identify the tangent-projected gradient, the Riemannian gradient of the manifold, as the stationarity measure natural to LoRA training and computable from the factor gradients alone. Under this measure we give the first global convergence guarantees for both LoRA-Pro and LoRA-TSD, with rates that drive the factor-gradient norms to zero. Across six commonsense and natural-language-inference benchmarks with Llama-3.2-1B, Llama-3.1-8B and Qwen3-32B, LoRA-TSD outperforms every competing LoRA optimizer and stays robust to the adapter rank. Code is available at this https URL.

---


### 152. [Choosing a PEFT Variant for Per-Patient Dysarthric ASR: A Single-Speaker Case Study on Two ASR Bases](https://arxiv.org/abs/2609.02735)

**<font color=#1a73e8>作者：</font>** Bernard Muller, László Tóth, LaVonne Roberts  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Per-patient adapters are the preferred production architecture for dysarthric automatic speech recognition (ASR), yet parameter-efficient fine-tuning (PEFT) variants have not been compared in the speaker-dependent, per-patient regime. We present a single-speaker case study comparing seven LoRA-family methods (LoRA, QLoRA, AdaLoRA, DoRA, LoHA, VeRA, VB-LoRA) on two production bases (Whisper-large-v3 with Hungarian fine-tuning, and a multilingual Qwen3-ASR-1.7B checkpoint) for one post-stroke Hungarian male speaker (S1, 409 utterances; severe dysarthria on auditory-perceptual clinical assessment). Attention-projection adapters substantially improve CER on both bases. Across three seeds, a paired bootstrap detects no significant LoRA-DoRA difference (p>0.5; 13.86/13.90 % CER on Whisper, 28.10/28.33 % on Qwen3-ASR), so we adopt the simpler, cheaper LoRA. Real 4-bit (NF4) QLoRA is worse on every seed and both bases (14.56/30.09 % CER) with no memory saving at this scale, and LoHA, VeRA, VB-LoRA and AdaLoRA do not reach the LoRA family, though LoHA still gives an 18.6 % relative CER reduction on Whisper. On the same base, full fine-tuning is more accurate (11.43 % CER), but a 115 MB LoRA that also adapts the feed-forward blocks reaches within 0.66 pp of it at approximately 3.7 % of the per-patient storage. A 6-point enrollment grid shows about 5 min of patient audio captures 45.6 % of the zero-shot-to-30-min CER reduction, with further gains at 10 and 30 min (caveat: one speaker, one language, severe post-stroke dysarthria). Training scripts and recipes will be released, source-available under a research-use licence, on publication.

---


### 153. [Language Models Can Control Their Own Attention](https://arxiv.org/abs/2609.02737)

**<font color=#1a73e8>作者：</font>** Namgyu Ho, Huzama Ahmad, Woosung Koh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models spend most of their attention on a small fraction of context, yet they read the entire KV cache to find the few tokens that matter. If the user asks about a previous detail in a 1M-token conversation, global attention layers must scan the full context to generate each token of the reply. A prominent approach mitigates this cost by pre-selecting relevant tokens via lightweight proxy scores, but this extrinsic scoring still incurs O(N) per step. We take an intrinsic approach motivated by the simple question: wouldn't the model already know which parts of the context are relevant? To this end, we introduce Declarative Attention (DA), a protocol that elicits the model to declare where it needs to attend within its chain-of-thought, partitioning generation into three modes: <global> (full context), <focus> (a specific region), and <local> (recent output only). The inference engine parses these declarations like tool calls and skips most of the KV cache read. Under zero-shot evaluation across 15 long-context tasks, DA on off-the-shelf models (Gemma-4-31B, Qwen-3.6-27B) significantly reduces total attended tokens during decoding (52.0%, 31.1%) with modest accuracy drops (1.27pp, 2.75pp) that shrink with model scale. DA unlocks a new axis of sparse attention, with further potential under training-based methods that future work can explore.

---


### 154. [Repo-To-Skill: Distilling GitHub Repositories Into AI4AI Skills](https://arxiv.org/abs/2609.02749)

**<font color=#1a73e8>作者：</font>** Jianlyu Chen, Yuyang Hu, Hongjin Qian 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents are beginning to carry out machine-learning (ML) research end to end. These agents combine a model backbone with a harness for planning, execution, memory, and verification, but this architecture still leaves domain-specific know-how outside the agent. We call this missing layer operational knowledge, the know-how that separates knowing a method from making it work. That knowledge is not absent from the field. It appears in repositories and papers, but in forms written for human readers and too large to load during a task. Once distilled into compact, verified skills, this knowledge can be reused across tasks rather than rediscovered during each run.
We present DisCo, a skill-powered research agent that creates skills and uses them during research. Its distillation runs in two complementary forms: task-agnostic, condensing the field's widely used repositories into reusable skills, and task-oriented, producing the skills a concrete task calls for. The former, applied across the open ecosystem, yields the AREX-Skill Library, with 5,000+ verified skills distilled from 1,000 widely used ML repositories and organized into 20 areas and 178 capability families. With the GPT-5.5 backbone, research harness, and downstream execution budget held fixed, the skill-equipped research agent scores 134.3% higher on MLE-bench, 34.4% higher on PaperBench, 9.2% higher on FrontierCS, and 14.0% higher on PassNet than the same agent without skills. These gains come from adding distilled operating context under that fixed setup.

---


### 155. [Bilevel Coordinated Reflection: A Game-Theoretic Approach to Multi-Agent LLM Systems](https://arxiv.org/abs/2609.02750)

**<font color=#1a73e8>作者：</font>** Yihang Chen, Yuxiang Chen, Yuxuan Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems commonly use an orchestrator to decompose a task for a team of workers and then improve through textual reflection. Despite strong empirical results, these systems lack a unified account of coordination, memory improvement, and the role of external verification. We model orchestrator-worker interaction as a bilevel coordination game: under bounded coupling, the workers' local-update game is an approximate potential game whose equilibrium slack is controlled by decomposition quality. We then analyse reflection as stochastic movement over semantic memory states. For free-form reflection, we derive a finite-time upper bound, prove worst-case tightness, and give a positive lower bound under a falsifiable persistent-harm condition. We further prove an information-theoretic impossibility result: no gate that observes only the generated transcript can improve uniformly over text-indistinguishable environments, whereas an environment-grounded gate can. Motivated by this separation, we introduce Stochastic Reflective Memory Ascent (SRMA), which accepts a candidate memory only after a grounded evaluation risk strictly decreases. Under calibration and non-degenerate corrective mass, SRMA converges exactly, geometrically or polynomially; matching constructions show that both rate regimes are order-tight. We also provide confidence gating for stochastic evaluation and re-anchoring guarantees for piecewise-stationary environments. Experiments instantiate these objects with environment-grounded metrics and test the predicted coordination and drift laws. On 500 SWE-bench instances, the complete Kimi-based system resolves 72.2% versus a 70.8% public mini-SWE-agent reference. Code: this https URL

---


### 156. [Multi-Tool Image Editing Attribution in Facial Forgery](https://arxiv.org/abs/2609.02751)

**<font color=#1a73e8>作者：</font>** Sheng Liu, Qiang Sheng, Danding Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As generative AI tools become increasingly powerful and easy to use, people can easily edit portrait images with a prompt, necessitating the task of image editing attribution, which predicts the involved editing tools from the given image. Existing attribution methods hold the single-tool assumption and can only attribute a specific editing tool, but struggle to handle the more complex and increasingly common multi-tool editing scenarios, where artifacts left by different editing tools are composite and overlapped. To address this gap, we explore Multi-Tool Image Editing Attribution (MIEA), which aims to identify multiple editing tools involved in a multi-tool edited facial image. To simulate the real-life editing operations on facial images, we then construct a new dataset, MultiEdit, which contains 500k+ edited facial images and covers six types of editing tools that support face swapping (Deepfake) and various facial enhancements. Inspired by the findings from data analysis, we design DPEC, a multi-tool attribution method that can capture distinguishable, locality-aware editing tool traces from both spatial and frequency domains with the support of an error-based curriculum learning strategy. Experiments show \Method\ outperforms nine methods for facial images edited in at most five steps.

---


### 157. [Untangling the Mechanisms of Misleading Context in Medical Question Answering](https://arxiv.org/abs/2609.02754)

**<font color=#1a73e8>作者：</font>** Robin Linzmayer, Noémie Elhadad  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models now answer medical questions with expert-level performance. However, the context these systems act on can be misleading, and misleading context can corrupt a model's medical judgment. To understand how misleading context corrupts this judgment, we examine the model's susceptibility to the context, disclosure of it, mechanism of corrupted reasoning, and monitorability of the decision. On the medical reasoning subset of MedMisBench, a clinician-reviewed question-answering benchmark of 8,627 questions, we inject two types of misleading context cues, fabricated evidence and a bare assertion. We test three reasoning models, two that expose their full reasoning trace and one frontier model that exposes only its response. All three are more susceptible to the assertion than to the fabricated evidence, adopting the asserted answer 10 to 27 points more often. The misleading cues are disclosed in 81 to 98% of traces but only 7 to 90% of responses, and the assertion is disclosed less often than evidence based cues. Resampling from reasoning traces without disclosure shows the two cues corrupt reasoning differently, evidence entering early and accumulating while the assertion redirects the conclusion near its end. An LLM monitor catches 78% of corrupted decisions at 5% false positives when reading an open model's trace with guidance, against at most 32% from any response. The misleading context that models are most susceptible to is disclosed least, and was caught reliably only from an open reasoning trace, which frontier providers withhold.

---


### 158. [Do Tabular Foundation Models Know Physics? Contamination, Units, and the Deterministic Limit](https://arxiv.org/abs/2609.02766)

**<font color=#1a73e8>作者：</font>** Wassim Tenachi, Yashar Hezaveh, Laurence Perreault Levasseur 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) learn to fill in tables the way language models fill in text, and tables are arguably the format in which most physical measurement arrives. Did they learn any physics in the process? They are Bayesian by construction, so the question is what their prior contains. We probe it directly, evaluating four of them (TabPFN-3, TabICLv2, TabDPT and Real-TabPFN-2.5) against six baselines on datasets sampled from 316 physical equations, in and out of domain. TFMs dominate, out of the box and after tuning. But we show that their prior can represent neither a noiseless mechanism nor physical units, which is why they interpolate physics without yet being able to act as physical models.

---


### 159. [From Reweighting to Rewriting: Unlocking the Intervention Effects of Influential Samples in Training Data Attribution](https://arxiv.org/abs/2609.02771)

**<font color=#1a73e8>作者：</font>** Yuzhang Luo, Chenpeng Wang, Jianhui Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training data attribution (TDA) aims to identify training examples that shape model behavior, but its intervention value depends on both which examples are selected and how they are modified. Influence functions (IF) estimate behavioral changes under infinitesimal reweighting, yet IF-selected examples often show limited advantages over random selection under conventional weight-based interventions. This raises the question of whether influential examples lack intervention value or whether reweighting fails to realize their behavioral this http URL introduce influence-guided response rewriting, which uses IF to identify intervention targets and replaces their responses with behavior-aligned or behavior-opposed supervision while keeping instructions fixed. Across four open-weight LLMs, we compare rewriting and reweighting on the same influence-selected examples using epistemic abstention as our primary testbed. Response rewriting produces stronger, more persistent, and bidirectional behavioral shifts, while reweighting the same examples yields weak and inconsistent effects. Further analyses show that influence-selected examples provide greater rewriting leverage than alternative selectors, with changes remaining concentrated on target-relevant behaviors. The same qualitative contrast extends to safety refusal. These results distinguish the local reweighting effects captured by influence estimates from the broader intervention leverage of the examples they identify, motivating intervention-aware evaluation of TDA methods.

---


### 160. [HyperStyler: Low-resource Authorship Style Transfer via Context-aware Style Navigation and Hypernetworks](https://arxiv.org/abs/2609.02772)

**<font color=#1a73e8>作者：</font>** Jongkyung Shin, Minguk Jeon, Chanwoo Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-resource authorship style transfer (LAST) aims to rewrite text into the style of an arbitrary target author using only a few reference examples while preserving the original meaning. Existing methods often struggle to achieve both high style fidelity and semantic preservation because they compress diverse references into a single static author embedding, which averages out context-dependent stylistic variation, and rely on hidden representations for style control, which entangle style with content. We propose HyperStyler, a novel architecture that decouples LAST into style selection and style realization. Stylo-navigator predicts style coordinates by jointly modeling the source context and target-author references, and Stylo-hypernet realizes them via dynamic parameter modulation instead of hidden-state injection. Our experiments on Reddit, Blog, and News datasets demonstrate that HyperStyler consistently outperforms prior methods including LLM-based approaches and generalizes robustly across domains. Notably, HyperStyler achieves superior performance with as few as 2.4% additional parameters over T5-large, while being over 1.8x faster than LLMs at inference.

---


### 161. [ShallowStream: Index Shallow then Answer Deep for Streaming Video Understanding](https://arxiv.org/abs/2609.02780)

**<font color=#1a73e8>作者：</font>** Jitai Hao, Ke Yang, Qiang Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding is a critical capability for real-world applications, including embodied intelligence, autonomous driving, industrial monitoring, surveillance and early warning, and wearable assistants. However, processing continuous video streams with multimodal large language models (MLLMs) is computationally expensive. Existing efforts have explored reducing streaming overhead through visual token pruning, token merging, quantization, on-demand frame retrieval, and context offloading. However, most existing methods overlook the dimension of model depth. Repeatedly executing full-depth MLLM prefill over incoming frames is prohibitively expensive, incurring substantial computational overhead and causing the KV cache to grow at a rate directly proportional to the prefill depth. To address these challenges, we propose ShallowStream, a novel framework that leverages the shallow layers of an MLLM to simultaneously perform frame encoding and retrieval index building. During stream processing, ShallowStream maintains an always-on lightweight index using the KV cache of shallow layers. During query-time answering, we leverage the attention scores generated by the shallow layers to score context frames and employ a diversity-aware selection strategy to retrieve precise and comprehensive evidence. ShallowStream achieves performance on par with the strongest existing streaming methods, while reducing per-frame prefill latency and 10-second end-to-end latency by up to 52.1x and 11.9x, respectively. Our code is available at this https URL.

---


### 162. [EarlyEval: Cheaper Agent Evaluation via Early Outcome Prediction](https://arxiv.org/abs/2609.02783)

**<font color=#1a73e8>作者：</font>** Yuling Shi, Zhensu Sun, Junsen Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating LLM agents is essential for guiding their development, yet it has grown prohibitively expensive: a single pass of a frontier model over an agentic benchmark can cost hundreds to thousands of dollars, a price paid repeatedly across iterative development cycles. Prior efforts, centered on benchmark distillation, reduce the number of evaluation tasks but leave the cost of executing each retained task untouched. In this work, we introduce early outcome prediction, a complementary axis of efficiency that instead cuts cost within each task. Our key insight is that an agent's final outcome is often evident from its intermediate behavior well before execution completes. We instantiate this idea in EarlyEval, a lightweight framework that trains a pair of LightGBM success and failure classifiers over behavioral, textual, and reference-solution features, and halts an agent run the moment either classifier crosses a calibrated confidence threshold, adding negligible per-step overhead. Across three benchmarks, SWE-bench Verified, TerminalBench, and Toolathlon, EarlyEval can eliminate 13%-26% of agent steps and up to 44.1% input tokens and 29.4% output tokens at 89%-97% prediction accuracy, while perturbing per-agent resolve rates by only one to two percentage points on average.

---


### 163. [DiscoSign: Discourse-Aware Text to Sign Language Gloss Translation](https://arxiv.org/abs/2609.02796)

**<font color=#1a73e8>作者：</font>** Vasileios Baltatzis, Mert Inan, Connor Gillis 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sign language processing systems have traditionally operated at the sentence level, ignoring critical discourse phenomena fundamental to sign language comprehension. We introduce DiscoSign, a computational approach for discourse-aware text to sign language gloss translation grounded in linguistic research. We address three key phenomena within our modular Large Language Model (LLM)-based translation framework: (i) spatial coreference resolution, where entities maintain consistent spatial locations throughout discourse; (ii) Question-Answer Clauses (QACs), pseudocleft structures serving specific discourse functions; and (iii) concept-gloss consistency, ensuring stable mappings between English concepts and American Sign Language (ASL) signs. Traditional translation metrics fail to capture discourse-level quality, so we introduce a suite of novel evaluation metrics designed to assess each dimension of discourse coherence addressed by our framework. Experiments on sentence-level and discourse-level datasets show that our approach for discourse-aware processing significantly improves spatial consistency and entity tracking relative to sentence-only translation, while maintaining competitive single-sentence gloss translation quality. Our work establishes the first systematic framework for discourse-level text to sign language gloss translation with corresponding evaluation methodology.

---


### 164. [Large Language Models (LLMs) for Telecom Root Cause Analysis (RCA): A Structured Reasoning Framework for Evidence-Grounded Diagnosis](https://arxiv.org/abs/2609.02805)

**<font color=#1a73e8>作者：</font>** Hao Zhou, Mandar Kulkarni, Hao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Root cause analysis (RCA) is a critical task in telecom network operations, but diagnosing performance degradations in modern 5G and emerging 6G networks remains challenging due to complex cross-layer dependencies. While large language models (LLMs) offer promising capabilities for reasoning and knowledge integration, directly applying vanilla LLMs to telecom RCA often leads to hallucination, unstable reasoning, and poor alignment with structured network evidence. This work first reviews the evolution of telecom RCA from rule-based and machine learning (ML) approaches to emerging LLM-enabled techniques, and provides an overview of recent paradigms, including structured reasoning, retrieval-augmented knowledge grounding, agentic orchestration, and verifiable reasoning. Building upon these insights, we propose a structured reasoning framework for LLM-enabled telecom RCA that aligns diagnostic reasoning with telecom-specific evidence and domain knowledge. The proposed approach first organizes heterogeneous network telemetry into canonical contexts, and then enforces decision-path reasoning during diagnosis, and finally generates evidence-grounded explanations for reliable fault identification. Experimental results on two 5G RCA datasets, TeleLogs and TelecomTS, demonstrate that the proposed framework consistently improves diagnostic accuracy and decision consistency compared with baseline techniques. These cross-dataset results highlight the importance of structured reasoning design for practical LLM-based RCA systems in next-generation telecom networks.

---


### 165. [Cliff: Learning Process Rewards from the First Mistake](https://arxiv.org/abs/2609.02817)

**<font color=#1a73e8>作者：</font>** Peixuan Han, Runhui Wang, Ketan Ramaneti 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has emerged as a powerful paradigm for large language model (LLM) post-training, but its reliance on coarse outcome rewards leads to limited guidance on intermediate reasoning processes. Existing approaches such as process reward modeling and on-policy distillation introduce additional constraints, such as reliance on a specialized reward model or assuming identical reasoning patterns between teacher and student. Nevertheless, we observe that once a reasoning process first goes wrong, evaluating the subsequent reasoning provides limited additional information, as it is already conditioned on an invalid prefix. Therefore, we propose Cliff, a reward shaping strategy that utilizes an off-the-shelf LLM as a teacher to identify the first mistake in each rollout. As a result, the rollout is naturally decomposed into two parts: a correct prefix and an incorrect suffix. Cliff then converts this signal into token-level advantages, assigning positive advantages for the correct prefix and negative feedback afterward. Experiments across 12 different scenarios demonstrate that Cliff consistently improves reasoning performance, outperforming on-policy distillation by 15% and standard GRPO by 7%, even with teachers of modest capability. Furthermore, we analyse the role of ``ground truth'' in Cliff and investigate its training dynamics. These results establish Cliff as a simple, general and effective approach for improving RLVR with richer, fine-grained supervision.

---


### 166. [UE5M3 FP4 Block Scaling for Stable Language Model Pretraining](https://arxiv.org/abs/2609.02846)

**<font color=#1a73e8>作者：</font>** Robert Hu, Carlo Luschi, Paul Balanca  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stable 4-bit floating-point (FP4) pretraining is difficult because the E2M1 payload represents only a narrow range of magnitudes. NVIDIA's Transformer Engine \nv{} recipe addresses this with current-tensor scaling, a randomized Hadamard transform (RHT), and bfloat16 (BF16) final layers, adding work outside the FP4 matrix multiplications. We instead pair E2M1 payloads with unsigned E5M3 (\ue{}) block scales. Their wider range permits periodic tensor scaling, while our recipe applies selective stochastic rounding to backward gradients, omits RHT, and uses FP4 in all eligible internal linears.
We pretrain a Nemotron-H 8B model for nearly 190 billion tokens. Compared with Transformer Engine \nv{}, the proposed block-16 recipe finishes with lower final-window training loss and, under their respective quantized-inference policies, lower validation loss measured as held-out negative log-likelihood. Its quantized-inference downstream point estimates are also higher on all three reported aggregates. A native \nv{} execution ablation that jointly removes RHT and the BF16 final-block exemption increases measured model-body token throughput by 21.2\%. These results demonstrate end-to-end software-emulated \uefp{} pretraining with a simpler recipe and motivate native support for \ue{} block scaling.

---


### 167. [Post-Training Language Models for Gold-Medal Performance in Coding Competitions](https://arxiv.org/abs/2609.02849)

**<font color=#1a73e8>作者：</font>** Aleksander Ficek, Sean Narenthiran, Mehrzad Samadi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Competitive programming has become a key test of large language model reasoning, with international competitions such as IOI and ICPC representing its most challenging settings. We present an end-to-end specialization pipeline combining large-scale problem curation, synthetic reasoning traces, supervised fine-tuning (SFT), and reinforcement learning (RL). Using 22,000 curated problems, we train Nemotron-3-Nano-CC (30B-A3B) with SFT and RL and Nemotron-3-Ultra-CC (550B-A55B) with SFT alone. We further introduce GenCorrect, a feedback-driven test-time compute strategy that iteratively generates, evaluates, and refines diverse solutions. On IOI 2025, Nano-CC improves from 130 points to 291 after post-training and to 468 with GenCorrect, exceeding the gold threshold of 438.3 while Ultra-CC reaches 502. Guided by these results, we develop a competition-specific Ultra-CC system and evaluate it prospectively during IOI 2026. Under the same time, internet-access, and submission constraints as human contestants, it scores 535.4 out of 600, exceeding both the gold threshold of 361.12 and the top human score of 498.27. To our knowledge, this is the first AI system to outscore the highest-scoring human contestant on an IOI problem set.

---


### 168. [The Implications of Linguistic Illegibility for LLM Security](https://arxiv.org/abs/2609.02852)

**<font color=#1a73e8>作者：</font>** James Mickens  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs are trained to generate natural language. However, various strands of evidence indicate that an LLM's externalized linguistic outputs and mechanistically-extracted linguistic features can be an unreliable lens for understanding internal model computation. We introduce the term ``linguistic illegibility'' to broadly refer to scenarios in which an LLM's externalized or mechanistically-probed language artifacts fail to represent how the model actually thinks. We argue that the specter of linguistic illegibility is unavoidable for LLMs whose internal computations are not directly expressed via language, but rather math over activation spaces (with lossy translations between activation spaces and natural language happening at the bookends). If linguistic illegibility is always possible, then security mechanisms that rely on a model's linguistic self-reporting (e.g., chain-of-thought monitoring, constitutional self-critique, activation probing for linguistically-defined feature vectors) can never be completely sound; the model sandbox will always need isolation techniques whose guarantees do not depend on reading a model's linguistic state at all. We argue that observing a model's outputs using taint tracking is a promising approach for an effective sandbox: regardless of how a model linguistically self-reports, a taint tracking policy can define, a priori, various pieces of system state that should never be influenced by model-produced data. We also discuss several additional sandboxing mechanisms (e.g., robust virtualization, third-party auditing of sandboxing configurations) which collectively provide a critical floor beneath linguistic monitoring, and would have mitigated recent sandbox exploits by frontier models.

---


### 169. [User Feedback Provides a Unique Signal that LLMs Can not Detect](https://arxiv.org/abs/2609.02859)

**<font color=#1a73e8>作者：</font>** Shachar Don-Yehiya, Leshem Choshen, Omri Abend  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Harnessing naturally occurring feedback from user interactions offers a promising learning signal for Large Language Models (LLMs). However, recent studies suggest this feedback is inherently noisy and difficult to leverage effectively. We challenge this conception by demonstrating that user feedback is a highly actionable signal for improvement, and that its perceived ineffectiveness stems from a systematic bias in current evaluation paradigms. To isolate the usefulness of feedback, we construct synthetic data with a definitive ground truth, alongside naturalistic data to validate that our findings hold in real-world scenarios. By comparing model revisions generated with and without access to feedback across both settings, we show that feedback-informed revisions resolve targeted issues at significantly higher rates than baseline revisions. Finally, we expose the root of the evaluation bias: when a model successfully fixes an issue exclusively due to feedback, LLM judges frequently fail to identify the genuinely corrected response, systematically preferring inferior baseline outputs instead.

---


### 170. [Graph Machine: Towards Better Pretraining via Edges](https://arxiv.org/abs/2609.02881)

**<font color=#1a73e8>作者：</font>** Lintai Hou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the Graph Machine (GM), an architecture that maintains an $O(n)$-sized state and accesses it through sparse, dynamic routing. Unlike methods with fixed-size states or sparse but static routing, GM preserves $O(n)$ complexity in its sparse layers without restricting the potentially accessible state size to $O(1)$. Instead, GM uses edges - pointer-like objects updated differentiably by a referral mechanism resembling pointer chasing. We replace 75% of the dense Transformer layers in Qwen3-0.6B with GM sparse layers and pretrain from scratch on 15.7B tokens. With only 2 of 4,096 tokens retrieved per KV head in each sparse layer, loss degrades only slightly; with 4, the best model marginally improves loss.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 171. [A Survey on Self-Improving Test-Time Intelligence: Feedback-Driven Adapting, Learning, and Scaling at Inference](https://arxiv.org/abs/2609.01679)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shuaicheng Niu, Guohao Chen, Yaofo Chen 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The ability of AI systems to improve their behavior during deployment is becoming increasingly important. As inference moves beyond the static execution of a fixed trained model, a growing body of work studies how models can refine their behavior on the fly by exploiting test-time information and additional computation. These developments have largely evolved along two directions: methods that modify the model's state using test-time signals, and methods that improve predictions through extra inference-time resources such as more sampling and tool use. However, these directions are often studied in separate communities with different terminology, making their connections harder to see. In this survey, we present feedback-driven Test-Time Intelligence (TTI) as a unified perspective for understanding such deployment-time improvement. We use this view to relate test-time adaptation, test-time learning, and test-time scaling, highlighting both their distinctions and their growing overlap in hybrid systems. This unified framework helps connect previously fragmented ideas and provides a clearer conceptual foundation for studying inference-time self-improvement. We review major methodological paradigms, representative applications, and open challenges across vision, language, multimodal learning, generative models, robotics, and healthcare. Our goal is to provide a coherent foundation and research roadmap for the study of self-improving AI systems at test time.

---


### 172. [Cross-Model Distillation of a Human-Pose Foundation Model from Unannotated Infant Video for Markerless 3D Pose Estimation](https://arxiv.org/abs/2609.01840)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** R. James Cotton, Divya Joshi, Colleen Peyton  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spontaneous movement is one of the earliest windows onto an infant's neuromotor health, and structured clinical instruments that score it are validated early predictors of cerebral-palsy risk. However, they require specially trained raters, are time-consuming, and carry inter-rater variability. This motivates automated, video-based markerless assessment, especially as marker-based motion capture is impractical in infants. Yet the foundation models that make markerless capture possible are trained almost entirely on adults: our recent multi-view infant study found that no single model is jointly best, with strong 2D keypoint accuracy and direct 3D body recovery split across different models. While that study identifies this trade-off, it does not resolve it. Here, we perform cross-model distillation from the Sapiens 2 pose model into the SAM 3D Body model, using unannotated infant video alone. A frozen teacher supplies dense pseudo-labels, and a differentiable renderer aligns the predicted mesh to them in the training loop. On eleven held-out infants (18 sessions, 173 recordings) under our prior study's multi-view protocol, fine-tuning improves same-view 2D keypoint agreement with the Sapiens reference (median body percentage of correct keypoints @ 10px 0.22 -> 0.42, face 0.22 -> 0.42) and Procrustes-aligned mean per joint 3D position error (25.5 -> 22.2 mm). This demonstrates how cross-model distillation improves SAM 3D Body model performance on infants.

---


### 173. [OutageDiT: A Generative Foundation Model for Power Outage Forecasting and Scenario Simulation](https://arxiv.org/abs/2609.01896)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yunqin Zhu, Feng Qiu, Yao Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Power-outage planning requires scenarios before an event occurs. These scenarios must represent uncertainty in magnitude, timing, and duration while preserving temporal dependence. However, severe events are rare, and data from any single region contain few examples of extreme outage and restoration patterns. To address this challenge, we introduce OutageDiT, a foundation model for generating seven-day outage trajectories at quarter-hour resolution, trained on outage and weather records across the United States. Specifically, a condition encoder processes the historical context and known future covariates once per forecast, and a shallow flow decoder reuses the resulting horizon-aligned states to generate complete trajectories. The resulting samples support point forecasting, uncertainty quantification, and conditional event simulation within one deep generative model. Across outage forecasting benchmarks, OutageDiT improves forecast accuracy and scenario quality over strong baselines and supports zero-shot transfer to held-out regions. Together, these results position conditional outage simulation as a bridge from outage forecasting to operational planning under uncertainty.

---


### 174. [Morphology signal in whole slide image foundation models can automatically triage slides](https://arxiv.org/abs/2609.01987)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ayushi Sinha, Shashank Yadav, Benjamin Holmes 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Patient exams in the cancer diagnosis and staging process typically generate several whole slide images (WSIs). One of the initial steps in training models on WSI data is identifying one or a few slides containing tumor or other diagnostic biomarkers necessary for downstream prediction tasks such as estimating recurrence risk or progression-free survival. This step requires tedious manual curation by experienced pathologists. Many published datasets make the artificial assumption of 1 slide per patient. Alternatively, all slides per patient may be used for model training, which may dilute the signal from the few slides containing tumor or other relevant information. In this paper, we present a pipeline to overcome these challenges using publicly available WSI foundation models (FMs). Our evaluations show that ranking WSIs based on predictions from zero-shot classification using WSI FMs accurately identifies slides with the most tumor, indicating that WSI FMs contain sufficient morphology signal to automatically triage slides. We also present a formulation for ranked evaluation to benchmark FM performance in slide triage. We show, on multiple datasets, that tumor slides are identified in the top-2 ranked slides for patients with up to 43 slides.

---


### 175. [World-Coherent Decoding: Self-Verifying Test-Time Planning for World Action Models](https://arxiv.org/abs/2609.02159)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chuhan Zhang, Seiji Ito, Kenta Hoshino 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) aim to control robots by stochastically generating visual futures and then decoding actions, but empirical observations indicate that the results can strongly depend on which future is selected. We propose World-Coherent-Decoding (WCD), a self-verifying test-time planning framework that treats WAM rollouts as falsifiable future--action hypotheses. At each decision step, WCD samples multiple candidates from a frozen WAM and ranks them using internal generative signals: flow-based video surprisal for visual plausibility and action path effort for action-generation stability. After execution, the realized observation audits the selected imagination, yielding an imagination--reality mismatch that trains a lightweight online predictor for future candidate selection. Thus, WCD converts delayed self-verification into pre-execution reliability estimation without updating the backbone model. On RoboTwin 2.0, WCD improves Hard success under limited randomized-scene supervision from $55.80\%$ to $60.90\%$, with a $+16.43$ gains on Horizon-3 tasks, and shows qualitative robustness on real Franka visual-shift tests. These results highlight a simple principle: test-time scaling for WAMs depends less on sampling more futures than on selecting reliable ones.

---


### 176. [Before the Script, Set the Stage: How Worldview Simulation Amplifies Psychologically Grounded Persuasion in Multi-Turn Jailbreaking](https://arxiv.org/abs/2609.02414)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Siyu Chen, Haoran Wang, Xiaojian Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-turn jailbreak attacks demonstrate that harmful intent can be distributed across dialogue, yet existing methods obscure what conversational mechanisms drive vulnerability. We introduce BLUEPRINT, a safety-evaluation framework separating a factorized social-influence strategy space from WORLDVIEWSIM, a cross-turn situational context module. Monte Carlo Tree Search optimizes turn-level combinations of 18 theory-grounded influence factors across a four-turn trajectory. Across six frontier models, BLUEPRINT achieves near-ceiling ASR on major open-weight and proprietary models, while requiring the fewest average queries (2.46). The resulting trajectories further reveal model-specific vulnerability among resistant targets: each responds to distinct influence factors and strategy transitions, yet all share a common recovery pathway-shifting toward concrete, executable task framing consistently escapes hard-refusal states. Ablations confirm operational cues matter most: making requests actionable has the largest impact, gain framing is unusually potent, and some legitimacy appeals can backfire. These findings suggest robust multi-turn safety requires monitoring not only harmful content, but also how dialogue state makes unsafe requests appear concrete and locally executable.

---


### 177. [Adapting a Foundation Model for Lunar Surface Height Estimation](https://arxiv.org/abs/2609.02448)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Patrick Bauer, Marius Schwinning, Melanie Siegel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital elevation models (DEMs) can provide accurate height information, making it invaluable for analyzing the lunar surface. As the European Space Agency (ESA) prepares for future lunar missions that aim to land on the Moon, a precise method for height estimation will be essential for hazardous terrain that could endanger the landing approach. Traditional approaches to generate DEMs from imagery, such as shape from shading (SfS) and stereophotogrammetry (SPG) have been proven highly valuable for this task. However, due to advancements in machine learning, especially computer vision, the focus has shifted towards monocular depth estimation via deep learning. The lunar surface is covered by rocks and craters, and classic hazard detection methods rely solely on 2D image data. Our goal is to address this issue by developing a relative lunar surface height estimator that can provide additional information for hazard localization. In this letter, we present a methodology that builds on the well-known zero-shot relative depth estimation model Depth Anything V2 (DAV2). Other works have been using it as a state-of-the-art comparison for their proposed lunar DEM estimation method, but without adaptations to the target domain. Thus, it may underperform. Therefore, we propose a fine-tuning strategy with publicly available SPG-derived DEM data of the lunar surface. Our results demonstrate a significant improvement in performance compared to the zero-shot model, effectively transforming DAV2 into a reliable relative depth estimator of the lunar surface.

---


> [!TIP]
> 当前位于：**151-177**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-177**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
