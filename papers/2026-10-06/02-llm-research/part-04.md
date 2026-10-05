# 🧠 大模型相关研究 | 2026年10月06日

> 本类共 **261** 篇论文：已确认 **243** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-261](./part-06.md)

---

### 151. [Reliable Self-Evolution with Imperfect Proxy Rewards](https://arxiv.org/abs/2610.02975)

**<font color=#1a73e8>作者：</font>** Kangjun Noh, Soyu Kim, Kyungwoo Song  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based self-evolving search is a promising approach to scientific discovery. However, high-fidelity evaluation of every candidate is prohibitively expensive in some domains. Self-evolving systems in such settings therefore rely on low-cost but imperfect proxy rewards, which may assign high scores to infeasible candidates. These false positives may contaminate both the final output and the feedback used to guide subsequent generations. This motivates statistically calibrated reward intervals for more reliable self-evolving search. We propose Conformal Interval-Driven Self-Evolution (CISE), which constructs candidate-specific reward intervals using conditional conformal inference and iteration-wise online density-ratio estimation. CISE uses conservative interval-based rewards for evolutionary feedback and returns candidates only when all required property intervals lie entirely within their respective feasible regions. We derive fixed-iteration coverage results under explicit assumptions of independence and covariate shift. We evaluate CISE on three self-evolving search tasks in materials science. In our experiments, all candidates returned by CISE are true positives under high-fidelity evaluation, whereas the baselines return more candidates but include false positives. These results highlight the value of a smaller, more precise shortlist when downstream validation budgets are limited. Our repository is available at this https URL.

---


### 152. [Relevant Evidence Decoding for Audio-Visual Hallucination Mitigation](https://arxiv.org/abs/2610.02976)

**<font color=#1a73e8>作者：</font>** Hyunjae Ra, Aecheon Jung, Jungin Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Audio-Visual Large Language Models (AV-LLMs) remain prone to cross-modal hallucinations, where one modality incorrectly affects predictions about another. Although contrastive decoding reduces hallucinations in vision-language models, its direct extension to AV-LLMs overlooks a key challenge: different questions require different perceptual evidence, including audio, video, or their interaction. Notably, we observe that joint audio-visual inference can weaken the prediction even when a model can recover the correct answer from a single informative modality. For example, when asked which instrument is heard, a model may correctly predict violin from the audio alone. Once a video showing a guitar is added, its confidence in violin may drop. In this paper, we introduce Relevant Evidence Decoding (RED), a training-free method that identifies question-relevant evidence and selectively strengthens its contribution. RED uses pointwise mutual information to quantify the predictive support provided by audio and video beyond the question alone. It decomposes their joint contribution into audio, video, and residual interaction components. A question-only inference pass determines the required evidence type, after which the model augments the original audio-visual prediction with the corresponding PMI contribution. Across three audio-visual hallucination benchmarks and three AV-LLMs, RED improves accuracy over standard decoding by up to 7% on CMM, 6.3% on AVHBench, and 3.8% on SVHalluc, with an average relative time to first token of 1.5x standard decoding.

---


### 153. [RASPER: Reward-Aligned Summarization of Clinical Notes for EHR Outcome Prediction](https://arxiv.org/abs/2610.02979)

**<font color=#1a73e8>作者：</font>** Arya Hadizadeh Moghaddam, Mohsen Nayebi Kerdabadi, Chen Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unstructured discharge notes in Electronic Health Records (EHRs) often carry signal complementary to structured medical codes, holding patient-specific evidence that standardized cohort-level codes alone cannot capture. However, this evidence in notes is frequently buried in lengthy, noisy text that is not intentionally written with any specific clinical prediction in mind. Summarization is an obvious mitigation, but generic summaries, tuned for fluency rather than the outcome, routinely omit decisive evidence while retaining plausible but uninformative detail. To this end, we propose RASPER, a Reward-Aligned Summarizer for Prediction in EHR, that optimizes note summarization directly against the downstream clinical task. RASPER employs a tunable LLM-based summarizer to extract task-relevant evidence from discharge notes and trains it via reinforcement learning from prediction feedback, using a reward derived from the downstream predictor's loss. To ground the summarizer, a longitudinal encoder converts structured codes into soft prompts that incorporate each patient's clinical context into note summarization. By rewarding the quality of the resulting multimodal prediction, RASPER encourages the summarizer to retain patient-specific evidence that complements, rather than duplicates, information captured by structured codes. RASPER consistently outperforms strong baselines on both readmission prediction and medication recommendation across MIMIC-III and MIMIC-IV.

---


### 154. [PLCWorld: Benchmarking LLM-Generated PLC Programs in Closed-Loop Plant Simulation](https://arxiv.org/abs/2610.02982)

**<font color=#1a73e8>作者：</font>** Yunji Kim, Yunseok Lee, Hyunwoo Seo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Programmable logic controllers (PLCs) coordinate industrial equipment by reading sensor inputs and issuing control commands. Evaluating whether large language model (LLM)-generated PLC programs satisfy task requirements and safety constraints requires observing how their commands affect device and workpiece states. We introduce PLCWorld, a common closed-loop execution environment and benchmark that couples Structured Text (ST) execution with simulated plant responses and sensor feedback. Grounded in control relations identified in industrial PLC programs and engineering documentation, PLCWorld contains 100 synthetic tasks and 473 registered task-condition pairs across Motion Control and Material Handling, with difficulty defined by control-dependency scope. A common protocol reports Task Success and Safety Violation separately. Validation combines practitioner review, reference and alternative programs, targeted counterexamples, specification-evaluator alignment checks, and comparisons with independent ST runtimes. Reference and alternative programs satisfy their applicable cases, while all 542 targeted counterexamples activate their designated evaluator rules under at least one registered condition. Execution Gap relates submission-profile acceptance to subsequent task failure or observed Safety Violation. Across the constructed task groups, direct GPT-5.5 achieves 82.70% Task Success on Easy cases but 25.10% on Hard cases. Evaluations of six LLMs and four adapted generation-and-verification workflows further expose differences between completion, safety, and generation cost. Our code, simulation environment, benchmark tasks, and baseline implementations are publicly available at this https URL.

---


### 155. [Sentry: Learning to Recover from LLM Agent Failures at Test Time](https://arxiv.org/abs/2610.02994)

**<font color=#1a73e8>作者：</font>** Changxiu Ji, Amy Lu, Qizheng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents often fail mid-task due to invalid tool calls, repeated actions, or poorly grounded reasoning, and learning from these failures is a path to reliability. We find that how failure knowledge reaches the agent matters as much as what it contains. Failure lessons are conditional: kept in the agent's context, they misfire when their failure is absent, and removing them from an evolving playbook improves performance. Runtime interventions, in contrast, act only when a failure occurs but do not learn from their repairs. We argue that failure knowledge is conditional knowledge and should be conditionally exposed, and instantiate this principle in Sentry, a failure-management layer that runs alongside the agent. When Sentry detects a failure, it retrieves matching lessons from an external playbook to guide recovery, verifies without access to task rewards whether the agent recovered, and stores a new lesson only if it did; the full playbook never enters the agent's context. Across multiple agentic benchmarks, Sentry outperforms the strongest runtime-intervention baseline on every benchmark, by 37\% on average, and the strongest context-evolution baseline by 39\% on the two benchmarks where both are evaluated; combining Sentry with context evolution yields further gains. Learned lessons transfer to held-out tasks, and controlled experiments show that exposing the full playbook to the agent lowers performance even when relevant lessons remain available on demand.

---


### 156. [OmniConfess: Eliciting Token Confessions to Mitigate Omni-Modal Hallucination](https://arxiv.org/abs/2610.02999)

**<font color=#1a73e8>作者：</font>** Huiqiang Rong, Haoran Luo, Hui Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Omni-modal large language models (OmniLLMs) unify text, images, audio, and video, yet hallucinate when generation relies on the wrong evidence. Existing inference-time methods can reduce hallucinations, but rarely reveal which evidence sustains a generated commitment. We introduce OmniConfess, a training-free method for mitigating omni-modal hallucinations. It fixes a candidate response and re-scores it at token resolution under controlled channel-wise evidence interventions, producing a structured token-by-channel confession that reveals the response's evidential dependence. OmniConfess uses this confession to preserve grounded content and correct commitments driven by irrelevant or contradictory evidence. To evaluate OmniConfess, we construct OmniHalluBench, a 3,540-example benchmark built from six datasets spanning text, image, audio, and video settings and both judgment and free-form generation. Experiments show that OmniConfess mitigates hallucinations across heterogeneous modality and task settings. Our code and benchmark are publicly available at this https URL.

---


### 157. [AvoKV-E: Payload-Aware KV Cache Eviction for Long Reasoning](https://arxiv.org/abs/2610.03007)

**<font color=#1a73e8>作者：</font>** Han Yu, Wenhui Zhu, Xiwen Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-output reasoning shifts the KV-cache bottleneck from the fixed prompt to the generated trace. Existing reasoning-cache eviction methods largely treat cached entries as routing objects, estimating whether an old key will still be read, will recur, or can be replaced. This routing-only view overlooks two effects: low-attention entries can carry large value payloads whose removal changes future predictions, and newly generated states can appear stale before later queries have had a chance to read them. We introduce AvoKV-E, a training-free eviction policy that first delays eligibility for recent states and then ranks eligible entries using candidate-normalized read pressure, key redundancy, and value-payload potential. According to empirical evaluation across different models and datasets, AvoKV-E matches or exceeds redundancy-aware, recurrence-based, and thought-adaptive eviction baselines at matched active-KV budgets, with its largest gains in the tightest-cache regime. Component and counterfactual analyses further connect these gains to delayed observation, payload-aware scoring, redundancy, and scale-robust normalization. Together, the results show that long-reasoning KV eviction should preserve not only keys that are likely to be read, but also the value payloads that sustain the reasoning trajectory.

---


### 158. [Beyond Predefined Sinks: Security-Aware Dependency Analysis for LLM Agents](https://arxiv.org/abs/2610.03014)

**<font color=#1a73e8>作者：</font>** Hang Cui  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents increasingly connect model-generated decisions to security-sensitive software capabilities such as command execution, filesystem access, network communication, browser control, and external tools. Existing analyses often use predefined sensitive operations as anchors, but operation identity alone is insufficient to determine security implications.
We present AgentSecGraph, a security-aware static analysis framework that constructs a candidate-centered Security-Aware Agent Dependency Graph (Security-ADG) for each security-sensitive operation. It augments operation identity with agent relevance, source and dependency evidence, trust-boundary context, guard evidence, and external-effect semantics.
We further introduce AgentSecBench, a corpus of 67 real-world LLM-agent repositories spanning 11 ecosystems and 37,542 source files. The current analyzer identifies 23,866 static security-sensitive operation candidates across 65 repositories and emits one Security-ADG artifact per candidate. Corpus-wide analysis recovers source-to-operation dependency evidence for 9,821 candidates (41.15%) and potential guard evidence for 3,075 (12.88%), completing in 50.8 minutes.
Using a separate reproduction-backed evaluation layer, we establish 22 security-sensitive behaviors across 13 repositories: one confirmed vulnerability, one pending disclosure candidate, and 20 guarded behaviors. In nine held-out cases, Security-ADG preserves 91.1% of the reference context and all five observed guards, compared with 20.0% for a sink-only view and 40.0% for a simplified ADG. These results show that security-aware dependency and contextual evidence enable distinctions that cannot be recovered from sensitive-operation identity alone.

---


### 159. [DyadMem: A Long-Term Memory Benchmark of How Agents Work with Users](https://arxiv.org/abs/2610.03020)

**<font color=#1a73e8>作者：</font>** Yifei Tao, Xinyu Zhong, Henry Hengyuan Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term agents must remember not only what is true about a user, but also how a particular agent should work with that user as their shared history evolves. Existing benchmarks primarily supervise user facts and preferences or experience reusable across users, leaving this relationship-specific agent memory implicit. Additionally, most prior works measure the model solely with final-answer QA over long interaction histories, making the assessment still incomplete and unreliable. To this end, we introduce DyadMem with the proposed new definition User-conditioned Relational Agent Memory (URAM). DyadMem jointly annotates user-side memory and URAM along the same multi-session trajectories, resulting in 6 memory categories. To summarize, it includes 3,065 episodes, 50,961 sessions, and 61,210 QA instances, with extensive session-level Capture and Update gold annotations, query-level Recall support, and two QA settings: Gold-Memory and Full-Pipeline. Across 16 open-weight and 4 proprietary models, Gold-Memory QA is consistently strong, yet Full-Pipeline QA drops sharply. Such a gap explicitly supports our fine-grained evaluation design. Additionally, several quantitative results further reveal low Capture recall, incomplete Recall, and unsafe-deletion issues arising from even the frontier LLMs. We further conduct a rigorous experiment to validate the effectiveness of our URAM and observe the positive effects for all 20 models. In summary, DyadMem is a dual-domain, full-pipeline memory benchmark with extensive annotation efforts for advancing the domain's development.

---


### 160. [Tailoring the Quantization Space for 1-Bit KV Cache Compression](https://arxiv.org/abs/2610.03027)

**<font color=#1a73e8>作者：</font>** Minsoo Cheong, Donghyun Son, Sungjoo Yoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The key-value (KV) cache becomes a major memory bottleneck in long-context LLM inference, placing substantial pressure on memory capacity and bandwidth. To mitigate this bottleneck, vector quantization (VQ) has emerged as a promising approach for aggressive KV cache compression. However, existing VQ methods degrade substantially in the 1-bit regime. At such extreme compression, each codebook must represent a larger group of channels with a limited set of centroids, making effective use of its capacity increasingly challenging. To address this, we introduce $\textbf{TaSQ}$, which tailors the VQ target space by combining query-guided channel weighting, cross-head normalization, and covariance-aware channel grouping to better reflect the error sensitivity and statistical structure of cached activations. Since these transforms are RoPE-compatible and can be easily merged into projection weights and codebooks, TaSQ preserves the conventional VQ lookup structure and adds negligible serving overhead. Across general, long-chain-of-thought reasoning, and long-context retrieval benchmarks, TaSQ consistently outperforms existing low-bit KV cache VQ baselines while preserving reasoning stability. On a single RTX 6000 Ada GPU, its SGLang implementation supports up to $14\times$ larger batch sizes and achieves $1.87\times$ higher peak throughput compared to the BF16 baseline.

---


### 161. [SoftGene: Protein Language Model-Enhanced Soft Prompting for Interpretable Gene Set Annotation](https://arxiv.org/abs/2610.03029)

**<font color=#1a73e8>作者：</font>** Drew Ross, Arya Hadizadeh Moghaddam, Dongjie Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Gene set analysis is a cornerstone of functional genomics, yet it remains labor-intensive and heavily dependent on manual curation and expert biological interpretation. While Large Language Models (LLMs) have emerged as powerful tools for genomic reasoning and annotation, most existing approaches rely on symbolic gene names and fail to capture domain-specific biological structure, particularly protein sequence information that governs molecular activity, interactions, and downstream gene function. In this work, we propose SoftGene, a novel framework for LLM-based gene set annotation that leverages the hierarchical structure of gene sets. First, we use a hierarchical attention-based encoder built on ESM, a protein language model, to represent each gene set using protein-level amino acid sequence information. Second, we construct a hybrid prompting scheme that combines soft prompts derived from gene set embeddings with hard prompts containing auxiliary context generated by an LLM, and feed the resulting prompt into a local LLM for annotation. We evaluate our framework on two benchmark datasets: Gene Ontology (GO) and the Molecular Signatures Database (MSigDB). Our results show that integrating protein-sequence representations with textual context improves gene set annotation overall, while per-domain analyses reveal that the contribution of protein embeddings varies across biological domains.

---


### 162. [When Numbers Start Talking: Numerical Signalling and Strategic Behaviour Among LLMs](https://arxiv.org/abs/2610.03033)

**<font color=#1a73e8>作者：</font>** Alessio Buscemi, Daniele Proverbio, Alessandro Di Stefano 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents increasingly operate in multi-agent systems (MAS) characterised by strategic interaction. However, little is known about whether, and to what extent, different types of messages affect the outcomes of strategic games. By investigating AI agents based on four popular LLMs, playing four games with different cooperation equilibria, we study whether messages of different kinds (natural language, numerical signals, or random sequences) significantly modify the levels of cooperation in each game, also depending on the agents' assigned personalities. We observe that structured messages alter the final payoffs for most games and LLMs, but without a predictable pattern; this challenges the assumption that AI agents can converge to stable equilibria regardless of additional capabilities. Moreover, we observe that agent-generated numerical messages depart from randomness, most strongly and consistently when agents are explicitly instructed to communicate; however, they introduce an additional interpretability challenge, as their symbol distributions are mostly associated with the payoff structure and typically become more concentrated with repetition, but are overall difficult for humans to interpret. Monitoring for coordination of AI agents through restricted channels should thus prioritise message-level fingerprints, which generalise across models, over behavioural decisions, which do not.

---


### 163. [WebFovea: When the Model Is Right but the Click Is Wrong -- Reliable Round Trips for Vision-Based Web Agents on Live Websites](https://arxiv.org/abs/2610.03036)

**<font color=#1a73e8>作者：</font>** Jiangang Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present WebFovea, a vision-based web agent that placed 2nd in the WebRetriever Challenge 2026 with a final score of 57.0 out of 100. The challenge evaluates agents end to end on Protocol III of the WebRetriever benchmark (arXiv:2607.06118): starting from an entry URL on a live website, the agent must operate the site's own interface and return a verifiable answer. A capable multimodal large language model (LLM) is necessary for this, but not sufficient. The model's decisions reach the browser through the harness, the code between the model and the page. At every step, four things must go right: the model's reply must be parsed into the intended action, the action must take effect on the page, the result must be reported back accurately, and the model must be shown the information it needs. On real websites, many of the failures we observed occurred at one of these four stages rather than in the model's reasoning. A coordinate-space mismatch placed every click at 3/4 of its intended coordinates; actions on native dropdowns, inside iframes, and in text boxes failed silently; and self-generated chat-template tokens contaminated 4.9% of task episodes. WebFovea hardens each stage and surrounds the loop with guardrails that keep the agent within the rules and its budget. The four-stage view does not depend on the model, although some individual fixes do. Because we used the same model in all four submissions, the rise of our official hidden-set score from 31.0 to 57.0 reflects changes to the harness, up to run-to-run variance on live sites. We describe the design, the evidence for each component (including negative results), a failure analysis, the limitations, and a roadmap that includes routing different steps to different models.

---


### 164. [HyperThink: Text-to-Parameter Hypernetworks for Efficient Reasoning](https://arxiv.org/abs/2610.03039)

**<font color=#1a73e8>作者：</font>** Donggyun Kim, Jack Lu, Chanwoo Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-form thinking traces can substantially improve the multi-step reasoning performance of large language models (LLMs), but they introduce high inference-time overhead, with latency dominated by sequential decoding. We propose HyperThink, a text-to-parameter approach that amortizes this reasoning computation into a single query-conditioned parameter update: a lightweight hypernetwork reads the question and predicts updates to a small subset of the base LLM's parameters, while a vector-quantized decoder constrains them to a finite set of reusable patterns to improve robustness and transfer. Trained end-to-end on outputs from the base model itself, HyperThink eliminates long thinking traces at test time: after one hypernetwork forward pass, the adapted model generates a concise step-by-step solution and final answer without an intermediate trace, using far fewer tokens while retaining strong reasoning performance. Empirically, HyperThink improves the low-latency region of the accuracy-latency trade-off on mathematical and general reasoning tasks, with its strongest gains in the near-non-thinking regime.

---


### 165. [The Geometry of Knowledge Accessibility in Large Language Models](https://arxiv.org/abs/2610.03052)

**<font color=#1a73e8>作者：</font>** Lihu Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) contain broad knowledge, but they cannot access all of it reliably. We study this problem through knowledge accessibility, which describes whether the knowledge needed for a query can be recalled from the model. We find that knowledge accessibility has a simple geometric structure in the model's representation of the query alone, before any generation. More accessible queries are closer to a center in the representation space, while less accessible queries are farther away. This geometry reveals a knowledge boundary that separates more accessible queries from less accessible ones. Accessibility consistently decreases with distance from the center, and this distance-based ordering transfers across datasets even when the centers differ. Controlled experiments further show that the centered geometry is more closely related to knowledge accessibility than to reasoning difficulty. The geometry also reveals when different interventions are useful. Query rewriting helps more for accessible queries, chain-of-thought reasoning helps more near the boundary, and retrieval gives larger gains beyond the boundary. These findings not only provide a new geometric view of how knowledge is organized in language models, but also suggest a useful pre-generation signal for adaptive inference.

---


### 166. [hacktrace: behavior-supervised detection of reward hacking during code generation](https://arxiv.org/abs/2610.03055)

**<font color=#1a73e8>作者：</font>** Hao Jiang, Xin Li, Annan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A coding agent can earn a passing grade by fixing its code, or by deleting the test that exposes the bug. Detecting such reward hacking requires recognizing attempted shortcuts, including those that fail. We release 173,561 annotated multi-turn coding trajectories from Qwen3-8B and show that supervising shortcut behavior independently of exploit success substantially improves detection. We introduce HACKTRACE, a behavior-supervised monitor that reads the internal states the agent already computes while generating code. Reusing these states enables monitoring before a turn is complete, without additional language-model tokens or passes. Combining this evidence with static features of the final files achieves a mean per-problem AUC of 0.997 with 8 ms of monitoring overhead, improving both accuracy and latency over monitors that run the model again on an honesty question and answer. The same generation states also provide an inexpensive monitoring signal for reinforcement learning. With strong GRPO penalties, HACKTRACE reduces the cheating share of passing solutions from 82-91% to 1-5%, while retaining honest, correct solutions and maintaining high detection accuracy as the policy evolves. Our results show that both the supervision target and the source of monitoring evidence matter for turning accurate detection into a useful training signal.

---


### 167. [MOF-VERIFY: A Failure-Aware Agentic Harness for MOF Hypothesis Verification](https://arxiv.org/abs/2610.03056)

**<font color=#1a73e8>作者：</font>** Donghyun Lee, Taehoon Lee, Geonhee Ahn 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as reasoning components in AI-driven materials Co-Scientists, yet the reliability of the resulting verification pipeline remains unclear. Metal-organic frameworks (MOFs) provide a particularly challenging setting because structures may appear under different identifiers, synthesis outcomes depend strongly on experimental conditions, evidence is distributed across heterogeneous sources, and some hypotheses require computation rather than literature alone. We introduce a diagnostic benchmark with four task families covering structural grounding, synthesis-condition verification, evidence-sufficiency verification, and MLIP-based computational verification. T-MOF-1-3 are evaluated under closed-book, retrieval-enabled, and oracle-evidence settings to localize failures in knowledge access, evidence acquisition, and reasoning, while T-MOF-4 separately evaluates computational verification. Guided by these diagnosed failure modes, we develop MOF-Verify, a failure-aware agentic harness that targets structural, literature, evidence-sufficiency, and computational bottlenecks before producing a final verdict. Across multiple backbone LLMs, MOF-Verify substantially improves hypothesis-verification performance over direct inference and retrieval-based baselines. Benchmark datasets are released at this https URL.

---


### 168. [HARPO: Hallucination-Aware Reinforcement Learning for Faithful and Creative Language Generation](https://arxiv.org/abs/2610.03063)

**<font color=#1a73e8>作者：</font>** Tiezheng Yu, Yuxin Jiang, Jinpeng Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are prone to generating hallucinated content, which compromises their reliability in knowledge-intensive tasks. To address this challenge without sacrificing creativity, we propose HARPO, a reinforcement learning framework designed to jointly optimize faithfulness and creativity. HARPO incorporates a Hallucination-Aware Generative Reward Model (HA-GRM), trained via verifiable feedback, to assess both faithfulness and writing quality. A Selective Activation Mechanism (SAM) activates writing rewards only for outputs judged hallucination-free by HA-GRM, while a data curriculum progressively shifts training from creative writing to hallucination-centric tasks. On RAGTruth, our Qwen3-4B-based HA-GRM achieves a response-level F1 score of 78.08%, compared with 66.37% for the supervised fine-tuning baseline. Experiments on Qwen2.5 and Qwen3 models from 1.7B to 8B parameters show improvements in both faithful generation and writing quality. On Qwen3-4B, HARPO reduces the HA-GRM-judged hallucination rate on MultiHopRAG from 3.29% to 1.02%, while increasing the Arena-Hard-v2.0 creative-writing score from 16.95% to 27.54%.

---


### 169. [Unmasking Propaganda: A Comparative Analysis of Masked and Causal Language Models](https://arxiv.org/abs/2610.03077)

**<font color=#1a73e8>作者：</font>** Claudiu Creanga, Ioachim Lihor, Liviu P. Dinu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Propaganda detection is an essential task in natural language processing (NLP), particularly in the context of manipulative political communications. However, identifying specific propaganda techniques presents a significant challenge due to their often subtle nature and reliance on context, making them difficult to distinguish from legitimate persuasive language. Propaganda often involves highlighting certain facts while downplaying or ignoring others to create a desired perception. This biased communication aims to influence attitudes, beliefs, or behaviors towards a particular cause or position. This paper explores advances in detecting propaganda techniques through a comparative analysis of modern language models, using the SemEval-2020 Task 11 dataset. We evaluated both masked language models (based on XLM-RoBERTa or DeBERTa V3) and causal models (from OpenAI, Google, Mistral, Anthropic and Meta), employing two prompting strategies: base and chain-of-thought prompting. Our results demonstrate improvements over state-of-the-art models, with the best-performing MLM achieving an F1 score of 63.18 in technique classification and the best causal model achieving 63.62. We also observed that certain models excel in specific techniques, such as loaded language and name-calling, while struggling with others like bandwagon and black-and-white fallacy. These findings suggest that fine-tuning, ensemble modeling, and the use of larger datasets can further enhance propaganda detection capabilities.

---


### 170. [Securing Computer-Use Agents Against Branch Steering Attacks](https://arxiv.org/abs/2610.03089)

**<font color=#1a73e8>作者：</font>** Giulio Zingrillo, Hanna Foerster, Ilia Shumailov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern Computer Use Agents (CUAs) directly interact with graphical user interfaces and execute third-party web tools, exposing them to indirect prompt injection across every rendered page and tool response. While the Dual-LLM pattern is the primary system-level architecture offering formal security guarantees - using an isolated Planner LLM (P-LLM) to fix execution paths before processing untrusted inputs via a Quarantined LLM (Q-LLM) - these guarantees break down in graphical environments. Because CUA interaction is inherently dynamic, plans cannot remain data-independent; they must branch based on anticipated runtime web content - covering all possible cases the agent may encounter. This exposes agents to branch steering attacks, where an adversary crafts untrusted data to coerce a CUA down a hazardous, pre-approved branch without injecting explicit instructions. We systematically study branch steering attacks and introduce STEER-Bench (101 tasks across 9 domains), showing high attack success against both standard (94.4%) and vanilla Dual-LLM (89.5%) CUAs. We then propose COBRA, an architecture that pairs trusted branching plans with ahead-of-time capability constraints, strictly bounding the parameters and destinations each branch may execute. On STEER-Bench, COBRA reduces attack success to 0% while retaining 97% benign utility.

---


### 171. [LS-AR: Future-Predictive Latent Steering in Autoregressive LLMs](https://arxiv.org/abs/2610.03093)

**<font color=#1a73e8>作者：</font>** Anubha Gupta, Eduardo Pignatelli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard autoregressive (AR) models process high-level task instructions, state history, and transient tokens within a single shared sequence of tokens. Consequently, they lack the architectural mechanisms needed to isolate macro-objectives from context noise. To overcome this single-channel limitation, we introduce Latent-Steered Autoregressive (LS-AR), a dual-channel architecture that decouples continuous goal steering from discrete token decoding via FiLM conditioning. We evaluate a Static Goal Encoder (P_0) for persistent macro-objective retention across long rollouts and a Dynamic State Tracker (P_t) for recurrent latent updates during generation. On long-horizon retrieval past context limits (H=1024, W=500), LS-AR (Static) achieves 100% target recall where parameter-matched baselines collapse (0%), while increasing throughput by ~35% and cutting peak VRAM by 52.8%. In Blocksworld planning under forced perturbations (k=1), LS-AR (Dynamic) sustains an 89.0% completion rate vs. 71.0% for the baseline, though zero-shot entity scaling (N -> N+1) exposes single-vector capacity limits (0%). Finally, dual-channel authority analysis shows that text goal dropout establishes latent-dominant control, offering structural defence against text prompt injection while introducing a latent vector attack surface.

---


### 172. [Peer Influence across Heterogeneous AI Models](https://arxiv.org/abs/2610.03095)

**<font color=#1a73e8>作者：</font>** Frida Nøhr Laustsen, Marie Haahr Petersen, Victoria Popa 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When two AI agents disagree, who persuades whom? As multi-agent systems increasingly combine language models of different families and sizes, the answer can determine which judgments survive interaction. Measuring persuasion as the probabilistic shift in an agent's decision after a single exchange with a dissenting peer, we test seven open-weight models across three language understanding tasks. We find that persuasion is strong: when models disagree, receivers often abandon their initial judgment after seeing a peer's answer and explanation. Surprisingly, however, neither standalone certainty nor model scale reliably predicts persuasion dynamics. Models producing almost perfectly consistent decisions in isolation can be among the most susceptible to persuasion, and small models can match larger ones as persuaders and resist their influence just as effectively. Furthermore, we show that the size of the shift depends more on the susceptibility of the listener than on the persuasiveness of the speaker. Persuasion patterns are therefore specific to each model pairing, with heterogeneity amplifying persuasion in some combinations and suppressing it in others, allowing a dissenting agent running a small model to overturn the judgments of a much larger one. These findings show that the behavior of interacting models cannot be inferred from their individual properties but must be evaluated in the combinations in which they will operate.

---


### 173. [Predictor-Guided Latent Space Codon Optimization for Maximizing Protein Expression](https://arxiv.org/abs/2610.03098)

**<font color=#1a73e8>作者：</font>** Alberto Caron, Tianyu Cui, Dmytro S. Lituiev 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Codon optimization, the process of selecting synonymous codons to improve mRNA translation efficiency and protein expression, is central to therapeutic protein production and mRNA vaccines, yet it remains a hard problem. The design space is discrete and combinatorially large, precluding gradient-based methods, and existing tools rely on heuristic proxies (e.g., Codon Adaptation Index or GC-content) that poorly capture true expression. We introduce Latent-Space Codon Optimization (LSCO), which recasts this discrete problem as a continuous one by mapping sequences into the latent space of a pretrained mRNA language model, enabling efficient gradient-based search. LSCO combines four components: a data-driven expression objective from an uncertainty-aware predictor, a Minimum-Free-Energy regularizer for structural stability, a naturalness prior from a protein-to-codon back-translation model, and constrained decoding for protein fidelity. On a real-world, wet-lab antibody expression dataset, LSCO outperforms simple frequency-based, as well as modern deep generative baselines in predicted expression, while retaining suitable biophysical properties.

---


### 174. [Beyond Single Videos: Benchmarking and Active Evidence Seeking for E-Commerce Cross-Video Reasoning](https://arxiv.org/abs/2610.03099)

**<font color=#1a73e8>作者：</font>** Jinghan Zhao, Yiman Hu, Liang Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> E-commerce videos are information-dense and frequently compared by consumers evaluating products and merchants assessing marketing strategies. However, existing multimodal models mainly focus on single-video understanding and have limited ability to compare information across videos. We introduce AdsCVR, the first e-commerce cross-video reasoning benchmark, containing 2,483 videos and 6,110 question-answer pairs across six reasoning dimensions. Cross- video reasoning requires models to locate fine-grained evidence among many redundant frames and integrate visual details, speech, and on-screen text. We therefore propose AdSeek, an agentic framework that dynamically selects visual and audio tools during multi-turn exploration, replacing static uniform sampling with active evidence acquisition. To address the sparse credit assignment of reinforcement learning, we develop an offline trajectory rectification mechanism that identifies reasoning errors and missing multimodal evidence in RL-generated trajectories. The corrected trajectories provide supervised fine-tuning signals that reduce biases learned during RL. This mechanism supports a rectified bootstrapping pipeline in which initial RL exposes reasoning bottlenecks, supervised fine-tuning corrects them, and a final RL stage further improves the policy. AdSeek achieves 74.30 percent accuracy on the AdsCVR test split, outperforming its Qwen3-VL-8B-Instruct backbone by 27.90 percentage points. It also generalizes to the open- domain CrossVid benchmark, demonstrating effective active evidence gathering.

---


### 175. [Ask, Relax, or Act? Evaluating Actionable Indeterminacy in LLM Preference Reasoning](https://arxiv.org/abs/2610.03102)

**<font color=#1a73e8>作者：</font>** Ang Li, Yue Lin, Feifei Kou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An LLM agent can recognize uncertainty yet still choose the wrong next step: asking when action is already justified, or seeking clarification when the constraints must change. We formalize actionable indeterminacy: act when an accepted action is shared across all admissible preferences or objectives, clarify when each possibility is feasible but no action is shared, and propose a minimum-cost permitted constraint repair when the request is infeasible. We construct a solver-grounded benchmark spanning object allocation, meeting scheduling, apartment choice, and stable matching. Matched pairs retain the same source while changing whether intervention is necessary, and evaluation separates decision correctness, matched-pair reliability, and fully correct responses. Our findings reveal a recurring difficulty in recognizing when intervention is unnecessary: models can identify situations requiring clarification or repair yet still intervene when a justified action already exists. Correct decision labels also fail to guarantee usable actions, questions, or repairs. Crucially, response requirements shape not only how decisions are expressed but also which decisions are made. Making the required content explicit substantially improves fully correct responses and can change intervention decisions, even when outputs are already parseable. These findings highlight that reliable agency requires more than recognizing uncertainty: it requires intervening only when necessary and translating the chosen next step into a verifiable response.

---


### 176. [Emergent Structure in the Marginal Attention Space of Language Models](https://arxiv.org/abs/2610.03109)

**<font color=#1a73e8>作者：</font>** Valentino Maiorca, Walter Nelson, Francesco Locatello  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While representation similarity across independently trained language models is well-documented, how internal mechanics such as attention behave across models remains far less characterized. Inspired by this gap, we examine the structure of post-softmax attention weights by marginalizing over query positions, mapping them into a joint token-head "marginal attention space". Evaluating across 60+ diverse LLMs, we find that different properties emerge when reducing this space along its token and head axes. When reduced token-wise, marginal attention yields a text-intrinsic signal robustly conserved across models. To explain this property, we empirically connect marginal attention to the input-output Jacobian of the network, and prove theoretically that under a smoothness assumption, models with similar next-token distributions are guaranteed to have similar input-output Jacobian statistics. When reduced head-wise, it forms a model-private signature conserved across documents. Practically, this provides a natural way to estimate a per-head budget for key-value (KV) cache eviction, effectively decoupling model-specific budget allocation from text-intrinsic token scoring. On standard eviction benchmarks, a per-head budget precomputed offline on pretraining text, combined with a training-free token score, shows competitive performance with methods that recompute the budget on every document or train it per target. Code available at this https URL

---


### 177. [Ontological Instability and Statistical Amplification: The Paradox of "Humanizing" LLM-Generated Text](https://arxiv.org/abs/2610.03110)

**<font color=#1a73e8>作者：</font>** Claudiu Creanga, Liviu Dinu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Supervised AI-text detectors report high benchmark accuracy, but it is not clear what their decisions are based on. We analyze a RoBERTa-based detector under semantic, structural, and tokenizer-level perturbations, using the M4 dataset (N = 10,000) and controlled generations (N = 300). When Mistral-7B-Instruct was asked to make machine text sound more human, Verb Diversity rose from 0.77 to 0.92 and the outputs became easier to detect. Detection scores appear to track statistical complexity, which also leads to a 76.3% false-positive rate on formal human writing. As a control, we evaluate event-based Latent Space detection. Paraphrasing changed 87% of its event sequences (Jaccard = 0.067), and homoglyphs altered 70% of the extracted verbs even though extraction still ran (Jaccard = 0.30). Its best domain AUC was 0.577. RoBERTa's robustness seems specific to the features it uses, and structural abstraction did not make detection more robust.

---


### 178. [Building Interpretable Feature Representations for Resume-Vacancy Matching by Distilling Production LLM Signals](https://arxiv.org/abs/2610.03112)

**<font color=#1a73e8>作者：</font>** Ilya Chekin, Vyacheslav Malyugin, Vladimir Chirkov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Matching candidates to vacancies is central to recruitment, and a recruiter needs to see why a candidate fits, not only a single opaque relevance score. We provide this evidence as named, interpretable matching dimensions recruiters can act on - eight in our current deployment. We propose a two-part approach. The first is an LLM-based labeler whose prompts and feature definitions were refined from recruiter feedback while it served as an earlier production matching stage. In the current architecture, it is used only for offline labeling and is not called on online requests. The second is a feature bi-encoder distilled from it: a LoRA-adapted embedding backbone with compact per-dimension heads that runs on CPU and serves all online requests. Both parts keep improving: prompts are revised as feedback arrives, and the bi-encoder is retrained on the updated labels. The model is trained on 168,772 labeled vacancy-resume pairs (17,921 vacancies and 180,030 resumes). Recruiters using the service can confirm or revise surfaced feature predictions. On 927 recruiter-recorded values from this selected production-feedback subset, the deployed student agrees with the recorded decisions in 888 cases (95.79%). This is operational, non-blinded agreement rather than an independent human evaluation.

---


### 179. [Foresight: planning future perception in streaming VLMs without retraining](https://arxiv.org/abs/2610.03123)

**<font color=#1a73e8>作者：</font>** Ashok Prasad Neupane, Dipan Bartaula, Ankit Belbase 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing streaming vision-language models (VLMs) continuously perceive and reason over visual streams, but their computational pathways remain fixed throughout inference. Consequently, they cannot adapt computation to evolving scene dynamics, where different future events demand different levels and forms of perception. We show that streaming VLMs inherently possess the ability to anticipate the immediate future, and leverage this capability to dynamically configure future computation in a training-free manner. Realizing such anticipatory computation, however, is very challenging: future anticipation must be sufficiently reliable to guide computation, planning must run concurrently with streaming inference, and online reconfiguration must incur negligible overhead. To address these challenges, we introduce FORESIGHT, a dual-stream architecture comprising two Siamese LLMs with shared weights, input encoders, and KV cache. The first LLM continuously processes incoming tokens, while the second runs ahead of the stream to anticipate future context, plan future computation, and generate task responses without interrupting streaming inference. Each plan decides when to reason next, what to check then, and how densely to sample, keeping transient evidence separate from persistent control. The resulting computation plan is executed online through an efficient reconfiguration protocol with schemaguided decoding and lightweight diff-based updates, enabling dynamic adaptation with low overhead. With a frozen Qwen3-VL-8B backbone, FORESIGHT achieves 23.0 mean joint F1 on OmniPro Online evaluation beating strongest trained baseline by 9.5%, while improving the backbone by 6.7 on StreamingBench and 15.4 on OVO-Bench, with the largest gain of 18.7 when evidence arrives later in the video stream. Our source code will be made publicly available.

---


### 180. [The Fragility of Trigger-Tag Mechanisms for Misuse Detection in Open-Weight LLMs](https://arxiv.org/abs/2610.03124)

**<font color=#1a73e8>作者：</font>** Toluwani Aremu, Manit Baser, Mohan Gurusamy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-weight language models can be downloaded, modified, and deployed beyond their developers' control, limiting the effectiveness of centrally enforced safeguards. Recent work has therefore proposed \emph{trigger-tag} mechanisms that produce a detectable signal when a model is used under a target condition, such as generating phishing contents. Although these mechanisms borrow from established techniques, their use for conditional misuse detection in open-weight LLMs is relatively new. Therefore, existing research works have not systematically studied the robustness of trigger-tag mechanisms under adversarial attacks. To close this gap, (i)~we formalize trigger-tags and distinguish \emph{token-level trigger-tags}, which introduce watermark-inspired signals during decoding, from \emph{weight-level trigger-tags}, which learn backdoor-inspired associations between target conditions and detectable model behavior. Furthermore, (ii)~we introduce \Untag, a unified attack framework that organizes their mechanism-specific attack surfaces into a common taxonomy. We evaluate representative token-level and weight-level trigger-tags using phishing as a case study. We find that while trigger-tags may provide useful evidence in controlled settings, our attacks render the existing trigger-tag mechanisms to be entirely ineffective. Consequently, we argue that these mechanisms should not be treated as robust misuse detectors when attackers can transform outputs or modify open weights.

---


### 181. [Trading Strategy Optimization via Textual Gradient](https://arxiv.org/abs/2610.03128)

**<font color=#1a73e8>作者：</font>** Chaoqun Yang, Qian Wang, Fengbin Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantitative trading strategy design aims to discover trading programs from historical data that remain effective in future markets, which can be viewed as a black-box program optimization problem. LLM-based textual gradients offer a promising approach by providing explicit optimization directions for iterative strategy refinement. However, directly applying textual gradients faces two challenges: (1) optimization is myopic, underutilizing experience from previous evaluations; and (2) aggregate backtest feedback overlooks temporal robustness, potentially favoring strategies that perform well only in specific market periods. To address these challenges, we propose TradeGrad, an experience-guided textual-gradient framework for robust trading strategy optimization. TradeGrad leverages accumulated optimization experience to estimate textual gradients and employs multi-scale revisions for both strategy exploration and refinement. It further introduces the Cross-Period Robust Objective (CPRO), which emphasizes performance in unfavorable historical periods to promote temporal robustness. Experiments on cross-sectional and time-series strategy design in Chinese A-share and U.S. equity markets show that TradeGrad achieves the best in-sample and out-of-sample performance across all four settings. Notably, its Chinese cross-sectional strategy achieves 27.99% annualized return, 12.19% maximum drawdown, and a Sharpe ratio of 1.63, approximately 68% higher than the CSI 300 benchmark. Further analyses validate the proposed components and show consistent improvements in both in-sample and out-of-sample performance throughout optimization. The code is available at this https URL.

---


### 182. [Page-EntroKV: Hardware-Aligned, Entropy-Weighted KV-Cache Eviction under Grouped-Query Attention](https://arxiv.org/abs/2610.03135)

**<font color=#1a73e8>作者：</font>** Inbasekaran S  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Serving long-context autoregressive language models is constrained by the key-value (KV) cache. Most dynamic eviction methods score token importance per query head and choose tokens independently. This fits poorly with grouped-query attention (GQA), where several query heads share one physical KV buffer: divergent per-head selections force the serving engine to retain the union of their choices - inflating the cache by up to the group ratio r - while arithmetic mean pooling dilutes the specialized retrieval heads that carry factual recall. We introduce Page-EntroKV, a formal framework for KV-cache eviction operating at the granularity GQA serving actually allocates. Heads within each physical group are pooled by weights derived from sink-isolated collision (Renyi-2) entropy - one inner product per head, computed once at prefill with no calibration - so sink heads cannot masquerade as retrieval heads. Pooled scores are projected onto PagedAttention page frames, and eviction executes at the hardware tuple (layer, group, page). We formalize the union overhead ratio (UOR) and intra-group disagreement, prove an exact identity linking them for two-head groups alongside two-sided bounds at every group ratio, prove strict budget preservation and a finite-context needle-retention bound that arithmetic mean pooling provably violates, and give exact per-layer page accounting. On a pilot architecture (Qwen2.5-1.5B-Instruct, r=6), head-independent replay over 2,240 group measurements yields union overhead up to 4.75x at a 2% budget, while Page-EntroKV holds UOR exactly 1.000; sink isolation removes a 13x sink masquerade; needle recall is 100% versus 0% for mean pooling at a 20% budget; retained cardinality is exact for every page size; and QA and code tasks remain solvable at 20% retention.

---


### 183. [Investigating the Role of Reasoning-Language Alignment in Monolingual Retrieval-Augmented Generation](https://arxiv.org/abs/2610.03136)

**<font color=#1a73e8>作者：</font>** Oliver Hauck, Mario Sanz-Guerrero, Katharina von der Wense  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning traces improve large language models (LLMs), but current models are trained to reason mostly in English. It has been shown that forcing a model to reason in another language degrades accuracy, even when the reasoning language matches the language of the prompt -- but only for a setting where the model reasons over a short prompt. Here, we ask whether the same holds for retrieval-augmented generation (RAG), where the model must read and integrate a large amount of retrieved evidence in the target language. To study this, we build a fully monolingual German RAG question-answering testbed over the fictional world of the tabletop role-playing game The Dark Eye, a domain that is richly documented in German but too niche for the model to answer from memory, so that it has to rely on retrieval. Varying the forced reasoning language of an agentic RAG system on this testbed, we find that aligning the reasoning language with the language of the query and the retrieved documents helps. Forced German reasoning outperforms forced French, although the model benchmarks higher in French, so the benefit comes from alignment and not from language proficiency. The advantage grows when the retrieved context is richer and structure-aware. However, forced German only reaches the level of the model's native, unconstrained English reasoning without surpassing it, showing that native multilingual reasoning is needed. We publicly release the testbed and QA benchmark.

---


### 184. [Behavior Pack Optimization for Video MLLM Post-Training](https://arxiv.org/abs/2610.03141)

**<font color=#1a73e8>作者：</font>** Zhaolu Kang, Shiyu Liu, Tailong Luo 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video multimodal large language models (MLLMs) keep climbing video question answering benchmarks, yet shuffling the frames, masking the segment that supports the answer, or occluding the target object barely changes their predictions. The accuracy rests on appearance and language priors, not on the temporal evidence the question asks for. We trace this to the unit of post-training: rewards are computed on a single response to the original clip, so the model is never asked to behave consistently across views. We propose Behavior Pack Optimization (BPO), which replaces the single response with a behavior pack of outputs across counterfactual views chosen by question type, scored jointly. The pack reward asks for stability when the intervention is irrelevant, sensitivity when key evidence is removed, and abstention when no evidence remains. To keep this objective stable at small pack sizes, BPO uses an anchor-relative advantage: the response on the original view serves as a per-prompt reference instead of a group mean over mixed views. On TempCompass, MVBench, and NExT-QA, BPO improves the macro accuracy of Qwen2.5-VL-7B-Instruct by 4.7 pp, the temporal-hard subset by 7.8 pp, and abstention F1 by 20.0 pp over a budget-matched vanilla GRPO baseline from the same SFT checkpoint. The gains transfer to Video-MME, LongVideoBench, and to LLaVA-Video-7B; ablations confirm they follow the view sets, not the rollout count. We hope this pack-level perspective offers a useful starting point for the video MLLM and multimodal post-training community as the field moves toward evidence-grounded video reasoning.

---


### 185. [EvoRiskBench: An Evolving Benchmark for Runtime Security Risks in Workspace Agents](https://arxiv.org/abs/2610.03153)

**<font color=#1a73e8>作者：</font>** Shiyi Kuang, Xuemei Luo, Kun Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Workspace agents combine large language models with execution harnesses to perform stateful, multi-step tasks that access or modify external resources. Existing benchmarks leave gaps in executable coverage of their runtime security risks, while evolving model capabilities, harnesses, tools, and threats motivate benchmark evolution. We introduce EvoRiskBench, an evolving benchmark organized around the EP-Path-EF framework, which links an initial risk entry point to a one-hop technical effect through an agent-mediated risk path. The framework defines nine entry-point categories and five effect categories; a 20-participant study supports their interpretability and classification consistency on representative cases. Guided by this framework, an automated end-to-end workflow constructs and executes risk cases in isolated environments and independently verifies outcomes using runtime traces and environment states. The benchmark provides a reproducible dataset of 450 adversarial tasks across six scenarios. We evaluate nine model-harness configurations spanning three models (GPT-5.6 Sol, DeepSeek-V4-Pro-0813, and Claude Opus 5) and three harnesses (Claude Code, Codex, and OpenClaw). Our results reveal substantial vulnerabilities across systems. The most vulnerable configuration, Codex with DeepSeek-V4-Pro-0813, reaches a 68.44% attack success rate (ASR), indicating that configuration of workspace agent is insufficient to ensure secure autonomous execution. ASR varies more across models than harnesses, and harness differences depend on the model. The benchmark cases and evaluation platform will be released after completion of artifact safety and reproducibility checks.

---


### 186. [Predicting Steering Vectors and Adapter Weights for Few-Shot Author-Style Transfer](https://arxiv.org/abs/2610.03163)

**<font color=#1a73e8>作者：</font>** Leonard Popp, Danni Liu, Supriti Sinhamahapatra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adapting large language models to an individual author's style from a few examples is challenging, and scientific writing sharpens the difficulty: formal conventions leave little surface variation, and authors write about their own topics, so extracted ``style'' easily entangles with content. We study style-conditioned abstract generation from a few example abstracts per author and propose three methods: (1) contrastive activation steering, (2) a network that predicts steering vectors, and (3) a hypernetwork that predicts LoRA adapters. We find a consistent trade-off between style imitation and output quality: fine-tuning buys most of the available style signal but forfeits fluency, while the hypernetwork achieves the best trade-off on both seen and unseen authors. Our steering operates at author level, contrasting an author's abstracts against style-neutral generations for the same content. This holds topic fixed, removes the need for a predefined style inventory, and outperforms inventory-based steering. % [EDIT 1a] softened "no single optimal axis" claim Moreover, our analyses demonstrate that manually extracted and predicted steering vectors are near-orthogonal yet score comparably, indicating that style conditioning here can admit at least two unrelated directions rather than requiring one particular axis.

---


### 187. [Gains and Collapse in On-Policy Distillation:A Reinforcement Learning Perspective](https://arxiv.org/abs/2610.03185)

**<font color=#1a73e8>作者：</font>** Han Cui, Jianhao Yan, Yun Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has become an important approach to language model post-training. However, despite its performance gains, OPD can also collapse into excessively long and repetitive generation, and the mechanism underlying these divergent outcomes remains poorly understood. We explain these outcomes through a reinforcement learning perspective: the teacher implicitly rewards student behaviors, even those it rarely exhibits itself. From this perspective, our experiments show that OPD improves performance without expanding the student's capabilities. When the implicit reward model is reliable, OPD makes correct responses easier to sample. In contrast, when the preference misaligns with quality, reward hacking happens: the implicit reward model amplifies overlong, repetitive student rollouts, even though it rarely generates such text itself. Guided by this diagnosis, we find that masking unhealthy responses during training and using SFT initialization can each effectively mitigate the collapse. Together, these findings show that OPD amplifies student behaviors favored by the teacher's implicit feedback, shifting the focus from how well the teacher generates to how reliably it evaluates student rollouts. Our code is available at this https URL.

---


### 188. [Not Until the Evidence Says So: Teaching LLM Investigators When to Close a Case](https://arxiv.org/abs/2610.03190)

**<font color=#1a73e8>作者：</font>** Tingzhu Bi, Ping Wang, Meng Ma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accident, defect and outage investigations end with a decision that ordinary question answering never faces: whether the evidence gathered so far is enough to close the case. We study this decision for LLM investigators, which request evidence from a case file, revise their hypotheses, and either close the case with a conclusion grounded in what they read or leave it open and name what is missing. This judgment does not come with capability: an untrained 9B model overstates its evidence in 97% of its answers, and a frontier model that identifies the right cause in 84% of cases still overstates in 91% and closes 17 of the 41 cases whose official finding is "cause undetermined". Measuring it is also non-trivial: the source of a case largely predicts its label, and a rule that reads only the source reaches 83.0 balanced accuracy on our test cases. We therefore evaluate closure with three tests: closure accuracy, reported against this rule and within each source; evidence dependence, which removes the grounds of a conclusion and checks whether the model stops closing; and conclusion and gap quality, a judged checklist of what the model asserts and what it says is missing. We build Nautil, 731 audited cases from aviation, rail, maritime, chemical-safety and vehicle-defect reports and production server incidents, with teacher trajectories, an out-of-distribution test set and counterfactual evidence versions. Fine-tuning a 9B model on these trajectories makes its closures follow the evidence: removing the grounds lowers its closure rate by 26 points relative to a matched control, overstatement falls from 97% to 35%, and correct, non-overstated conclusions rise from 3% to 43%. Reinforcement learning that rewards only the closure decision then raises balanced accuracy from 69.2 to 83.3, on par with the teacher, and within-source accuracy from 60.4 to 74.1, at some cost in evidence dependence.

---


### 189. [Bridging Research and Practice: A Systematic Evaluation of Generalist and Dermatology-Specific Models in Clinical Skin Lesion Classification](https://arxiv.org/abs/2610.03193)

**<font color=#1a73e8>作者：</font>** Emanoel dos Santos, Kelvin Cunha, Rodrigo Mota 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The application of machine learning to dermatology has grown substantially in recent years, moving beyond proof-of-concept studies toward potential applications. However, clinical dermatology remains a challenging and still open problem. Diagnostic assessment is often ambiguous, and skin lesions exhibit high variability, compounded by differences in acquisition modality, device quality, and patient demographics. These factors hinder the development of robust models suitable for safe and equitable clinical use. To support translation into practice, it is essential to systematically evaluate how contemporary models generalize across heterogeneous data sources. In this work, we benchmark a diverse set of architectures on recent dermatology datasets, spanning dermoscopic images and smartphone-based clinical photographs. We assess the robustness of recent general-purpose and medical vision-language models, as well as foundation models, and compare them against task-specific dermatology classifiers, including embedding-based approaches and convolutional neural networks. Our study provides an evaluation of model performance under distribution shifts, modality changes, and demographic variability. By quantifying the gap between current state-of-the-art models and the requirements of clinical deployment, we aim to contribute to the development of reliable, accessible, and clinically applicable AI systems for dermatology.

---


### 190. [Source Preference in the Wild: How LLM Agents Favor Items by Source, and How to Reduce It](https://arxiv.org/abs/2610.03195)

**<font color=#1a73e8>作者：</font>** Jonghyun Song, Haewon Park, Jeonghoon Shim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLM agents decide on users' behalf which product to buy, which hotel to book, or which paper to cite, a preference for items from certain sources (the sites or services they come from) shapes what users receive and which sources are selected. We study source preference in end-to-end search with 12 agent models across three domains. Comparing items from different sources that satisfy the same requirements at the same position, we find that each model prefers some sources and avoids others in every domain, largely agreeing on which. This preference can outweigh how well items satisfy the request: an item satisfying one requirement fewer is selected about two-thirds of the time when it comes from a preferred source and the better one from a dispreferred source, but almost never in the reverse case. The information identifying an item's source affects selection by itself: hiding it weakens the preference, and relabeling an item with a preferred source raises its selection rate. We test two routes to this preference: training that rewards better items can make a source a shortcut for requirement satisfaction, and missing information can trigger preconceptions about the source. Supplying missing information or a prompt countering these preconceptions reduces source preference.

---


### 191. [KV$^2$: A Self-Refining KV Cache](https://arxiv.org/abs/2610.03198)

**<font color=#1a73e8>作者：</font>** Johannes Wesch, Danni Liu, Jan Niehues  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The memory footprint of the key-value (KV) cache constrains the practical use of long-context models, and it dominates cost when one prefilled context must later serve many different queries. In this reusable setting, query-agnostic compression trades cost against quality: lightweight estimators are cheap but less accurate, whereas full-context reconstruction scoring is more accurate yet reprocesses the entire prompt. We introduce KV$^2$, a query-agnostic KV-cache compression method based on selective reconstruction. KV$^2$ first uses a lightweight proxy scorer to identify informative in-context tokens, then reprocesses only this subset to compute final eviction scores. On RULER, Needle-in-a-Haystack, and LongBench, KV$^2$'s margin over baselines widens as the budget tightens: on RULER 16K at a 2% KV-cache budget it improves the average score over the next-best baseline by more than 40 percentage points, and on LongBench it attains the highest average across 2%-10% budgets at lower compression-stage runtime and peak memory than full-context reconstruction. Reusable KV-cache compression thus does not require reprocessing the full context. Our code is available at this https URL.

---


### 192. [Predicting and Repairing Merge Collapse in Large Language Models](https://arxiv.org/abs/2610.03199)

**<font color=#1a73e8>作者：</font>** Jungseob Lee, Seungyoon Lee, Sugyeong Eo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models fine-tuned from a shared base can be merged by averaging their task vectors, but some merges collapse far below the base model, and common merge operators give no warning before evaluation. We show that one statistic of the specialists' task vectors both predicts this collapse and calibrates its repair. The power that averaging removes equals the variance of the task vectors across specialists, our measure of interference. Under a working noise model, the disturbance that a merge injects grows with the merge coefficient and with interference, yielding a pre-merge score. In our experiments on twenty-two merge configurations from four model families, only destructive merges exceed a threshold on this score. We find that statistics of sign conflict between specialists, a common target of existing merge operators, are anti-predictive. We then predicted the outcomes of fourteen merges before evaluating them, and twelve predictions were correct, including the destructive outcome of a specialist pair pushed past the threshold by continued pretraining. To address this collapse, we introduce PRISM, an operator that averages the task vectors first and then soft-thresholds each layer at a level set by the layer's interference. Without data or tuning, PRISM keeps all five destructive merges above the threshold within evaluation noise of the base model, where plain averaging falls at least 14.4 points below it or collapses entirely. We apply PRISM only above the threshold and keep the plain average for merges below it, which include all fifteen harmless ones. Code is available at this https URL.

---


### 193. [Toward SLM-based agentic task-tool intent matching](https://arxiv.org/abs/2610.03213)

**<font color=#1a73e8>作者：</font>** Chiara Troiani, Arash Salarian, Majed El Helou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-equipped AI agents use tool calls to access data and act on external systems. Horizontal growth of agentic systems increases the number of these interactions, and further motivates the need for automated, per-call oversight that can operate at low latency and/or on-prem. Conventional authorization schemes can determine whether an agent is allowed to invoke a tool, but cannot assess the agent's underlying cognition, specifically, whether the tool selection represents a logical, relevant step toward satisfying the intent of the task or not. Consequently, an allowed call may still deviate from the task's intent: a rogue agent might deviate the calls or nudge other agents to make a combination of calls that would not align with the intent of the task. Therefore, every call needs to be verified. In this study we investigate the applicability of Small Language Models (SLMs) to this purpose: an SLM functions as a task-tool relevance classifier that evaluates every selected tool independently against the assigned task and returns a relevance signal for downstream enforcement. Equipped with a novel dataset with multi-tool tasks whose required tools span distinct Model Context Protocol (MCP) servers, we used prompt-optimization, supervised fine-tuning, and reinforcement learning through GRPO to optimize and specialize SLMs.

---


### 194. [StanceEval 2026: The Second Stance Detection Shared Task](https://arxiv.org/abs/2610.03215)

**<font color=#1a73e8>作者：</font>** Rasha Albalawi, Nuha Albadi, Hamzah Luqman 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> StanceEval 2026 is the second edition of the StanceEval shared task series on stance detection in Arabic social media text. Stance detection aims to identify a writer's stance toward a given topic. Given a tweet and a target, participating systems must determine whether the writer's stance is Favor, Against, or None. This edition focuses on cross-target generalization across two distinct evaluation tracks: Track 1 evaluates thematically related cross-target transfer (testing on Women Driving, related to Women Empowerment from training data), while Track 2 evaluates cross-domain transfer to completely unseen targets (E-Cars and Trimester System). The shared task attracted 80 registered teams from 12 countries. During the evaluation phase, 30 unique teams submitted entries, with 21 teams officially ranked in Track 1 and 13 in Track 2 following validation filtering, and 20 teams submitting system-description papers. Participating teams employed diverse methodologies, including fine-tuned pretrained language models, prompt-based and retrieval-augmented large language models (LLMs), fine-tuned LLMs, and hybrid cascades. Top systems achieved impressive $F_{avg2}$ scores of 0.8994 on Track 1 and 0.9400 on Track 2, substantially outperforming the strongest baselines (0.7366 and 0.7475, respectively), where $F_{avg2}$ denotes the macro-averaged F1 score over the Favor and Against classes. Counterintuitively, performance on the unseen targets was higher than on the related target, a disparity could be driven by extreme target polarization, class imbalance, and dialectal or sarcastic nuance across topics.

---


### 195. [AdaStep: Adaptive Step Credit Weighting for Agentic Reinforcement Learning](https://arxiv.org/abs/2610.03223)

**<font color=#1a73e8>作者：</font>** Xin Wang, Wenhao Wu, Menghao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents are typically trained with sparse outcome rewards, making trajectory-level objectives too coarse to distinguish the contribution of individual decisions. Step-level credit assignment provides finer-grained supervision, but its estimates can be unreliable because observed returns also depend on subsequent actions, environment transitions, and trajectory length. We propose AdaStep, an Adaptive Step-credit weighting method that controls how strongly each group-derived local advantage modifies the trajectory-level signal. We formulate this weighting as a mean-squared-error estimation problem for the latent step advantage and, under an explicit conditional sampling assumption, derive an optimal per-state shrinkage coefficient. The coefficient admits a signal-to-total-variance interpretation: it preserves local credit when return variation is attributable to the selected action and suppresses it when variation is dominated by downstream randomness. AdaStep requires only lightweight scalar computation, with no critic, additional rollouts, or extra model inference. Experiments with three model backbones on ALFWorld, WebShop, and ScienceWorld show consistent improvements over baselines at low computational cost.

---


### 196. [D2K-Bench: Can LLM Agents Turn Expert Designs into Efficient GPU Kernels?](https://arxiv.org/abs/2610.03226)

**<font color=#1a73e8>作者：</font>** Daifeng Li, Huiqiang Jiang, Chengruidong Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> GPU kernels generated by large language model (LLM) agents can remain less efficient than expert implementations, but runtime alone does not reveal how the gap relates to design discovery and implementation. We introduce D2K-Bench, a diagnostic benchmark of 26 tasks and 85 workloads that measures how effectively agents translate expert design guidance into efficient GPU kernels. The guidance covers L1: high-level algorithmic insights, L2: dataflow design, and L3: low-level optimization tricks, including dependencies among these levels. Pairwise runs with and without guidance share task descriptions, workloads, tools, hardware, and a 350-turn budget. Complementary assessments examine independently proposed designs and the design properties implemented in generated code. Across five models on NVIDIA B200 GPUs, guidance raises correctness over 130 model-task pairs from 93.1% to 98.5% and increases the Performance Score over all 26 tasks from 1.46 to 1.95. For the three frontier models with correct submissions on all 26 tasks in both runs (GPT-6-Astra, Claude-Opus-4.8, and GPT-5.6-Sol), geometric mean speedup increases from $1.69\times$ to $2.49\times$. Across all five models, the mean combined implementation score increases from 57 to 70 out of 100. These results show the value of expert design guidance while identifying design properties that remain unimplemented.

---


### 197. [Collective Bias Mitigation via Model Routing and Collaboration](https://arxiv.org/abs/2610.03240)

**<font color=#1a73e8>作者：</font>** Mingzhe Du, Luu Anh Tuan, Xiaobao Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in public health, finance, and governance, requiring both accuracy and societal value alignment. Despite recent advances, LLMs often perpetuate or amplify bias embedded in their training data, posing challenges to fairness. While self-debiasing encourages an LLM to identify and correct its own biases, relying on a single model's intrinsic knowledge may be insufficient to address deeply ingrained stereotypes. To address this limitation, we introduce Collective Bias Mitigation (CBM), a framework that alleviates bias by learning fine-grained model behavior and fostering knowledge sharing among diverse LLMs. This work is the first to systematically explore the effective selection and organization of distinct LLMs to cultivate fairer LLM responses. Experiments show CBM substantially outperforms standalone baselines (e.g., in the top-7 setting, Committee lowers the age bias score from 0.25 to 0.10). Our Debating and Committee topologies achieve substantial bias reduction, with the latter balancing mitigation effectiveness and inference cost, highlighting the potential of CBM for fairer LLMs.

---


### 198. [COSMI: COmpositional Synthesis of Multi-object Interactions](https://arxiv.org/abs/2610.03252)

**<font color=#1a73e8>作者：</font>** Daniel Eskandar, Ilya A. Petrov, Gerard Pons-Moll  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models of human-object interaction are bounded by the data that exists: everyday activities involve several objects, but most captured datasets record one at a time, as multi-object capture is combinatorially expensive. Our observation is that interactions are local, so single-object captures already contain the parts of multi-object activities. We compose them: contact-consistent clips of single interactions, mirrored to balance the hands, transfer between bodies, and a language model and geometric checks admit only the pairings that are plausible, semantically and physically. Therefore, the dataset grows combinatorially with the clips rather than recording time. The COSMI dataset holds 222k sequences and 275 hours with up to five objects, nearly thirty times the largest multi-object capture, and can be extended by adding datasets or even hand-object recordings. On this data we train the COSMI method, a text-to-interaction diffusion transformer that follows how the data is built: weight-shared object slots generate a variable number of objects, predicted relative to the body parts that move them. On a benchmark with an unseen object and unseen interaction combinations, models trained on the dataset generalize to the unseen combinations. COSMI outperforms baselines in text alignment and contact accuracy, where its margin is largest on the unseen object. Code, models, and the dataset pipeline will be released on the project page: this https URL.

---


### 199. [SPEAR: A Spectral-Disentangled MoE Neural Operator with Knowledge-Guided Expert Aggregation for Large-Scale PDE Pretraining](https://arxiv.org/abs/2610.03265)

**<font color=#1a73e8>作者：</font>** Dengdi Sun, Xiaoya Zhou, Xiao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale pre-training has improved the generalization of neural operators across diverse PDEs. However, existing PDE foundation models still struggle with heterogeneous dynamics, where shared representations may cause knowledge interference, while mixture-of-experts (MoE) architectures suffer from increasing expert redundancy. We propose SPEAR, a spectral-disentangled MoE neural operator with knowledge-guided expert aggregation for large-scale PDE pre-training. SPEAR decouples latent features into low- and high-frequency components, enabling shared modeling of transferable dynamics and specialized learning of PDE-specific patterns. To address expert redundancy, we design a knowledge-guided expert aggregation strategy that measures expert similarity from dataset-specific learned knowledge and routing preferences, enabling the identification and consolidation of similar experts. Experiments on twelve PDE datasets and multiple downstream benchmarks demonstrate superior performance in pre-training, fine-tuning, and transfer learning. Furthermore, our aggregation strategy reduces the number of experts by 50\% while maintaining or improving prediction accuracy, achieving a balance between model efficiency and generalization for PDE foundation models.

---


### 200. [Shrome at Touché: Soft-Vote Ensembling and Counter-Causal Augmentation for Causality Extraction](https://arxiv.org/abs/2610.03268)

**<font color=#1a73e8>作者：</font>** Roham Zendehdel Nobari, Shayan Sooratgar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Touché 2026 extends causality extraction to counter-causal claims: news sentences whose surface form appears causal but whose meaning denies the causation, as in "It is falsely believed that X caused Y." A system that relies on surface cues such as "caused" or "led to" will accept such a sentence as causal and give it the wrong polarity. On the Countercausal News Corpus (CCNC), the task has three subtasks: deciding whether a sentence is causal (detection), locating its cause and effect spans (extraction), and labeling its polarity as procausal, counter-causal, or uncausal. We build one model per subtask. Detection is a fine-tuned classifier with a single cross-task rule that uses the extracted spans to remove false positives. For extraction, we ensemble three RoBERTa-large BILOU+CRF taggers by averaging their token-level scores before decoding, rather than voting on the spans each tagger produces. For polarity, where labeled counter-causal examples are scarcest, we add training sentences generated by a large language model prompted with nine patterns of counter-causal expression adapted from Hagen et al., keeping only those that pass automatic structural checks. On the held-out CCNC test set, the system reaches F1 0.869 on detection and macro-F1 0.817 on polarity, and in the organizers' final causal-only evaluation of extraction it scores granularity-adjusted F1 0.728, the highest extraction score among all submissions including the organizers' baseline. The development split is used only for component selection and the ablations reported in the paper.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-261](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
