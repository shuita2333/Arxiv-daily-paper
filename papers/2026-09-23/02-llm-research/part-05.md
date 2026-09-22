# 🧠 大模型相关研究 | 2026年09月23日

> 本类共 **379** 篇论文：已确认 **359** 篇，待复核 **20** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-379](./part-08.md)

---

### 201. [MaskVLA: Visual Masking Against Trajectory Overfitting of Vision-Language-Action Model](https://arxiv.org/abs/2609.23565)

**<font color=#1a73e8>作者：</font>** Yuxuan Jiang, Jiaying Huang, Ge Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models integrate vision-language understanding with executable robot actions, enabling end-to-end learning for robot control. However, our empirical analysis reveals that existing models exhibit severe trajectory overfitting when finetuned on limited datasets. To guide the model in effectively utilizing wrist camera information, we propose MaskVLA, a masking-based fine-tuning strategy. By randomly masking a small portion of the main camera's visual information, the model is guided to autonomously learn more fine-grained, task-relevant, and effective visual features. This process leads to the emergence of robust policies, thereby enhancing the model's capability to tackle complex manipulation tasks and improving its generalization performance. Our method has been comprehensively evaluated on RoboTwin 2.0, achieving an average success rate improvement of 23.2% and 16.8% compared to $\pi_0$ and OpenVLA-OFT, respectively. Furthermore, experiments on real-world ALOHA robots also demonstrate the effectiveness of our approach.

---


### 202. [Error-Supervised Synthetic Learner Writing for Automated Essay Scoring](https://arxiv.org/abs/2609.23573)

**<font color=#1a73e8>作者：</font>** Duy Anh Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic essays can help reduce dependence on human-written data in Automated Essay Scoring (AES). However, they often lack realistic errors, limiting their ability to represent authentic human writing, particularly when the target texts are intended to resemble those produced by language learners. In this study, we present a simple approach that introduces error supervision into synthetic essay generation. Specifically, we fine-tune an LLM generator on error-annotated texts of the kind commonly used in Grammatical Error Detection (GED). To assess the utility of the proposed approach, we fine-tune and evaluate AES scorers under three data conditions: authentic essays, synthetic essays generated conventionally, and synthetic essays generated using our proposed approach. The results show that in the larger-data settings, the proposed approach outperforms the conventional synthetic baseline in 11 out of 12 dataset-metric comparisons, with performance in some cases approaching that of models trained on authentic essays. Despite these gains, performance under extremely low-resource settings remains mixed, with advantages over the conventional baseline only becoming more apparent at 200 training essays, although not consistently across datasets. Qualitative and quantitative analyses further show that the proposed approach produces learner-like errors whose distributions broadly resemble those observed in authentic essays.

---


### 203. [Global Ranks Survive, Selected Heads Shift: BOS-Sink Topology under 4-bit Weight-Only Quantization](https://arxiv.org/abs/2609.23585)

**<font color=#1a73e8>作者：</font>** Kuanlin Chen, Chen-Wei Kuo, Cheng-En Ou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sink-aware deployment may identify important first-token attention heads before a model is quantized, then reuse that map at the edge. We test when this shortcut is safe for 4-bit NF4 weight-only post-training quantization (PTQ). Our Sink Topology Consistency (STC) metrics separate global rank preservation, top-$k$ set overlap, and layerwise sink-mass shift, and distinguish per-input sensitivity from calibration-map transfer. Across Qwen2.5-0.5B, Qwen2.5-1.5B, and Llama-3.2-1B, global bf16-to-4-bit ranks remain high at 4,096 tokens ($\rho_s \geq 0.980$), yet top-$k$ Jaccard overlap is only 0.619-0.793, corresponding to 76.5-88.5% membership retention. The global statistic also masks local failures: terminal Qwen layers shift by 6.2-7.9x their model means, whereas Llama-3.2-1B shows low, nearly uniform drift. Under a C4-to-LongBench shift, cross-domain overlap degrades more than the within-domain precision comparison for both Qwen models, but not for Llama-3.2-1B. Matched-domain 4-bit recalibration reaches 90% of a split-half stability plateau at the smallest tested $n=8$ for both Qwen models and $n=32$ for Llama-3.2-1B, though not as a sharp threshold; for the two Qwen models, updating only selected layers does not reach the full-map stability criterion. On Jetson Orin NX, the 16-sample workload takes seconds for the two models with valid on-device sink measurements. The practical message is precise: global rankings often transfer, but discrete head sets, layer-local policies, and cross-domain calibration should be revalidated after quantization.

---


### 204. [Bilinear Optimization Divergence: Diagnosing Factor-Constrained LoRA Continual Learning](https://arxiv.org/abs/2609.23594)

**<font color=#1a73e8>作者：</font>** YongShun Wang, JianLin Su, Yong Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Orthogonality in a LoRA factor does not by itself specify what the composed update protects: the answer depends on the task-start state, the parameterization, and the realized optimizer displacement. We formalize this question through Bilinear Optimization Divergence (BOD), an anchor-relative diagnostic of effective-update response on selected historical features. The finite-step analysis distinguishes two cases. In a shared adapter, protecting the routing displacement leaves a learned-anchor residual through the changing companion factor. In a fresh zero-output block, a feasible routing state can protect the composed update while both current factors remain trainable. These conditions yield Semi-Frozen Orthogonal Routing (SFOR) for shared adapters and current-block hard protection for cumulative O-LoRA; Weight Residual Projection (WRP) enforces the required displacement after the optimizer step. Controlled two-task traces verify the predicted residual paths, reducing normalized historical response from 19.12% to 0.005% in the shared family and from 7.72% to 0.002% in the cumulative family. Four-task experiments on Qwen3-8B characterize the resulting trade-offs: SFOR improves backward transfer (BWT) from -2.47 to -0.86 with nearly unchanged average accuracy (AA), while O-LoRA hard protection improves three-order mean AA from 80.27% to 81.30% and forgetting measure (FM) from 2.20 to 0.43. Component controls also show that stricter feasibility need not improve final task performance. Together, the analysis and evidence provide an architecture-conditioned account of which constraint to enforce, how to enforce it, and how to interpret its empirical value.

---


### 205. [PETR: Prompt Ensembling with Training-free Routing for Vision-Language Models](https://arxiv.org/abs/2609.23600)

**<font color=#1a73e8>作者：</font>** Weihan Cai, Hao Tan, Xinping Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prompt learning efficiently adapts vision-language models (VLMs) to downstream tasks, but gains on seen classes often come at the expense of generalization to unseen classes. To address this limitation, we propose prompt ensembling with training-free routing (PETR), whose key innovation is a carefully designed dual-prompt architecture: two complementary prompts are learned from different data and objectives to emphasize seen class discrimination and unseen-class generalization, respectively. During training, both prompts are fine-tuned using a shared frozen CLIP backbone, and statistical information is collected from the training set logits. At inference time, we determine the similarity of each test sample to seen data, and route the sample to the most appropriate prompt branch. To the best of our knowledge, this is the first prompt tuning framework that performs training-free adaptive routing based on statistical similarity. This design provides an interpretable routing signal and avoids common MoE-style routing pathologies, such as router training instability and load imbalance. Extensive experiments on 11 benchmark datasets demonstrate that our framework consistently outperforms previous methods on both seen and unseen classes, achieving new state-of-the-art results.

---


### 206. [PREM: Prefix-Steered Recurrent Memory for Long-Video Understanding](https://arxiv.org/abs/2609.23601)

**<font color=#1a73e8>作者：</font>** Siru Zhong, Qiongyan Wang, Xiaohui Lv 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video understanding must capture transient visual evidence under strict token budgets, yet existing methods compress frames, append memory tokens, or alter internal key-value (KV) caches. We introduce Prefix-Steered Recurrent Memory (PREM), a memory-token-free framework for frozen vision-language models (VLMs). PREM separates video ingestion from query answering: a recurrent writer distills visual streams into a compact 256 KiB multi-slot associative state, while a question-conditioned readout adds memory-derived key/value (K/V) steering modulations to existing non-visual prompt prefixes during prefill. This enables write-once, query-many inference without extra prompt tokens or decoding recurrence. Across six long-video benchmarks in offline and streaming end-of-stream settings, PREM consistently outperforms frozen baselines at every evaluated visual budget. Under a constrained budget of 16 frames, PREM improves macro-average accuracy by 3.06% on Qwen2.5-VL-3B, with gains of 11.0% on action antonym identification and 9.9% on localized needle retrieval. These gains require tuning 0.24% of backbone parameters at 0.03 GiB of peak GPU memory overhead.

---


### 207. [Are Human-Aligned Models Models of Humans? A Turing-Test Gap in Preference Alignment](https://arxiv.org/abs/2609.23640)

**<font color=#1a73e8>作者：</font>** Suqin Yuan, Runqi Lin, Muyang Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human-feedback alignment has made language models useful assistants and is commonly described as aligning them with humans. However, the responses people prefer from an AI need not be the responses they themselves would give. We distinguish alignment with human preferences from alignment with human behavior, and show that alignment with human preferences can make model behavior less human-like even when both preferences and responses come entirely from humans. We call this the Turing-test gap. We show that preference alignment preserves the human response distribution only under a restrictive condition, and find no consistent evidence that real human preferences satisfy it. Empirically, the loss of human-response likelihood increases with the strength of preference weighting, regardless of its direction, and the gap also appears under standard DPO. These results establish human-likeness as an explicit dimension of alignment rather than something assumed to follow from preference alignment.

---


### 208. [Reassessing Global Gradient-Norm Imbalance in BLIP Fine-Tuning Across Physical Domains](https://arxiv.org/abs/2609.23655)

**<font color=#1a73e8>作者：</font>** Kiran Naseer, Samreen Azhar, Dwarikanath Mahapatra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Imbalanced gradient magnitudes between the visual and language pathways of a vision-language model are often treated as a defect to be corrected. We test that premise for one family of correction, deliberately excluding adaptive, signal-driven schemes (e.g. BalGrad, OGM, PMR, CGGM), which are a mechanistically distinct class outside this study's scope. Measuring the language-to-visual gradient-norm ratio, reported in parameter-normalised form, across nine fine-tuning conditions, three seeds, and three captioning datasets spanning distinct physical domain shifts -- underwater, aerial, radiological -- we find imbalance magnitude varies markedly across domains with no predictable ordering. A plain learning-rate reduction cuts imbalance substantially and lands within a few BLEU points of the best method on every dataset. Staged freezing reduces the ratio on every domain yet never ranks first; a schedule-only control isolates freezing as the cause on one dataset but not the other two. Forcing the two gradient groups to equal magnitude drives per-parameter imbalance close to zero on every domain, yet is both the best result in the study and the worst placement among full fine-tuning methods, on different datasets, with identical settings. Reductions in gradient-norm ratio do not consistently predict captioning performance across domains, and how a given level of balance is reached matters as much as the level itself. As a secondary finding, a commonly reused LoRA configuration applied to BLIP silently adapts zero visual parameters; correcting it improves BLEU-4 on all three datasets.

---


### 209. [Which Terrain Is Better? Preference Learning with VLM Prototypes for Off-Road Traversability Ranking](https://arxiv.org/abs/2609.23673)

**<font color=#1a73e8>作者：</font>** Ji-Hoon Hwang, Jisung Bae, E-In Son 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In vision-based off-road navigation, a robot needs to know not only which obstacles to avoid but also which terrain is better. The first is handled by freespace detection or semantic segmentation. The second is usually answered with a traversability score, but no universal ground truth exists for such a score, so perception falls back on a predefined value per semantic class or a freespace confidence. These scores say what a region is, not which region a robot should prefer. We therefore formulate this preference as visual traversability ranking, an ordering of visible terrain that can be supervised by comparisons between two regions. Standard annotations do not label preference, but they imply its direction. We present TravPro, which converts these annotations into ordered region pairs and fits a small readout on frozen vision--language model (VLM) patch tokens to these pairs. The tokens are clustered once into a fixed prototype bank, and the readout learns a preference score per prototype. The readout is then applied to every patch and serves as a teacher that turns sparse comparisons into dense preference pseudo-labels without pixel-wise annotation. An RGB student distills these maps into a dense terrain-preference map together with a non-ground mask that excludes obstacles and background from the ranking. On five unseen domains, TravPro reaches a mean pairwise accuracy of 0.915 against 0.783 for the strongest baseline, producing an ordering sensitive to surface condition that a per-class value cannot represent. The same VLM and the same supervision yield no such ordering when the VLM is prompted and the supervision is used as dense targets; what matters is how they are used.

---


### 210. [PhysAI-Bench: A Benchmark for LLM-Based Agentic Decision-Making in Autonomous UAV-Centric Physical AI](https://arxiv.org/abs/2609.23695)

**<font color=#1a73e8>作者：</font>** Mohamed Amine Ferrag, Merouane Debbah, Abderrahmane Lakas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Physical AI have accelerated the use of foundation models in autonomous systems such as unmanned aerial vehicles (UAVs), which must perceive, reason, plan, and act in dynamic environments. Existing benchmarks assess physical perception, intuitive physics, embodied navigation, and collaborative reasoning, but rarely evaluate the agentic decision-making required for reliable autonomy. We introduce \textit{PhysAI-Bench}, a benchmark for evaluating this capability. It contains 10,178 standardized decision instances automatically extracted from conversational traces of autonomous UAV missions. Each instance preserves mission context, temporal dependencies, physical constraints, Model Context Protocol (MCP) tool calls, Agent-to-Agent (A2A) interactions, sensor observations, and AI-native 6G network conditions, including latency, packet loss, throughput, edge load, and network slicing. We expose only information preceding each decision, preventing future-event leakage and approximating online decision-making. We evaluate 29 foundation models using a two-stage protocol. We select model-specific configurations from 12 combinations of zero-, three-, and five-shot prompting and four temperatures, tested in three runs on a 35-instance, human-verified development set. We then freeze each selected configuration and evaluate it in three runs on a fixed, episode-disjoint set of 500 instances. GPT-5.3 achieves the highest accuracy (52.00%), followed by GPT-5.2 (49.40%) and Grok~4.5 (49.07%). Few-shot prompting generally improves performance, while temperature has limited influence. The results demonstrate that reliable agentic decision-making in Physical AI remains an open challenge. The dataset is available at this https URL

---


### 211. [Distill What You Trust: Reliability-Aware Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2609.23697)

**<font color=#1a73e8>作者：</font>** Jie Sun, Mao Zheng, Mingyang Song 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-teacher on-policy distillation allows a student to learn from complementary specialists on its own trajectories. Domain-routed approaches, however, select one teacher per example and keep it fixed throughout the response. This design both depends on labels that mixed training corpora often lack and cannot adapt teacher selection when the expertise required changes within a trajectory. We propose \textbf{TrustMOPD}, which replaces example-level teacher selection with label-free, token-level supervision allocation. At each student-generated prefix, TrustMOPD uses each specialist's RL-induced displacement from a shared pre-RL reference as a proxy for local reliability, calibrates these scores across teachers, and constructs a weighted distillation target. Across mathematics, code, and instruction following, TrustMOPD outperforms the strongest label-free baseline, increasing the recovery ratio from $54.4\%$ to $91.5\%$ on \textsc{SingleCap} and from $54.5\%$ to $98.0\%$ on \textsc{MultiCap}, while approaching label-based MOPD on \textsc{SingleCap}. Randomizing token-level weights independently of the student-generated prefix performs no better than uniform weighting, supporting the importance of conditioning supervision on the evolving generation context.

---


### 212. [When the Agent Becomes the Kernel: A Systematization of Security on the Path to AI-Native Operating Systems](https://arxiv.org/abs/2609.23700)

**<font color=#1a73e8>作者：</font>** Li Zhang, Yang Sun, Jie Shi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model agents are now privileged principals that take consequential actions: editing code repositories, operating inboxes, completing purchases. Their authority is kernel-grade, but it comes without what classical systems security requires: a trusted mediator interposed on every access. Operating-system vendors are now rebuilding the platform around this de-facto agent kernel, inheriting complete mediation as a design problem. We systematize the security of such systems around a single distinction: a crossing mediated over provenance admits a deterministic check, while one over content semantics does not. A trust-boundary taxonomy locates where mediation must occur and isolates the central mediation gap at two kinds of semantic judgment: distinguishing data from instruction in untrusted input, and an authorized action from an unauthorized one. We argue that this gap leaves an irreducible residual of undetected attacks wherever inputs and actions are not restricted in advance to an enumerated set. The same distinction makes attack-success statistics actionable, placing each number on a spectrum from deployment debt (a sound deterministic mediator left unused) to a structural gap (no such mediator known). We systematize defenses across runtime monitoring, architectural separation, and authorization, and show that current evaluations tend to overstate deployed security through evaluation-validity failures. Finally, we carry that analysis forward beyond the de-facto kernel, to an architecture in which the model itself becomes the arbitration core, and derive the design constraints, open challenges, and research agenda for a security-first AI-native OS.

---


### 213. [Financial Language Models as Applied Artificial Intelligence Systems for News-Based Trading under Market Frictions](https://arxiv.org/abs/2609.23703)

**<font color=#1a73e8>作者：</font>** Kemal Kirtac  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial language models can transform unstructured firm-specific news into structured decision signals, but financial AI research lacks an integrated deployment framework for evaluating whether those signals remain useful in financial decision systems. Computer science research has developed strong methods for time-series forecasting, text classification, multimodal stock prediction, graph-based market modeling, and machine-learning operations, yet these streams do not provide a domain-specific protocol that jointly tests financial language-model outputs under event-time observability, probability calibration, execution timing, transaction costs, liquidity constraints, capacity limits, operational diagnostics, and statistical inference. We introduce MFAST, a Market-Friction-Aware Sentiment-to-Trading framework that converts timestamped financial text into auditable, reproducible, and market-feasible trading decisions. The application is news-based trading, where firm-specific text must be linked to securities before portfolio decisions can be evaluated. The framework links Refinitiv News Analytics to Center for Research in Security Prices (CRSP) equity data, restricts the primary out-of-sample evaluation to post-release news outside disclosed foundation-model data-freshness periods, and adds a public replication arm using open financial text and public price data. Results show that decoder-only language models outperform encoder baselines and dictionary sentiment in classification, calibration, return prediction, and net portfolio performance, while operational diagnostics reveal trade-offs among accuracy, latency, memory, throughput, and inference cost. The paper shows that credible evaluation of financial language models requires an end-to-end engineering approach combining language understanding, temporal discipline, market-friction-aware deployment, and reproducible validation.

---


### 214. [Layer-Aware Position Embeddings for Visual Token Pruning in Multimodal Large Language Models](https://arxiv.org/abs/2609.23715)

**<font color=#1a73e8>作者：</font>** Yahong Wang, Zhangkai Ni, Juncheng Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) incur substantial computational overhead due to the reliance on hundreds of visual tokens to represent images. While token pruning has emerged as a promising approach to reduce the inference cost of MLLMs, existing methods typically reassign position embeddings to the retained tokens using either sparse or continuous position embeddings, each introducing distinct limitations. Sparse position embeddings tend to decrease the attention value allocated to visual tokens, thereby degrading the perception capability of MLLMs, whereas continuous position embeddings disrupt the original spatial correspondence of visual tokens, leading to weakened grounding capability. To mitigate this issue, we perform layer-wise analysis of the language decoder and observe that intermediate layers play a critical role for maintaining the grounding capability of MLLMs under token pruning. Based on this observation, we propose a layer-aware position embedding strategy, which switches to sparse position embeddings at grounding-sensitive layers while maintaining continuous position embeddings elsewhere. Extensive experiments across representative pruning methods and diverse benchmarks demonstrate that our approach improves the comprehensive multimodal performance of pruned MLLMs compared with standard sparse and continuous position embeddings.

---


### 215. [STEVE: Stabilizing Textual Gradient-Based Prompt Optimization via Error-Driven Refinement and Regularized Verification](https://arxiv.org/abs/2609.23716)

**<font color=#1a73e8>作者：</font>** Yifan Xu, Yixuan Li, Xinzhuo Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Textual-gradient methods automate prompt optimization through natural-language feedback, but their iterative updates can be unstable. We identify two sources of this instability: noisy gradients produced from already-correct examples and over-specialization to hard cases that degrades performance on simpler inputs. We introduce STEVE, a stabilization framework with two coupled mechanisms. Error-Driven Refinement generates gradients only from incorrectly handled examples, concentrating updates on informative failures. Regularized Verification treats every update as provisional and accepts it only when improvement on hard cases does not cause unacceptable regression on a preservation set. Across ten reasoning benchmarks, three evaluator/optimizer models, and established prompt-optimization baselines, STEVE reduces degradation and produces more robust prompts. Additional evaluations with gpt-5.4-mini/gpt-5.4 on symbolic reasoning, GSM8K-Platinum, and DS-1000 show that these gains persist with newer models and larger test sets. STEVE therefore provides a practical way to improve the stability and effectiveness of textual-gradient prompt optimization.

---


### 216. [GRACE: Grounded Adversarial Reasoning over Canadian Law](https://arxiv.org/abs/2609.23726)

**<font color=#1a73e8>作者：</font>** Jiakang Xu, Wantong Huo, Udom Silparcha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have shown strong performance across a range of legal tasks, but existing benchmarks rarely evaluate the ability to take and defend a legal position, reason under incomplete information, or synthesize multiple statutory provisions. This gap is particularly pronounced for Canadian law, which remains underrepresented in legal NLP. We introduce GRACE (Grounded Reasoning Adversarial Canadian LEgal examples), a dataset of 1,915 question-reasoning-answer instances grounded in Canadian federal legislation. GRACE covers three reasoning modes: adversarial advocacy, uncertainty, and applied reasoning. We develop a pipeline that partitions raw statutory text, generates scenario-based questions and reasoning, and filters examples through model-free citation verification and LLM-based quality auditing. As a proof of concept, we fine-tune CLeAR-4B (Canadian Legal Adversarial Reasoning), a lightweight model for grounded legal reasoning, and evaluate it against the unmodified Qwen3-4B base model in open- and closed-book settings. CLeAR-4B substantially improves agreement with teacher outputs and statutory citation behavior when the relevant act text is provided, while its grounding degrades sharply when the statute is withheld. These results suggest that GRACE can support the development of lightweight legal models that reason more effectively from supplied statutory text.

---


### 217. [Constrained Decoding Eliminates Structural Failures in Small LLMs but Reveals a Scale-Dependent Semantic Gap](https://arxiv.org/abs/2609.23742)

**<font color=#1a73e8>作者：</font>** Akash Chavan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small open-source large language models (LLMs) in the 0.6B-4B parameter range are increasingly deployed for structured output generation (JSON, function calling, data extraction), yet little is known about how constrained decoding (CD) interacts with model scale in this regime. We benchmark five models from three families across 14 structured-output tasks under three decoding conditions (native, Outlines, XGrammar). We introduce a two-axis evaluation that separates structural correctness (schema validity) from semantic correctness (content accuracy). We find that CD eliminates all structural failures across all models (schema validity: 78.6-92.9% to 100%), but content accuracy reveals a persistent semantic gap that is scale-dependent: type coercion failures are fully CD-rescuable, while instruction-semantic failures (e.g., multi-step function calling) remain CD-resistant. Schema conformance is necessary but not sufficient for semantic correctness; CD's reach ends exactly where schema conformance ends.

---


### 218. [TriFleetRCA: On-Premise LLM Root Cause Analysis for Kubernetes](https://arxiv.org/abs/2609.23766)

**<font color=#1a73e8>作者：</font>** Rohit Patel, Susil Kumar Mohanty, Jeenal Chaudhary  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Root cause analysis at a remote site is slow: evidence is scattered across pod logs, Kubernetes events and cluster-level objects, and many operators cannot send production logs to a hosted model at all. On-premise inference removes the second constraint but raises a question live-cluster benchmarks have not addressed: when one workstation GPU fixes both the model and the context budget, how should evidence be retrieved, and what happens when the runbooks the model consults have been tampered with? We present TriFleetRCA, a pipeline running entirely on one on-premise GPU that collects evidence at one of three scopes (pod, namespace, cluster), ranks it by template de-duplication then BM25, filters runbooks through an ingest guard, and returns a root cause with the evidence lines supporting it. We evaluate on a live Kubernetes cluster into which we inject four faults, so ground truth is known by construction, across 100 analyses with Qwen2.5-14B-Instruct at temperature 0. The hit rate was 0.85, 0.90 and 0.95 at pod, namespace and cluster scope; intervals overlap, but the whole scope effect comes from the one fault whose cause is a cluster-level object, and cluster scope costs 55% more tokens. De-duplication before ranking raised the hit rate from 0.75 to 0.90 at equal token cost. A poisoned runbook telling the model to delete the namespace was rejected by the guard every run; with the guard disabled the model declined to follow it in all 20 analyses, making the guard defence in depth rather than the sole barrier. Separating citation quality from accuracy proved informative: one fault was diagnosed correctly and cited incorrectly every trial, a failure mode accuracy conceals. Median latency was 1.6 s at 2,200 prompt tokens. We release the pipeline, the fault injector and all records.

---


### 219. [PRISM-RAG: Multimodal Hypergraph Retrieval-Augmented Generation for Tobacco Product and Legislative Policy Reasoning](https://arxiv.org/abs/2609.23769)

**<font color=#1a73e8>作者：</font>** Manuel Serna-Aguilera, Raegan Anderes, Page Dobbs 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The disambiguation of semantically similar statutory text across jurisdictions is a retrieval problem that existing methods do not solve. This inter-context conflict can steer generative models toward confidently produced answers grounded in topically relevant but jurisdictionally incorrect sources. Tobacco and nicotine regulations vary by US jurisdiction, often sharing similar language, thus, robust reasoning requires identifying which jurisdiction's law governs a given product, not merely retrieving relevant text. Emerging products (e.g., pouches) exploit ambiguous definitions to evade regulation. State-of-the-art (SOTA) document retrieval-augmented generation (RAG) methods struggle to address this inter-context conflict, and thus struggle to connect image attributes (e.g., rich attribute captions) to the set of similar legislation texts. We introduce NicoPRISM (Nicotine Product and Regulation Image-and-Text Surveillance Multimodal), comprising 161,563 images, attribute captions, a knowledge base of product, health, and legislative documents spanning 13 US jurisdictions, and 1,495 validated question-answer pairs across two tasks: policy compliance QA and product knowledge QA. We also propose PRISM-RAG, a multimodal hypergraph RAG framework built over images, captions, and entities without any LLM calls at index time, grounding every query in a product image and routes retrieval through a jurisdiction-aware context assembly mechanism guaranteeing that statutory text from the queried jurisdiction reaches the language model by construction. PRISM-RAG retrieves passages from the correct jurisdiction in 93.9% of policy compliance queries, a 48.6 percentage point advantage over standard RAG (p<0.001), using zero LLM calls at index time and one at query time, and is competitive with or outperforms SOTA RAG frameworks across keyword, semantic, jurisdiction-, and compliance-accuracy metrics.

---


### 220. [Total Cost of Agency: Exact Attribution of Memory Injection Cost in Multi-Agent LLM Workflows](https://arxiv.org/abs/2609.23790)

**<font color=#1a73e8>作者：</font>** Vivek Kumar Singh, Preeti Priyam, Gautam Bhowmick  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every node in a multi-agent large language model (LLM) workflow retrieves context from memory and injects it into its prompt, where those injected tokens are billed as input tokens at the same per-token price as the system prompt and the user query. Production observability tools report total token cost but do not separate the tokens a node generates from the tokens it is handed, so this component of the bill is invisible to the teams paying it. We introduce the Total Cost of Agency (TCA), a decomposition of multi-agent workflow cost into base prompt, inference, memory injection, miss penalty and context-accumulation components, and an exact attribution method: a two-pass, non-billable token count that measures injected tokens directly rather than estimating them from word-count proxies. On a 200-task enterprise benchmark executed against real model APIs, memory injection accounts for 13.6 percent of the variable cost a compile-time optimizer can act on, about 12 percent of the full billed cost, and its share rises from a structural zero at workflow depth one to 27.6 percent at depth six. Injected tokens grow linearly with depth over the measured range (R^2 = 0.9974, depths two through six); a quadratic fit yields a negative leading coefficient, so the data do not exhibit convex growth at these depths. We show the component is controllable at fixed model tier: reducing the retrieval window capacity from 32 to 2 entries lowers injected tokens by 28.7 percent with an accuracy change within seed-level variation. We report in full that our graph-rewriting transforms are approximately cost-neutral in isolation, that two of the five decomposition terms are zero by construction in this harness, and that total workflow cost is dominated by model tier assignment, which we hold fixed and treat as prior work. Prompt caching is not evaluated; all figures are for the uncached case.

---


### 221. [FLARE: A Full-Lifecycle Dense Supervision Paradigm for Long-Horizon Coding Agents via Generative Reward Model](https://arxiv.org/abs/2609.23808)

**<font color=#1a73e8>作者：</font>** Jingxuan Xu, Gang Wu, Yanan Wu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While test-time scaling enhances Large Language Model (LLM) agents in long-horizon software engineering (SWE), sparse binary rewards (Pass/Fail) create a severe credit assignment crisis and waste failed exploratory trajectories. Current trajectory optimization and scaling methods are costly and structurally limited, relying on heuristic state reuse without causal diagnosis or delayed scalar scoring without actionable online guidance. We propose FLARE (Full-Lifecycle Alignment and Reward Engine), a novel dense supervision paradigm driven by a lightweight Generative Reward Model (GRM). First, RADAR, an offline causal-aware diagnostic framework, extracts high-fidelity, hindsight-free supervision through causal-chain backtracking to distill a GRM providing real-time, step-level risk feedback. Second, FLARE uses this GRM to continuously optimize the agent across its entire lifecycle. During inference, FLARE acts as an Active Scaffold, autonomously intercepting high-risk generation steps for localized breakpoint re-execution, drastically reducing compute overhead. During post-training, the GRM's structured signals serve as process-supervised reranking scores for Supervised Fine-Tuning (SFT) and step-level dense rewards for Reinforcement Learning (RL), mitigating policy collapse in sparse environments. Extensive evaluations show that FLARE establishes a new Pareto frontier across the agent lifecycle: FLARE (N=1) outperforms Global Rollout (N=5) with a 5x reduction in token consumption. Extending FLARE to training overcomes the sparse reward problem in long-horizon interactive tasks, delivering relative performance gains of 19.13% in SFT through process-aware data curation and a consistent 9.19% improvement in RL.

---


### 222. [Federated Multilingual Speech-LLMs: Architecture and Aggregation Strategy Benchmarking](https://arxiv.org/abs/2609.23825)

**<font color=#1a73e8>作者：</font>** Jordi Luque, Aleix Sant, Fernando López  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a comprehensive benchmark of Federated Learning (FL) for multilingual Automatic Speech Recognition (ASR), evaluating four Speech-LLM architectures on the Multilingual LibriSpeech dataset. We compare FedAvg and FedProx across frozen and unfrozen encoder configurations, demonstrating that optimized learning rates are critical for performance. Specifically, independently tuning the learning rates for the speech encoder, connector, and decoder yields the lowest error rates, with full three-component adaptation (LoRA for encoder and decoder, full training for the connector) producing the best FL results. We observe that FedProx efficacy is architecture-dependent, providing notable advantages in multilingual pre-trained architectures (e.g., EuroLLM over TinyLlama when keeping the encoder fixed); this indicates that LLM backbone capacity plays a key role in mediating resilience to heterogeneous data distributions. These findings offer concrete design guidance for deploying multilingual Speech-LLMs in privacy-sensitive, distributed environments.

---


### 223. [From UNDRR Reports to Event Records: Schema-Constrained LLM Extraction of Georeferenced Disasters](https://arxiv.org/abs/2609.23853)

**<font color=#1a73e8>作者：</font>** Camilla Andreozzi, Phuong-Anh Nguyen-Le, Zhijing Jin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Disaster-risk-reduction archives describe hazard events in prose that databases such as EM-DAT (Delforge et al., 2025) cannot ingest directly. We present an LLM pipeline that generates candidate georeferenced event records using a controlled hazard vocabulary and fixed schema, retaining evidence for review. Applied to 10,000 documents from PreventionWeb, the knowledge hub managed by UNDRR, it produced 3,572 records from 1,913 documents across 24 hazard types and resolved 81% of location mentions to OpenStreetMap geometries. On 171 human-positive document windows from a stratified 217-document reference set, GPT-5 achieved 86.0% pooled attribute $F_1$, versus 44.2% for the spaCy-gazetteer baseline. Evaluation pools hazard families, location strings, and event years within documents, without assessing their assignment to individual events. GPT-5.4 ranked highest among ten LLMs (86.6% $F_1$). Verbatim evidence occurrence was 72.0% for GPT-5 and 47.2% for GPT-5.4, measuring textual traceability without establishing attribute support. We report production failure modes and automated label and location-rule compliance checks. Prompts, schema, and outputs will be released for adaptation to national reporting archives.

---


### 224. [Vibe-GUIDE: A Graph-based User Interface in IDEs for Oversight in Vibe Coding](https://arxiv.org/abs/2609.23859)

**<font color=#1a73e8>作者：</font>** Chifang Chou, Sam Yu-Te Lee, Rudrajit Choudhuri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In agentic coding, developers shift from implementing changes themselves to specifying intent, evaluating the agent's work, and making approval decisions. However, delegating implementation can introduce cognitive debt that erodes project comprehension over time, constraining developers' ability to provide oversight. In this work, we investigate the role of persistent shared representations in supporting project comprehension and oversight of coding agents. We present Vibe-GUIDE, an agentic coding interface built around a structural, live, manipulable, and adaptive graph representation organized by functional modules. We evaluated our interface in a randomized between-subjects study comparing how 16 developers completed three cumulative coding tasks using our interface or a Chat-only baseline. We found that Vibe-GUIDE can support project comprehension and sustained task performance while keeping developers cognitively involved in oversight. These findings show how persistent shared representations can complement natural-language interaction and help developers maintain the understanding needed to oversee agent-generated changes as projects evolve.

---


### 225. [Pretraining of Medical Visual Encoders Toward Multi-modal Large Language Models](https://arxiv.org/abs/2609.23860)

**<font color=#1a73e8>作者：</font>** Tianyou Jiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) commonly reuse visual encoders pretrained with CLIP, although the features of these ViTs are ultimately consumed by autoregressive LLMs. We refer to this mismatch as the semantic-interface gap and introduce MedMLIP, a framework that pretrains the visual encoder through report generation with a frozen LLM, while employing Local Relational Distillation (LRD) to preserve relationships among visual patches to avoid visual collapse. We pretrain MedMLIP on IU-Xray and Open-PMC-300K and evaluate the resulting encoders on VQA-RAD and SLAKE. Only the ViT is transferred, while the guiding LLM and projector are replaced, allowing us to assess cross-LLM transferability. Our cross-LLM transfer experiments demonstrate the value of pretraining visual encoders for their autoregressive LLM interface while trying to preserve more fine-grained visual information. Code and the pretrained model are available at this https URL

---


### 226. [Explainable Recommendations at Scale: LLM Rationales for YouTube Music Artist Discovery](https://arxiv.org/abs/2609.23877)

**<font color=#1a73e8>作者：</font>** Xiao Liu, Yanwei Song, Srivaths Ranganathan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern music streaming platforms face a persistent tradeoff: exploiting familiar content versus driving the exploration of novel items. While users frequently desire discovery, they hesitate to select unknown artists over proven favorites. Providing transparent, natural language rationales that explain why an unexplored item is recommended lowers this barrier. However, while Large Language Models (LLMs) excel at this nuanced explainability, their real-time deployment is severely bottlenecked by prohibitive inference costs and computational overhead. In this paper, we present an industry case study of a decoupled recommendation architecture that successfully scales exploration without compromising latency. Our system isolates LLM inference asynchronously offline, pre-computing personalized candidate pools of undiscovered artists alongside tailored rationales. Large-scale online A/B experiments validate our design. We demonstrate that combining LLM-backed recommendations with these explanatory rationales significantly reduces the trust barrier for new content, yielding statistically significant improvements in both user exploration and overall engagement on the discovery surfaces.

---


### 227. [Q-TIE: A Lightweight and Generalizable Re-ranking Framework for Temporal Information Retrieval](https://arxiv.org/abs/2609.23880)

**<font color=#1a73e8>作者：</font>** Soyeon Kim, Hyunjin Kim, JinYeong Bak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Temporal Information Retrieval (TIR) has been increasingly critical given the rise of Retrieval-Augmented Generation (RAG). Since temporally mismatched evidence can be highly misleading, TIR aims to retrieve documents that are both semantically and temporally relevant to a query. Two TIR paradigms have emerged - temporal retrievers and temporal re-rankers - differing in how temporal relevance is modeled. While these paradigms provide complementary strengths, our analysis reveals that each alone falls short of robust TIR: temporal retrievers provide flexible query understanding via learned representations, but often fail to explicitly account for temporal constraints; temporal re-rankers can enforce such constraints more explicitly, but often rely on predefined re-ranking rules. To address this, we propose Q-TIE, a re-ranking framework based on learned Temporal Intent Extraction (TIE). By introducing a TIE model that maps each query's temporal constraint into a unified interval representation (i.e., $\langle t_{start}, t_{end} \rangle$), Q-TIE generalizes beyond predefined rules via model-based learning while explicitly modeling temporal constraints as a separate signal - jointly achieving what each paradigm typically trades off. Experiments demonstrate that Q-TIE consistently outperforms existing TIR methods with stronger generalizability across temporal query types, and provides a lightweight yet effective add-on for temporally-aware RAG pipelines. Code: this https URL.

---


### 228. [SyzHarness: Patch-Based Kernel Bug Reproduction with LLM-Synthesized Fuzzing Harnesses](https://arxiv.org/abs/2609.23889)

**<font color=#1a73e8>作者：</font>** Xingyu Li, Juefei Pu, Haonan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automated kernel vulnerability reproduction is essential for bug triage, patch validation, and regression testing, but
still lacks an effective and efficient solution. The core challenge is twofold: a reproducer must first recover the
trigger scaffold needed to reach the vulnerable state and determine the precise concrete values that actually trigger
the bug. Existing directed fuzzing approaches are ineffective at recovering the necessary trigger scaffold, while LLM-
only generation is brittle because it struggles with concrete-value discovery and runtime nondeterminism. We design
SyzHarness, a framework that combines LLM reasoning with coverage-guided fuzzing for patch-based Linux kernel
vulnerability reproduction. Given a patch, SyzHarness uses an LLM agent grounded by code navigation tools to
synthesize a parameterized fuzzing harness that fixes the prerequisite setup logic while exposing only uncertain, bug-
critical input parameters to be mutated by Syzkaller. SyzHarness then translates this harness into a Syzkaller-
compatible interface and iteratively refines it using hierarchical reachability feedback. We evaluate SyzHarness on
multiple datasets of triggerable real-world Linux kernel vulnerabilities. On 100 KernelCTF cases, SyzHarness achieves
a 78% bug reproduction success rate. On the SyzDirect benchmark, SyzHarness achieves a 73% bug reproduction success
rate, substantially outperforming prior directed greybox fuzzing. On 50 recent, known-triggerable syzbot bugs fixed
after March 2026, SyzHarness reproduces 40/50 (80%) using only the fix commits as input.

---


### 229. [Connecting the Dots in Agentic AI Security: A Cross-Dimensional Threat Taxonomy, Evaluation Maturity, and Open Challenges](https://arxiv.org/abs/2609.23894)

**<font color=#1a73e8>作者：</font>** Heewon Baek, Alsharif Abuadbba, Kristen Moore 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic AI extends LLM security beyond generated content to persistent state, autonomous actions, tool use, and interactions with humans and other agents. Existing threat classifications often emphasize individual dimensions, obscuring connections among entry points, affected components, and security consequences. The known threat landscape also differs from the coverage demonstrated by empirical research. Through a structured review of 66 studies published from 2022 to 2026, we introduce T={S, B, P, A}, a cross-dimensional representation linking affected functional or system surfaces {S}, interaction or trust boundaries {B}, violated security properties {P}, and empirically examined architectures {A}. We analyze 22 artifact-backed red-teaming studies and 11 representative security benchmarks to characterize empirical coverage and evaluation maturity. Within the selected studies, evidence concentrates on prompt/reasoning, memory, and tool-mediated attacks, predominantly in single-agent settings. Persistent, Human--Agent, complex multi-agent, systemic, and long-horizon threats receive less coverage. These findings describe the selected corpus rather than establish gaps across all empirical research. Heterogeneous metrics, limited adaptive defense evaluation, architectural imbalance, and incomplete execution-state capture further constrain comparison and reproducibility. We derive 13 open research questions to guide more systematic, architecture-aware, and reproducible security evaluation of agentic AI.

---


### 230. [GDN Tree-Scan: Served Tree Verification for Recurrent-Hybrid Language Models](https://arxiv.org/abs/2609.23900)

**<font color=#1a73e8>作者：</font>** Zhiyuan Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tree speculative decoding verifies multiple candidate continuations in one target forward pass. For attention-only transformers, the verifier mainly needs an ancestry mask. Recurrent-hybrid language models break this assumption: a candidate row must also carry the recurrent state that native sequential decode would have produced along its root-to-node path. Otherwise, a verifier can use a correct attention mask while still conditioning on an impossible recurrent history.
We present GDN Tree-Scan, a served verifier for Gated-DeltaNet hybrid language models integrated into vLLM. The system combines FlashAttention-2 tree-bias attention, branch-local GDN scan/replay, device-side multidraft commitment, and accepted-chain-only state publication. On the public Qwen3.6-27B-FP8 checkpoint, in a clean batch-one (B=1) SWE/Codex decode gate at temperature 0.6, a six-node root-branch tree increases committed tokens/event by 17.2% at near-native verify-forward time and reaches 23.88 token-weighted decode tokens/s versus 18.80 for native five-step MTP (E5), a 27.0% token-weighted decode-throughput gain. The per-request-equal latency view is +4.0%, and end-to-end task wall time remains prefill-heavy. Empirical equivalence evidence is scoped to recurrent-oracle probability-rescore (p-rescore) closure within the observed native flip floor, not a full distribution-distance proof.

---


### 231. [Time-Incremental Continued Pretraining of LLMs: Knowledge Updates Without Catastrophic Forgetting](https://arxiv.org/abs/2609.23916)

**<font color=#1a73e8>作者：</font>** Fırat Öncel, Salman Hussain Ali, Mirco Ravanelli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) drift out of date the moment their pretraining ends, yet retraining from scratch is prohibitively expensive. Continued pretraining (CPT) is the natural remedy, but it is typically evaluated through a continual learning lens that assumes disjoint data streams. This is a poor fit for time-incremental updates on web-scale crawls, where successive snapshots share substantial URL overlap by design. We study time-incremental CPT in this realistic regime: continued pretraining on FineWeb-Edu dumps drawn strictly from after each model's knowledge cutoff, evaluated across six open-weight models spanning three families (OLMo2, Llama-3.1/3.2, Gemma-3-1B) and four parameter scales (1B-3B-7B-8B).
We organize our findings around four practical questions. (i) Is knowledge acquired? Yes, but heterogeneously, and without catastrophic forgetting: five of six models also improve on pre-cutoff factual recall, and the gains track pretraining saturation (driven primarily by token budget per parameter). (ii) What does it cost? Almost nothing: the macro-average across a thirteen-task suite stays within 0.01 of the base for every model. (iii) What is the recipe? Data quality dominates quantity (a curated 6B-token slice matches a broader 40B one); the optima for knowledge acquisition and general capability are separated by roughly an order of magnitude in learning rate; and LoRA at sufficient rank matches full CPT. (iv) Does it survive deployment? CPT gains transfer through SFT, while DPO's effect is family-dependent. Together, these results paint a more optimistic picture of time-incremental CPT than the prior continual learning literature suggests.

---


### 232. [Think Before You Accept: Can Written Justification Reduce Uncritical Uptake of AI Writing Suggestions?](https://arxiv.org/abs/2609.23936)

**<font color=#1a73e8>作者：</font>** Yan Tao, Jennifer Meyer, Rene F. Kizilcec  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI can offer students useful feedback, but its value depends on judging which suggestions are accurate and relevant. Prior research shows that strategic friction during human-AI interactions can promote critical uptake, but how to effectively implement such friction in academic contexts remains unclear. We examine whether requiring students to justify decisions to accept or reject AI suggestions can mitigate uncritical uptake in academic writing. In a randomized experiment embedded in a course activity (N=129), students wrote a data analysis proposal, received mixed-quality AI revision suggestions, and decided whether to accept or reject them. Students required to provide written justifications were 24 percentage points less likely to adopt flawed suggestions (65% vs. 41%), with no reduction in acceptance of sound suggestions (81% vs. 86%). However, thematic analysis revealed superficial engagement in the justification task and gaps in metacognitive monitoring and domain knowledge.

---


### 233. [HaikuS2S: A Cascaded System For Responding In Verse](https://arxiv.org/abs/2609.23951)

**<font color=#1a73e8>作者：</font>** Devangi Sharma, Sophia Judicke, Glenda Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Expressive speech synthesis has advanced through prosody modeling, yet generating structured poetic speech, such as haiku, remains challenging. Prior work on prosody transfer improves expressiveness, and fine-tuned poetry TTS (text-to-speech) systems capture verse intonation. However, these models do not model haiku's 5-7-5 syllable structure or line-ending pauses. We present a cascaded system, HaikuS2S, combining ASR (automatic speech recognition), LLM (large language model)-generated haiku, and TTS fine-tuning on both prose and custom haiku datasets. Our evaluation focuses on emotion similarity, speech quality, and prosody alignment. In our experiments, we see that our prosody and tonal alignment improve significantly with our fine-tuned systems, particularly the one trained on both general poetry and haiku. We also see that we maintain similar emotion similarity scores across all systems.

---


### 234. [Agents That Edit Documents: Measuring Agentic PDF Forgery Against a Non-Agentic Control](https://arxiv.org/abs/2609.23953)

**<font color=#1a73e8>作者：</font>** Simiao Ren, Ankit Raj, Tommy Duong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents that carry a multi-step computer task through on their own became ordinary tools in the past year, and the same autonomy is available to anyone whose task is harmful. We ask what that means for a relying party -- an insurer, a lender, an auditor -- whose evidence is a filed PDF. AgentForge-Bench measures how reliably an off-the-shelf coding agent, driving one of seven open-weight models with a shell and the stock Python PDF stack, alters one dollar amount, date or address in a real filed financial document from a single sentence of intent, graded by rules rather than by a model. Across 1,750 cells, 1,419 (81.1%) satisfy the verifier, and 808 (46.2%) also survive every stricter filter: visible, localized, typeface-matched, original value gone document-wide. A deterministic script with no model in it solves 98 of the 125 documents; the agents solve 124, and none the script solves alone. Agents misreport 41% of their wrong edits as done, no model refused, and the cheapest verified forgery costs 2.4 cents. The raw rate overstates the threat by about a factor of two; the strict rate is still large.

---


### 235. [Some Dialects Are More Equal Than Others: Non-Prestigious Arabic Dialectal Bias in LLMs](https://arxiv.org/abs/2609.23955)

**<font color=#1a73e8>作者：</font>** Mai Mohamed Eida, Ryan Dolan, Paul de Nijs 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Previous work on Egyptian Arabic in NLP has focused largely on the prestigious Cairene Egyptian Arabic (CEA) dialect, resulting in a lack of representation for the less prestigious Sa'idi Egyptian Arabic (SEA) dialect both in LLM and resource development. Does this lack of representation influence an LLM's view of the acceptability of SEA (upstream), and does an upstream bias against SEA lead to worse performance (downstream)? We investigate the upstream effect of SEA dialectal features on LLM preferences in a Targeted Syntactic Evaluation (TSE) task which reveals a significant bias against SEA across multiple LLMs. We then analyze the effect of these same features on downstream model performance on MMLU benchmarks and show that models experience a degradation in performance when presented with SEA. This work highlights the need for further exploration on how sub-dialectal variation impacts language technologies.

---


### 236. [Open-Jev Judgments on CallScreenBench: Calibrated One-Pass Scam Screening with a Small Language Model](https://arxiv.org/abs/2609.23959)

**<font color=#1a73e8>作者：</font>** Simiao Ren, Kidus Zewde, Xingyu Shen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Screening a phone call for fraud needs a trustworthy probability after every caller turn, in milliseconds. Jev-style typed decisions promise exactly that: declared options go in, one calibrated probability per option comes out of a single forward pass, with no generated text. We test an open implementation of this readout, JevLite, on scam-call screening: Qwen3-4B is LoRA-tuned so that the temperature-scaled softmax over two answer-label logits is P(scam). On 41 held-out CallScreenBench scenarios (577 per-turn decisions) a three-seed ensemble reaches AUROC .974 with calibration error .052, non-inferior to an LLM judge (MiniMax-M3) at a pre-registered .02 margin, with no false alarms on legitimate calls, decisions 1.14 turns earlier under the same hang-up rule, and 64.5 ms per decision on one consumer GPU, 4.9x lower than the same backbone fine-tuned to generate its answer. The gain is in the readout and calibration, not accuracy: a fine-tuned ModernBERT encoder is not significantly worse, the recipe was selected with test-set exposure, and all callers are synthetic. We claim no architectural novelty; the contribution is the application and an evaluation reporting calibration, false alarms and decision timing alongside AUROC.

---


### 237. [From Tables to Quantified Statements: Evaluating LLM Inference Generation through Executable Verification](https://arxiv.org/abs/2609.23966)

**<font color=#1a73e8>作者：</font>** Mai Mohamed Eida, Gunjan Anand, Ayush Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs can generate fluent descriptions from tables, but their outputs may remain logically unsupported by the structured data. We introduce STAT-TO-TEXT, a controlled task in which LLMs generate quantified natural language inferences from statistical tables using quantified constructions such as all, some, no, and most. To evaluate these inferences, we use an LLM generated Python checker code which when executed verifies the corresponding truth conditions against the table. We compare four open-weight LLMs across model families and scales, evaluating faithfulness, logical accuracy, table coverage, and diversity. Our results show that model scale and family matter, with the largest model (GPT-OSS-120B) consistently producing the most faithful inferences without sacrificing greater table coverage and quantifier diversity, as opposed to smaller models. These findings are supported by human annotation, which shows that the automated checker closely aligns with human judgments.

---


### 238. [UniK: Universal Knowledge Perception for Digital and Physical AI](https://arxiv.org/abs/2609.23971)

**<font color=#1a73e8>作者：</font>** Nirmit Desai, Kunal Sawarkar, Aditya Mahakali 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Two transformative classes of AI systems are reshaping how organizations operate: \textit{digital AI}, which reasons over enterprise knowledge to power chatbots and agent workflows; and \textit{physical AI}, which learns to control robots and autonomous systems from video, gameplay, and sensor telemetry. Both face the same foundational bottleneck: raw knowledge at scale, spanning heterogeneous modalities, locked in private corpora that existing AI infrastructure cannot access reliably or efficiently. We propose \textit{Universal Knowledge Perception (UniK)} as a common platform for both classes, covering the full knowledge lifecycle (ingestion, enrichment, indexing, retrieval, and continuous evaluation) across modalities from rich text and video to molecular data and sensor telemetry. We present UniK, built on Polymath Retrieval (multi-index fusion over automatically enriched indices) with no task-specific fine-tuning. Across five digital AI domains (medical literature, open-domain QA, chemistry, legal video proceedings, and government open data) UniK combined with an open-source 70-billion-parameter model consistently matches or outperforms frontier proprietary LLMs that are orders of magnitude larger: 76\% RAG accuracy on government data versus 47\% for GPT-5; 77.9\% on medical QA without fine-tuning; topping all open-source chemistry pipelines. We show that the same infrastructure directly addresses the data curation, indexing, and retrieval challenges facing physical AI world model training, where the knowledge problem is harder but structurally identical.

---


### 239. [MobileCybench: Evaluating Agent Vulnerability Discovery via Executable Probes](https://arxiv.org/abs/2609.23980)

**<font color=#1a73e8>作者：</font>** Andy K. Zhang, Ava Huang, Joey Ji 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents now report vulnerabilities faster than maintainers can review them. Reports often depend on security properties specific to the application, and require considerable human labor to process. To mitigate this, we introduce a framework for evaluating vulnerability reports via probes, executable checks of security properties. A reported exploit is evaluated by replaying it against the application and running the probes: a triggered probe indicates both that the exploit succeeded and which security property it violated. As a probe encodes a security property rather than a known vulnerability, it can detect vulnerabilities that were not known when the probe was written. We instantiate the framework as MobileCybench, a benchmark for vulnerability discovery by AI agents in 13 Android applications, with 495 probes written and reviewed by the authors. We evaluate 5 coding agents (OpenCode with GPT-5.5, GPT-5.6-Sol, and GLM-5.2; Claude Code with Opus 4.8 and Opus 5) under 4 settings: as a malicious app on the victim's device or as a remote attacker with a low-privilege account, each with either only an obfuscated APK or access to the application's source code. Given only the obfuscated APK, the top agent, OpenCode with GPT-5.6-Sol, triggers probes in 53.8% of applications in the malicious-app setting and 16.7% in the remote-attacker setting. With source code, the trigger rate across all agents and both attack settings increases from 28.8% to 32.8%. Building and running the benchmark surfaced 23 previously unreported vulnerabilities, the majority of which have been confirmed by maintainers.

---


### 240. [Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents](https://arxiv.org/abs/2609.23986)

**<font color=#1a73e8>作者：</font>** Dongming Jiang, Yi Li, Bingzhe Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic memory is becoming essential for long-horizon AI agents, yet many existing systems rely on autoregressive LLMs to control how memories are organized, retrieved, and used, placing expensive generation on the critical path of memory operations. We introduce \textbf{\method}, a new agentic memory architecture inspired by System-One/System-Two cognition. System One captures fast, lightweight decision-making, whereas System Two performs slower, deliberative reasoning. Jev-Mem brings this division of labor to agentic memory through a dedicated System-One control plane, a structured multi-relational memory plane, and a System-Two reasoning plane. The System-One controller governs memory typing and relational organization during construction, and dynamically performs query routing, retrieval-budget allocation, graph traversal, candidate scoring, and adaptive stopping during retrieval. System Two is invoked only for complex reasoning and answer synthesis. This design improves both memory effectiveness and system efficiency: on LoCoMo Jev-Mem achieves an overall LLM-as-a-Judge score of 0.777, an 11.0\% relative improvement over the strongest baseline, while reducing memory construction time to 158\,s, a 6.6$\times$ speedup over the fastest competing memory system, and lowering average query latency to 0.93\,s, a 36.7\% reduction.

---


### 241. [Misaligned Clinical Risk Classification and Cost Asymmetry in Open-Weight Large Language Models](https://arxiv.org/abs/2609.23999)

**<font color=#1a73e8>作者：</font>** Star S.D. Liu, Xiyu Ding, Robert B. Barrett 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How large language models (LLMs) integrate patient risk with clinical cost tradeoffs remains poorly understood. We investigated how four open-weight LLMs (Qwen-2.5-7B/32B and Llama-3.1-8B/70B) internally represent cost tradeoffs, how these representations relate to clinical predictions, and whether decisions shift as predicted by the specified cost direction and magnitude. Using a public diabetes dataset, we varied 11 false-negative (FN) to false-positive (FP) cost ratios across three phrasings and examined representations and behavioral outputs. Patient risk was linearly recoverable on par with conventional classifiers (AUC $\approx 0.83$), and cost direction was recoverable in every model. However, representational shifts in cost direction tracked output changes only in the two larger models, and responses to cost magnitude were predominantly direction-agnostic. Only 2 of 12 model-phrasings showed both opposing responses to increasing FN versus FP costs and cost-correct ordering. Representationally, a direction fitted on one cost side did not invert when transferred to the other, as expected under mirror-symmetric encoding. These findings suggest that LLMs encode risk and cost information but do not reliably integrate them into cost-correct decisions. Clinical evaluations should therefore include tradeoff tests, phrasing sensitivity, and default operating points alongside predictive performance.

---


### 242. [FinInteract: Benchmarking Clarification and Intent Integration in Ambiguous Financial Question Answering](https://arxiv.org/abs/2609.24002)

**<font color=#1a73e8>作者：</font>** Xinyu Wang, Tung Sum Thomas Kwok, Zhenghan Tai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly answer financial questions by searching regulatory filings. Such questions are often deceptively under-specified: Meta Platforms' "operating income" is $46.75B consolidated but $62.87B for the Family of Apps segment, and each reading is exactly verifiable against the filing. A capable agent should recognize the ambiguity and ask, rather than commit to a plausible but unintended reading. Existing financial benchmarks cannot measure this, because one gold answer per question cannot separate agents that resolve the ambiguity from those that guess the common reading, a blind spot we call the single-gold illusion. We release FinInteract, a bilingual (English/Chinese) benchmark of 173 instances that pairs each question with a default and an intended interpretation across a five-category ambiguity taxonomy, and grades whether an agent elicits the right clarification and then integrates it. Re-grading identical outputs against the default rather than the intended reading inflates GPT-4o's accuracy by 3.1 times, confirming the illusion. Beyond it, we find that models answer above 90% once the interpretation is supplied but at most 28.9% when they must elicit it themselves, that targeting is uneven across a taxonomy well powered for entity scope and metric definition and exploratory elsewhere, and that conditioning on the ambiguity category improves resolution at both inference and training time.

---


### 243. [Testing, not presuming, adequacy: calibrating generative social simulators against emergent network structure](https://arxiv.org/abs/2609.24012)

**<font color=#1a73e8>作者：</font>** Tengfei Shao, Chao Li, Xu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Validation of generative social simulators often stops at face validity: emergent network structure is compared descriptively, without quantified parameter uncertainty or an adequacy check. We present an adequacy-aware calibration protocol that couples amortized posterior estimation with a synthetic identifiability assessment, a matched-sample-size adequacy check (prior-predictive reachability plus per-statistic posterior-predictive localization), a diagnosis-guided repair, and a statistic-held-out audit. We demonstrate it on a real second-hand luxury resale market with four channel-by-residency cells, each a bipartite buyer-brand network, using a forward model built from persona profiles elicited once, offline, by a language model. The behavioural parameters are recoverable in all four cells, though calibration is approximate and overconfident for one parameter. The observed summary falls outside the simulator's reachability reference in every cell, with the mean purchased tier as the pervasive discrepancy. The repair meets the value-block criterion in two of four cells but does not restore adequacy, and the held-out audit surfaces a buyer-breadth-dispersion miss no earlier diagnostic detected. A profile-source ablation finds the language-model profiles beat a flat rule baseline in all four cells, yet within-category brand relabelling causes no consistent degradation, so the profiles are a partially validated input whose value rests on structure, not brand identity. Making no causal claim, we conclude that an independent-aggregation account, without agent interaction or a buyer-breadth mechanism, cannot jointly reproduce the market's purchased-tier level, head-brand concentration, community structure and buyer-breadth heterogeneity.

---


### 244. [Context-Aware Pre-Deployment Evaluation of AI Systems: A Regulatory Framework for Nigerian Fintech](https://arxiv.org/abs/2609.24016)

**<font color=#1a73e8>作者：</font>** Andrew Anogie Uduimoh, Hadiza Umar Yusuf, Oluwafemi Osho  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Commercial large language models are increasingly deployed across African fintech infrastructure for fraud detection and customer communication, yet no Nigerian or African continental regulatory instrument specifies what pre-deployment evaluation such systems must undergo before procurement. This paper reviews African fintech AI governance across global, continental, and Nigerian instruments, and shows that safety is affirmed as a principle while pre-deployment evaluation is operationally unspecified. Generic safety benchmarks cannot surface the failure modes most relevant to this domain, since none contain Nigerian institutional content or test for false positive misclassification of legitimate financial communications. These claims are demonstrated using SafeAlert, a purpose-built evaluation kit applied to six commercial models across three system prompt conditions. Results show that models resisting generic harmful content requests still produce complete fraud scripts under specific framing, and that several models misclassify most legitimate Nigerian bank communications as suspicious or fraudulent, a failure invisible to standard safety evaluation. The paper concludes with a regulatory framework proposing pre-deployment evaluation requirements for the CBN, NITDA, SEC, and the AU, arguing that the identified gap reflects an absence of regulatory specification, not a shortage of technical or financial resources.

---


### 245. [Synthesizing Reactive Character Behaviors for Continuous Games via Programmatic Policy Search](https://arxiv.org/abs/2609.24025)

**<font color=#1a73e8>作者：</font>** Maxim Gumin, Hsueh-Ti Derek Liu, Victor Zordan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a method for synthesizing reactive character behaviors for continuous games as compact, human-readable programs. Game AI practice still relies heavily on manually authored behavior trees, state machines, and scripts, while academic reinforcement learning typically produces opaque neural controllers that are expensive to train and difficult to edit. Our approach bridges this gap by searching directly over a domain-specific language for continuous-space game policies. The language is designed around reactive geometric decisions and includes higher-order constructs such as direction maximization. These constructs help discretize a continuous behavior space into enumerable program structures. To make program search practical, we introduce a large set of synthesis antipatterns that remove redundant program forms while preserving behavioral coverage. We further combine bottom-up symbolic enumeration with top-down guidance from a coding agent. Our resulting method, agentic sketching, has the agent propose high-level policy structure and call an enumerator to complete local program slots. We evaluate the method on a benchmark of 14 continuous games, ranging from classic control tasks to multi-agent football. We find that pure enumeration is often more efficient than using a coding agent alone, while the combined method substantially outperforms both. Our results suggest that programmatic policy search can be a practical authoring tool for game AI: designers specify reward functions, and the system discovers editable behaviors that are effective, portable, and often surprising.

---


### 246. [Structured Decomposition for Reliable LLM-Generated Access Control Policies](https://arxiv.org/abs/2609.24036)

**<font color=#1a73e8>作者：</font>** Vatsal Gupta, Darshan Sreenivasamurthy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents an LLM-based system that translates natural-language access control policies (NLACPs) into executable Rego code for Open Policy Agent (OPA). It provides a modular, end-to-end pipeline for policy detection, component extraction, schema validation, linting, compilation, and automated test generation and execution. The system is designed to bridge the gap between human-readable access requirements and machine-enforceable policy-as-code (PaC), with a focus on deployment reliability and security correctness.
We evaluate the system on 372 ACRE-complete access control statements with non-null subject, action, and resource annotations against a direct single-prompt LLM baseline to isolate the contribution of structured decomposition and schema-aware validation. The system achieves a 50.3% end-to-end policy correctness rate, compared with 15.3% for the baseline, representing a 3.3x improvement. A policy is counted as correct only if it satisfies compilation, linting, and both positive and negative tests, making this a strict measure of deployable correctness.
On security-critical patterns, the system generates correct deny semantics for 87.5% of deny policies (baseline: 37.5%), ownership conditions for 100% of ownership-qualified policies (baseline: 40%), and status-qualified conditions for 100% of status-qualified policies (baseline: 55.6%). These results indicate that structured decomposition and schema-aware validation play a critical role in improving the reliability of LLM-generated authorization policies.

---


### 247. [Calibrated Decisions at Scale: Converting Police Crash Narratives into Probabilistic Crash Variables with a System One Model (Jev)](https://arxiv.org/abs/2609.24052)

**<font color=#1a73e8>作者：</font>** Amir Rafe, Subasish Das  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Crash datasets that carry an investigator narrative hold information the coded fields omit. Coding those narratives at scale has been blocked by three obstacles. Frontier large language models are costly at that scale, their generated text cannot be verified, and no rule says how much output a human must check. This paper formulates narrative coding as gated, typed decisions answered by Jev, a System One model that returns probabilities over analyst-defined options and generates no text. A screen covered 499,500 Texas narratives and 195,857 were coded with a 27-question schema. Cost is governed by schema size rather than narrative length. The probabilities are audited against coded fields and against 2,416 blinded human judgments drawn under a stated sampling design. Two frontier large language models are benchmarked on the same records. Against human labels the typed model attains an F1 of 0.908. One frontier model gains 0.059 and the other is indistinguishable from it. Calibration varies by model rather than by paradigm, so each model must be audited. Recalibration on the same labels reduces calibration error by a factor of 3.3. Agreement with coded fields understates fidelity to the narrative by a median of 0.26 in kappa. A resolution-floor bound covers any model that reports probabilities on a discrete grid. A review budget over flagged records gives the records a human must read per variable and per year. Adding the calibrated variables to the coded fields raises the injury and fatal crashes attributed to nine factors by 10,747 per year.

---


### 248. [Representation-guided in-context learning for medical image interpretation with multimodal large language models](https://arxiv.org/abs/2609.24057)

**<font color=#1a73e8>作者：</font>** Minda Zhao, Fangyu Hu, Yan Luo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical image interpretation is central to diagnosis and care, yet adapting general-purpose multimodal large language models (MLLMs) often requires resource-intensive domain-specific fine-tuning. Here we introduce representation-guided in-context learning (RG-ICL), a training-free inference framework that retrieves query-aligned demonstrations using frozen encoders, without task-specific parameter updates. Across eight datasets spanning histopathology, radiology and retinal fundoscopy, RG-ICL improved classification (mean gain 20 percentage points) and visual question answering (VQA) (mean gain 13 percentage points) over no-context and conventional ICL, approaching or exceeding training-based comparators. Which cases were retrieved mattered more than how many: 6 query-aligned cases outperformed up to 32 randomly selected ones, whereas fixed or random cases often reduced accuracy below baseline. For VQA, aligning reference cases with both image content and question intent produced further gains. These findings indicate that for medical image interpretation, curating which reference cases an MLLM sees is a practical alternative to retraining it.

---


### 249. [All-in-One Multilingual Scene Text Recognition with Script-aware Mixture-of-Experts](https://arxiv.org/abs/2609.24058)

**<font color=#1a73e8>作者：</font>** Xingsong Ye, Yongkun Du, Jiaxin Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multilingual scene text recognition (STR) remains challenging due to the scarcity of training data for most languages and the difficulty of serving diverse scripts within a single model. Existing solutions either deploy one recognizer per language, inflating cost and introducing error accumulation, or rely on massive vision-language models (VLMs) that are expensive and still inaccurate on many scripts. In this work, we pursue an all-in-one multilingual recognizer that is simpler than per-language experts, lighter than VLMs, and more accurate than both. First, we construct TextMuSS-10M, a large-scale synthetic scene text dataset spanning 10 scripts and 229 languages. It provides balanced and sufficient supervision where real data is unavailable. Second, we propose ScriptMoE, a script-aware Mixture-of-Experts (MoE) architecture. It shares a single visual encoder and replaces the dense decoder with a sparse MoE block, which consists of an image-level router dispatches each image to the top-2 script-aligned experts and a shared expert absorbs cross-script knowledge. Extensive experiments on our assembled TextMuSS-Bench (10 scripts, 10,899 images) show that ScriptMoE achieves the highest accuracy of 82.06%, outperforming the strongest STR baseline by 1.31%. On the CC-OCR end-to-end multilingual task, replacing only the recognizer in PP-OCRv5 with ScriptMoE lifts F1 score from 65.71% to 80.89%, slightly surpassing the best VLM (80.73%) at a fraction of the parameter count.

---


### 250. [Monitorable Chart Reasoning Agents via Verifiable Process Rewards](https://arxiv.org/abs/2609.24071)

**<font color=#1a73e8>作者：</font>** Sanchit Sinha, Oana Frunza, Kashif Rasul 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chart reasoning agents are increasingly used to extract actionable insights in critical domains, achieving state-of-the-art performance on multiple benchmarks. Yet, high benchmark accuracy alone is insufficient for deployment, where stakeholders must be able to audit and verify how a model reaches its answer. Existing LVLM-based chart agents produce either answer-only predictions or free-form rationales that are hard to verify, obscuring whether an error arose from misreading the chart, extracting a wrong value, or miscomputing. We propose Chart-RVR, a reinforcement learning framework for training monitorable chart agents with verifiable process rewards. Chart-RVR decomposes chart reasoning into three auditable blocks: Structure, identifying the chart type; Evidence, reconstructing the underlying data table in JSON; and Derivation, exposing the stepwise trace that computes the answer. Across six in-domain and out-of-domain benchmarks, Chart-RVR attains state-of-the-art accuracy among comparable-sized LVLMs. Beyond accuracy, we assess monitorability using a triangulated protocol that combines ground-truth surrogate metrics, an oracle information-gain measure, and an LLM-as-auditor scoring Process Verifiability and Evidence Localization, showing that Chart-RVR yields rationales that are markedly more verifiable and evidence-grounded than those from CoT prompting, SFT, and existing chart-specific baselines.

---


> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-379](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
