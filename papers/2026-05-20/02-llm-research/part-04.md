# 🧠 大模型相关研究 | 2026年05月20日

> 本类共 **346** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-346](./part-07.md)

---

### 151. [ConflictRAG: Detecting and Resolving Knowledge Conflicts in Retrieval Augmented Generation](https://arxiv.org/abs/2605.17301)

**<font color=#1a73e8>作者：</font>** Chenyu Wang, Yingmin Liu, Yang Shu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems implicitly assume mutual consistency among retrieved documents -- an assumption that frequently fails in practice. We present ConflictRAG, a conflict-aware RAG framework that detects, classifies, and resolves knowledge conflicts prior to answer generation. The framework introduces three contributions: (1) a two-stage conflict detection module combining a lightweight embedding-based MLP classifier with selective LLM refinement, reducing API costs by 62% while maintaining 90.8% detection accuracy; (2) an Entropy-TOPSIS framework for data-driven source credibility assessment, improving selection accuracy by 7.1% over manual heuristics; and (3) a Conflict-Aware RAG Score (CARS) for diagnostic evaluation of conflict-handling capabilities. Experiments on three benchmarks against six baselines demonstrate 88.7% conflict-detection F1 and consistent 5.3--6.1% correctness gains over the strongest conflict-aware baseline, with the pipeline transferring effectively across backbone LLMs.

---


### 152. [Compress the Context, Keep the Commitments: A Formal Framework for Verifiable LLM Context Compression](https://arxiv.org/abs/2605.17304)

**<font color=#1a73e8>作者：</font>** Natalia Trukhina, Vadim Vashkelis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM context is not just tokens; it is a set of commitments. Long-running conversations accumulate goals, constraints, decisions, preferences, tool results, retrieved evidence, artifacts, and safety boundaries that future responses must preserve. Existing context-management methods reduce length through truncation, retrieval, summarization, memory systems, or token-level prompt compression, but they rarely specify which semantic commitments must survive compression or how their preservation should be measured. We propose Context Codec, a commitment-level framework for compressing prompts and chat histories.
Context Codec represents dialogue state as typed, source-grounded semantic atoms with canonical identity, equivalence, conflict, confidence, risk, and evidence spans. It separates five concerns - extraction, normalization, representation, rendering, and verification - and introduces metrics for Critical Atom Recall, Weighted Atom Recall, Commitment Density, and round-trip recoverability. It also defines a taxonomy of semantic compression errors, a concrete normalization procedure, conservative fallback rules for low-confidence and safety-critical atoms, and Context Compression Language (CCL), an ASCII-first compact rendering of canonical JSON atoms. In a small diagnostic study, CCL-Core occupies a useful middle ground between structured prose and JSON: more explicit and auditable than prose, usually more compact than JSON, and less risky than heavily minified notation. The result is not a claim that shorthand solves compression, but a framework for making context compression verifiable: compress the conversation, keep the commitments.

---


### 153. [CyberCorrect: A Cybernetic Framework for Closed-Loop Self-Correction in Large Language Models](https://arxiv.org/abs/2605.17305)

**<font color=#1a73e8>作者：</font>** Yuning Wu, Yingmin Liu, Yang Shu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) self-correction -- the ability to detect and fix errors in generated outputs -- remains largely ad hoc, relying on generic prompts such as "please reconsider your answer" without systematic error analysis or convergence guarantees. We propose CyberCorrect, a framework that formalizes LLM self-correction as a closed-loop control system grounded in cybernetic theory. The framework models the LLM generator as the plant and introduces a tri-modal Error Detector (combining self-consistency, verbalized confidence, and logic-chain verification) as the sensor. A type-directed Correction Controller generates targeted repair instructions based on diagnosed error categories, while a Convergence Judge determines iteration termination using stability criteria adapted from control theory. We further introduce three control-theoretic evaluation metrics -- convergence rate, overshoot rate, and oscillation rate -- that capture correction dynamics beyond final accuracy. Experiments on our constructed CyberCorrect-Bench (440 reasoning tasks with annotated error types and correction paths) show that CyberCorrect achieves 79.8% final accuracy, improving upon the best existing self-correction method by 6.2 percentage points, while reducing overshoot (erroneous over-correction) by 41% through its convergence control mechanism.

---


### 154. [Reasoning Before Diagnosis: Physician-Inspired Structured Thinking for ECG Classification](https://arxiv.org/abs/2605.17308)

**<font color=#1a73e8>作者：</font>** Yang Wu, Xiaoyan Yuan, Hau-San Wong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electrocardiogram (ECG) diagnosis in clinical practice relies on structured reasoning over multiple hierarchical aspects, including cardiac rhythm, conduction properties, waveform morphology, and overall diagnostic impression. However, most existing approaches predict labels directly from ECG signals without explicit clinical reasoning, resulting in opaque decisions that lack clinical alignment. To bridge this gap, we propose CardioThink, a physician-inspired multimodal large language model (MLLM) framework that explicitly models the diagnostic reasoning process through human-interpretable intermediate stages (rhythm, conduction, morphology, and impression) to derive final classification results. Furthermore, we introduce Structured Set Policy Optimization (SSPO) to jointly optimize adherence to this structured reasoning format and the accuracy of variable-size diagnostic sets, without requiring manually annotated reasoning traces. Extensive experiments on diverse ECG benchmarks demonstrate the significant superiority of our approach in diagnostic accuracy, while simultaneously providing interpretable clinical reasoning. Notably, reasoning quality evaluations confirm that SSPO substantially enhances the clinical validity of the generated rationales. These findings reveal that moving beyond direct label prediction toward structured reasoning offers a more clinically aligned direction for future ECG modeling.

---


### 155. [Attention Hijacking: Response Manipulation Across Queries in Vision-Language Models](https://arxiv.org/abs/2605.17310)

**<font color=#1a73e8>作者：</font>** Zhiqiang Wang, Dongrui Liu, Yan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing adversarial attacks on vision-language models (VLMs) can steer model outputs toward attacker-specified target responses, but their effectiveness often degrades when the same perturbed input is paired with different textual queries. This paper studies cross-query response manipulation, where a single adversarial example is expected to remain effective across diverse user queries. We first analyze the limitations of existing attacks and find that successful transfer is closely associated with preserving an image-dominant attention pattern during response generation. Motivated by the observation, we propose \textbf{Attention Hijacking}, a novel adversarial attack that explicitly steers internal attention distributions toward a persistent image-dominant pattern. By amplifying the influence of visual tokens on target response tokens while suppressing the competing influence of textual tokens, our method reduces the dependence of the manipulated output on the specific wording of the query. Extensive experiments on widely used VLMs show that Attention Hijacking substantially improves cross-query transferability across diverse target responses and unseen queries. The method also extends effectively to multiple attack scenarios, offering new insights into the role of attention stability in transferable response manipulation for VLMs.

---


### 156. [Leveraging Error Diversity in Group Rollouts for Reinforcement Learning](https://arxiv.org/abs/2605.17333)

**<font color=#1a73e8>作者：</font>** Wenpu Liu, Yuqi Xu, Weichu Xie 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Verifiable Rewards (RLVR) typically samples multiple responses per prompt and assigns binary rewards based on individual correctness, yet the collective structure of the group output, specifically the distribution of errors, is largely discarded. We identify this as a missed opportunity: empirical analysis reveals that error diversity within a group is a strong predictor of training success, with problems eliciting diverse wrong answers benefiting substantially more from RLVR than those producing homogeneous failures. Motivated by this observation, we propose Error Diversity Advantage Shaping (EDAS), a lightweight, algorithm-agnostic technique that modulates the advantage signal for incorrect rollouts based on intra-group error diversity. EDAS amplifies penalties for dominant, repeated errors and attenuates penalties for rare, exploratory ones, thereby encouraging the model to maintain diverse reasoning paths and discouraging error perseveration. Crucially, EDAS operates as a simple post-hoc adjustment that can be seamlessly integrated into any RLVR algorithm. We validate EDAS on top of several mainstream RLVR methods across a series of models and seven challenging math benchmarks, demonstrating consistent improvements. Notably, EDAS yields an average improvement of 6.29 points over DAPO on Qwen3-8B across seven benchmarks, confirming that exploiting the latent information in group rollouts is a broadly effective strategy for strengthening RLVR.

---


### 157. [Olivia: Harmonizing Time Series Foundation Models with Power Spectral Density](https://arxiv.org/abs/2605.17340)

**<font color=#1a73e8>作者：</font>** Jingru Fei, Kun Yi, Alex Xing Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models rely on large-scale pretraining over diverse datasets across domains, yet their heterogeneity in temporal patterns could hinder the effectiveness of training and learning transferable time series representations. Inspired a fundamental concept, normalized power spectral density (PSD) in signal processing, we assume harmonizing datasets via PSDs in the spectral domain could reduce mismatches and enhance pretraining. We then go beyond the direct intractable minimization optimization and innovatively reformulate it as a principled harmonization approach. Specifically, we propose Harmonizer, a module that reshapes spectral structures and implicitly harmonizing PSDs across datasets, which theoretically corresponds to a shared reparameterization of second-order temporal correlations. Our theoretical analysis further reveals token interactions with Harmonizer can be efficiently mediated by a compact set of resonators, motivating a HarmonicAttention design that performs self-attention in a low-dimensional interaction space. Then, we propose Olivia, a novel time series foundation model built upon these harmonization mechanisms. Extensive experiments on two large-scale benchmarks (TSLib and GIFT-Eval) and extra 6 datasets from GluonTS, demonstrate Olivia consistently achieves state-of-the-art performance under zero-shot, few-shot, and full-shot forecasting scenarios. Our code is available at \url{this https URL}.

---


### 158. [Single-Sample Black-Box Membership Inference Attack against Vision-Language Models via Cross-modal Semantic Alignment](https://arxiv.org/abs/2605.17341)

**<font color=#1a73e8>作者：</font>** Jiaqing Li, Yajuan Lu, Xiaochuan Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have achieved remarkable success, yet their reliance on massive datasets and unintended memorization of training data raise significant data security risk. Membership Inference Attacks (MIAs) aim to assess these risks by determining whether a data sample was included in a model's training set. However, existing MIA methods against VLMs face critical bottlenecks: gray-box method relies on internal logits that are typically restricted in real-world Application Programming Interfaces (APIs), while black-box method depends on large-scale statistical distributions, which struggle in single-sample scenarios. To this end, we investigate MIAs from the perspective of cross-modal semantic alignment, and observe that member images exhibit significantly stronger image-caption alignment due to training memorization, whereas generated captions for non-members may deviate from the original visual content. Leveraging this insight, we propose a novel MIA framework designed for strict black-box and single-sample setting that quantifies such alignment within a joint embedding space, thereby bypassing these unrealistic assumptions. We conducted extensive experiments on three open-source and two closed-source VLMs. On the VL-MIA/Flicker dataset, our method achieves an AUC of 0.821 against LLaVA-1.5, significantly outperforming existing baselines. Furthermore, it remains robust under diverse image perturbations, highlighting its practicality.

---


### 159. [Transitivity Meets Cyclicity: Explicit Preference Decomposition for Dynamic Large Language Model Alignment](https://arxiv.org/abs/2605.17342)

**<font color=#1a73e8>作者：</font>** Yucong Huang, Xiucheng Li, Kaiqi Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard RLHF relies on transitive scalar rewards, failing to capture the cyclic nature of human preferences. While some approaches like the General Preference Model (GPM) address this, we identify a theoretical limitation: their implicit formulation entangles hierarchy with cyclicity, failing to guarantee dominant solutions. To address this, we propose the Hybrid Reward-Cyclic (HRC) model, which utilizes game-theoretic decomposition to explicitly disentangle preferences into orthogonal transitive (scalar) and cyclic (vector) components. Complementing this, we introduce Dynamic Self-Play Preference Optimization (DSPPO), which treats alignment as a time-varying game to progressively guide the policy toward the Nash equilibrium. Synthetic data experiments further validate HRC's structural superiority in mixed transitive--cyclic settings, where HRC converges faster and achieves higher accuracy than GPM. Experiments on RewardBench 2 demonstrate that HRC consistently improves over both BT and GPM baselines (e.g., +1.23% on Gemma-2B-it). In particular, its superior performance in the Ties domain empirically validates the model's robustness in handling complex, non-strict preferences. Extensive downstream evaluations on AlpacaEval 2.0, Arena-Hard-v0.1, and MT-Bench confirm the efficacy of our framework. Notably, when using Gemma-2B-it as the base preference model, HRC+DSPPO achieves a peak length-controlled win-rate of 44.75% on AlpacaEval 2.0 and 46.8% on Arena-Hard-v0.1, significantly outperforming SPPO baselines trained with BT or GPM. Our code is publicly available at this https URL.

---


### 160. [AMATA: Adaptive Multi-Agent Trajectory Alignment for Knowledge-Intensive Question Answering](https://arxiv.org/abs/2605.17352)

**<font color=#1a73e8>作者：</font>** Taolin Zhang, Dongyang Li, Chen Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite substantial advances in large language models (LLMs), generating factually consistent responses for knowledge-intensive question answering remains challenging. These difficulties are primarily due to hallucinations and the limitations of LLMs in bridging long-tail knowledge gaps. To address this, we propose AMATA, an Adaptive Multi-Agent Trajectory Alignment framework that dynamically integrates external knowledge to improve response interpretability and factual grounding. Our architecture leverages six specialized agents that collaboratively perform structured actions for complex question reasoning. We formalize multi-agent collaboration with external tools as a trajectory preference alignment problem, incorporating question-aware agent customization and inter-agent preference harmonization. AMATA introduces two principal innovations: (1) Intra-Trajectory Preference Learning, which learns objective-oriented preferences to prioritize critical agents, and (2) Inter-Agent Dependency Learning, which captures cross-agent tool dependencies through a novel dependency-aware direct preference optimization technique. Empirical results show that AMATA consistently outperforms baseline approaches, knowledge-augmented frameworks, and LLM-based trajectory systems on five established knowledge-intensive QA benchmarks. Further analysis demonstrates the efficiency of our method in reducing token consumption.

---


### 161. [Learning Transferable Topology Priors for Multi-Agent LLM Collaboration Across Domains](https://arxiv.org/abs/2605.17359)

**<font color=#1a73e8>作者：</font>** Taolin Zhang, Zijie Zhou, Jiuheng Wan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems have shown strong potential for complex reasoning by coordinating specialized agents through structured communication. However, existing topology-evolution methods typically construct or optimize a collaboration topology for each query from scratch, leading to substantial online search overhead, high inference-time token consumption, and limited scalability in multi-domain settings. We propose TopoPrior, a framework for learning transferable topology priors for multi-agent LLM collaboration across domains. Rather than repeatedly searching for effective collaboration structures online, TopoPrior learns reusable topology priors from reference collaboration graphs collected offline from multiple domains and uses them to generate query-conditioned initial collaboration graphs for downstream refinement. By shifting part of topology search from per-query online optimization to offline prior learning, TopoPrior amortizes search cost while remaining compatible with existing topology-evolution backbones. Technically, TopoPrior contains two key components. First, a transferable topology prior learning module employs a conditional variational graph framework to capture reusable structural regularities across domains in a latent space. Second, a query-conditioned latent adaptation module introduces adversarial alignment to reduce unnecessary domain discrepancy while preserving query-relevant structural variation. Experiments on multi-domain reasoning benchmarks show that TopoPrior consistently improves several heterogeneous topology-evolution backbones while reducing online inference-time token usage, with only modest additional trainable parameters. These results suggest that transferable topology initialization is an effective and lightweight mechanism for improving the efficiency of multi-agent LLM collaboration across domains.

---


### 162. [Omni-DuplexEval: Evaluating Real-time Duplex Omni-modal Interaction](https://arxiv.org/abs/2605.17360)

**<font color=#1a73e8>作者：</font>** Chaoqun He, Mingyang Xiang, Yingjing Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time duplex interaction is essential for multimodal AI systems operating in real-world scenarios, where models must continuously process streaming inputs and respond at appropriate moments. However, most existing multimodal large language models (MLLMs) are evaluated in offline settings, where the entire video input is processed before any response is generated. While recent work has started to explore real-time duplex MLLMs, there is still no comprehensive benchmark or automatic evaluation method for this setting. To address this gap, we propose Omni-DuplexEval, a benchmark for systematically evaluating real-time duplex interaction. The benchmark consists of two complementary scenarios: (1) Real-Time Description, which evaluates the ability to generate continuous, time-aligned responses that track evolving multimodal inputs, and (2) Proactive Reminder, which evaluates the ability to identify salient events and respond at appropriate moments. Omni-DuplexEval contains 660 videos with fine-grained, human-annotated labels and precise temporal metadata, spanning 9 tasks grounded in real-world scenarios, where all questions are formulated as open-ended queries. We further introduce an automatic evaluation framework based on LLM-as-a-Judge, which enables systematic assessment by jointly evaluating response-content alignment and response timing through timestamp-aware and sequential reasoning, achieving strong alignment with human judgments. Experiments on state-of-the-art duplex MLLMs reveal substantial limitations. The best-performing model achieves only 39.6% overall, while scoring only 20.0% on Proactive Reminder. Our analysis identifies two key challenges: models struggle to balance timely responses with coherent, holistic content generation, and they often fail to determine both when to respond and what to produce. We hope our work facilitates further progress in MLLMs.

---


### 163. [\textsc{MasFACT}: Continual Multi-Agent Topology Learning via Geometry-Aware Posterior Transfer](https://arxiv.org/abs/2605.17361)

**<font color=#1a73e8>作者：</font>** Xuefei Wang, Jialu Wang, Fengbo Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) powered by large language models (LLMs) have emerged as a powerful paradigm for complex problem solving, where performance critically depends on the underlying inter-agent communication topology. However, existing topology generation methods mainly optimize for isolated tasks, while real-world deployments involve streams of evolving tasks, requiring previously effective collaboration patterns to be retained and reused rather than rediscovered or overwritten. We identify a previously underexplored failure mode, \emph{topology forgetting}, in which adapting to new tasks shifts the topology generator away from communication structures required by earlier tasks. This issue stems from cross-task misalignment in both agent-level functional semantics and relational communication structures. To address this challenge, we propose \textbf{\textsc{MasFACT}}, a geometry-aware posterior transfer framework that preserves and reuses historical collaboration knowledge as transferable topology priors. We transfer these priors across task-specific agent spaces through Fused Gromov-Wasserstein optimal transport and perform PAC-Bayes-guided conservative posterior adaptation to balance task-specific plasticity with structural stability. Experiments across class-, domain-, and task-level continual settings demonstrate that \textsc{MasFACT} consistently improves average accuracy while reducing topology forgetting compared to strong topology generation and replay-based baselines, and can be seamlessly integrated with different MAS topology generators.

---


### 164. [NewsLens: A Multi-Agent Framework for Adversarial News Bias Navigation](https://arxiv.org/abs/2605.17364)

**<font color=#1a73e8>作者：</font>** Joy Bose  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Media bias detection has predominantly been framed as a classification task: assign a political label to an article or outlet. We argue this framing is too shallow: it identifies that bias exists but not where, how, or crucially, what is structurally omitted. We present NewsLens, a five-agent adversarial pipeline for structured news bias navigation. A Fact Verifier, Progressive Framing Analyst, Conservative Framing Analyst, Propaganda Detector, and Neutral Summarizer collaborate to deconstruct articles into interpretable framing maps, exposing ideological omissions, rhetorical manipulation, and framing boundaries. The system is evaluated on 15 articles across four geopolitical event clusters (India-Pakistan Kashmir, Gaza, Climate Policy, Ukraine) using Qwen2.5-3B-Instruct (4-bit quantised, Google Colab T4), with cross-model validation using Mistral 7B on the Kashmir cluster. Center outlets show the highest mean Perspective Divergence Score (PDS: Qwen 0.907, Mistral 0.729 on Kashmir subset); conservative-framing outlets show the highest mean Manipulation Index (MI: 0.600 across both models). Cross-model comparison shows high consistency for high-propaganda content (Republic World delta-PDS=0.125, MI=0.8 both models) and greater variance for nuanced reporting. Mann-Whitney U tests find no statistically significant between-group differences at n=15, reported honestly as a sample-size limitation confirmed by post-hoc power analysis. A partial ablation removing the Propaganda Detector shows degraded omission precision in the Neutral Summarizer output. The architecture extends prior lexical-geometric bias work to agentic LLM reasoning, and is fully reproducible using open-weight models without API keys.

---


### 165. [CBT-Audio: Evaluating Audio Language Models for Patient-Side Distress Intensity Estimation in CBT Session Recordings](https://arxiv.org/abs/2605.17370)

**<font color=#1a73e8>作者：</font>** Qixuan Hu, Shuchang Ye, Xumou Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cognitive behavioural therapy is widely used to help patients understand and manage psychological distress. It is often delivered through spoken conversation, where therapists attend not only to what patients say, but also to how they say it, because these cues can help therapists decide how to respond and adapt treatment. Progress in building AI systems for CBT remains largely limited to text, partly because most available datasets are text based and shareable spoken CBT data are scarce under ethical and privacy constraints. This creates a blind spot because text based models and evaluations cannot capture the mismatch between the transcript and the patient's voice, even though therapists often rely on this mismatch to understand patient distress. We introduce CBT-Audio, a dataset for evaluating patient distress estimation from spoken CBT sessions with audio language models. CBT-Audio contains 1,802 patient turns from 96 publicly available CBT recordings, with turn-level distress labels validated on an experts-annotated subset. We evaluate 10 open source audio language models under three input conditions, where models receive only patient audio, only the transcript, or both audio and transcript. Our results show that audio can provide useful information beyond text, especially when combined with transcripts. Adding audio to transcript input improves distress estimation over using the transcript alone in 8 of 10 model families, with significant gains in 4, and case studies show the clearest benefit when verbal content and vocal delivery diverge. CBT-Audio makes spoken patient behaviour measurable for AI evaluation in CBT-related tasks and supports future work on audio language models for mental health interaction.

---


### 166. [Learning Faster with Better Tokens: Parameter-Efficient Vocabulary Adaptation for Specialized Text Summarization](https://arxiv.org/abs/2605.17379)

**<font color=#1a73e8>作者：</font>** Gunjan Balde, Soumyadeep Roy, Mainack Mondal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models pretrained on general-domain corpora often exhibit tokenization inefficiencies when applied to specialized domains. Although continual pretraining for domain adaptation partially alleviate performance degradation, it does not resolve the fundamental vocabulary mismatch. To address this gap, we introduce a targeted parameter-efficient domain adaptation approach that combines vocabulary adaptation with pretraining for LLM-based text summarization. Our unified framework augments pretrained tokenizers with domain-specific tokens while selectively replacing under-trained and unreachable tokens to limit parameter growth. We evaluate our approach on Llama-3.1-8B and Qwen2.5-7B across legal and medical summarization tasks on a challenge-oriented evaluation protocol focused on expert-driven text and summaries which typically has higher concentration of over-fragmented Out-of-Vocabulary (OOV) words. The vocabulary adaptation algorithm enhances the overall quality of the summarization model by improving semantic similarity between the generated summaries and their references. In addition, the adapted model produces summaries that incorporate more appropriate novel and domain-specific words, leading to improved coherence, relevance, and faithfulness. We further observe that our proposed approach significantly reduce training time by $35-55\%$ over continual pretraining and reduce parameter counts up to $37\%$ w.r.t expansion-only methods. We make the codebase publicly available at this https URL.

---


### 167. [ADR: An Agentic Detection System for Enterprise Agentic AI Security](https://arxiv.org/abs/2605.17380)

**<font color=#1a73e8>作者：</font>** Chenning Li, Pan Hu, Justin Xu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present the Agentic AI Detection and Response (ADR) system, the first large-scale, production-proven enterprise framework for securing AI agents operating through the Model Context Protocol (MCP). We identify three persistent challenges in this domain: (1) limited observability -- existing Endpoint Detection and Response (EDR) tools see file writes but not the agent reasoning, prompts, or causal chains linking intent to execution; (2) insufficient robustness -- static defenses constrained by pre-defined rules fail to generalize across diverse attack techniques and enterprise contexts; and (3) high detection costs -- LLM-based inference is prohibitively expensive at scale. ADR addresses these challenges via three components: the ADR Sensor for high-fidelity agentic telemetry, the ADR Explorer for systematic pre-deployment red teaming and hard-example generation, and the ADR Detector for scalable, two-tier online detection combining fast triage with context-aware reasoning. Deployed at Uber for over ten months, ADR has sustained reliable detection in production with growing adoption reaching over 7,200 unique hosts and processing over 10,000 agent sessions daily, uncovering hundreds of credential exposures across 26 categories and enabling a shift-left prevention layer (97.2% precision, 206 detected credentials). To validate the approach and enable community adoption, we introduce ADR-Bench (302 tasks, 17 techniques, 133 MCP servers), where ADR achieves zero false positives while detecting 67% of attacks -- outperforming three state-of-the-art baselines (ALRPHFS, GuardAgent, LlamaFirewall) by 2--4x in F1-score. On AgentDojo (public prompt injection benchmark), ADR detects all attacks with only three false alarms out of 93 tasks.

---


### 168. [QQJ: Quantifying Qualitative Judgment for Scalable and Human-Aligned Evaluation of Generative AI](https://arxiv.org/abs/2605.17382)

**<font color=#1a73e8>作者：</font>** Marjan Veysi, Pirooz Shamsinejadbabaki, Mohammad Zare 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid progress of generative artificial intelligence has exposed fundamental limitations in existing evaluation methodologies, particularly for open-ended, creative, and human-facing tasks. Traditional automatic metrics rely on surface-level statistical similarity and often fail to reflect human perceptions of quality, while purely human evaluation, although reliable, is costly, subjective, and difficult to scale. Recent approaches using large language models as evaluators offer improved scalability but frequently lack explicit grounding in human-defined evaluation principles, leading to bias and inconsistency. In this paper, we introduce Quantifying Qualitative Judgment (QQJ), a scalable and human-centric evaluation framework that explicitly bridges the gap between human judgment and automated assessment. QQJ separates the definition of quality from its execution by anchoring evaluation in expert-designed, multi-dimensional rubrics and calibrating large language model evaluators to align with expert reasoning using a small, high-quality annotation set. This design enables consistent, interpretable, and scalable evaluation across diverse generative tasks and modalities. Extensive experiments on text and image generation demonstrate that QQJ achieves substantially stronger alignment with human judgment than traditional automatic metrics and unconstrained LLM-based evaluators. Moreover, QQJ exhibits improved stability across repeated evaluations and superior diagnostic capability in identifying critical failure modes such as hallucination and intent mismatch. These results indicate that structured qualitative judgment can be operationalized at scale without sacrificing interpretability or human alignment, positioning QQJ as a practical foundation for reliable evaluation of modern generative AI systems.

---


### 169. [MiniGPT: Rebuilding GPT from First Principles](https://arxiv.org/abs/2605.17398)

**<font color=#1a73e8>作者：</font>** Jibin Joseph  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents MiniGPT, a compact from-scratch implementation of GPT-style autoregressive language modeling in PyTorch. The aim is to rebuild the core GPT pipeline from first principles after studying the design of nanoGPT by Andrej Karpathy, while keeping the model and training code independently written in a single notebook. MiniGPT implements token and positional embeddings, causal multi-head self-attention, pre-LayerNorm Transformer blocks, residual connections, feed-forward MLP layers, next-token cross-entropy training (teacher forcing), validation tracking, checkpoint selection, and autoregressive text generation. This paper evaluates the implementation on Tiny Shakespeare dataset using character-level tokenization. A baseline 0.83M-parameter model reaches a validation loss of 1.7236 after 3000 training iterations. A stronger 10.77M-parameter configuration, using a larger context length and improved training settings, reaches a best validation loss of 1.4780 and generates text with recognizable Shakespeare-style dialogue structure. MiniGPT does not introduce a new language-model architecture. Instead, it documents a clear and reproducible implementation path from raw text to trained character-level generation, including design choices, training behavior, generation quality, and practical limitations.

---


### 170. [DP-SelFT: Differentially Private Selective Fine-Tuning for Large Language Models](https://arxiv.org/abs/2605.17432)

**<font color=#1a73e8>作者：</font>** Haichao Sha, Zihao Wang, Yuncheng Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are commonly adapted to downstream tasks through fine-tuning, but fine-tuning data often contains sensitive information that may be leaked by the resulting model. Differential privacy (DP) offers formal protection against such leakage, yet DP fine-tuning of LLMs still suffers from substantial utility degradation due to gradient clipping and noise injection. Existing work improves this trade-off by combining DP with parameter-efficient fine-tuning methods such as LoRA, which constrain the form of updates. In this work, we study a complementary direction: selective fine-tuning, which constrains where updates are applied.
We propose DP-SelFT, a framework for differentially private selective fine-tuning of LLMs. DP-SelFT addresses three DP-specific challenges in parameter selection: avoiding repeated privacy cost, improving stability under noisy estimates, and selecting parameters that remain useful under clipped and noisy updates. It first constructs a lightweight DP synthetic dataset and performs selection only on this synthetic data, so the selection stage incurs no additional privacy cost. It then conducts layer-level selection by temporarily training candidate layer subsets on a synthetic training split and evaluating them on a synthetic validation split. Crucially, this temporary training is performed under a perturbation regime matched to downstream DP fine-tuning, with worst-case perturbations of the same scale as DP noise. This favors layer subsets that are not only learnable but also robust to noisy private updates. Experiments on benchmark tasks show that DP-SelFT consistently improves the privacy--utility trade-off over existing DP fine-tuning baselines under the same privacy guarantees.

---


### 171. [Medical Context Distorts Decisions in Clinical Vision Language Models](https://arxiv.org/abs/2605.17436)

**<font color=#1a73e8>作者：</font>** David Restrepo, Ira Ktena, Maria Vakalopoulou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly proposed for clinical decision support, yet their reliability in real-world scenarios that require integrating both visual and textual context from medical records remains poorly characterized. This paper identifies three failure modes: (1) modality over-reliance on text over images, (2) spurious reliance on irrelevant clinical history, and (3) prompt sensitivity across semantically equivalent inputs. We evaluate a diverse set of general-domain and medically-tuned open and closed VLMs on chest x-ray tasks using MIMIC-CXR. By systematically manipulating image-text alignment, clinical history, and prompt formulations, we found that VLM decisions are dominated by the text modality, even when visual evidence is available. Moreover, we observed that VLMs are heavily influenced by irrelevant reports, while minor prompt changes can reverse correct image-based predictions. Our findings underscore the need for explicit safeguards and stress-testing before considering the use of these models in clinical practice.

---


### 172. [Analyzing Error Propagation in Korean Spoken QA with ASR-LLM Cascades](https://arxiv.org/abs/2605.17443)

**<font color=#1a73e8>作者：</font>** Donghyuk Jung, Youngwon Choi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We analyze how automatic speech recognition (ASR) errors propagate through ASR-LLM cascades in Korean spoken question answering (SQA), focusing on downstream semantic failures that conventional ASR metrics cannot fully capture. Our analysis shows that the relative downstream degradation caused by ASR errors is consistent across LLMs with different absolute performance, suggesting that cascade degradation largely tracks ASR-stage information loss. We further identify single-character Korean ASR errors as a distinct semantic-failure channel, where the gold answer becomes entirely absent from the downstream prediction despite only a minimal transcription difference. Finally, an auxiliary comparison shows that a large audio language model outperforms an ASR-LLM pipeline with a matched language backbone in noisy Korean SQA, indicating the potential of direct audio input to mitigate transcript-induced information loss.

---


### 173. [DeTrack: A Benchmark and Altitude-Aware Dual World Model for Drone-embodied Tracking](https://arxiv.org/abs/2605.17451)

**<font color=#1a73e8>作者：</font>** Guyue Hu, Haoming Liu, Siyuan Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial object tracking has broad applications in public safety, emergency rescue, wildlife monitoring, and related fields. However, existing aerial tracking benchmarks are mainly based on passive 2D video sequences captured from fixed camera locations or predefined flight paths, where drones are treated as passive cameras rather than embodied agents that actively perceive, interact, and control their motion in dynamic 3D scenes. In this paper, we define a new drone-embodied tracking task, termed DeTrack, which requires a drone to track a target in interactive 3D environments using online egocentric observations and active flight control in a closed loop. We build a large-scale benchmark containing 11,368 target trajectories across diverse scenes, rendering conditions, semantic regions, and moving distractors, together with evaluation metrics for target visibility, tracking accuracy, and trajectory success. We further propose AaDWorlds, an altitude-aware dual world model framework for drone-embodied tracking. AaDWorlds consists of an altitude-aware perception module and dual world models that imagine future states under both high- and low-altitude regimes. By combining pseudo altitude-aware observations and imagined future states, AaDWorlds alleviates the intrinsic altitude-mediated contradiction between target visibility and flight safety. Experiments on the DeTrack benchmark demonstrate that AaDWorlds improves closed-loop tracking performance across all evaluation metrics.

---


### 174. [VerifyMAS: Hypothesis Verification for Failure Attribution in LLM Multi-Agent Systems](https://arxiv.org/abs/2605.17467)

**<font color=#1a73e8>作者：</font>** Hezhe Qiao, Hanghang Tong, Ee-Peng Lim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model-driven multi-agent systems (LLM-MAS) excel at complex tasks, yet unreliable agents remain a key bottleneck to system-level reliability. Automatic failure attribution is therefore critical, but existing approaches, such as direct prediction of agent-error pairs and agent-first failure attribution, rely on local logs of agents and miss global failures that only manifest over full interaction trajectories, such as cross-step inconsistencies and inter-agent coordination errors. Moreover, directly predicting failures induces a large combinatorial search space, hindering fine-grained attribution. To address these challenges, we propose VerifyMAS, a hypothesis verification framework for agent failure attribution. Instead of directly predicting faulty agents and error types, VerifyMAS formulates and verifies failure hypotheses against full trajectories. This verification-based approach decomposes attribution into trajectory-level error validation and fine-grained agent localization, providing an error-first attribution approach that captures global failure patterns while substantially reducing the search space. We further introduce a hypothesis-based data construction strategy grounded in a structured error taxonomy and fine-tune a specialized LLM verifier model for trajectory-level failure verification and agent attribution. Experiments on Aegis-Bench and Who&When show that VerifyMAS consistently improves diverse backbone models, including open-source Qwen and API-based GPT models, outperforming prior methods without sacrificing inference efficiency for long multi-agent trajectories.

---


### 175. [An Interpretable Closed-Loop Intelligent Tutoring System for Multimodal Affective Feedback in Asynchronous Presentation Training](https://arxiv.org/abs/2605.17468)

**<font color=#1a73e8>作者：</font>** Hung-Yue Suen, Kuo-En Hung  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper presents an interpretable closed-loop Intelligent Tutoring System (ITS) that supports feedback-guided practice for developing on-camera oral presentation skills at scale. The system operationalizes a seven-dimensional Behaviorally Anchored Rating Scale (BARS) and implements a three-layer interpretable feedback architecture that connects rubric-aligned multimodal scoring, audience-perceived expressive diagnostics, and retrieval-augmented conversational coaching to support deliberate practice. Built on an XGBoost backbone, the ITS maps multimodal inputs (facial, vocal, textual, and oculomotor features) into evidence-based feedback that can be traced back to observable performance cues. Trained on 10,360 Massive Open Online Course (MOOC) video segments, the system achieved rubric-aligned scoring with performance levels comparable to expert ratings (R2 = 0.48-0.61, Spearman's rho = 0.69-0.78, MAE = 0.43-0.57). In a pre-post validation study with 204 adult learners over a 30-day practice window, participants demonstrated significant improvements across all seven BARS dimensions (Cohen's d = 0.39-0.90), with practice frequency showing a strong positive association with posttest performance after controlling for baseline scores and demographics. The results demonstrate how multimodal analytic outputs can be systematically transformed into observable behavioral change through an integrated feedback architecture, advancing explainable and pedagogically grounded ITS design for performance-based competencies.

---


### 176. [WinQ: Accelerating Quantization-Aware Training of Language Models Around Saddle Points](https://arxiv.org/abs/2605.17471)

**<font color=#1a73e8>作者：</font>** Dongyue Li, Zechun Liu, Kai Yi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization-aware training (QAT) is widely adopted to quantize language models by training full-precision weights using gradients from the quantized model. The main bottleneck is its slow convergence and early performance plateau, particularly below 4-bit-widths. While this problem has been observed in prior work, its precise cause remains unclear. In this paper, we analyze the convergence of QAT by estimating the spectrum of the loss-surface Hessians. We find that the weights converge to flat regions around saddle points, where a large fraction of the Hessian eigenvalues are both positive and negative. During training, an increasing fraction of Hessian eigenvalues concentrates around zero, whose magnitude decreases. At lower bit-widths, the magnitude of eigenvalues in the Hessian spectrum is significantly smaller. To mitigate these issues, we propose an algorithm called WinQ to accelerate QAT, which involves: (1) periodically resetting weights to the linear interpolation of full-precision and quantized weights, reducing the distance to the quantization grid and increasing eigenvalue magnitude, and (2) computing gradients of noise-injected weights to regularize the Hessian. Extensive experiments show that WinQ accelerates QAT by up to 4 times across various quantization methods and models. Under the same training cost, WinQ improves state-of-the-art sub-4-bit quantization by up to 8.8%. These results are consistent across 16 settings with different language models, quantization methods, and bit widths.

---


### 177. [Omni-Customizer: End-to-End MultiModal Customization for Joint Audio-Video Generation](https://arxiv.org/abs/2605.17488)

**<font color=#1a73e8>作者：</font>** Yuheng Chen, Qingdong He, Teng Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The landscape of joint audio and video generation has been fundamentally transformed by the advent of powerful foundation models. Despite these strides, achieving cohesive multimodal customization for the simultaneous preservation of visual identities and vocal timbres across multiple interacting subjects remains largely underexplored. To bridge this gap, we present Omni-Customizer, an end-to-end framework targeted at the precise binding and seamless fusion of multimodal identity information. Specifically, we introduce an Omni-Context Fusion (OCF) module that effectively enriches the base textual prompt with dense, multimodal identity cues, along with a Masked TTS Cross-Attention (MTP-CA) mechanism explicitly designed to prevent the severe "speech leakage" problem. Within this architecture, we propose Semantic-Anchored Multimodal RoPE (SA-MRoPE) to anchor visual and audio reference tokens, along with TTS embeddings, to their corresponding semantic descriptions, enabling structured multimodal fusion and robust identity binding. Furthermore, we devise a comprehensive training strategy that incorporates interleaved audio-video scheduling to rapidly adapt the audio branch to multilingual scenarios without degrading foundational priors, and a progressive in-pair to cross-pair curriculum to facilitate the learning of high-level and robust identity features. Extensive experiments demonstrate that Omni-Customizer achieves state-of-the-art performance in dual-modal customized generation, excelling across visual identity similarity, timbre consistency, precise audio-video synchronization, and overall video-audio fidelity.

---


### 178. [Employing Vision-Language Models for Face Image Quality Assessment](https://arxiv.org/abs/2605.17489)

**<font color=#1a73e8>作者：</font>** Erdi Sarıtaş, Eren Onaran, Vitomir Štruc 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face Image Quality Assessment (FIQA) is a crucial control step in biometric pipelines. It ensures only reliable samples are processed to maintain system accuracy. State-of-the-art FIQA methods achieve high utility but typically operate as "black boxes." They produce scalar scores without human-interpretable justifications. This lack of transparency limits their effectiveness in human-in-the-loop scenarios, such as automated border control, where actionable feedback is essential. In this paper, we investigate the potential of off-the-shelf Vision-Language Models (VLMs) to bridge this gap by performing FIQA in a zero-shot setting. We present a comprehensive evaluation framework for assessing VLM performance. This involves benchmarking traditional FIQA methods through error-versus-reject curves. Additionally, using a diverse set of datasets, ranging from surveillance-oriented to synthetically generated, we analyzed their interpretability, consistency, and robustness to prompt changes. Our results show biometric utility performance depends significantly on architecture, not merely on parameter count. Most VLMs' outputs align with those of traditional methods. We also find that VLM ranking performance and the generated scores may vary across prompts. Our synthetic ablation study shows that while increasing the parameter count can improve internal consistency, it yields worse degradation-detection performance than smaller models. These findings suggest that zero-shot FIQA score estimation using VLMs is promising and could effectively complement conventional FIQA pipelines as an interpretability module. The codes are available at this https URL.

---


### 179. [Self-Supervised On-Policy Distillation for Reasoning Language Models](https://arxiv.org/abs/2605.17497)

**<font color=#1a73e8>作者：</font>** Zhiquan Tan, Yinrong Hong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> GRPO-style RLVR trains reasoning models from multiple on-policy attempts per prompt, but typically uses these attempts only through terminal rewards. We show that a mixed group contains a richer process signal: a correct completion is a self-generated witness of how the current policy can solve the problem, while a wrong completion provides on-policy prefixes where the policy needs correction. We introduce \emph{Self-Supervised On-Policy Distillation} (SSOPD), which distills a teacher distribution conditioned on the shortest correct completion into prefixes of the longest wrong completion. This converts intra-group correct--wrong contrast into dense process supervision without external solution traces. A stopping-time view motivates the shortest-correct / longest-wrong rule as a finite-group approximation to editing persistent failures toward fast-success actions, and a prompt-level frontier weight concentrates the auxiliary loss where correct and wrong branches coexist. Across AIME 2024, AIME 2025, and HMMT 2025, SSOPD improves over GRPO in all nine model-benchmark settings. On Qwen3-8B, it reaches a macro Avg@12 of 65.6, outperforming GRPO by 1.6 points and the solution-conditioned OPSD baseline by 0.8 points. Code will be released at this https URL.

---


### 180. [RAG-based EEG-to-Text Translation Using Deep Learning and LLMs](https://arxiv.org/abs/2605.17503)

**<font color=#1a73e8>作者：</font>** Enrico Collautti, Xiaopeng Mao, Luca Tonin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The decoding of linguistic information from electroencephalography (EEG) signals remains an extremely challenging problem in brain-computer interface (BCI) research. In particular, sentence-level decoding from EEG is difficult due to the low signal-to-noise ratio of these recordings. Previous studies tackling this problem have typically failed to surpass random baseline performance unless teacher forcing is used during the inference phase. In this work, we propose a retrieval-augmented generation (RAG)-based sentence-level EEG-to-text decoding pipeline that combines an EEG encoder aligned with semantic sentence embeddings, a vector retrieval stage, and a large language model (LLM) to refine retrieved sentences into coherent output. Experiments are conducted on the Zurich Cognitive Language Processing Corpus (ZuCo) dataset, which contains single-trial EEG recordings collected during silent reading. To evaluate whether the system extracts meaningful information from these EEG signals, the results are compared with a random baseline. In nine subjects, the proposed pipeline outperforms the random baseline, achieving a mean cosine similarity of 0.181 +- 0.022 compared to 0.139 +- 0.029 for the baseline, corresponding to a relative improvement of 30.45%. Statistical analysis further confirms that this improvement is significant, following a strict evaluation workflow where inference is performed without access to ground-truth labels.

---


### 181. [CasualSynth: Generating Structurally Sound Synthetic Data](https://arxiv.org/abs/2605.17528)

**<font color=#1a73e8>作者：</font>** Zehua Cheng, Wei Dai, Jiahao Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) generate realistic synthetic data but offer no guarantee that their outputs respect the causal mechanisms governing the target domain. We introduce CausalSynth, a framework that decouples causal structure generation from semantic realization, yielding synthetic data that is both causally valid and linguistically rich. The framework operates in three phases. First, a Structural Causal Model (SCM) - a tuple of structural equations defined over a directed acyclic graph (DAG) generates causal skeletons, i.e., variable assignments that satisfy the Global Markov Property of the governing DAG, via ancestral sampling. Second, an LLM acts as a constrained \emph{realizer}, a conditional translator that maps each skeleton to a high-dimensional observation such as a clinical note or a transaction log. Third, an Iterative Consistency Verification module detects structural violations through deterministic extraction and feeds targeted corrections back to the LLM, forming a closed-loop refinement process. We identify the Semantic Backdoor problem the systematic tendency of LLMs to override imposed causal facts with pre-training priors -- and prove that our iterative mechanism reduces the resulting selection bias relative to standard rejection sampling. On three causal benchmarks (ASIA, ALARM, and MIMIC-Struct), CausalSynth preserved conditional independencies with false-positive rates near the nominal $\alpha=0.05$ level and achieved realizability rates above 96% with 70B-parameter LLM backbones. The framework additionally supports principled interventional and counterfactual generation through noise retention and graph mutilation.

---


### 182. [Self-supervised Hierarchical Visual Reasoning with World Model](https://arxiv.org/abs/2605.17537)

**<font color=#1a73e8>作者：</font>** Yuanfei Xu, Lin Liu, Wengang Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> 3D open-world environments with adversarial opponents remain a core challenge for reinforcement learning due to their vast state spaces. Effective reasoning representations are essential in such settings. While existing self-supervised visual foresight reasoning approaches often suffer from multi-step error accumulation, many recent studies resort to injecting domain-specific knowledge for more stable guidance. Our key insight is that the photorealistic fidelity of visual reasoning representations is secondary; what truly matters is providing informative, task-relevant signals. To this end, we propose ResDreamer, a hierarchical world model in which each higher-level layer is trained to reconstruct the residuals of the layer below. This design enables progressive abstraction of increasingly sophisticated world dynamics and fosters the emergence of richer latent representations. Drawing inspiration from the "Bitter Lesson", ResDreamer trains its reasoning representations in a purely self-supervised manner. The higher-level residual representations are used to modulate lower-level predictions, allowing the world model to scale effectively with only linearly increasing cross-layer communication costs. Experiments show that ResDreamer achieves state-of-the-art sample efficiency and parameter efficiency. This scalable hierarchical visual foresight reasoning architecture paves the way for more capable online RL agents in open-ended, dynamic environments. The code is accessible at \url{this https URL}.

---


### 183. [Memory-Guided Tree Search with Cross-Branch Knowledge Transfer for LLM Solver Synthesis](https://arxiv.org/abs/2605.17539)

**<font color=#1a73e8>作者：</font>** Fatemeh Haji, Javier Delarosa Quiros, Peyman Najafirad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Combinatorial optimization (CO) underlies decision-making from logistics to chip design, where infeasible solutions are operationally unusable and small quality gains translate into substantial economic value. Recent work uses large language models (LLMs) to automate solver synthesis: generating executable solver programs from natural-language specifications. However, existing tree-search and evolutionary agents refine candidate trajectories in parallel without explicit knowledge transfer, reintroducing the same constraint violations and converging on similar algorithm families. We introduce MEMOIR, a memory-guided tree-search framework with a two-level memory hierarchy: branch-local memory preserves execution-grounded refinement details within a branch as it iterates on a single algorithmic design, while global memory stores compressed algorithmic and failure-mode summaries across branches. A reflection step at branch termination distills these summaries, enabling cross-branch transfer without polluting future contexts with low-level debugging traces. Across seven CO problems spanning scheduling, routing, packing, and geometric design, MEMOIR achieves 96.7% solution validity (a 9.2 point gap over the strongest baseline) and improves the average normalized score by 7.3 points at matched per-method execution budget. Over three independent runs on four problems, MEMOIR's run-to-run validity standard deviation is more than an order of magnitude below that of every baseline we evaluated in this setting, suggesting that memory-guided exploration yields consistent improvements rather than reflecting sampling variance.

---


### 184. [Evaluating Deep Research Agents on Expert Consulting Work: A Benchmark with Verifiers, Rubrics, and Cognitive Traps](https://arxiv.org/abs/2605.17554)

**<font color=#1a73e8>作者：</font>** Tanmay Asthana, Aman Saksena, Divyansh Sahu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier deep research agents (DRAs) plan a research task, synthesize across documents, and return a structured deliverable on demand. They are being deployed in enterprise workflows faster than they are being evaluated. Existing benchmarks measure factual recall, single-hop QA, or generic agentic skill, missing the multi-document, decision-grade work DRAs are deployed to produce. We introduce a benchmark targeting the structured analytical deliverables that fill a management consultant's typical week.
We grade three frontier agents, namely Claude Opus 4.6 with web search, OpenAI o3-deep-research, and Google Gemini 3.1 Pro deep-research, on 42 SME-authored prompts. Each of the 126 responses is scored on two layers: deterministic ground-truth verifiers (mean 13.8 per task) and a five-criterion 0-3 SME rubric, composed into a Verifier-Rubric Score (VRS) on 0-100. Most prompts embed cognitive traps that penalize surface-pattern matching. Acceptance under our joint threshold (rubric mean >= 2.5 and verifier rate >= 80%) is uniformly low: Gemini 21.4%, o3 9.5%, Claude 9.5%.
Mean VRS scores agree with published rubric-based benchmarks (our top 62.6 vs. APEX-v1 64.2, ProfBench 65.9, ResearchRubrics < 68%), validating the rubric construct. ACCEPT rates sit below APEX-Agents' MC-segment Pass@1 band (12.3-22.7%) on dedicated DR agents; our floor is three points lower despite the harness advantage, opened by stricter conjunctive grading and trap design.
Each agent fails distinctively. Claude produces the deliverable most reliably (4.5x the others' rate on file-required tasks) but carries the highest fabrication signature. o3 has the cleanest reasoning average yet drops required sections and propagates arithmetic errors. Gemini is bimodal, with the highest acceptance rate alongside the most zero-scored rubric cells.

---


### 185. [Beyond Accuracy: Robustness, Interpretability and Expressiveness of EEG Foundation Models](https://arxiv.org/abs/2605.17562)

**<font color=#1a73e8>作者：</font>** Urban Širca, Maryam Alimardani, Stefanos Zafeiriou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG foundation models (EEG-FMs) have been evaluated predominantly on clean, in-distribution accuracy, leaving their robustness, interpretability and representational quality largely unexamined. This study addresses these gaps by benchmarking six EEG-FMs against a baseline deep learning model across eight datasets. Beyond clean accuracy, we conduct three layers of analysis: (i) Robustness: we apply test-time perturbations including additive noise, random and region-based channel dropout and region-specific noise injection. Our analyses show that no single model dominates all failure modes. The most noise-robust model is among the most fragile under channel dropout and much of the dropout fragility disappears when channels are removed rather than zero-padded. (ii) Interpretability: we present the first application of Attention-Aware Layer-Wise Relevance Propagation (AttnLRP) to EEG-FMs and show that models broadly concentrate relevance on task-appropriate brain regions consistent with known neurophysiology. However, attribution maps remain spatially stable under perturbation while predictions degrade, suggesting that the models attend to the correct brain regions but decode corrupted content. (iii) Expressiveness: With block-wise probing we show that late blocks are repurposed during fine-tuning, while early blocks already hold task-related information. Furthermore, we demonstrate that the poor head-only performance previously attributed to low-quality pre-trained representations is largely explained by pooling and that EEG-FMs possess sufficient representational capacity when their token-level embeddings are preserved. Together, these findings provide the first systematic assessment of robustness, interpretability and expressiveness for EEG-FMs and highlight critical considerations for their development.

---


### 186. [Generalization or Memorization? Brittleness Testing for Chess-Trained Language Models](https://arxiv.org/abs/2605.17565)

**<font color=#1a73e8>作者：</font>** Ethan Tang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work has fine-tuned language models on chess data and reported high benchmark scores as evidence that the resulting models can understand the rules of chess, play full chess games at a professional level, or generate human-readable explanations grounded in expert knowledge. We train KinGPT, a 25M-parameter character-level language model trained only on (position, best-move) pairs, who exceeds 3B-parameter ChessGPT on a 600-puzzle mate-in-N suite and 4B-parameter C1-4B over a 20-theme puzzle benchmark. We examine several claims made in existing literature regarding chess-trained language models and assert that their impressive benchmark performance is largely explained by pattern-matching. We also demonstrate how LLM-Modulo, a verifier-in-the-loop framework, raises RedPajama 3B's best move accuracy from 1.2% to 21.2% and move generation validity from 19.3% to 95.3% on mate-in-N chess puzzles, comparable to gains achieved from ChessGPT's fine-tuning on chess-specific web corpora at a fraction of the cost. Our results illustrate how pairing a general LLM with an external verifier offers a more flexible alternative to directly training on synthetic data for well-defined domains. We open source all training/evaluation code, datasets, puzzle samples, and KinGPT model checkpoints for reproducibility.

---


### 187. [How Off-Policy Can GRPO Be? Mu-GRPO for Efficient LLM Reinforcement Learning](https://arxiv.org/abs/2605.17570)

**<font color=#1a73e8>作者：</font>** Minghao Tian, Yunfei Xie, Chen Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) has been a key driver of recent progress in reinforcement learning with verifiable rewards (RLVR) for large language models, but it is typically trained in a low-staleness, near-on-policy regime that incurs substantial system overhead. We ask a simple question: How off-policy can GRPO be? We show that GRPO-style algorithms can tolerate substantially larger rollout staleness than previously assumed, and propose Mu-GRPO, an RL training framework that organizes training into a small number (e.g., four) of large sequential generation-optimization stages. This design induces high rollout staleness while greatly reducing rollout-optimization switching overhead. To stabilize learning under stale data, Mu-GRPO combines relaxed clipping, which preserves useful stale-rollout gradients, with negative-advantage veto, which removes destabilizing post-trigger suffix updates in negative-advantage responses. Across five language models and multiple math reasoning benchmarks, Mu-GRPO matches or exceeds the performance of standard GRPO while achieving around 2x speedup in wall-clock training time, establishing a substantially improved performance-efficiency trade-off for LLM reinforcement learning.

---


### 188. [TAME: Test-Time Adversarial Prompt Tuning via Mixture-of-Experts for Vision-Language Models](https://arxiv.org/abs/2605.17577)

**<font color=#1a73e8>作者：</font>** Xin Wang, Yixu Wang, Jiaming Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale pre-trained Vision-Language models (VLMs), such as CLIP, exhibit strong zero-shot generalization, yet remain highly vulnerable to imperceptible adversarial perturbations, raising serious safety concerns for open-world deployment. To enhance robustness without requiring downstream task-specific retraining, we propose TAME, a novel test-time defense. Building upon our prior Test-Time Adversarial Prompt Tuning (TAPT), TAME introduces an architectural reformulation by replacing TAPT's single adaptive prompt with an input-conditioned Mixture-of-Experts (MoE) framework, enabling more expressive and adaptive defense. Specifically, TAME maintains a bank of learnable expert prompts and employs an input-dependent routing mechanism to aggregate a customized prompt mixture for each unlabeled test sample at inference time. This test-time defense mechanism is driven by three unsupervised objectives: (1) multi-view prediction entropy minimization, (2) layer-wise alignment of visual token statistics to precomputed clean and adversarial reference distributions, and (3) MoE regularization for balanced expert utilization and prompt diversity. We evaluated TAME on 11 benchmark datasets, including ImageNet and 10 additional zero-shot datasets. The results show that TAME improves the zero-shot adversarial robustness of the original CLIP by at least 49.1% under AutoAttack while largely preserving generalization on clean samples. TAME also consistently outperforms existing adversarial prompt tuning methods across multiple prompt designs, yielding an average robustness gain of at least 30.2%.

---


### 189. [ECG-WM: A Physiology-Informed ECG World Model for Clinical Intervention Simulation](https://arxiv.org/abs/2605.17580)

**<font color=#1a73e8>作者：</font>** Zhikang Chen, Yue Wang, Sen Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electrocardiogram (ECG)-based models have achieved strong performance in diagnostic tasks, yet they remain limited in modeling how cardiac dynamics evolve under external interventions. In particular, existing approaches focus primarily on static prediction and lack mechanisms to capture ECG variations under different pharmacological conditions. In this work, we propose an ECG World Model for action-conditioned predictive simulation of cardiac electrophysiology. Moving beyond disjoint pipelines, our framework features a principled integration of physiological ordinary differential equation (ODE) priors into latent diffusion dynamics via energy regularization. This structural constraint enables the synthesis of physiologically plausible post-intervention ECG trajectories while effectively mitigating generative hallucinations. Building on this simulation process, we introduce an uncertainty-aware evaluation strategy that leverages the stochasticity of diffusion sampling to characterize both the expected clinical risk and its variability, allowing a more reliable comparative assessment of candidate interventions. We evaluate our method across diverse settings, including controlled drug-response scenarios and real-world clinical records. Beyond standard waveform metrics, experimental results demonstrate improved risk calibration and strong alignment with expert-informed treatment preferences. These results establish our approach as a robust foundation for safe and intervention-aware clinical decision support.

---


### 190. [NeuSymMS: A Hybrid Neuro-Symbolic Memory System for Persistent, Self-Curating LLM Agents](https://arxiv.org/abs/2605.17596)

**<font color=#1a73e8>作者：</font>** Mujahid Sultan, Sri Thuraisamy, Daya Rajaratnam  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present NeuSymMS, an adaptive memory system that enables large language model (LLM) agents to learn, remember, and reason about users across sessions via a hybrid neuro-symbolic architecture. NeuSymMS couples neural fact extraction from unstructured dialogue with a CLIPS-based expert system that classifies, deduplicates, and reconciles facts under explicit lifecycle rules. The system represents knowledge as subject-relation-value triples stored in relational database management system, supports user/agents/agent-to-agents scoping, and implements a dual-horizon short-term/long-term memory model with access-based promotion and time-based pruning. NeuSymMS maintains continuity of memory while avoiding context-window bloat and cross-entity contamination. We argue that this architecture offers a practical path to trustworthy, auditable memory for production agentic systems and discuss its novelty relative to log retrieval, summarization, and key-value approaches.

---


### 191. [Mixture of Experts for Low-Resource LLMs](https://arxiv.org/abs/2605.17598)

**<font color=#1a73e8>作者：</font>** Ori Bar Joseph, Smadar Arvatz, Noam Kayzer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures enable efficient model scaling, yet expert routing behavior across underrepresented languages remains poorly understood. We analyze routing dynamics in two architecturally distinct MoE models -- a pure Transformer (Qwen3-30B-A3B) and a hybrid Mamba-Transformer (Nemotron-3-Nano-30B-A3B) -- using Hebrew as a morphologically rich, low-resource testbed. Both pre-trained models exhibit \emph{deep-layer routing collapse}: usage entropy drops sharply in final layers and tokens concentrate on a narrow expert subset, a pattern largely absent for English. Continual pre-training (CPT) on balanced bilingual data substantially corrects this imbalance, increasing entropy and shifting routing toward shared, language-agnostic experts; supervised fine-tuning (SFT) alone achieves less complete correction. Extending the analysis to Japanese reveals quantitatively consistent collapse signatures, providing cross-linguistic evidence that the phenomenon is a systematic consequence of pre-training underrepresentation rather than any language-intrinsic property. Routing improvements correlate with consistent downstream benchmark gains, positioning routing entropy and expert specialization as principled diagnostics for multilingual capacity in MoE systems.

---


### 192. [AutoRubric-T2I: Robust Rule-Based Reward Model for Text-to-Image Alignment](https://arxiv.org/abs/2605.17602)

**<font color=#1a73e8>作者：</font>** Kuei-Chun Kao, Daixuan Huo, Yuanhao Ban 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aligning Text-to-Image (T2I) generation models with human preferences increasingly relies on image reward models that score or rank generated images according to prompt alignment and perceptual quality. Existing reward models are commonly trained as Bradley-Terry (BT) preference models on large-scale human preference corpora, making them costly to train, difficult to adapt, and opaque in their evaluation criteria. Meanwhile, Vision-Language Model (VLM) judges can provide more fine-grained assessments through textual rubrics, but their manually designed or heuristically generated scoring rules may fail to reliably reflect human preferences. In this paper, we propose AutoRubric-T2I, the first rubric learning framework in T2I that automatically synthesizes and selects explicit rubrics for guiding VLM judges. AutoRubric-T2I first synthesizes reasoning traces from preference pairs into candidate rubrics, then uses a VLM judge to score paired images under each rubric, producing pairwise rubric-score differences for preference learning. To remove noisy and redundant rules, we further employ a $\ell_1$-Regularized Logistic Regression Refiner, which selects the Top-$N$ most discriminative rubrics. Extensive evaluations show that AutoRubric-T2I produces high-quality, interpretable reward signals using less than 0.01% of the annotated preference data, substantially reducing the need for large-scale reward-model training. On image reward benchmarks such as MMRB2, AutoRubric-T2I outperforms strong reward model baselines. We further validate AutoRubric-T2I as an RL reward on downstream T2I tasks, including TIIF and UniGenBench++, where it improves generation quality over scalar reward models using the Flow-GRPO pipeline on diffusion models.

---


### 193. [SafeLens: Deliberate and Efficient Video Guardrails with Fast-and-Slow Screening](https://arxiv.org/abs/2605.17610)

**<font color=#1a73e8>作者：</font>** Shahriar Kabir Nahin, Hadi Askari, Muhao Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid growth of online video platforms and AI-generated content has made reliable video guardrails a key challenge for safety and real-world deployment. While most videos can be screened through fast pattern recognition, a small subset requires deeper reasoning over temporally complex content and nuanced policy constraints. Existing approaches typically rely on large vision-language models applied uniformly across all inputs, resulting in high inference costs and inefficient allocation of computation. We propose SafeLens, a video guardrail framework that introduces a fast-and-slow inference architecture for efficient and accurate content moderation with variable computational cost across inputs. Additionally, we construct a high-quality dataset by applying influence-guided filtering to the SafeWatch Dataset, retaining only 2.4% of the original data. To further address limitations of training-time scaling, we enable test-time reasoning by augmenting the filtered data with structured Chain-of-Thought traces. Across real-world and AI-generated video benchmarks, SafeLens achieves state-of-the-art performance, outperforming strong open-source video guardrails (e.g., SafeWatch-8B, OmniGuard-7B) and closed-source models (e.g., GPT-5.4, Gemini-3.1-pro) while significantly reducing inference cost, demonstrating that efficient design serves to be more effective than scaling data or model size alone.

---


### 194. [Episodic-Semantic Memory Architecture for Long-Horizon Scientific Agents](https://arxiv.org/abs/2605.17625)

**<font color=#1a73e8>作者：</font>** Nikola Milosevic  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) evolve into persistent scientific collaborators, context window saturation has emerged as a critical bottleneck. Scientific workflows involving iterative data analysis and hypothesis refinement rapidly saturate even extended contexts with dense technical content, while monolithic approaches suffer from quadratic cost scaling and cognitive degradation. We evaluate a Dual Process Memory Architecture that decouples immediate episodic needs (constant 10-message window) from long-term consolidated knowledge (growing at approximately 3 tokens/message). Unlike prior social agent memory systems, our domain-specific consolidation addresses contradictory parameter evolution, multi-hop reasoning across experimental phases, and precise technical fact retention. Through large-scale evaluation spanning 15,000 messages with cross-model validation across six LLMs from three families (OpenAI, Anthropic, Google), totaling 1,440 queries, we establish three key findings. First, while full-context models fail at 10,000 messages due to context overflow, our system maintains 70-85% accuracy with 1-2 second latency using 62% fewer tokens (45,434 vs 120,000+ limit). Second, cross-model validation reveals architecture-level trade-offs independent of specific LLMs: Dual Process excels at numeric/temporal queries (65-90% accuracy) while RAG excels at historical retrieval (60-85%), suggesting complementary deployment strategies. Third, we identify a "Sim-to-Real" gap where synthetic tests maintain constant memory but realistic workflows exhibit linear growth (about 3 tokens/message), with consolidation quality emerging as the primary scalability bottleneck. The architecture successfully manages profiles with 14,000+ scientific facts (125k tokens), demonstrating that domain-specific memory consolidation enables sustained operation beyond full-context limits.

---


### 195. [SegRAG: Training-Free Retrieval-Augmented Semantic Segmentation](https://arxiv.org/abs/2605.17630)

**<font color=#1a73e8>作者：</font>** Abderrahmene Boudiaf, Irfan Hussain, Sajid Javed  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Here's a trimmed version under 1920 characters:
Open-vocabulary segmentation models such as SAM3 achieve strong performance through concept-level text prompting, yet degrade when the target class is visually underrepresented in pretraining data or when its appearance departs from canonical depictions. Text prompts provide no spatial signal to resolve such ambiguity. We present SegRAG, a training-free retrieval-augmented segmentation framework that grounds SAM3 with spatially precise, class-specific point prompts derived from a curated DINOv3 feature bank. During an offline stage, patch-level descriptors are extracted from annotated reference images using a frozen DINOv3 ViT-L/16 backbone and filtered by Intra-Class Cohesion Distillation (ICCD), retaining only prototypes that reliably retrieve within-class foreground. At inference, Topographic Similarity Grounding (TSG) computes a cosine-similarity landscape between the query image and retrieved prototypes, identifies spatially coherent high-confidence regions via connected-component analysis, and extracts peak locations through non-maximum suppression. These point prompts are delivered to SAM3 alongside the class-name text in a single joint grounding pass, enabling the mask decoder to resolve semantic intent and spatial evidence together. SegRAG requires no task-specific training and no synthetic data. On four open-vocabulary benchmarks it achieves consistent gains over the SAM3 text-only baseline, with improvements of up to +3.92 mIoU on LVIS. On AgML agricultural benchmarks representing a zero-shot domain transfer setting, it raises mean IoU from 25.27 to 59.24 (+33.97) and recovers individual classes from zero to over 95 mIoU. Ablation studies confirm that ICCD, TSG, and joint prompting each contribute independently and compound when combined. Code is available at this https URL.

---


### 196. [Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents](https://arxiv.org/abs/2605.17641)

**<font color=#1a73e8>作者：</font>** Saksham Sahai Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents rely on persistent memory to support interactions across sessions, yet existing memory systems often retrieve context using semantic similarity or broad history inclusion, treating retrieved memories as uniformly useful. This assumption is fragile because memories may be topically related while remaining irrelevant, stale, or misleading. We propose Causal Memory Intervention (CMI), a causal memory-selection technique that estimates how candidate memories affect the model's answer under controlled interventions, selecting memories that improve task performance while suppressing unstable, irrelevant, or harmful ones. To evaluate this setting, we introduce Causal-LoCoMo, a causally annotated benchmark derived from long conversational data, where each example contains a user request, a structured memory bank, useful memories, irrelevant distractors, and synthetic harmful memories. We compare CMI against vector, graph, reflection, summary, full-history, and no-memory baselines. Results show that CMI achieves a stronger balance between answer quality and robustness to misleading memory, suggesting that reliable long-term memory requires selecting context based on causal usefulness rather than relevance alone. The full framework, benchmark construction code, and experimental pipeline are available at this https URL.

---


### 197. [LLMForge: Multi-Backend Hardware-Aware Neural Architecture Search with Infinite-Head Attention for Edge Language Models](https://arxiv.org/abs/2605.17653)

**<font color=#1a73e8>作者：</font>** Xinting Jiang, Junyi Luo, Ruichen Qi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sub-billion-parameter Transformer language models are increasingly deployed on edge devices, where the privacy, latency, and operating-cost advantages of on-device inference are constrained by tight memory-bandwidth, energy, and thermal budgets that make architectural choice and accelerator-specific cost central to efficient inference. We present LLMForge, a hardware-aware neural architecture search (NAS) framework whose three composable contributions together make edge-LM architecture search hardware-conditioned, since different substrates impose different hardware cost bottlenecks. Infinite-Head Attention (IHA) decouples the number of query heads, KV groups, and per-head query/key and value dimensions, expanding the feasible per-layer attention configuration space by approximately 400x over grouped-query attention within our search-space ranges. Forge-Former, an encoder-based surrogate for ranking architectural candidates, outperforms MLP and random-forest baselines. Forge-DSE, an NSGA-II-based design-space-exploration engine, pairs Forge-Former with a multi-backend hardware cost model spanning GPUs, systolic accelerators, and ring-dataflow edge accelerators. Across four different hardware substrates, the searches converge to visibly different architectures whose shapes track each substrate's cost bottleneck. On the multi-chip ring substrate, our co-search returns three 300M-scale deployment-aware variants on the Pareto front. Each is re-trained on FineWeb-Edu-10BT under matched recipe against SmolLM2-360M and Qwen-0.5B architecture baselines. The accurate variant has the lowest validation loss 2.798 and competitive benchmark performance with fewer parameters, the energy-optimized variant lowers energy per token by 40%, and the latency-optimized variant lowers TTFT and TPOT by 43%.

---


### 198. [Multimodal Cultural Heritage Knowledge Graph Extension with Language and Vision Models](https://arxiv.org/abs/2605.17669)

**<font color=#1a73e8>作者：</font>** Yang Zhang, Nada Mimouni, Jean-Claude Moissinac 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The preservation and interpretation of cultural heritage increasingly rely on digital technologies, among which Knowledge Graphs (KGs) stand out for their ability to structure vast amounts of data. However, the construction and expansion of these KGs often face challenges due to the diverse and complex nature of cultural heritage information. In this paper, we propose a novel approach for extending KG resources in the domain of cultural heritage, which we applied to French data. First, we introduce a new knowledge graph in the domain of French cultural heritage, WJoconde, which is distinguished by its multimodality as it integrates both textual and image information of the entities. We further introduce three variants of WJoconde to facilitate downstream research, such as Knowledge Graph Completion (KGC). We also built a comprehensive benchmark for KGC methods on our dataset. Second, we propose a new framework for extending cultural heritage KGs using multi-modal approaches leveraging Large Language Models (LLMs) and Vision-Language Models (VLMs), which includes automated data extraction from unstructured resources combined with a special validation pipeline for grounding the output of both models, to further extend WJoconde. Our results show that by integrating the rich text and image information in cultural heritage data, we can efficiently enhance KGs with high reliability. We open-source all code and benchmark datasets with text and images, as well as the original data with an interactive access point

---


### 199. [Stop When Reasoning Converges: Semantic-Preserving Early Exit for Reasoning Models](https://arxiv.org/abs/2605.17672)

**<font color=#1a73e8>作者：</font>** Dehai Min, Giovanni Vaccarino, Huiyi Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) achieve strong performance by generating long chains of thought (CoT), but often overthink, continuing to reason after a solution has already stabilized and thereby wasting tokens and increasing latency. Existing inference-time early-exit methods rely primarily on answer-level signals, such as confidence or trial-answer consistency, to decide when to stop. However, these signals mainly reflect answer readiness rather than reasoning convergence: they may trigger before the model has finished exploring or self-correcting, causing premature exits that can degrade final-answer accuracy and leave the retained reasoning chain semantically incomplete. We identify reasoning-level semantic redundancy as a complementary signal for semantic-preserving early exit: when successive steps no longer add novel progress and instead revisit established conclusions, the reasoning trajectory has likely converged. Building on this insight, we propose PUMA, a plug-and-play framework that combines a lightweight Redundancy Detector with answer-level verification. The detector flags semantically redundant candidate exits, while verification confirms whether stopping is safe, allowing PUMA to remove redundant continuation while preserving both answer accuracy and a coherent reasoning prefix. Across five LRMs and five challenging reasoning benchmarks, PUMA achieves 26.2% average token reduction while preserving accuracy and retained CoT quality. Additional experiments on code generation, zero-shot vision-language reasoning, and learned stopping-policy internalization further demonstrate that reasoning-level redundancy is a robust, transferable, and learnable signal for efficient reasoning. Our code is available at \url{this https URL}.

---


### 200. [PULSE: Agentic Investigation with Passive Sensing for Proactive Intervention in Cancer Survivorship](https://arxiv.org/abs/2605.17679)

**<font color=#1a73e8>作者：</font>** Zhiyuan Wang, Ariful Islam, Indrajeet Ghosh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cancer survivors face elevated rates of depression, anxiety, and general emotional distress, yet the precise moments they most need support are often the moments when self-report is sparse, a phenomenon we term the diary paradox. Passive smartphone sensing offers a continuous, unobtrusive alternative, but prior sensing-based affect prediction has been limited by an accuracy ceiling, suggesting a bottleneck not only in available data, but in how behavioral signals are interpreted. We present PULSE, a system that shifts from fixed feature pipelines to agentic sensing investigation: LLM agents equipped with eight purpose-built tools autonomously query smartphone sensing data, compare current behavior against personalized baselines, and calibrate inferences through retrieval-augmented population-level comparisons. Rather than receiving pre-formatted feature summaries, agents decide which modalities to inspect, how far back to look, and how deeply to investigate, mirroring hypothesis-driven clinical reasoning. We evaluate PULSE through a 2*2 factorial design crossing reasoning architecture (structured vs. agentic) with data modality (sensing-only vs. with diary) on 50 cancer survivors from a longitudinal study of cancer survivors. Agentic reasoning is the primary driver of performance: agentic multimodal agent achieves balanced accuracy of 0.743 for emotion regulation desire with diary and sensing data, while agentic agents predict intervention availability at 0.713 with passive sensing data only. These results suggest that agentic investigation may be a cornerstone for unlocking the clinical value of passive sensing, advancing the feasibility of proactive just-in-time mental health support.

---


> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-346](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
