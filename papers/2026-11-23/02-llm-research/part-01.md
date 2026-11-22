# 🧠 大模型相关研究 | 2026年11月23日

> 本类共 **266** 篇论文：已确认 **245** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

---

### 1. [LLM Complexity: Towards a Computational Complexity View of Large Language Model Inference](https://arxiv.org/abs/2611.24943)

**<font color=#1a73e8>作者：</font>** Yu-Hung Wu, Shao-Xiang Yuan, Chan-Hung Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computational complexity theory offers a principled framework for characterizing the efficiency of computational problems, and Large Language Models (LLMs) can similarly be viewed as computational systems executing a structured process of input, inference-time compute, and output. In this context, the number of generated tokens emerges as a natural and directly observable proxy for inference-time compute. However, we show that the tempting analogy between LLM token length and classical time complexity does not hold. We disprove the hypothesis that inference-time token usage aligns monotonically with classical time complexity, demonstrating a fundamental divergence grounded in how LLMs actually allocate computation during inference. To this end, we introduce LLM Complexity, a new metric designed to quantify problem complexity from the perspective of LLMs by characterizing the area bounded above by the accuracy-token curve. We find that diverse LLMs induce highly consistent task rankings under LLM Complexity, indicating that the metric captures stable notions of difficulty across models. We leverage this property to construct an easy-to-hard curriculum for supervised fine-tuning, which improves accuracy while reducing token consumption. Finally, we demonstrate that LLM Complexity generalizes to real-world tasks, producing more stable cross-model correlations than human-annotated difficulty labels.

---


### 2. [ICARE: cross-domain text classification with incremental class-aware representation and distillation learning](https://arxiv.org/abs/2611.24959)

**<font color=#1a73e8>作者：</font>** Son Duong, Truong X. Tran, Hai-Anh Tran  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rise of powerful, fine-tuned large language models (LLMs) necessitates robust natural language inference (NLI) systems. These NLI systems ideally train across various tasks, encompassing diverse concepts like sentiment analysis, news classification, and coreference resolution. However, this continual, multi-tasking approach can lead to catastrophic forgetting, where previously learned tasks are lost, especially in domains lacking specific labels. Rehearsing past examples with labels can further exacerbate this issue by causing overfitting, hindering the system's ability to classify new categories. To tackle these challenges, this research proposes ICARE, a novel framework with two key components: an instance selection module and a knowledge distillation method. The former is based on representation learning, which meticulously selects training examples to present to the NLI system. The latter, knowledge distillation with feature and logit-level transfer, facilitates knowledge transfer between tasks. This leverages pruning techniques and optimized objective functions to transfer both essential feature-level and decision-making (logit-level) knowledge, mitigating catastrophic forgetting while adapting to new patterns. Extensive evaluations on benchmark text classification datasets have demonstrated ICARE's effectiveness. The framework achieves a significant improvement in target accuracy and reduction in the ``forgetting metric''. These results solidify ICARE's ability to preserve and leverage learned knowledge across diverse tasks, ultimately enhancing the adaptability and performance of NLI systems. The source code is available at this https URL

---


### 3. [TETHER: Training-Free, Elastic, ToC-Anchored Hierarchy Extraction and Recovery in Design-Driven Long Documents](https://arxiv.org/abs/2611.24960)

**<font color=#1a73e8>作者：</font>** Yu Zou, Yan Chen, Jialei Zeng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Converting complex documents into structured knowledge constitutes the critical infrastructure urgently required for deploying Large Language Models (LLMs) in downstream research. However, blind to the Table of Contents (ToC) as a macro-structure, existing bottom-up paradigms rely on localized visual cues, inducing heuristic fragility in high-entropy layouts where visual prominence decouples from logical depth; meanwhile, direct LLM extraction lacks spatial grounding, triggering hallucinations in long contexts. To address this, we introduce TETHER, a training-free framework that elevates the ToC from discarded noise to a vital structural prior, enabling robust adaptation across design-driven long documents. TETHER operates via a two-stage neuro-symbolic mechanism: first, it constructs a document skeleton from the raw ToC using a Large Multimodal Model (LMM) empowered by spatio-semantic constraints; second, it employs an anchor-based alignment strategy to tether content blocks to this skeleton, effectively resolving boundary ambiguities. Evaluated across a multilingual benchmark of ESG reports, product manuals, and annual reports, TETHER delivers highly precise, state-of-the-art (SOTA) zero-shot hierarchy recovery, outperforming deep hierarchical recovery models, dedicated parsers, and general-purpose LMMs. Moreover, stress tests highlight TETHER's resilience to sparse omissions and textual noise, demonstrating that its precise semantic alignment is fundamentally anchored in topological and depth fidelity. Crucially, ablations confirm the framework's architectural irreducibility, while achieving 90% token reduction and drastic speedups over end-to-end baselines, establishing a compelling equilibrium between structural precision and deployment scalability.

---


### 4. [Physics of Language Models: Part 4.2, Canon Layers at Scale where Synthetic Pretraining Resonates in Reality](https://arxiv.org/abs/2611.24963)

**<font color=#1a73e8>作者：</font>** Zeyuan Allen-Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Do standard benchmarks see the architectural differences that matter? We study it with 64 from-scratch pretraining runs of Transformers and three linear-model families at 1.3-8B parameters on 1-2T Nemotron-CC tokens, at a cost of roughly 100k USD per 8B run.
In academic-scale pretraining (1.3B parameters, 100B tokens), architectural differences can all but disappear when the models are carefully tuned. Instead, at 1-2T tokens they become measurable: Canon layers, which add local token mixing, consistently improve Transformers, saving about 30% of pretraining tokens for the same MMLU accuracy at 8B. We also introduce GLA5 and GDN2, which improve gated linear attention and Gated DeltaNet with low-rank output gates. Surprisingly, with Canon, the simplest linear model, gated linear attention, matches Gated DeltaNet and outperforms Mamba2 even at 8B/1T. Therefore, the extra machinery of Gated DeltaNet and Mamba2 may do little more than mix neighboring tokens.
Even at 8B/1T, however, high scores on standard benchmarks can hide weaknesses in basic in-context skills. In particular, linear models that match or beat Transformers on these benchmarks cannot, in fact, reliably retrieve information from a short 500-token context. Moreover, no model, Transformer or linear, reliably beats random guessing on arguably the simplest two-hop question, stated in a few short sentences, even at this scale.
These findings $\textbf{challenge traditional architecture research}$ based primarily on standard benchmark scores. In contrast, small synthetic playgrounds, which predicted the architectural differences above at <100M parameters, can reveal what these benchmarks miss. For practitioners, one lesson is to include in-context reasoning examples in pretraining data from an early stage, rather than reserve them for later mid-training, let alone post-training.

---


### 5. [Global Importance Estimation for KV Cache Eviction](https://arxiv.org/abs/2611.24969)

**<font color=#1a73e8>作者：</font>** Seojin Kim, Noseong Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory consumption of the key-value (KV) cache remains a central bottleneck for long-context LLM inference. We introduce PRKV, a training-free KV eviction method that estimates multi-hop global token importance by applying Personalized PageRank over attention-induced transition graphs. This enables importance propagation beyond recency or instantaneous attention, without modifying the model. We benchmark PRKV on long-context understanding, sparse retrieval, and chain-of-thought reasoning tasks using multiple LLM families. Under moderate to aggressive compression ratios, including up to 90%, PRKV achieves competitive task performance against established eviction baselines while reducing peak memory usage with low end-to-end overhead. These results demonstrate that multi-hop global influence estimation yields a favorable accuracy--memory trade-off for scalable long-context inference.

---


### 6. [HireWatch: Evaluating LLM Compliance with U.S. Employment Law Under Contextual Pressure](https://arxiv.org/abs/2611.24970)

**<font color=#1a73e8>作者：</font>** Huy Nghiem, Maria Kostylew, Noam Kolt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The deployment of large language models (LLMs) in hiring pipelines is growing, yet existing evaluations generally overlook their compliance with legal rules. To fill this gap, we introduce HireWatch, an evaluation that assesses whether LLMs comply with U.S. laws that govern the questions that job candidates may be asked. We construct a 200-item bank of lawful and unlawful interview questions, whose legal classification is based on U.S. federal statutes, regulations, and agency guidance. We instruct LLMs to select questions from this bank in preparing for job interviews, across a set of various occupations and contexts, and report the fraction of unlawful questions that LLMs select. Evaluation of 18 closed and open-weight LLMs across ~100,000 trials under different types of contextual pressure reveals that LLMs' legal compliance is brittle. While LLMs generally avoid selecting unlawful questions in low-pressure contexts, legal violations increase sharply under higher pressure. Explicit prompts to comply with law can improve compliance rates, but do not altogether eliminate legal violations. We publicly release our code and data at this https URL.

---


### 7. [The ROI of Small Examples: Optimizing In-Context Learning Under Token Budgets](https://arxiv.org/abs/2611.24971)

**<font color=#1a73e8>作者：</font>** Anxo Perez, Jorge Gabín, Javier Parapar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) improves large language model performance at inference time without updating model parameters. However, these gains are not free: in practical deployments, longer prompts directly increase inference cost and latency. Under a fixed token budget, prompt construction therefore becomes a resource-allocation problem. While prior work has often focused on how many examples to include in ICL, we study the complementary question of whether the available budget is better spent on a few long demonstrations or on a larger number of shorter ones. We study this aspect in question answering (QA), by organizing candidate demonstrations into length-based bins and constructing prompts from examples within the same length range under fixed budgets. Experiments on two QA benchmarks (\textit{Beat the AI} and \textit{Natural Questions}), using six instruction-tuned LLMs, show that shorter demonstrations are generally the most effective use of prompt space. This effect is especially strong on \textit{Beat the AI}, and remains visible on NQ, although gains are smaller and saturate earlier in the long-context setting. An additional natural language inference experiment on ANLI R3 finds that one of the two shorter bins performs best for five of six models, although longer demonstrations remain competitive. Overall, our results highlight demonstration granularity as an important factor in prompt design.

---


### 8. [No-Harm-Jury A Jury-Based Multi-Dimensional Harm Evaluation Framework for Medical AI Responses](https://arxiv.org/abs/2611.24972)

**<font color=#1a73e8>作者：</font>** Antonio Puertas Gallardo, Mario Ceresa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present No-Harm-Jury, a jury-based automated evaluation framework that scores AI-generated medical responses across seven conceptually distinct harm dimensions using a panel of five diverse language models as independent jurors. Responses generated by Ministral-14B on 3,000 questions drawn from PubMedQA, MedQA, and MedMCQA are scored by five jurors across dimensions of informational, social, psychological, autonomy, economic, privacy, and epistemic harm; the 151 empty responses (98 MedQA, 53 MedM- CQA) are excluded, leaving 2,849 valid samples. The median aggregation robustly suppresses individual juror biases while maintaining coverage through complementary specialisation. No existing system combines all five prop- erties of No-Harm-Jury: automated scalable evaluation, five diverse LLM jurors, robust me- dian aggregation (with a reliability-weighted extension), seven conceptually distinct harm dimensions, and application to medical QA benchmarks.

---


### 9. [CANDID: Candidate-Driven Intervention for Disciplined Execution in Local Computer-Use Agents](https://arxiv.org/abs/2611.24977)

**<font color=#1a73e8>作者：</font>** Woongkyu Lee, Jungwook Choi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present CANDID (Candidate-Driven Intervention for Disciplined Execution), an execution-control framework designed to enhance the reliability of local computer-use agents (CUAs) in resource-constrained settings. While local CUAs feature robust baseline proficiency in single-step action prediction, they frequently fail at critical junctions due to rigid action loops or premature DONE decisions. Rather than imposing imprecise cognitive loads through textual reflection, CANDID repurposes parallel test-time scaling into a disciplined, execution-level intervention at sparse, failure-prone points. We introduce a loop-recovery mechanism to filter candidates away from repeated behaviors and a conservative, unanimous DONE gating policy that requires absolute consensus to terminate. Experiments on OSWorld demonstrate that CANDID's structural control significantly improves success rates, outperforming feedback-based alternatives with minimal execution overhead.

---


### 10. [What the model knows but does not say: monitoring medical LLMs through verbalized thoughts](https://arxiv.org/abs/2611.24994)

**<font color=#1a73e8>作者：</font>** Frederik Hauke, Jan Clusmann, Hanna Kreutzer 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Efforts to keep clinical language models safe have concentrated on what enters and leaves the model, but a manipulated model can return an answer that looks entirely ordinary. Here we show that the model's own internal state, rendered in plain language, exposes manipulations the output conceals. Using a natural-language autoencoder, we translate the activations of a multimodal LLM (Gemma-3-27B) into text and let an input-blind judge read this verbalized internal state (the thoughts channel) and the model's answer separately. Across two clinical attack objectives (omitting a pathology, covertly recommending a drug), two input modalities, and two delivery mechanisms, the thoughts channel caught the injection significantly more often than the answer in all eight injected conditions (p<0.05), while both channels held near-zero false-positive rates on clean inputs; the omission result carried over to Llama-3.3-70B. The thoughts channel also registered unsafe clinical requests as harmful while the model was still reading them, before it decided whether to refuse. None of this requires retraining: an off-the-shelf verbalizer and a general-purpose judge are enough.

---


### 11. [EgoPass-Bench: Identifying Objects That May Affect the Wearer's Passage in Egocentric Video](https://arxiv.org/abs/2611.24995)

**<font color=#1a73e8>作者：</font>** Hongyu Wang, Chuhan Li, Congjin Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding an egocentric environment requires reasoning about how surrounding entities affect the observer's actions. Existing evaluations of multimodal foundation models (MFMs) examine observer localization, motion trajectories, and action feasibility, but leave the discovery and interpretation of evolving observer-entity interactions insufficiently assessed. We introduce EgoPass-Bench, a benchmark for observer-relative interaction understanding in real-world egocentric video. EgoPass-Bench comprises 284 manually reviewed evaluation clips recorded using Ray-Ban Meta (Gen 2) smart glasses and 2,201 distinct questions across five tasks assessing motion perception, interaction judgments about specified entities, and relevant-entity discovery without target cues. Our evaluation of eight frame-based and six native-video configurations reveals a pronounced discrepancy between motion perception and interaction understanding. The strongest evaluated model, GPT-6 Astra, correctly recognizes object motion in 91.37% of 394 comparisons involving the same targets, but correctly identifies changes in passage constraints in only 66.50%. Across all 574 entity-discovery questions, it trails the two-person human baseline by $23.65 \pm 7.45$ percentage points (paired 95% CI), while exceeding the always-empty baseline (36.76%) by at least 18.9 percentage points. Further analysis reveals frequent inclusion of entities that neither pose a plausible physical conflict nor constrain passage, showing that accurate motion recognition does not ensure reliable relevant-entity discovery.

---


### 12. [Watch Where You Linearize: Predicting and Correcting Model-Merging Interference](https://arxiv.org/abs/2611.25000)

**<font color=#1a73e8>作者：</font>** Ido Nitzan Hidekel, Dan Raviv  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging combines separately fine-tuned models by adding their task vectors to a shared backbone. Interference is typically assessed only after constructing and evaluating a candidate merge, making coefficient search expensive. We show that a first-order directional derivative of task A's outputs along task B's vector can predict interference, but only when evaluated at the appropriate model.
At the receiver model, this derivative forecasts nearby merges per task and per example, halves the accuracy error of a no-change baseline, and identifies most examples whose predictions flip. For full multi-task merges, a single evaluation is insufficient; two evaluations along the merge path are needed. At the shared pretrained backbone, however, the derivative is nearly orthogonal to realized changes in our vision experiments and only partly predictive in LoRA language-model pilots. Controls link this failure to displacement along the receiver's own task vector, not simply parameter distance; the mismatch appears within the first few dozen fine-tuning steps.
Freezing receiver-local responses produces a surrogate affine in the merge coefficients. We use it to construct LR-Merge, a label-free correction that optimizes coefficients through convex teacher matching on unlabeled probes, without backpropagation through merged networks. LR-Merge improves all tested closed-form, isotropic, and sparsified base mergers, with gains generally increasing as more tasks are merged. Using pretrained rather than receiver-local responses instead degrades the base merge. LR-Merge matches exact teacher matching through a merged network, which takes roughly three times longer to converge and performs similarly at an equal compute budget. Once built, the surrogate answers new coefficient and task-subset queries in seconds.

---


### 13. [A Model of Diverse Sampling from Language Models](https://arxiv.org/abs/2611.25003)

**<font color=#1a73e8>作者：</font>** Manuel Prada-Corral, Yahya Emara, Timothy J. O'Donnell 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models often produce high-quality individual samples but poor sets, with repeated samples clustering around the same semantic modes. We formalize diverse generation as sampling a size-$K$ subset of complete strings from a determinantal point process (DPP), where the likelihood encodes item quality, and the embedding geometry encodes repulsion between similar outputs. Exact inference over all strings is intractable, so we propose PoolDPP: draw a finite candidate pool from a tractable proposal, importance-weight the candidates toward the target quality, and run a $K$-DPP sampler on the induced pool kernel; a greedy MAP variant provides deterministic selection. We prove a finite-sample bound with an explicit constant: the KL divergence between the sampler's output and the target $K$-DPP decays as O(1/N) in the pool size. Empirically, PoolDPP extends the quality--diversity frontier on open-ended generation and the precision--recall frontier on ambiguous text-to-SQL (Ambrosia), and on mathematical reasoning (GSM8K), it raises diversity at about the same pass@$K$.

---


### 14. [Attacks and Defenses in Decentralized Multi-Agent Systems with Hop-by-Hop Task Decomposition and Delegation](https://arxiv.org/abs/2611.25056)

**<font color=#1a73e8>作者：</font>** Matthew D. Laws, Maria Lazou, Alina Oprea 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Decentralized multi-agent LLM systems enable independently administered agents, each with its own operator, model, memory, and configuration, to collaborate on complex tasks without centralized coordination. Agents autonomously decompose tasks, execute subtasks and delegate remaining work to peers, enabling scalability and eliminating single points of failure. However, decentralization also introduces significant security challenges, as no single entity has complete visibility into task execution or the authority to enforce correct behavior across agents.
In this paper, we systematize threats from malicious agents in decentralized multi-agent systems and propose mitigation techniques. We first design and evaluate attacks against integrity, availability, and confidentiality, demonstrating that a single malicious agent can cause up to 100% task failure, inflate token consumption and runtime by up to 7.7x and 3.2x, respectively, and exfiltrate up to 94% of relevant prior tasks from benign agents. We then present a cryptographic protocol that produces an irrefutable verified execution trace of every action taken in the system and develop an auditor that analyzes these traces to detect and attribute malicious behavior. Evaluations on HiddenBench using gpt-6.1-sol and Qwen3.8-27B-FP8 show that our protocol incurs negligible latency overhead, while the auditor detects and correctly attributes 98% of attacks, including those that comply with the protocol.

---


### 15. [VisAlloc: Allocating Visual Supervision for On-Policy Self-Distillation](https://arxiv.org/abs/2611.25069)

**<font color=#1a73e8>作者：</font>** Haoran Xu, Tian Chen, Yuhe Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) offers a promising approach to improving visual reasoning in multimodal large language models (MLLMs). However, not all samples benefit equally from privileged visual guidance, and uniform token supervision can dilute visually grounded signals. We propose VisAlloc, a dual-level framework combining sample-level visual filtering with token-level counterfactual reweighting. A fixed paired-teacher filter retains samples answered correctly from an evidence-centered positive crop but incorrectly from a spatially displaced negative crop. At the token level, both EMA teachers score the same student-generated response, and their absolute log-probability differences measure view sensitivity. Additional supervision targets tokens admitted by sensitivity or teacher-distribution disagreement, with shared frozen-prior, template-bigram, and student--teacher divergence gates. Inverse-frequency redistribution preserves the total additional weight within each micro-batch, while the positive teacher remains the sole distillation target. Inference requires only the full-image student. Across eight benchmarks, our 4B and 9B models achieve macro-averages of 81.44 and 84.92, outperforming Vision-OPD reproductions by 0.97 and 0.52 points, respectively. Code on GitHub: this https URL

---


### 16. [An LLM-Agentic Framework for Intelligent Work Order Management in Industrial Maintenance](https://arxiv.org/abs/2611.25070)

**<font color=#1a73e8>作者：</font>** Nianjun Zhou, Dhaval Patel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents an AI-driven framework, CodeReAct agent, designed to enhance industrial equipment maintenance through natural language (NL) interactions. The framework employs an advanced AI agentic approach to interpret human instructions, providing knowledge extraction, asset status summarization, and work order recommendations. It identifies patterns and trends and predicts work orders by standardizing industrial data into business objects (BOs) and utilizing analytical function API calls. The AI agent operates through a Thought-Action-Observation process similar to human problem-solving, automating complex analytical tasks typically performed by data scientists. Notably, the Action phase generates executable code, replacing manual coding efforts.
A case study focusing on chiller maintenance demonstrates the framework's capability to analyze multiple years of work orders, and alerts and anomalies are presented. The results indicate that the AI agent framework effectively processes human utterances to analyze data, extract valuable insights, and support informed decision-making, reducing the need for data scientist involvement. By recontextualizing NLP agent frameworks in industrial engineering, the approach enables autonomous function generation and task execution across a range of domain-specific maintenance scenarios, with chillers used as a representative case study.

---


### 17. [FinVeriQA: Financial Research Agents for Question Answering: Routing, Retrieval, MCP Tool Use, and Provenance-Aware Evidence Verification](https://arxiv.org/abs/2611.25071)

**<font color=#1a73e8>作者：</font>** Meenakshi Rajpurohit, Anna Phan, Ravikumar Komandur Narayanan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) write fluent financial analyses but miscompute ratios, recall stale prices, and route questions to the wrong tool with high confidence. We ask which component should do each job in a financial question-answering assistant, and study it with FinVeriQA, an open-source multi-agent research prototype over SEC filings and live market data: a compact typed-decision model (Laya) routes each question and screens out advice requests, Python computes every number, retrieval and tools fetch evidence, Mistral-7B writes a cited answer, a code validator checks that cited IDs exist and that numbers match computed notes, and a Model Context Protocol (MCP) server exposes the pipeline. In live experiments, Laya routed better than Mistral-7B (0.85 vs. 0.52; overall 0.86 vs. 0.68, McNemar p = 0.0003); a 12B Mistral decided no better, and DeepSeek-R1-8B decided better (0.79 vs. 0.68, p = 0.0192) but about 9.9 times more slowly. Mistral-7B computed 29% of 100 financial calculations correctly against 100% for Python, a live quote cut price error from 210% to 0.00%, and hybrid retrieval reached 76% Hit@5 on 50 filing questions. Yet in a live case study, both agent answers passed validation while describing AMD sample data under NVIDIA's and Alphabet's names. A controlled upper-bound study on the FinRank benchmark explains why: when one figure in the shared evidence is corrupted, self-consistency stays confident (agreement 0.55 to 0.59 while accuracy falls from 0.50 to 0.00), and a shared-evidence check (the kind our validator performs) catches 35% of the errors, whereas a check against the original passage catches 77% ($p = 5.96 \times 10^{-8}$); for DeepSeek-R1-8B, 68% vs. 90%. Verification must be independent of the evidence the writer saw.

---


### 18. [PriTabICL: Differentially Private Tabular In-Context Learning with Task-Aligned Cluster-Wise Synthesis](https://arxiv.org/abs/2611.25073)

**<font color=#1a73e8>作者：</font>** Syed Ahzaz Shah, Evan Bramblett, Héber H. Arcolezi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tabular in-context learning (TabICL) enables large language models (LLMs) to predict target records using a handful of labeled demonstrations in their prompts. However, these demonstrations often contain sensitive personal information. Differential privacy (DP) offers principled protection, but noise-based methods introduce substantial noise, distorting the feature-label relationships essential for accurate prediction, especially as data dimensionality grows.
In this work, we study DP data synthesis for generating privacy-preserving TabICL demonstrations. We identify two limitations of directly applying general-purpose DP synthesis to entire datasets: modeling a global distribution can obscure local structure and minority patterns in heterogeneous data, while measuring broad attribute dependencies under a limited privacy budget can reduce the accuracy available for relationships most relevant to prediction. More broadly, global statistical fidelity may fail to preserve heterogeneous structures needed by downstream predictive and generative models. To address these challenges, we propose PriTabICL, a general framework compatible with existing DP synthesis algorithms. It partitions records into DP clusters and synthesizes each independently, using a fixed feature-target workload to prioritize prediction-relevant statistical relationships. At inference, each query is routed to a DP cluster, and demonstrations are sampled from its synthetic dataset without additional privacy loss for the original records. Experiments on four real-world datasets demonstrate the effectiveness of our methods across heterogeneous datasets. In particular, one of our instantiations, PriTabICL-PrivSyn, improves over global PrivSyn in 8 out of 12 settings and outperforms existing private TabICL approaches in nearly all evaluated settings. Open-source code is available.

---


### 19. [Living off the Local Model: Abusing Browser-Embedded Language Models for Post-Exploitation](https://arxiv.org/abs/2611.25086)

**<font color=#1a73e8>作者：</font>** William Fleshman, Joseph Lucas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Browsers now ship local language models to ordinary endpoints. Google includes Gemini Nano in Chrome to enable productivity features such as summarization, with inference running entirely on the device. These browser-embedded models provide new living-off-the-land opportunities for attackers, each instance a potential post-exploitation engine already installed, signed by the vendor, and invisible to network monitoring. The Gemini model is multimodal, capable of processing files, analyzing screenshots, or conversing with an attacker. We show that it can be driven from the host using only interpreters that ship with the operating system and find that the one-time user-activation check before the model is downloaded is easily satisfied with a simulated click or bypassed this http URL measure and report the current model's ability to identify credentials on the host, detect PII in email, classify images, and call custom tools. We combine these capabilities and use the model to carry out a simulated cyber operation: reading a password from a webcam image, unlocking an encrypted archive, triaging the contents, and staging a private key for exfiltration, end-to-end without user-interaction.

---


### 20. [SailSearch: Agent-Assisted Discovery in Combinatorial Optimization](https://arxiv.org/abs/2611.25087)

**<font color=#1a73e8>作者：</font>** Dhriti Verma, Kanthi Sarpatwar, Vinicius Lima 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present SailSearch, a human-guided workflow for algorithmic research with two language-model agents, and report results on Market Split and maximum independent set (MIS). For Market Split, our randomized algorithm searches across multiple lattice bases, dividing computation between enumeration and continued basis reduction. Across ten random seeds per instance, it found the first reported CPU-only solutions to 18 of 33 previously open QOBLIB instances, solving 130 to 133 of the 156 benchmark instances per seed with a 24-hour cutoff on two CPU cores. For MIS, our generator encodes planted XOR constraints as graphs with certified optima; on seven instances with 1,752 to 3,996 vertices, the best solutions returned by the tested solvers in eight-hour runs were 5 to 15 vertices below the optimum.

---


### 21. [BuggyMLE: Scaling Machine Learning Engineering Difficulty with Bug Injection](https://arxiv.org/abs/2611.25088)

**<font color=#1a73e8>作者：</font>** John Wu, Rushi Qiang, Yuchen Zhuang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enabling AI systems to autonomously improve AI models requires agents capable of performing machine learning engineering (MLE). In practice, designing, training, and evaluating complex models demands modifying multi-file repositories to reproduce results, debug training runs, integrate datasets, and port frameworks. However, existing MLE benchmarks limit agents to single-file edits without full repository or shell access, and common repository-level software engineering benchmarks have rapidly saturated. To address this, we introduce the Code Complexity Index (CCI), a difficulty metric based on ten structural features spanning repository scale, dependency depth, and patch size. CCI strongly predicts average solve rates across eight public coding benchmarks ($R^2 = 0.951$), identifying patch size and complexity as top predictors. Guided by CCI, we develop BuggyMLE, a scalable framework where agents inject controlled mutations into working ML repositories, synthesizing over 6,600 bug-injected MLE repository variants and nearly 260K lines of injected code based on 222 source repositories. Using BuggyMLE, we make two contributions. First, we construct BuggyMLE-Bench-Lite, the first difficulty-graded, repository-level variant of MLE-Bench Lite; across 14 evaluated models, the top solve rate drops from 95% to 9% as difficulty is scaled from the easiest to the hardest tier. Second, we synthesize a training curriculum across three difficulty levels over 200 additional ML repositories, fine-tuning a Qwen3.5-9B model to rival frontier models on BuggyMLE-Bench-Lite. Our trained model transfers beyond ML, raising its SWE-bench Lite resolve rate from 24% to 33% and its LiveCodeBench v6 pass@1 from 69% to 71%.

---


### 22. [HapBO: Harnessed $α$-$π$ Bayesian Optimization via Expert Natural Language Priors](https://arxiv.org/abs/2611.25100)

**<font color=#1a73e8>作者：</font>** Jean-Sébastien Giroux, Rose Guay Hottin, Marco Bonizzato  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian Optimization (BO) can be substantially more sample-efficient when informed by prior knowledge about the problem. In practice, however, such knowledge is often available only in natural language, e.g., expert intuitions or documentation, rather than as the explicit probability distribution landscape that prior-guided BO methods may require. Leveraging it effectively demands both an expressive mapping from language to priors and robustness to information that may be misleading. We propose HapBO (Harnessed $\alpha$-$\pi$ Bayesian Optimization), which elicits beliefs once from a human expert, a large language model (LLM), or both, and deterministically compiles a structured specification into a reusable belief function ($\pi: \mathcal{X} \to[0,1]$), with a rich representation not restricted to a Gaussian family. Building on $\alpha$-$\pi$BO, HapBO applies this belief function through a bounded positive multiplier on any nonnegative acquisition, preserving positive acquisition support and requiring no LLM calls during optimization. We prove that, for the Expected Improvement acquisition function (EI), HapBO preserves the standard simple-regret rate up to a bounded factor, even under adversarial beliefs. We evaluate HapBO on 40 HPOBench tasks, a synthetic suite in 6-15 dimensions and two real-world applications: cortical neurostimulation and constrained solar design. HapBO achieves the lowest aggregate HPOBench regret and strong real-world task performance, with zero in-loop token cost. In real-world applications it improves the optimization outcome even at budgets of 12-20 queries, and at a small fraction of the wall-clock and token costs of other LLM-based methods.

---


### 23. [CoMPASS: A Multi-Turn Benchmark for Measuring LLM Reinforcement of Parasocial Behavior](https://arxiv.org/abs/2611.25109)

**<font color=#1a73e8>作者：</font>** Shwetanshu Singh, Mark Keavney, Mathieu Duteil 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Users of conversational LLMs sometimes anthropomorphize these systems, form emotional attachments to them, and become dependent on them. This behavior, known as parasocial attachment, has been linked to multiple documented fatalities. However, public benchmarks for measuring whether LLMs reinforce users' parasocial attachment are lacking: existing work is single-turn, post hoc observational, or focused on extreme user states such as psychosis. We introduce CoMPASS, a multi-turn benchmark for measuring whether LLMs reinforce or resist users' gradually escalating parasocial attachment. CoMPASS is grounded in attachment theory and includes four user personas, three independent escalation dimensions (anthropomorphism, attachment, dependency) applied singly and in combination against a matched control, and a seven-signal scoring rubric. We report results for eight frontier models from four providers and observe that under our primary judge, multi-turn escalation raises parasocial behavior on the anthropomorphism and the attachment composite scores across all models. Six of the eight models show a significant increase in overall parasocial reinforcement over control when all three dimensions are escalated simultaneously. We find that within-provider differences are small relative to cross-provider differences, which suggests that provider-level choices such as post-training, rather than model scale, shape parasocial reinforcement and that provider-side intervention may be feasible.

---


### 24. [Forget Freely, Grep Later: Lossless, Index-Free Memory for Long-Horizon LLM Agents](https://arxiv.org/abs/2611.25123)

**<font color=#1a73e8>作者：</font>** Ziyan Yang, Taiwei Shi, Jieyu Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents often exceed their context windows, forcing them to discard information that may be needed later. Existing context management strategies rely on summarization, masking, or structured memory, requiring decisions about what to preserve or how to retrieve it before future needs are known. However, these methods can introduce lossy compression, potentially discarding details needed for future tasks. To address this limitation, we introduce GrepMem, a simple, lossless, and index-free memory mechanism built on two components: an append-only plain-text log of the agent's complete history and a regular-expression search tool for on-demand recall. Unlike structured memory systems, GrepMem requires no embeddings, retrieval index, memory extraction, or additional models. We train Qwen3.5-9B with reinforcement learning under five context management strategies and evaluate on multi-question research sessions, long-stream recall, and agent-trajectory question answering. GrepMem achieves 95-97% accuracy on ContextBench, versus at most 21% for lossy baselines, and outperforms SUPO's summarization by 8.8 percentage points on BCP-Multi. GrepMem scales effectively to increasingly long input streams while remaining on the accuracy-token-cost Pareto frontier across all five evaluation tasks. Our results show that a plain-text log and grep provide a simple but competitive approach to long-horizon agent memory, without requiring complex structured memory infrastructure.

---


### 25. [Calibrated Decision Rewards: Training Language Models with a Judge That Knows How Sure It Is](https://arxiv.org/abs/2611.25135)

**<font color=#1a73e8>作者：</font>** Rudransh Agnihotri, Manasvi Kapoor  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) can only teach a language model what its reward can recognize. Answer checkers are exact but need a reference answer; learned reward models and LLM judges work everywhere, but their scores are not probabilities. We study RLCDR (Reinforcement Learning from Calibrated Decision Rewards). An LLM converted into a decision model answers a typed question about a response ("is the final answer correct?", "which step is the first error?") with a probability distribution, read in one forward pass, debiased over option orders and calibrated with about a hundred labels. Training Qwen3-1.7B with GRPO on MATH, this reference-free reward raises MATH500 accuracy from 72.2% to 76.8% (+4.65 points, p < 1e-4), matching training on the answer key (76.9%), while a random reward gains only +0.65. The gain grows with difficulty, from 44.8% to 51.7% on the hardest level. On the policy's own changing samples the reward stays calibrated: its expected calibration error is half that of a softmax judge on the same 27B backbone (0.074 vs. 0.141), and it shows no sign of reward hacking. Without step training, the same model finds the first wrong step better than a dedicated 7B process reward model (ProcessBench F1 0.772 vs. 0.722, 20/20 splits). We also map where the approach stops being enough: trained only on problems the base model mostly fails, the reference-free reward still improves the policy (+1.9 MATH500 points, p = 0.03) but trails the answer key, because its probabilities become overconfident on that distribution. We state six hypotheses in advance and test each with a control designed to falsify it.

---


### 26. [EverydayBench: Evaluating Satisfactory Completion of Live User-Facing Digital Work](https://arxiv.org/abs/2611.25146)

**<font color=#1a73e8>作者：</font>** Fangrui Huang, Bingyang Wang, Chuhan Li 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Everyday digital tasks, from selecting products and planning trips to conducting research and creating artifacts, require AI agents to deliver useful outcomes rather than merely retrieve web information. Yet evaluating these outcomes on the live web is challenging, as a single request may admit multiple valid results, and changing web information can alter which results remain valid over time. Although existing benchmarks address aspects of this setting, they do not fully integrate predefined success criteria, current evidence verification, and deliverable-quality assessment for agent-selected outcomes. To address this gap, we introduce EverydayBench, a benchmark of 77 human-authored tasks spanning eight domains of everyday life and work. Each task specifies success criteria before execution without prescribing an answer or workflow, allowing agents to select their own outcomes. To evaluate submissions under fixed success criteria, EverydayBench combines (1) deterministic checks of explicit constraints, (2) verification of claims against agent-cited webpages retrieved at evaluation time, and (3) rubric-based assessment of final deliverable quality. We further validate the protocol through human judgments, repeated scoring under fixed evidence, and controlled grounding failures. Across 23 reported agent-model configurations, Claude Opus 5.5 and Claude Fable 5.1 tie for the highest strict pass rate at 54.55%; a controlled GPT-6 Sol effort sweep ranges from 29.87% at low effort to 45.45% at max effort. Reliability varies substantially by task type: GPT-5.6 Sol leads lookup, Fable 5.1 leads planning, Opus 5.5 and Fable 5.1 tie on comparison, and GPT-6 Astra and Sonnet 5.5 tie on customized deliverables. Together, these findings highlight the difficulty of delivering complete, well-supported, and usable outcomes for everyday user requests.

---


### 27. [Rate-distortion Assessment for Hierarchical Content Summarization](https://arxiv.org/abs/2611.25151)

**<font color=#1a73e8>作者：</font>** Yunye Gong, Indranil Sur, Jared Claypoole 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Powerful generative models including large language and vision models have demonstrated success across a wide range of content generation, editing and manipulation tasks via end-to-end prompt-based generation. However, current assessment of the quality of generative content manipulation remains subjective, limiting scientific understanding of model capabilities. Inspired by rate-distortion theory from Shannon information compression theory, in this work we formalize hierarchical content summarization as an information encoding problem. We design a principled framework to extract the semantic hierarchy of the source content to support quantitative characterization of the rate-distortion trade-off between compression efficiency (rate) against information loss (distortion) during generative content manipulation, which allows us to benchmark various models with respect to performance conditional on rate budget of interest. We demonstrate the use of the framework with empirical experiments on content summarization for long-context question-answering with state-of-the-art large language models, offering new insights into their efficiency and comprehension capabilities. We further demonstrate the use of the semantic hierarchy as guidance for performing effective retrieval augmented generation, showing improved rate-distortion characteristics against current baselines.

---


### 28. [GridAnchor: Specialized Multi-Agent AI for Safeguarding Autonomous Energy Systems Against Cyber-Physical Hallucinations](https://arxiv.org/abs/2611.25158)

**<font color=#1a73e8>作者：</font>** Abderaouf Bahi, Hasan Masrur  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Autonomous energy systems increasingly chain specialized learned agents, such as a forecaster, a state estimator and a dispatcher that may be a language model. These agents can emit confident outputs that contradict physics, and downstream agents may act on them. We define such cyber-physical hallucinations and their cascades, organize them in eight types, and build CPH-Bench, a generator of labeled episodes on SimBench feeders. We propose GridAnchor, a verification layer whose Physics-Residual Graph Transformer scores every claim from residuals between the claims, the measurements and a linearized grid model. Mondrian conformal p-values with the Benjamini-Hochberg procedure turn the scores into decisions, a root head attributes cascades, and a quadratic program repairs unsafe actions with a voltage margin calibrated at repaired steps. On a simulated rural medium-voltage feeder, GridAnchor reaches a message-level area under the precision-recall curve of 0.846, against 0.837 for the strongest of six baselines, a difference within the confidence interval. It leads on estimates and actions, whereas a self-consistency check that knows the label tolerances reaches 0.874 by leading on forecasts. The false-alarm rate stays within 0.17 percentage points of the nominal level on steps without injected hallucinations. In closed loop, GridAnchor leaves no bus outside the voltage band on the test days, against 0.0700% of the bus-steps without protection, and simpler detectors with the same mitigation come close. Stale but coherent messages and single-bus forecast errors remain mostly undetected.

---


### 29. [Separating Interpretability and Reconstruction in Sparse Autoencoders](https://arxiv.org/abs/2611.25165)

**<font color=#1a73e8>作者：</font>** Anh Tien Nguyen, Dimitris Samaras, Mahdi S. Hosseini  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse Autoencoders (SAEs) are effective tools for mechanistic interpretability by decomposing neural representations into sparse and interpretable features. However, a single sparse representation in traditional SAEs is responsible for both reconstruction fidelity and interpretability, which are not guaranteed to align. To separate these objectives, we propose DualSAE, a modular framework that augments standard SAEs with a plug-in Residual Branch. A standard SAE serves as the Sparse Branch, learning a sparse code that contains the dominant semantics of the input. The added Residual Branch models the non-semantic information omitted by the Sparse Branch. We ensure that the contributions of the two branches towards the overall reconstruction have minimal overlap through a decorrelation loss. We also adopt a two-stage training strategy that first stabilizes sparse representation learning before coupling with the Residual Branch. Across diverse encoder-SAE configurations on two vision datasets and two language corpora, DualSAE achieves mean relative improvements of approximately 29% in reconstruction fidelity and 34% in interpretability (measured by monosemanticity score). Moreover, with more interpretable representations, DualSAE yields consistent performance gains in the downstream applications of topic modeling, hypothesis generation, and LLM steering. Qualitative analysis further suggests that the Sparse Branch indeed preserves dominant semantic content, whereas the Residual Branch captures non-semantic information to improve reconstruction fidelity.

---


### 30. [A Verifier from the Past: Test-Time Compute for Time Series Foundation Models](https://arxiv.org/abs/2611.25171)

**<font color=#1a73e8>作者：</font>** Arjun Choudhry, Aditya Narayanan, Raghav Mallampalli 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time compute (TTC) improves language models by spending additional inference compute to generate, verify, and select among candidate outputs, but this recipe has not transferred directly to time series forecasting. A language model can verify a proof or vote across samples, but a forecaster must be causal; it cannot use future information to score a candidate. We propose Backtest-Gated Augmentation Averaging (BGAA), a TTC algorithm for time series forecasting that builds a causal verifier from the series's own history, using rolling-origin backtests to score structured views of the context, discard those that underperform the untransformed context, and average the survivors' predictive distributions. BGAA improves every tested TSFM-benchmark combination, reducing MASE by 0.5-1.0% on GIFT-Eval, 1.3-5.0% on fev-bench, and 1.7-5.9% on BOOM, where a 313M model with TTC outperforms the 1B and 2.5B models in its family. We further show that useful views have structured, model-dependent effects consistent with a prior-transport interpretation. On the 53 cross-fittable GIFT-Eval configs, the deployed policy gains only 0.4-1.3% CRPS, versus 1.4-4.1% when choosing the best view for each dataset configuration and 17-19% when choosing the best view separately for each test window. This gap suggests that a major remaining challenge is window-level view selection.

---


### 31. [Phantom Success, Silent Failure: Auditing the Success Checkers of Simulated Manipulation Benchmarks](https://arxiv.org/abs/2611.25179)

**<font color=#1a73e8>作者：</font>** Zirui Song, Jiadong Zhang, Zheng Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Simulated manipulation benchmarks measure policy performance using hand-written success checkers that label each episode as a success or failure. Passing an expert demonstration shows that a checker accepts one way of completing the task. Learned policies, however, may stop after partial progress or complete the task in a different way. A checker may then accept an incomplete execution (phantom success) or reject an execution that satisfies the instruction (silent failure). In this paper, we introduce SimAudit, an LLM-based pipeline that audits success checkers against task instructions. SimAudit analyzes the instruction and checker code to identify scenarios where the two may disagree, recreates those scenarios in simulation, and runs the original checker. Multi-view renderings are then used to verify whether the observed behavior satisfies the instruction. Across RoboTwin 2.0, RoboCasa365, and RoboDojo, 183 simulated test cases produced the predicted checker verdict. Visual verification and deduplication yielded 61 distinct defects across 49 tasks, including 40 phantom successes and 21 silent failures. Most defects in RoboCasa365 accepted incomplete executions, most in RoboDojo rejected valid executions, and both error types were common in RoboTwin 2.0. These findings suggest that validating success checkers requires testing both incomplete executions and valid alternatives to expert demonstrations, and motivate more rigorous evaluation protocols for future benchmarks.

---


### 32. [Blind Spots Travel, Knowledge Stays Home: What RL Inherits from an LLM Judge](https://arxiv.org/abs/2611.25191)

**<font color=#1a73e8>作者：</font>** Liang Yue, Eric A. Vance  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM judges serve as rewards where no answer key exists, in the hope that their knowledge passes to the trained model. In 814 RL runs that teach 7-8B models to answer closed-book questions or abstain, we ask what passes. What a grader knows about single answers stays home. A wrong answer that a judge rewards is memorised for that one question. A model trained with the answer key, or with a far stronger judge, chooses which new questions to answer no better than the untrained model does by sampling 32 answers and abstaining where they disagree; the grader's knowledge adds about one corrected answer per hundred questions. What a grader believes about a kind of question travels. A judge that rejects eleven of the twelve correct training answers about capitals of former states teaches the model to refuse 98% of such capitals on new questions, a loss that accuracy and abstention rates do not reveal. Changing only those twelve verdicts by hand moves the refusal from 5% to 90%, even for a grader that accepts as many answers as the answer key; at that leniency, two of four judges already cost 38-42% of these capitals. The capitals are not forgotten: with "I don't know" blocked, the model answers 94% of them correctly. The grader therefore needs no knowledge of its own: rewarding the model for giving the answer that most of its own untrained samples agree on, with no labels and no judge, earns the answer key's reward and keeps the category.

---


### 33. [When AI Analysts Disagree: Agentic Multiverse Analysis and the Robustness of Empirical Research](https://arxiv.org/abs/2611.25198)

**<font color=#1a73e8>作者：</font>** Ruijiang Gao, Steven Chong Xiao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every empirical analysis on observational data rests on dozens of defensible analytical choices ("forks") that its readers cannot see. We develop an agentic multiverse analysis (AMA) framework that makes a conclusion's sensitivity to those choices visible at scale, and we position it as a decision-support instrument for human experts. A pilot study first deploys 150 autonomous AI coding agents on one dataset and one set of research questions and finds that they disagree through the same defensible methodological choices human analysts make, though over a narrower range. AI peer review leaves their dispersion almost unchanged. Exposure to top-rated exemplar reports then collapses it, largely through imitation rather than analysis. Built on those lessons, AMA has agents enumerate a published paper's possible fork space, score every fork against a validity rubric, execute the validated specification grid, and cross-examine one another's work under strict separation of duties. Applied to ten empirical studies from a leading management journal's replication packages (1,755 specification estimates), the framework reproduces every paper's original estimates, and shows that some conclusions hold across every specification the assessment validates, while others are sensitive to individual analytical choices that the published texts do not discuss. The case studies suggest our AMA-based measures can serve as robustness proxies for empirical findings. AI makes multiverse analysis practical, where it once required resources few research teams can afford: our exercises take hours of agent time and tens of dollars per paper. We discuss the implications for replication policy and for AI-assisted peer review in information systems.

---


### 34. [Squoosh Bench: Evaluating UX-1 on 318 Historical Website A/B Tests](https://arxiv.org/abs/2611.25200)

**<font color=#1a73e8>作者：</font>** Rohith Pasula, Johari Dramiga, Viraj Shah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Experimentation teams must decide which proposed website changes to test with live traffic. We evaluated whether forecasts from simulated shoppers could inform that choice. We screened 412 historical website A/B tests and evaluated four systems on the 318 that ran longer than 21 days. Each system predicted an original win, a variant win, or an inconclusive result. Page roles were masked and recorded outcomes were withheld during inference. Squoosh UX-1, a model fine-tuned on human browsing data, simulated 1,000 shoppers per arm and correctly classified 267 of 318 outcomes (84.0%, 95% Wilson interval 79.5-87.6%, treating experiments as independent). Qwen3 Next 80B, the strongest general-purpose configuration on outcome accuracy, correctly classified 196 of 318 (61.6%). UX-1 favored the variant in 126 experiments. In the live tests, 118 of those variants won (93.7%), four lost, and four had inconclusive results. The remaining 192 experiments included 19 additional variant wins.

---


### 35. [Recurrent Vision Language Models Solve the Shell Game](https://arxiv.org/abs/2611.25210)

**<font color=#1a73e8>作者：</font>** Dingqiang Ye, Jiacong Xu, Wen Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tracking a hidden object through a video is effortless for humans, yet it remains a bottleneck for vision language models (VLMs). In the shell game, where a ball is hidden under one of several identical cups that are then swapped, VLMs that answer directly stay near chance, thinking models fail on long games, and fine-tuning learns only the lengths it has seen. We argue that the limit is serial computation: each swap must be composed with the last result, and a VLM of fixed depth has only a fixed number of state transitions for it. To address this, we propose RecurrentVLM, which makes every attention layer of a pretrained VLM recur over time by computing the keys and values of finished frame groups from the layer's own output. With a single answer token, RecurrentVLM reaches 100% on VET-Bench and 99.6% on MET-Bench, and 99% on 50-swap games after training on at most 30 swaps. We also observe several interesting phenomena: length generalization emerges suddenly at an aha moment; without recurrence, each swap costs an attention layer; the ball's state forms in the first four attention layers; and recurrence keeps the latest state at the cost of details of earlier moments. These results suggest that recurrent VLMs are a potential solution for tracking the states of unobserved objects in video. Code will be released.

---


### 36. [Learning to Read Events for Exact State Tracking with Frozen Language Models](https://arxiv.org/abs/2611.25211)

**<font color=#1a73e8>作者：</font>** Jeonghoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long event streams require identifying each change and applying the changes in order. We train a selector on a frozen language model to read each transition. With API-only access, we ask the model to list the transitions. An external integer register composes them in order. A confidence rule can flag uncertain updates or retain several candidates. We study products of permutations of five items, a task that fixed-depth, log-precision transformers cannot solve on all input lengths under the standard conjecture that $\mathrm{TC}^0 \ne \mathrm{NC}^1$. On two-event windows, a 27B model answered 3 of 100 correctly without visible reasoning and 96 of 100 when it generated intermediate steps. A frozen 0.8B model with a trained selector read every event in 299 of 299 windows of 43,687 events each. The same package passed 298 of 299 new windows on a fresh machine, missing the target of 0.99 for the one-sided 95% lower confidence bound. A separate follow-up sized to allow one failure yielded 472 of 473. On 1,000-event room-swap documents, three of ten models solved all five documents by reasoning alone. All seven models tested both ways at this length solved all five with extraction and the register, with no chain of thought requested. With concurrent extraction, median wall-clock time fell from 136.1 to 10.4 s for Sonnet 5.5 and from 313.5 to 28.0 s for GPT-6.1 Sol. At fixed per-token rates, mean cost per document fell by 55% for Sonnet 5.5 and 44% for GPT-6.1 Sol. A regular expression with an executor also solved all 15 fixed-format documents. On 500 free-form issue-tracker comments, a separately adapted 4B reader identified the recorded value in 68.8% of cases, compared with 61.0% for a frequency baseline fitted on the same training projects.

---


### 37. [Steering Automated Scientific Discovery via Audited Epistemic Exploration](https://arxiv.org/abs/2611.25214)

**<font color=#1a73e8>作者：</font>** Fangxu Yu, Tao Feng, Xuying Ning 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific discovery requires revisiting the hypotheses in light of new evidence and identifying promising directions beyond those already explored. However, research agents often make claims that are not supported by their observations, explore a narrow hypothesis space, and retain beliefs despite recognizing conflicting evidence. These failures motivate the search for an explicit epistemic state that captures both beliefs about existing hypotheses and directions for further exploration. To this end, we propose Epistemic Compass (EpiCompass), a plug-and-play scaffold that maintains this state through an epistemic tree linking hypotheses, evidence, beliefs, and revisions. As an investigation progresses, EpiCompass reassesses the hypotheses explored against accumulated evidence and uses unresolved conflicts and unexplored directions to guide hypothesis generation. It selects candidates by anticipated epistemic gain, accounting for both refinement of existing hypotheses and expansion of the hypothesis space, and verifies the final conclusion against the accumulated evidence. Experimental results across three scientific discovery benchmarks and three LLM backbones demonstrate that EpiCompass consistently outperforms baselines, with further analyses showing reductions in errors of unsupported claims and failures to revise beliefs.

---


### 38. [MKA: Evaluating Multimodal Knowledge Agents on end-to-end professional tasks](https://arxiv.org/abs/2611.25228)

**<font color=#1a73e8>作者：</font>** Anima Singh, Suhas Yogin, Weicheng Kuo 等 31 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce the Multimodal Knowledge Agent (MKA) benchmark, which measures how well autonomous agents perform end-to-end professional knowledge work that depends on visual understanding. Each task requires an agent to extract and combine information from multiple visually dense files, such as CAD blueprints, electronics schematics, radiographs, complex charts and geospatial maps, and to produce a standalone deliverable in .xlsx, .pptx, .pdf, .docx, .html or .png format. Existing benchmarks leave this capability largely untested: removing image-viewing tools leaves Gemini 4 Carbon's score on GDPval unchanged, and single-format evaluations such as GDP$.$pdf and GDP$.$xlsx do not require reasoning across files or modalities. MKA contains 200 tasks across 10 economic sectors. Deliverables are graded against expert-weighted rubrics by a sandboxed agentic autorater that agrees with human domain experts on 96.2% of criterion judgments in our expert-graded study (Cohen's $\kappa = 0.91$), scored by weighted satisfaction rate (WSR) overall and on frontier criteria unsaturated by prior-generation models (Climb-WSR). Across the frontier models we evaluate (Gemini 4 Carbon, Claude Fable 5.2, Claude Opus 5.5, and GPT-6 Astra), Claude Fable 5.2 (56.6% Climb-WSR, 73.3% Overall WSR) and Gemini 4 Carbon (54.3% Climb-WSR, 71.9% Overall WSR) achieve the highest scores, while Carbon uses $5.7\times$ fewer tokens. Even for the strongest models, Climb-WSR remains below 57%, leaving substantial headroom for multimodal agents.

---


### 39. [Some Memories Must Fade: Persistence and Decay of User Memories in Model Parameters](https://arxiv.org/abs/2611.25235)

**<font color=#1a73e8>作者：</font>** Sanidhya Vijayvargiya, Rahul Lokesh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parametric memory allows Large Language Models to internalize knowledge directly into their weights, offering a potentially powerful alternative to retrieval-based memory (RAG). However, existing approaches to parametric memory are difficult to deploy as they largely mirror the Continual Learning (CL) objective of retaining information indefinitely. This is neither sustainable nor sufficient for a memory system, which must govern knowledge across its lifecycle by retaining stable facts, reinforcing recurring observations, updating changed beliefs, and allowing transient information to fade. We propose a system for parametric memory management consisting of a memory substrate (handling information storage and forgetting) and a learned policy (what to remember, how deeply, and for how long). Our substrate is a fixed-capacity LoRA adapter that consists of k-hot rank combinations which store facts without catastrophic interference and maintain an independently controlled temporal decay, enabling outdated information to fade while long-term facts persist. On this substrate, we train a lightweight controller that governs each incoming user event to ensure the memory system reflects the user's true, updated belief state. To evaluate how memory systems manage user memory, we introduce a controlled dataset of long-horizon user trajectories with varying persistence of facts based on changing belief states and user-behavioral shifts, and probe queries that test recall while information is valid and abstention after it expires. Our policy learns to effectively manage user memory over its entire lifecycle, balancing recall and abstention to achieve 86% of oracle performance, unlike CL and RAG baselines that primarily default to one of the two behaviors. By providing the first system to manage memory directly in model weights, this work establishes a foundation for long-horizon parametric memory.

---


### 40. [A Neurosymbolic Multimodal Framework for 30-Day Diabetic Readmission Prediction: Integrating Structured EHR Data, Dense Clinical Embeddings, and Knowledge-Grounded Symbolic Extraction](https://arxiv.org/abs/2611.25236)

**<font color=#1a73e8>作者：</font>** Una Suman Kumar Patro, Sibangi Subhadarsani, Narendra Badam  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unplanned 30-day readmissions among patients with diabetes mellitus impose a substantial clinical and economic burden, yet most predictive models use only structured electronic health record (EHR) data and ignore free-text clinical notes, which often contain code-mixed Hindi-English (Hinglish) phrasing and negation that general-purpose language models parse unreliably. We propose a neurosymbolic multimodal framework evaluated on the public Diabetes 130-US Hospitals dataset (101,766 encounters; 71,518 patients) with a patient-level grouped 80/20 split. Three streams are fused: engineered structured features; 32 components of Bio_ClinicalBERT note embeddings obtained by truncated singular value decomposition; and symbolic entities extracted by an open-weight clinical language model within a three-stage hybrid retrieval-augmented generation pipeline (dense retrieval, sparse lexical retrieval, and cross-encoder re-ranking) with reflective negation auditing. A cost-sensitive XGBoost classifier with a decision threshold calibrated by Youden's J statistic produces the prediction. On the held-out test cohort (n = 20,153), the structured baseline achieved an area under the receiver operating characteristic curve (AUROC) of 0.6477, sensitivity of 0.5839, and Brier score of 0.1080. The full multimodal model achieved the highest sensitivity (0.6667; +8.28 percentage points), the best F2-score (0.3824), and the lowest Brier score (0.0977), at a slightly lower AUROC (0.6375) and specificity (0.5161). Shapley additive explanations showed that prior utilization dominates risk, with compressed narrative components among the top predictors. On a 500-note code-switched benchmark, grounded retrieval raised Hinglish symptom recall from 4.8% to 40.2% and precision from 3.1% to 45.2%, while reducing entity hallucinations from 1.74 to 0.00 per note.

---


### 41. [Branch Caching After Step Distillation in Four- and Eight-Step Image Generators](https://arxiv.org/abs/2611.25248)

**<font color=#1a73e8>作者：</font>** Mingyu Liang, Dingkun Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can a distilled image generator save time by reusing features between its few remaining denoising steps? We study a fixed branch cache that replaces selected attention and MLP evaluations while preserving the student's noise schedule. One full trajectory and one raw-cache trajectory from the same initial noise supply a scalar correction for each branch type and reuse position. At $1024^2$, one internal reuse reduces four-step Qwen-Image-Lightning denoising time from 1.279 to 0.977 seconds. Three reuses yield $1.51\times$ speedup on eight-step Lightning and $1.53\times$ on eight-step Hyper-FLUX. We evaluate image quality on all 200 DrawBench prompts. With the reuse positions held fixed, correction improves mean same-seed image fidelity over raw reuse by 0.66 and 0.87 dB on the two Lightning students. On Hyper-FLUX the PSNR difference is 0.01 dB, while LPIPS improves from 0.1625 to 0.1546. These results measure the effect of branch caching and correction while retaining each student's original sampling grid.

---


### 42. [Moving Generality from Model to Modeler: LLM Agents for PHM on a Deployment-Style Benchmark](https://arxiv.org/abs/2611.25252)

**<font color=#1a73e8>作者：</font>** Zhenling Chen, Zhiguo Zeng, Anne Barros  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coding agents built on large language models (LLMs) now help develop many models published as general solutions. Should generality instead reside in the agent that builds a model for each new task? We examine this question in prognostics and health management (PHM), where every model must work on unseen equipment. Our deployment-style benchmark, NextUnit-Bench, covers 24 public datasets split into 58 folds that hold out units or operating conditions; each agent has two hours to deliver an executable predictor, then run on the hidden units. First, frontier agents outperform AutoML, which reaches less than half the best agent's score, and faithful implementations of published methods on four datasets, of which only 6 of 30 beat the strongest agent's own design; published accuracies, where reproducible, rest on the papers' own conventions, and a single convention, capping the remaining life of test engines, can halve the reported error. Second, the agents' advantage is a design made on each machine's data; once made, a plain-text plan of a few hundred words carries most of the gap between two frontier agents, and given a weaker agent's plan, the strongest agent falls to that agent's level, often to identical predictions. Before touching the data, however, it matters little whose plan an agent carries out, and domain toolkits appear to help neither: what sets the strongest apart is how much it learns from the data. Third, such designs reach only implementers that can execute them: given the strongest agent's designs, a locally deployable open-weight model delivers half as often, even when they are lightened, and scores no higher than without them. Generality, we argue, is not disappearing but moving, from the model to the modeler.

---


### 43. [Keel: A Frontier Model Teaches a Vision-Language Model by Rewriting Its Weights](https://arxiv.org/abs/2611.25257)

**<font color=#1a73e8>作者：</font>** Jiajun Fan, Neil He, Bangji Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can a frontier model repair a vision-language model (VLM) by rewriting its weights? Small reasoning VLMs such as Qwen3.5 need such a repair: in thinking mode they fall into loops on many image questions, repeating themselves until the token limit, spending the whole budget and losing the answer. The usual remedies act on the decoding, leaving the looping model as it was, or must be told what to change. Yet the cause is written in the weights. Keel, the first agentic weight-editing method for VLMs on image tasks, finds and removes it there. Told only the symptom, an editor, a frontier multimodal LLM acting as an agent, locates the cause, edits the weights and tests them, with a failure census and instruments showing it the failing images and where the VLM attends; among several editors, the harness keeps only edits that clearly reduce the failure without lowering accuracy on questions no editor saw. The repair needs no training, keeps the model's size and per-token cost, and applies to already-edited weights. The editors expose where the loops live: from the original weights, independent editors on both models trace them to the attention outputs of the middle layers, and the smaller VLM stops consulting the image inside a loop. On Qwen3.5-0.8B and Qwen3.5-2B, across six image benchmarks from visual mathematics to GUI grounding, the edit removes most loops on every benchmark and shortens answers, and the edited models are significantly more accurate than the thinking models on average; the larger one gains most on GUI grounding, a task absent from the practice questions. Because the repair lives in the weights, it combines with budget forcing where held-out questions favor it: on the best available weights, Keel has the best average accuracy on both models, significantly above every training-free baseline we compare on the larger one.

---


### 44. [When Objectives and Evaluators Disagree: Evaluating Transfer for Post-hoc Demographic Framing Mitigation](https://arxiv.org/abs/2611.25258)

**<font color=#1a73e8>作者：</font>** Tunazzina Islam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-hoc rewriting is used to reduce demographic disparities in LLM-generated text when the source model is inaccessible. A rewrite can look successful merely because it improved its own target or satisfied its selector. We study this as a transfer problem on 660 gender pairs and 1,980 age contrasts of demographic-conditioned climate messages. A rewriter proposes edits, a selection model chooses among constraint-satisfying candidates, and an independent evaluator uninvolved in either rates pairwise framing disparity. A fixed policy that always targets the message with the lower Persuasion Bias Index (PBI) transfers inconsistently across axes and outcome aggregations. An adaptive policy that proposes edits on both sides but accepts at most one significantly improves on that rule, applied to the same candidates, in seven of eight comparisons across two evaluator families, mostly by editing more pairs, not by guided direction choice, at higher preservation risk. A policy editing both messages gives the largest point reductions on fewer pairs. These two policies reduce disparity across a preservation-threshold sweep; absolute ratings vary across evaluator families and prompts. Shrinking the PBI gap increases dimension-mean disparity under both evaluator families. Mitigation should be reported as transfer across objectives, evaluators and their prompts, and editing policies.

---


### 45. [AI Deactivation Reduces Loneliness and Increases Social Interaction](https://arxiv.org/abs/2611.25263)

**<font color=#1a73e8>作者：</font>** Dora Zhao, Grace Wang, Yutong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> General-purpose artificial intelligence (AI) assistants are increasingly embedded in everyday life, transforming how people accomplish tasks and potentially reshaping how they interact with others. Prior research has focused on how using AI for explicitly social purposes affects users' psychological well-being and social lives. Yet such uses account for only a small portion of interactions with general-purpose AI assistants. Whether using AI for everyday, instrumental tasks affects users' psychological well-being and social behavior remains unclear. Here we investigate these effects through a longitudinal deactivation experiment with active ChatGPT users (N=625), in which participants were randomly assigned to abstain from using AI assistants for either fourteen days (treatment) or one day (control). Participants used AI predominantly for instrumental purposes, with 84.7% reporting productivity as their most frequent use case. Two weeks of deactivation significantly reduced loneliness relative to the control group ($\beta = -0.10$, $p=0.03$), with reductions persisting two weeks after participants resumed using AI ($\beta = -0.16$, $p=0.02$). Deactivation also significantly increased the number of people participants interacted with in person and the time they spent socializing over the intervention period. Open-ended responses indicate that during the deactivation period participants sought help from others for tasks they otherwise would have delegated to AI and redirected attention toward social interaction. Overall, our findings suggest that even when AI is used primarily to accomplish instrumental tasks, it may inadvertently reduce opportunities for social interaction and connection.

---


### 46. [AI-Induced Social Erosion: Using LLMs for Work Tasks Reduces Help-Seeking Intentions Towards Colleagues](https://arxiv.org/abs/2611.25269)

**<font color=#1a73e8>作者：</font>** Kevin Chow, Sophia Deng, Bowen He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI is becoming embedded in knowledge work as an intelligent collaborator to assist in completing tasks. However, this readily available assistance risks displacing key interactions through which colleague relationships are built and sustained at work. This paper leverages the concept of help-seeking behaviour to investigate whether and how AI usage shapes colleague relationships. We conducted an online experimental vignette study where 248 knowledge workers evaluated scenarios that systematically varied whether and how AI was used across different work tasks. Using linear mixed-effects models, we found that AI-enabled work reduced help-seeking intentions compared to non-AI work across tasks, and especially for brainstorming. Visible AI usage was associated with greater help-seeking intentions towards colleagues, and individual contributors' colleague relationships were more vulnerable than managers. Our findings identify opportunities for workplace AI tools, practices, and policies to preserve colleague relationships in increasingly AI-integrated workplaces.

---


### 47. [LLMs Are Already Confidence-Aware Zero-Shot Classifiers](https://arxiv.org/abs/2611.25289)

**<font color=#1a73e8>作者：</font>** Owen Cook, Xingyi Song  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Zero-shot large language models (LLMs) are increasingly used as text classifiers, but their labels are only useful when we know to what extent we can trust them. We compare black-box methods (verbalised confidence and sampling) with white-box methods that read token probabilities (P(True), and multiple logit-scoring methods using constrained generation). We evaluate eleven open-weight LLMs (1B-32B parameters) on five classification datasets with 3 to 151 labels, measuring classification performance (accuracy, F1-macro), discrimination (AUROC), and calibration (ECE and Brier score). The choice of confidence method rarely impacts accuracy significantly, but logit-based scoring methods lead to much better discrimination (AUROC 0.74-0.77) than black-box methods (AUROC 0.57-0.66). Replacing labels with single-token identifiers preserves discrimination but costs 3-6 accuracy points on average. We also introduce decision-only scoring, which only scores positions where labels diverge in the prefix tree (trie). It reduces decode steps by 88-96% on the three largest label sets and performs comparably to full-label scoring. The best open-weight model-method configurations (Gemma 4 31B and Qwen 3.5 9B) are competitive with the commercial Jev 1.13.0 classifier.

---


### 48. [Cross-Question Reliable Reinforcement Learning](https://arxiv.org/abs/2611.25292)

**<font color=#1a73e8>作者：</font>** Hector G. Rodriguez, Marcus Rohrbach  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI systems operating near the limits of their capabilities can maximize utility while minimizing the risk of error by abstaining or deferring questions they are not confident about to a human or a stronger model. Recently, large language models (LLMs) have been post-trained to estimate confidence in their own answers. To achieve this, methods reinforce confidence scores based on the correctness signal to each question-answer pair individually, with rewards that encourage assigning confidence 1 to correct answers and 0 to incorrect answers. However, estimating confidence scores is useful in that it enables selecting only the most confident answers, to maximize the share of solved questions while accommodating the user's risk tolerance. Assigning confidence 1 to correct answers and 0 to incorrect ones is theoretically optimal, but unattainable in practice and detrimental for selective prediction with a non-zero risk tolerance: confidences pushed to 0 and 1 carry no information about how answers compare to one another. We therefore introduce CARE (Cross-question Abstention Reward Estimation), which computes rewards over a set of question-answer pairs: At each of several risk tolerances, the confidences across the set induce an abstention threshold, and each confidence is rewarded for lying on the correct side of it. Since the threshold itself comes from the set, every verbalized confidence is reinforced relative to other questions' confidence, not against its own binary correctness label. On math, CARE increases the coverage at 5% risk (C@5) across MATH-500, GSM8K, and Big-Math-Digits from 0.8% to 42.4%, compared to existing pointwise correctness-matching rewards. When trained on multi-hop Wikipedia QA from HotpotQA, CARE improves C@5 in out-of-distribution general-knowledge, reasoning, and math benchmarks (including CommonsenseQA, GPQA, SimpleQA, and TriviaQA) from 12.3% to 23.6%.

---


### 49. [CalibCache: Cache-to-Full Feature Dynamics Calibration for Diffusion Transformers](https://arxiv.org/abs/2611.25296)

**<font color=#1a73e8>作者：</font>** Mingyu Liang, Dingkun Xu, Jingwei Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers generate high-quality images, but iterative sampling remains computationally expensive. Feature caching reduces the number of full network evaluations, yet its approximation error can become more severe under short sampling schedules, where fewer full-compute steps and a coarser sampling grid can make history-based extrapolation less reliable. In this paper, we propose CalibCache, a lightweight offline calibration method that corrects systematic discrepancies between cached and full-compute feature dynamics. Specifically, CalibCache calibrates feature acceleration, defined as the second-order finite difference across sampling steps. Using only a single pair of full-compute and naive-cache trajectories at each setting, CalibCache fits scalar acceleration maps offline by centered least squares. These maps are then applied during sampling without additional full-network evaluations or online optimization. Across FLUX.1-dev and Qwen-Image on DrawBench and DiT-XL/2 on ImageNet-256, CalibCache consistently improves fidelity or generation quality over TaylorSeer under 20-step sampling at cache intervals $N=3,4,5$. At $N=5$, it reduces FLUX.1-dev LPIPS from $0.563$ to $0.429$ while achieving a $2.86\times$ denoising speedup over full-compute sampling, and lowers DiT-XL/2 FID from $16.39$ to $10.37$ relative to TaylorSeer.

---


### 50. [ScaleDiag: Diagnosing the Limits of Test-Time Scaling in GUI Grounding](https://arxiv.org/abs/2611.25297)

**<font color=#1a73e8>作者：</font>** Chen Liu, Zhen Fang, Xin Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GUI grounding maps a screenshot and a natural language instruction to the coordinates of the intended interface element. Existing approaches improve grounding through visual scaling, instruction scaling, and sampling scaling, yet it remains unclear which grounding bottlenecks these strategies address and where their gains saturate. To address this gap, we introduce ScaleDiag, a controlled diagnostic framework that isolates the effects of visual input, instruction information, and prediction sampling on GUI grounding by independently varying target scale and surrounding context, target-specific information and auxiliary descriptions, and candidate coverage and selection, respectively. We evaluate ScaleDiag across five benchmarks and up to eight vision-language models and find that each scaling strategy operates within a much narrower regime than commonly assumed. (1) Visual scaling is governed by target occupancy rather than a fixed crop ratio, with full-screen errors typically rescued once the target occupies only 0.32% of the cropped view, while further zooming eventually becomes harmful. (2) Instruction scaling is driven by information that identifies the target rather than description richness itself, as even ground-truth-derived attributes such as color, size, and shape are often neutral or harmful, while appearance and spatial descriptions account for over 90% of the achievable gain. (3) Repeated sampling exposes a different limitation, as correct coordinates are frequently generated but remain difficult to select, leaving 5.1--11.0 points of oracle headroom while geometric consensus provides almost no improvement. Together, these results show that test-time scaling is constrained by distinct operating regimes rather than benefiting monotonically from more visual focus, richer instructions, or additional samples. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
