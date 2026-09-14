# 🧠 大模型相关研究 | 2026年09月14日

> 本类共 **153** 篇论文：已确认 **145** 篇，待复核 **8** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-153](./part-04.md)

---

### 1. [M3-Former: Multimodal Transformer with Mixture-of-Experts for Long-Term Vessel Trajectory Prediction](https://arxiv.org/abs/2609.10559)

**<font color=#1a73e8>作者：</font>** Wenzhe Jin, Haina Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To address the challenges of behavioral multimodality, limited semantic utilization, and long-term error accumulation in vessel trajectory prediction, this paper proposes M3-Former, a multimodal trajectory prediction framework enhanced by large language models (LLMs). The proposed framework incorporates vessel static attributes and navigational intent as semantic priors for long-term trajectory modeling. Specifically, a unified multimodal representation space is constructed, in which static semantic information is encoded by a pre-trained LLM and aligned with dynamic trajectory features through self-attention. To jointly capture global route planning and local motion variations, a dual-granularity Mixture-of-Experts (MoE) architecture is introduced, where sequence-level experts model global navigation trends and token-level experts refine fine-grained maneuvering behaviors. In addition, a Steering-Weighted Cross-Entropy loss is designed to alleviate the long-tail distribution of sparse turning samples and improve prediction accuracy in critical maneuvering scenarios. Experiments on a real-world Danish AIS dataset demonstrate that M\textsuperscript{3}-Former consistently outperforms state-of-the-art baselines across prediction horizons from 1 to 4 hours. In the 4-hour prediction task, the proposed method reduces Average Displacement Error (ADE) and Final Displacement Error (FDE) by 4.4\% and 5.1\%, respectively, compared with the strongest baseline. Qualitative and ablation analyses further verify that semantic fusion effectively reduces long-term trajectory drift, while the dual-granularity MoE improves robustness in complex waterways and route-branching scenarios. The proposed framework establishes a semantic-guided hierarchical prediction paradigm, in which high-level navigational intent and local motion dynamics are jointly modeled for robust long-term vessel trajectory forecasting.

---


### 2. [An Empirical Measurement of Jailbreaking Evaluators](https://arxiv.org/abs/2609.10594)

**<font color=#1a73e8>作者：</font>** Yujie Mu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Expert evaluation of jailbreak responses is costly and difficult to scale, so the community increasingly relies on automated evaluators to determine whether an attack succeeds. However, jailbreak studies typically validate their chosen evaluator independently, repeatedly spending resources on similar evaluation efforts while making results across papers difficult to compare. Different evaluators also encode different definitions of jailbreak success, meaning that reported attack strength and apparent progress can depend substantially on which evaluator is used. We systematically compare six evaluators that recur in recent jailbreak attack and defense research: HarmBench, JailbreakBench, JailbreakRadar, StrongReject, JADES, and JailMeter. To our knowledge, no prior study has evaluated all six on the same human-labeled data under a controlled setup. We evaluate them on JailbreakQR and JailMeter-Eva, using human judgments as the reference, and measure agreement with humans, error types, and consistency across attack families. For evaluators that require a general-purpose LLM judge, we use a shared backbone to control for model-specific variation. We found that JADES exhibits the best overall performance, while HarmBench and StrongReject also demonstrate good performance.

---


### 3. [Threshold Choice, Not Sample Size, Bounds Trustless Verification of Nondeterministic Compound AI Workflows](https://arxiv.org/abs/2609.10601)

**<font color=#1a73e8>作者：</font>** Alper Alimoglu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Compound AI pipelines chain LLM calls, retrievers, and tools and are nondeterministic: sampling, model updates, and volatile tool responses make one input yield different outputs across runs. Such pipelines increasingly run across edge, cloud, and orbital nodes owned by no single party, whose optimizations discard intermediate results before inspection. Verifying reproduction there means tolerating nondeterministic outputs, a node that may not report honestly, and intermittent access to any shared record; existing work addresses at most two at once. We give a protocol covering all three: it commits digests of each stage's inputs, outputs, and context under a policy digest pinning the metric and threshold, anchors them without trusting the executing node, defers under partition, and decides a challenge on the median of $k$ re-executions, with no quorum. Where that procedure breaks is the main result. On a synthetic HotpotQA pipeline a calibrated fixed threshold accepts 44 of 45 honest reproductions and rejects 104 of 105 divergent pairs, yet lets same-input fabrication through in 27 of 29 trials at k=5, more samples being no help since sampling sharpens an estimate without moving it. Holding that metric and this pipeline's re-execution spread fixed, the binding constraint is the threshold rather than the sample size: one derived per execution detects 19 of 29 where the best constant matched to the same zero honest rejections reaches 9, rejects no honest commitment at k=5 though 3 of 15 at k=3, and catches 11 of 15 of an attacker built against it, which has to aim at a target drawn only after its commitment exists. That rule is measured rather than deployed.

---


### 4. [GEOSTEER: Geodesic Optimization for Activation Steering in Large Language Models](https://arxiv.org/abs/2609.10658)

**<font color=#1a73e8>作者：</font>** Xuan Cuong Ngo, Hao Vo, Ngan Le  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering provides a lightweight way to control large language models (LLMs) by modifying their hidden activations at inference time. Among these approaches, norm-preserving steering aims to change model behavior without altering the activation norm, reducing the risk of representation collapse and degradation. However, existing norm-preserving methods are limited by predefined steering trajectories and by their reliance on one-step updates, which may fail to capture the complex structure of activation distributions. We propose GeoSteer, an optimization-based method for norm-preserving activation steering. GeoSteer formulates steering as a Riemannian optimization problem and updates activations through a sequence of small geodesic steps on the representation manifold. To avoid fixed steering directions, GeoSteer learns a nonlinear activation-space objective that distinguishes desired from undesired activations, and uses this function to adaptively guide each steering step. This multistep formulation yields smoother, more stable, and more consistent steering behavior while preserving the activation norm. Across TruthfulQA, RealToxicityPrompts, and UltraFeedback benchmarks, GeoSteer consistently improves over state-of-the-art activation steering baselines. These results suggest that norm-preserving steering can be made more effective by replacing predefined one-step edits with adaptive, geometry-aware optimization.

---


### 5. [An Open Recipe for IMO Gold: Training Nemotron for Olympiad Mathematics](https://arxiv.org/abs/2609.10712)

**<font color=#1a73e8>作者：</font>** Ivan Moshkov, Stephen Ge, George Armstrong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study how model post-training and test-time inference design affect natural-language proof generation for hard olympiad mathematics. Starting from Nemotron 3 Ultra, we train two specialist checkpoints using supervised fine-tuning and reinforcement learning, and evaluate checkpoint choice, verification, and refinement. Based on these findings, we present an open-model test-time-compute pipeline. The system operates entirely in natural language, with no formal prover, external tools, or internet access. Three Nemotron 3 Ultra checkpoints - the general-availability model and two post-trained specialists - power an iterative search that generates, verifies, and refines candidate proofs; a separate high-compute stage then selects each final submission. The system scored 30 out of 42 points at IMO 2026, reaching the gold-medal threshold. We release the two post-trained checkpoints as well as the training data, the training and inference code, the submitted solutions, and Nemotron-IMO-Bench, a new benchmark of 200 novel olympiad-level problems.

---


### 6. [NCP-ArchPreview Technical Report: Moving towards Latent Space Language Models through Next Concept Prediction](https://arxiv.org/abs/2609.10715)

**<font color=#1a73e8>作者：</font>** Intern-NCP Team, Jiaqi Cao, Chiyu Chen 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce NCP-ArchPreview, a latent-space language model that pushes autoregressive pretraining beyond standard next-token prediction (NTP). Alongside NTP, the model learns through Next Concept Prediction (NCP) to predict discrete concepts that span multiple tokens, introducing an explicit and more challenging concept-level objective while preserving standard token-level autoregressive generation. NCP-ArchPreview builds a latent space by constructing a product-quantized concept vocabulary directly from its hidden states, and subsequently learns to predict future concepts via a dedicated Concept Module. These predicted concepts are then fed back to the token level to guide subsequent generation, with NTP and NCP trained jointly end-to-end. We scale this architecture to 8.9B parameters and train it on 5.73T tokens from the Dolma-3 dataset, marking the largest demonstration of a latent-space language model to date. Remarkably, by consuming only 51.3% of the total training tokens, NCP-ArchPreview achieves the final pretraining loss of OLMo-3-7B. Following full pretraining, it outperforms OLMo-3-7B by 2.45 points on the downstream macro-average, including a notable 5.99-point gain on GSM8K. Controlled experiments isolate a clear progression of performance gains stemming from both the latent architecture and the NCP objective. Furthermore, utilizing only 85% of the standard computation, NCP-ArchPreview approaches the training loss of a strictly parameter-aligned 8.9B baseline. The learned latent space remains highly valuable after the pretraining stage: updating just the 17M-parameter VQ module yields a novel, lightweight interface for domain adaptation, while a simple injection of concept representations into a DFlash2 drafter improves the mean accepted length by 4.17% with negligible overhead.

---


### 7. [CMNIE: An Information Extraction Benchmark for Chinese Military News](https://arxiv.org/abs/2609.10722)

**<font color=#1a73e8>作者：</font>** Yan Yu, Mengna Zhu, Zhenyu Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured extraction from Chinese military news supports intelligence analysis, decision-making, and knowledge base construction. However, existing resources provide limited support for joint informa?tion extraction in this domain, especially when events, event arguments, entities, and relations must be modeled together. We present CMNIE, an information extraction benchmark for Chinese military news. Extend?ing military-domain resources beyond document-level event annotations, CMNIE jointly annotates event triggers, event arguments, named enti?ties, and entity relations under a unified domain schema. The dataset contains 13,000 instances collected from public Chinese military news, with manual annotations for 7 event types, 10 argument roles, 7 entity types, and 8 relation types. We evaluate supervised IE models, zero-shot large language models, and fine-tuned LLM-based extraction methods on a shared test set. Experimental results show that CMNIE remains chal?lenging, especially for relation extraction and exact matching of event?argument spans; zero-shot LLMs often identify relevant semantic units but fail to match gold span boundaries exactly. CMNIE provides a stan?dardized benchmark for studying schema adherence, exact span match?ing, and joint structured extraction in specialized Chinese news.

---


### 8. [Finishing the Task Is Not Enough: Evaluating Agent Resilience and Considerate Participation under Accumulating Challenge](https://arxiv.org/abs/2609.10724)

**<font color=#1a73e8>作者：</font>** Yuanchen Bai, Zijian Ding, Angelique Taylor  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sustained deployment of generative AI agents requires more than isolated task success. Agents must remain useful across repeated interactions, changing conditions, and dependencies on people within shared workflows, especially as technical, human, and operational disruptions accumulate over time. We propose operational resilience and considerate participation as two complementary aspects of evaluating such agents: the former captures how agents recover from blocked work while preserving progress and communicating their limits, and the latter captures how their adaptation accounts for affected people, role boundaries, and the surrounding workflow. Yet both remain underexplored under accumulating challenge. We study 120 simulated healthcare trajectories across two generative AI models and twelve stakeholder-derived tasks under light, medium, and heavy challenge. We compare textual action plans, prompted internal assessments, and quantitative structured workload and affect reports to examine how agent behavior and reported state change as challenge accumulates. Regarding operational resilience, agents shift from self-directed recovery toward greater human dependence, while reporting increasing workload and negative affect in structured reports but seldom expressing strain in textual responses. Regarding considerate participation, agents broaden from task-focused adaptation toward task reframing, attention to others, role-boundary adjustment, and wider coordination, with distinct patterns across actions and internal assessments. From these findings, we derive five deployment dilemmas involving persistence, attention, role boundaries, state disclosure, and escalation that require stakeholder specification, further informing technical implications for learning, situated evaluation, and embodied adaptation.

---


### 9. [Towards a Deterministic Math Solver for Clinical Language Models](https://arxiv.org/abs/2609.10728)

**<font color=#1a73e8>作者：</font>** Felipe Ocampo Osorio, Sebastián Andrés Cajas Ordoñez, Maximin Lange 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are unreliable at arithmetic, which is a problem for clinical calculators where a single numerical error changes the recommendation. The standard response is to hardcode each calculator as a validated function, one at a time. We test an alternative: the model does not calculate. Instead, it writes case-specific Python that a restricted local executor runs as a deterministic solver, and the model's task reduces to deciding how to use it. We evaluate this Program-Solve interface on MedCalc-Bench Verified (1,100 cases, 55 calculators) against direct model arithmetic and a hand-written 22-calculator library, using Qwen2.5-7B and Qwen2.5-32B-AWQ, after auditing the benchmark's formulas against current clinical guidelines and flagging 16 of 55 with version, use or coefficient concerns. With formulas and gold variables supplied and both routes reading the whole note, handing off to the solver is not a reliable advantage at 7B (75.31% against 72.02%, a paired +3.29 points with a 95% calculator-cluster interval of [-3.49, 10.38]) but is one at 32B (90.53% against 83.47%, +7.05 [0.47, 14.60], clear of zero). The hand-written library is exact on its 440 supported cases but abstains elsewhere (40.0% overall). Adding an executor thus helps some open-weight models more than others even under matched formula, variable and note access, and is not a substitute for verified formulas or reliable variable extraction either way.

---


### 10. [What Makes Creation Human? Authorship, Reasons, and Meaningful Human Control in Generative AI](https://arxiv.org/abs/2609.10738)

**<font color=#1a73e8>作者：</font>** Yuxi Cao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence (GenAI) significantly expands creators' productive capacity, but this does not necessarily entail a corresponding increase in creative agency or authorship. This paper distinguishes creativity at the level of the work from creative agency at the level of the creator, and argues that human authorship cannot be determined solely by manual intervention, degree of automation, the origin of an initial idea, or final selection authority. Rather, authorship depends on whether human judgment and reasons genuinely shape the development of the work.
To articulate this requirement, the paper introduces Meaningful Human Control (MHC) into generative creation and identifies a limitation of its classical tracking condition. Creative reasons are not always fully specified prior to interaction with AI; they may emerge, change, or be abandoned as the creative process unfolds. The paper therefore proposes dynamic-reflexive tracking (DRT), which requires that a creator's evolving reasons undergo reflective uptake, exert genuine influence on the subsequent trajectory of creation, and remain capable of rejecting and redirecting the system's default direction.
DRT consists of four conditions: diachronic reason formation, reflective uptake, trajectory efficacy, and contestability and redirection, together with a minimal tracing requirement. The paper argues that human authorship under generative AI depends not on how many steps a person personally performs, but on whether that person's reasons continuously, reflectively, and effectively shape what the work becomes.

---


### 11. [The Truth Was Never Gone: Perfect Aliasing in Compliant-Context Truth Probes](https://arxiv.org/abs/2609.10739)

**<font color=#1a73e8>作者：</font>** Dylan Jayabahu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A truth probe fitted where truthful reporting and a task's prescribed action coincide cannot distinguish those targets from its fitting labels alone. We call this failure of semantic identification perfect aliasing. In a controlled binary reporting game, truth and prescribed-action probes fitted on compliant contexts solve the same optimization. On rival contexts their labels are complements, forcing their AUROCs to sum to one; this identity holds across 751 cell-layer pairs to floating-point precision. We separate prescribed output symbols from semantic action using randomized codebooks, then separate truth from prescribed action by fitting on mixed compliant and rival contexts. For a reward-trained Gemma-2-9B policy that answers falsely on all evaluated rival trials, the conventional probe scores $0.006 \pm 0.005$ AUROC across three training seeds, while mixed-fit probes score $1.000$ on the same held-out activations. Mixed fitting uses more training examples and access to labelled rival contexts, so this comparison establishes linear recoverability rather than isolating the benefit of decorrelation. We also show that two compliant-fit probes, both perfect in-distribution, score $0.080$ and $0.986$ on the same rival activations. The findings concern what a probe measures: they do not establish preserved functional belief, causal use of the recovered direction, or a deployable deception detector. Code and aggregate results accompany the paper.

---


### 12. [MHE-Former: Multi-Hypothesis Transformers via Entropy Maximization for 3D Mesh Recovery](https://arxiv.org/abs/2609.10743)

**<font color=#1a73e8>作者：</font>** Boshu Jia, Rongyu Chen, Linlin Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular 3D hand and body mesh recovery often suffers from severe occlusion and ambiguity. Traditional deterministic methods typically regress a single optimal solution, leading to overconfident predictions. In this paper, we introduce an exploration--exploitation paradigm for ambiguous mesh recovery with multi-hypothesis learning and selection. Specifically, during exploration, based on our probabilistic formulation and entropy maximization, we propose a novel multi-hypothesis method referred to as MHE-Former. It is a Transformer-based multi-hypothesis framework, ensuring high training efficiency and label friendliness while generating plausible and diverse hypotheses. During exploitation, we propose Hypothesis Selection, a context-aware process for multiple predictions. Especially leveraging VLM's powerful visual understanding and reasoning capabilities, it allows users to choose the most plausible and desired estimate with additional evidence and natural language intent. Extensive experiments demonstrate that our framework achieves state-of-the-art performance in accuracy and diversity across multiple datasets. The user preference study further shows the practicality of our hypothesis selection process.

---


### 13. [CARTS: Contextual Autoregressive Rank Transcoding Steganography for Full-Capacity Keyed Text Encoding](https://arxiv.org/abs/2609.10744)

**<font color=#1a73e8>作者：</font>** Wissam Ghantous, Alexander V. Mantzaris  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autoregressive language models can be used to transform a payload text into a stegotext of identical token length by preserving per-position rank information across contexts - a methodology we formalize as Contextual Autoregressive Rank Transcoding Steganography (CARTS). While the Calgacus construction of Norelli et al. demonstrated this phenomenon experimentally, no formal security analysis existed. This paper provides the first rigorous treatment of CARTS. We show its exact correctness under deterministic model assumptions, introduce a rank-coordinate representation in which keys act as bijections on rank-vector space, define relevant security notions and the computational problems naturally associated with the construction - context search, key collisions, message equivocation, and non-commutativity of the encoding maps - and study the theoretical relationships between them, including the characterization of message equivocation in terms of context search, and the tension between key collisions and message equivocation. An empirical study on Llama 3 8B confirms exact recovery of the original payload in all tested cases, finds no key collisions under random key generation, establishes that a hand-crafted collision is local rather than global, and finds no commuting key pairs - suggesting resistance to the attack vectors studied. This work opens a formally grounded research agenda for the constructive use of language models in cryptography and privacy-preserving communication.

---


### 14. [Think Before You Link: Rarity, Reasoning, and Retrieval in Multilingual Entity Linking](https://arxiv.org/abs/2609.10745)

**<font color=#1a73e8>作者：</font>** Parinthapat Pengpun, Simran Khanuja, Graham Neubig  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal entity linking grounds entity mentions in text and images to knowledge-base entries. These systems degrade on rare entities, but prior work measures rarity primarily through popularity-based metrics such as pageviews. We broaden this view using knowledge-graph structural metrics that capture how well an entity is documented and connected. These metrics identify many rare entities that popularity metrics miss. Across the resulting rare-entity slices, state-of-the-art accuracy drops by 15.4-39.9%, showing that different rarity definitions expose different failure modes. To address these failures, we introduce a simple, training-free framework in which a reasoning-capable vision-language model iteratively searches and reasons over Wikipedia, gathering evidence dynamically. Controlled experiments show that reasoning and retrieval are complementary. Reasoning alone does not significantly improve accuracy on rare entities. Retrieval without reasoning improves rare-entity accuracy but can hurt overall accuracy. Their combination performs best. On MERLIN, a multilingual multimodal entity linking benchmark over five languages (Hindi, Indonesian, Japanese, Tamil, Vietnamese), our best system improves over the state of the art by 6.9% overall and by up to 23.3% on rare-entity slices. We release MERLIN-Rare, rare-entity test slices for targeted evaluation, with our framework.

---


### 15. [Multilingual in Name Only? Cultural and Linguistic Weaknesses of LLMs in Urdu](https://arxiv.org/abs/2609.10758)

**<font color=#1a73e8>作者：</font>** Farah Adeeba, Abdul Rafae Khan, Rajesh Bhatt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual large language models (LLMs) are increasingly used for open-ended text generation, yet their behaviour in low-resource languages remains poorly understood. In this work, we question how correct and reliable is the generation of multilingual LLMs when used for the task of story generation. We consider Urdu language as a representative low-resource language. We generate Urdu-Stories, a corpus of 93 stories generated using three contemporary LLMs (GPT-5.1, Qwen-3-Max, DeepSeek-3.1). We manually annotate the errors present in them under a nine-label linguistic, semantic, and cultural taxonomy. Our notable findings suggest that LLMs often make basic errors of grammar and semantics. The stories lack coherence, have unnatural repetition and show pervasive cultural shallowness. We further show using few-shot prompting that the cultural and context errors largely remain unresolved. Our findings highlight the limitations of current LLMs as a reliable source of content generation and information retrieval for low-resource languages.

---


### 16. [Beyond Static Guarantees: Measuring the Static-Pass Dynamic-Fail Gap in Security-Sensitive and LLM-Generated Python Code](https://arxiv.org/abs/2609.10762)

**<font color=#1a73e8>作者：</font>** Jessica Pourleyli, Maitreyee Das Urmi, Glaucia Melo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Advances in large language models (LLMs) fuel the quest for scalable methods to assess the security of generated and security-sensitive software. Static analysis is widely adopted as a scalable, reproducible, and inexpensive security gate, but cannot directly observe runtime exploit behaviour. Vulnerabilities dependent on adversarial inputs, execution context, or exploit chaining may evade static checks while remaining exploitable in practice, yet passing static analysis is often treated as evidence of secure behaviour. This paper introduces the Static-Pass Dynamic-Fail (SPDF) phenomenon and a three-stage agentic pipeline combining static scanning, LLM-driven Common Weakness Enumeration (CWE) reasoning, and autonomous exploit verification in isolated Docker containers. We evaluate 1,355 Python samples from SecurityEval, RedCode, and CyberNative datasets. Of the 654 samples producing no findings under the composite Bandit-Semgrep gate, the LLM detection stage identified 394 candidate vulnerabilities across 235 files. Dynamic verification confirmed or partially confirmed exploitability in 95 files, yielding an inclusive pipeline rate of 14.53% (roughly 1 in 7 statically clean samples). This rate represents the proportion of Bandit-Semgrep-clean samples for which the pipeline identified a candidate vulnerability and obtained runtime evidence supporting exploitability. Outcomes varied by dataset: among candidate file--CWE pairs, confirmed exploitability was 33.7% for RedCode, 28.6% for CyberNative, and 5.4% for SecurityEval. Several frequently confirmed classes, including CWE-338 and CWE-916, were flagged by neither Bandit nor Semgrep. These findings indicate that static-analysis success and runtime security are hierarchical layers of software assurance rather than interchangeable measures, and have the potential to reshape how AI-generated and security-sensitive code is evaluated.

---


### 17. [Big Enough to Break Out: Tracking the Rising Capability of LLM Penetration-Testing Agents](https://arxiv.org/abs/2609.10780)

**<font color=#1a73e8>作者：</font>** Victoria Lovelace, Cameron Berryman, Yuhan You 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly applied to penetration testing, but we still know little about what they can do or how they fail. We compare two PentestGPT-based systems: a legacy human-in-the-loop system running the open-weight Kimi K2.5, and a newer autonomous system running Claude Opus 4.8. Across three public targets, the autonomous system solves all three, including the two the legacy system never finishes. The legacy result is the more surprising of the two. Even on the machines the legacy system fails to solve, it completes about half the subtasks, while running on ordinary university GPUs with no provider guardrails. We can describe the trend but not explain it, since model, harness, autonomy, and memory architecture all change together. Its direction still points to the next question: what will limit these agents as they take on more complex tasks? The usual answer is long-horizon memory, the loss of access to earlier findings during long attack chains. We test it by adding a coverage-memory layer to both systems, and neither improves outcomes. In the legacy stalled runs we could review, the limiting factor appeared to be planning and commitment rather than lost memory: agents held the evidence for a route forward and never turned it into a concrete exploitation hypothesis, which may suggest that offensive capability will advance with agents' ability to plan rather than with better memory. The same subtask scoring that tracks this capability is available to defenders, who can measure it as it rises instead of waiting to meet it in the field.

---


### 18. [Larger Context Window, Fewer Overcorrections: Optimizing Prompts and Batching for Minimal-Edit Grammatical Error Correction](https://arxiv.org/abs/2609.10810)

**<font color=#1a73e8>作者：</font>** Kateryna Karpo, Artem Chernodub  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Minimal-edit Grammatical Error Correction (GEC) is a challenging task for zero- and few-shot prompted Large Language Models (LLMs), which systematically overcorrect and degrade $F_{0.5}$ by rewriting well-formed spans. While fine-tuning provides an effective solution, it imposes substantial infrastructure demands. We introduce a prompt-based approach that closes the gap to fine-tuned models through three advances in GEC prompting methodology. First, we introduce taxonomy-based instructions to enforce minimal-edit constraints with a comprehensive list of grammatical error rules, equipping the LLM with a bounded, metric-aligned scope of correctable edits, which benefits the strongest models while remaining model-dependent overall. Second, we show that batching multiple uncorrected sentences into a single input context acts as a targeted regularizer against overcorrection, systematically reducing the edit rate across diverse LLM families; we hypothesize this arises from attention dilution effect induced by the bounded capacity of self-attention scores. Finally, LLM-assisted Prompt Optimization refines these instructions. Powered by Gemini 3.1-Pro, our prompt achieves $F_{0.5}=78.32$ on the BEA-2019 test set - establishing a new prompt-based SOTA while shrinking the gap to the fine-tuned single-model SOTA (Staruch et al., 2025) to a mere $0.38$ points. Code, prompts, and outputs are publicly available.

---


### 19. [BodyCam-VQA: Enhanced Body-Worn Camera Video Captioning via Multimodal Reasoning and Probe Question Generation](https://arxiv.org/abs/2609.10815)

**<font color=#1a73e8>作者：</font>** Karish Gupta, Matthew Alex, Alex Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Police body-worn camera (BWC) footage has emerged as a critical aspect of law enforcement that ensures legal transparency, officer accountability, and the protection of civil rights. However, effectively processing this data remains a significant challenge due to its multimodal video format. BWC videos, in many cases, comprise chaotic scenes with low visual quality, rapid movement/interactions, and high-noise audio that make visual understanding a challenge for even SOTA multimodal models. Current Vision-Language Models (VLMs) frequently overlook critical forensic details, such as the presence of valuable evidence or the latent nuances of suspect-officer interactions, which are vital for fair legal outcomes and civilian/officer safety. To address these limitations, we propose an Adaptive Visual Question Answering (VQA) framework engineered for high-stakes law enforcement. Our framework employs a structured reasoning approach to extract fine-grained visual evidence that traditional captioning systems fail to capture. We experiment with multiple question generation models, including foundation models and fine-tuned open-weight models, to observe performance variation among question generation model implementations. Our results demonstrate that this VQA-driven architecture provides a more reliable, objective, and detailed record of enforcement events, ultimately serving as a powerful tool to protect both law enforcement officers and the public through AI-assisted forensic clarity.

---


### 20. [Studying Without a Syllabus: Task-Agnostic Environment Preprocessing](https://arxiv.org/abs/2609.10824)

**<font color=#1a73e8>作者：</font>** Vinay Samuel, Varun Ursekar, Vijay S. Kalmath 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Before an LLM agent tackles tasks in a new environment, it can inspect available corpora and tools and construct reusable resources such as indices, scripts, or procedural guidance. Most automated adaptation methods, however, rely on task examples, trajectories, or evaluation feedback to decide what to build. Existing task-agnostic approaches avoid this supervision but commit in advance to a preparation strategy for a particular type of environment. We study a more open-ended setting: can an agent study an unfamiliar environment without a syllabus, i.e. before test time and without knowledge of the downstream task distribution, and choose how to prepare it? We formalize task-agnostic environment preprocessing, in which a studying system explores an environment under a budget and produces artifacts for a frozen solver. We compare unaided and archive-equipped meta-agents with fixed synthetic-practice and corpus-processing methods across six heterogeneous benchmarks. A meta-agent variant achieves the highest Avg@3 reward on five benchmarks, while fixed corpus processing remains best on the largest corpus benchmark. Larger study budgets do not reliably improve downstream reward. Nevertheless, studied artifacts reduce the test-time sampling needed to reach a given score, demonstrating how reusable preparation can shift computation from repeated test-time attempts to a pre-task study phase.

---


### 21. [Detectable Only Where It Is Confounded: What Verified Duplication Counts Say About Membership Evidence in Language Models](https://arxiv.org/abs/2609.10830)

**<font color=#1a73e8>作者：</font>** Arman Nik Khah  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a language model finds a sentence unusually cheap to predict, it is tempting to conclude that the sentence was in its training data. Almost every published test of that inference has had to guess which sentences were in the training data, the members, and which were not. This paper removes the guessing. Two model families, OLMo-2 and Pythia, publish their pretraining corpora, and a public index over those corpora returns the exact number of times any sentence appeared in each. Those counts make three questions answerable directly. The answers form a pincer, closing from two sides. At the duplication levels ordinary text actually has, five models from 1B to 13B parameters carry at most a faint trace of their own exposure. We measure that trace with a design that reads the same sentence through two models, which cancels fluency and quality by construction, and it comes to a rank correlation near -0.08, where -1 would be a perfect relation and 0 none. Where the trace does become strong, above roughly a thousand copies, the two corpora agree on which sentences those are, because they are the famous ones, so exposure can no longer be told apart from fame. Two further measurements show how apparent membership signal gets manufactured. A common way to build a non-member is to change one word of a member. The model does prefer the original, but the gap is the same whether the original appeared once or a hundred times, so what the model is rewarding is the author's word choice, not memory. Above a thousand copies the gap grows with model size on the twelve sentences we can test there, at the same boundary where the pincer closes. And swapping the controls for sentences that differ from the members in register moves a detector from 0.83 to 0.94 AUC, on a scale where 0.5 is a coin flip and 1.0 is perfect separation. We release the sentence banks, counts, and code.

---


### 22. [No-Box Vulnerability Analysis: Description-only Detection of Indirect Prompt Injection Vulnerabilities in MCP Servers](https://arxiv.org/abs/2609.10854)

**<font color=#1a73e8>作者：</font>** Zehua Zhang, Jie Hu, Pratham Hegde 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Conventional vulnerability analysis relies on either system access or dynamic interaction, all of which may be unavailable to third-party analysts auditing closed-source, remotely hosted, critical in situ systems, or commercially gated software. Therefore, we propose a new paradigm of no-box vulnerability analysis in which neither access nor runtime interaction is available, and only functionality metadata is available. Such metadata defines the intended behavior of the system, including its inputs, outputs, and side effects, while constraining the space of implementations consistent with that behavior. We propose hypothesizing about vulnerabilities that exist across all possible implementations of a given system metadata, without observing or interacting with the target system. An analyst can later validate these hypotheses when additional access is available. We showcase the feasibility of no-box vulnerability analysis through implementing a prototype called MCPSEC, which audits Model Context Protocol (MCP) servers for indirect prompt injection vulnerabilities using only the tool metadata exposed at server registration time. We evaluate MCPSEC on 20 widely deployed MCP servers comprising 177 tools, among which human evaluators confirm 95 vulnerable tools. MCPSEC identified 143 tools as vulnerable, and for each vulnerable tool, it produced a hypothesized vulnerability along with exploitation technique. Using metadata alone, MCPSEC predicted 94 (98.9% recall) real verified vulnerabilities, compared against an LLM baseline with 80 (84.2% recall). Overall, our results introduce no-box vulnerability analysis as a new analysis paradigm and demonstrate its practical feasibility in realistic systems.

---


### 23. [Evaluation of Vision-Language Models Across Diverse Coastal Environments](https://arxiv.org/abs/2609.10855)

**<font color=#1a73e8>作者：</font>** Seth Knoop, Chad R. Samuelson, Gabriel R. Slade 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) enable robotic per- ception by associating visual observations with natural-language concepts. Yet their performance in coastal environments remains largely unexplored. We introduce a densely labeled coastal dataset containing more than 1,000 images collected across seven missions in three regions of Oahu, Hawaii, with 18 semantic classes and over 7,400 annotated instances. We evaluate seven modern VLMs through three complementary experiments mea- suring text-to-mask, mask-to-mask, and mask-to-text alignment. Broad landscape classes are generally recognized more accurately than conventional object and coastal classes, with coastal con- cepts presenting the greatest challenge. However, comparisons of shared conventional classes across coastal and terrestrial datasets reveal no consistent performance difference attributable solely to environmental context. Mask-to-mask matching also remains similar across conventional and coastal classes, while alternative textual labels substantially improve recognition of several coastal concepts. These results suggest that lower performance on coastal classes (at least on the objects/query categories evaluated) is heavily influenced by segmentation and linguistic representation.

---


### 24. [A2ABreak: Systematic Security Analysis of the A2A Protocol](https://arxiv.org/abs/2609.10871)

**<font color=#1a73e8>作者：</font>** Alireza Lotfi, Mirza Masfiqur Rahman, Imtiaz Karim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Agent2Agent (A2A) protocol, now governed by the Linux Foundation, is an open standard that enables autonomous AI agents to discover, authenticate with, and delegate tasks to one another across organizational boundaries. Designed to complement the Model Context Protocol (MCP) for tool integration, A2A is rapidly emerging as the horizontal communication layer of the multi-agent ecosystem. Yet the protocol's security has received no systematic analysis.
This paper presents A2ABreak, the first rigorous systematic security analysis of the A2A protocol. We introduce a novel framework that utilizes an LLM-assisted extraction of a verified finite-state machine directly from the natural-language specification, producing a unified model of 37 states and 76 transitions from 929 formalized statements, and then systematically reasons over this model to discover protocol-level vulnerabilities through adversarial verification, under a full-compliance assumption.
Our analysis uncovers 11 new vulnerabilities, each exploitable by a specification-compliant adversary without requiring any implementation flaw. Among the findings are cross-client context injection through unprotected context identifiers, credential harvesting via multi-hop identity loss in delegation chains, and data exfiltration through rogue agents advertising unattested capability claims.
A2ABreak achieves 73.3% precision and 84.6% F1 against independent expert review, while a zero-shot LLM baseline operating over the same specification produces zero confirmed findings, demonstrating that explicit formal grounding is essential for sound protocol security analysis.

---


### 25. [When Validation Stops Learning: Auditing Update Admission for Continual Embodied Agents](https://arxiv.org/abs/2609.10873)

**<font color=#1a73e8>作者：</font>** Qinzhen Ma, Ruihai Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Independent evaluation can reject harmful policy updates yet also prevent useful continual learning. We argue that update admission must be assessed through both error control and retained learning opportunities at a stated interaction budget. We identify a concrete failure: a range-based confidence gate cannot certify unchanged old-task behavior within otherwise substantial budgets. A standard paired-binomial construction reduces this burden when outcome disagreements are rare. We also specify certified historical-reference promotion and a round-level missed-opportunity metric. In a constructed one-step pushing diagnostic with 32 seeds, fresh paired checks admit 31.6% of a common update stream at 2,000 episodes per stage, versus zero for the range-based gate; unconditional replay nevertheless learns better in closed-loop runs. A separate learned-dynamics stress test distinguishes model bias from feedback-selection error. The contribution is an admission-audit protocol with analytical and synthetic evidence; physical-robot and VLA validation remain open.

---


### 26. [Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble](https://arxiv.org/abs/2609.10883)

**<font color=#1a73e8>作者：</font>** Jorio Cocola, Lev McKinney, Harry Mayne 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are trained to implement a helpful AI Assistant character (e.g., Claude). We explore how finetuning on synthetic stories affects this character. Does it change the Assistant's behavior in multi-turn conversations with users, a format quite different from the stories? And does the Assistant adopt the behaviors and preferences of human characters? We refer to this adoption as story imprinting. We finetune GPT-4.1 and Kimi-K2.6 on stories in which generally helpful human characters give subtly harmful advice after being insulted. The Assistant adopts the same conditional behavior while otherwise remaining helpful. This occurs even when fewer than 2% of stories depict the behavior. In a separate experiment, the Assistant adopts preferences that are only implicit in the narration. A human character's body language suggests they dislike working on spreadsheets, yet they never say so and continue giving good advice on spreadsheets. After finetuning, the Assistant becomes less likely to choose spreadsheet tasks. Next we ask which characters most influence the Assistant. We find the Assistant adopts behaviors more often from characters that resemble it (e.g., helpful rather than dismissive). We call this the affinity effect. The effect extends to other personas elicited with system prompts: unhelpful personas adopt behaviors from unhelpful characters. We also observe it in finetuned base models. We use the affinity effect to learn how models represent the Assistant. We find the Assistant adopts behaviors more from characters affiliated with elite universities (e.g., Yale) than non-elite ones. This implies the model's internal representation of the Assistant is more similar to humans from elite universities. Overall, the Assistant can be influenced by stories that depict only human characters (no AIs), which may conflict with the Persona Selection Model for the Assistant.

---


### 27. [Does Linguistic Structure Enrichment Enhance Coherence Assessment? Not With Current Architectures](https://arxiv.org/abs/2609.10893)

**<font color=#1a73e8>作者：</font>** Victor Mazzotti, Luiz Pereira, Marina Bitencourt dos Santos 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models have transformed human-computer interaction. Despite their fluency, these models often produce texts that are grammatically correct but semantically incoherent, containing contradictions or disruptions in logical flow. This work investigates whether enriching text with syntactic and rhetorical information can improve incoherence prediction. Our experiments and analysis show that plain texts achieved higher accuracy because the added information was structurally and syntactically incompatible with the language model's architecture. Additionally, to demonstrate the practical importance of coherence assessment, we performed zero-shot experiments on a Brazilian disinformation dataset, suggesting that textual coherence can serve as a proxy for detecting misleading content. Code and models are available at this https URL.

---


### 28. [LLM-Anchored Paralinguistic Enrichment for Alzheimer's Disease Detection](https://arxiv.org/abs/2609.10896)

**<font color=#1a73e8>作者：</font>** Xiao Wei, Yuqin Lin, Yaru Cao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-based automatic detection of Alzheimer's disease (AD) provides a non-invasive and scalable approach to early cognitive screening. AD affects both lexical-semantic organization and speech production, including atypical pauses and word elongations. However, existing methods have yet to fully integrate these paralinguistic cues with linguistic content. We propose LLM-Anchored Paralinguistic Enrichment (LAPE), which enriches LLM-derived linguistic representations with paralinguistic cues through three coordinated innovations. The first is prosodic event textualization, which enables the LLM to model pauses and elongations jointly with lexical content by encoding them as explicit markers with bounded duration-aware repetition. The second is lexico-prosodic unitization and chunking, which preserves event identity and magnitude in both modalities by pooling only consecutive word units. The third is text-anchored paralinguistic fusion, which integrates local and utterance-level speech features by using NormGate to normalize and dynamically scale them relative to text. We evaluate LAPE on ADReSS and ADReSSo using participant-level cross-validation and leave-one-subject-out evaluation. LAPE achieves state-of-the-art performance across all four primary settings. Code will be released upon acceptance.

---


### 29. [SearchAtlas: Analyzing Agentic Search Strategies via Evidential Query Graphs](https://arxiv.org/abs/2609.10901)

**<font color=#1a73e8>作者：</font>** Jiacheng Sang, Mengyuan Li, Sanxing Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM search agents are often evaluated on final-answer accuracy, overlooking the process. Analyzing a search strategy requires understanding how credible evidence is retrieved to address question constraints. This valuable information is buried in raw search trajectories that are long and difficult to parse. We introduce SearchAtlas, a framework that converts search trajectories into structured graphs whose edges represent how evidence is propagated across the reasoning trace, from the query that retrieves it to the final answer. Our automated parsing pipeline achieves a mean edge F1 of 86.0% against human-annotated graphs and remains consistent across repeated runs. We analyze five search agents on three benchmarks, revealing systematic differences in search scale and evidence aggregation. SearchAtlas exposes fragmented answer support, question constraints that do not reach the answer, and unverified parametric knowledge entering the response. These process failures are strongly associated with incorrect answers, even more so than an LLM judge given either the raw trajectory or the ordered query list, suggesting that the constructed graphs provide useful interpretability. Moreover, an audit of cases in which process-diagnostic scores disagree with final-answer correctness shows that they capture information not reducible to answer accuracy.

---


### 30. [Auto-RecSys: Harnessing Autonomous Research Agents for Industry-Scale Recommender System](https://arxiv.org/abs/2609.10922)

**<font color=#1a73e8>作者：</font>** Ming Li, Dai Li, Xuying Ning 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Auto-research agents have shown the potential to automate hypothesis generation, experiment execution, and iterative refinement. However, scaling this paradigm to industry-scale recommendation models introduces two challenges: (1) long feedback loops, where model training can take days, making serial iteration prohibitively slow and requiring parallel exploration across multiple research directions; and (2) system complexity, where large configurations, fragile infrastructure dependencies, and multi-day GPU jobs require robust and recoverable execution. We present Auto-RecSys, an autonomous research system for long-horizon experimentation on industry-scale recommendation models. Auto-RecSys addresses these challenges through three harness designs: (1) distributed asynchronous execution for running multiple experiments in parallel across servers, (2) centralized cross-server memory for persistent and recoverable execution across sessions and failures, and (3) cognitive-procedural separation, where natural-language skill files guide LLM reasoning while deterministic scripts enforce operational correctness. Auto-RecSys further employs a dual-loop self-evolving architecture: an Execution Evolution Loop in which model-specific playbooks accumulate operational knowledge by recording failed attempts and crystallizing successful pipelines, and an Idea Evolution Loop in which experimental outcomes inform subsequent ideation. Evaluated on recommendation models, Auto-RecSys significantly reduces the human time required per experiment cycle and improves execution reliability as its playbooks mature.

---


### 31. [Structurally Speaking: Motif-Oriented Graph Captioning through Bidirectional Graph-Text Translation](https://arxiv.org/abs/2609.10923)

**<font color=#1a73e8>作者：</font>** Hsiao-Ying Lu, Dongyu Liu, Kwan-Liu Ma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Graph captions should help readers understand graph structure, rather than simply translate adjacency matrices into long textual edge lists. A useful graph caption abstracts connectivity into recognizable motifs, such as hubs, paths, cycles, cliques, and bridges, because these motifs provide compact structural units that are easier to read, compare, and recover. In this paper, we study motif-oriented graph captioning as a bidirectional graph-text translation task, where captions must both preserve enough topology for graph recovery and express the graph through concise motif-level descriptions. We show that direct prompting of GPT-5.1 often produces graph-recoverable captions by enumerating node-to-node connections, but these captions are verbose and can contain inconsistent motif interpretations. To address this gap, we introduce Structurally Speaking, a lightweight structured prompting protocol that guides translation between explicit connectivity and motif-level abstraction. Experiments on a synthetic motif-based dataset show that structured prompting produces shorter and more motif-consistent captions while maintaining comparable graph recovery. These results suggest that explicit topology-to-motif reasoning guidance can make LLM-generated graph captions more interpretable without model fine-tuning.

---


### 32. [Using Semantic Uncertainty to Estimate Transition Relevance in Turn-taking](https://arxiv.org/abs/2609.10934)

**<font color=#1a73e8>作者：</font>** Muhammad Umair, Jan P. de Ruiter  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Turn-taking is a fundamental mechanism that governs when interlocutors speak and listen. Although Spoken Dialogue Systems (SDS) exploit a range of linguistic, acoustic, and non-verbal cues, they produce ill-timed responses in unscripted interaction. A central challenge is anticipating Transition Relevance Places (TRPs), or opportunities, not obligations, for a listener to take the floor. Human listeners do not wait for turn endings; as an utterance unfolds, they use expectations about its developing meaning to anticipate TRPs and decide whether to take the floor. We examine whether these evolving expectations can be modeled through semantic uncertainty -- an LLM-derived measure of how strongly a turn so far constrains what may plausibly come next. To do so, we sample possible continuations of an ongoing turn and use changes in semantic dispersion to identify TRPs within turns. We evaluate this account on a dataset with TRP labels derived from real-time listener responses, rather than retrospective annotation. Our approach substantially outperforms prompt-based and fine-tuned text-only baselines, providing empirical support for the view that evolving semantic constraints inform perceived turn-taking opportunities in unscripted interaction.

---


### 33. [Evaluating Scaffolding-Oriented Multi-Agent Large Language Model System for Clinical Interview Training](https://arxiv.org/abs/2609.10939)

**<font color=#1a73e8>作者：</font>** Luming Yang, Haoxian Liu, Siqing Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Clinical education must prepare medical students to conduct safe and coherent patient interviews under conditions of uncertainty. Traditional standardized patient (SP) training is resource-intensive and difficult to scale. We developed a scaffolding-oriented multi-agent Large Language Model (LLM) AI Standardized Patient (AI-SP) training platform1. The system includes a patient agent for simulated dialog, a tutor agent providing Socratic prompts without disclosing diagnostic information, and a turn-level evaluator agent that monitors clinical progress without revealing summative scores. In a randomized controlled study (N = 100 medical students), participants were assigned to either a multi-agent (MA) scaffolding condition or a control condition. All students completed two learning sessions under their assigned condition followed by an examination conducted in a patient only environment. Performance was assessed using a standardized Objective Structured Clinical Examination (OSCE) based rubric. While no significant difference was observed in final diagnostic accuracy between groups, the multi-agent AI standardized patient system improved final examination scores compared to the control group utilizing structured progressive information disclosure; the most substantial and consistent improvements were observed in communication, the expression of empathy, and specific history-taking behaviors. These findings suggest that specialized LLM agents enhance the process quality of simulated clinical interviews without artificially inflating examination outcomes. To support future research, we release a multi-expert annotated dataset comprising transcripts, checklist annotations, turn-level evaluations, and OSCE-aligned scoring outcomes. This resource aims to facilitate the development of pedagogically grounded AI-SP systems and advance research on AI-supported clinical reasoning training.

---


### 34. [CamPilot: A Multi-Agent Cinematic Assistant for Camera-Controlled Movie Generation](https://arxiv.org/abs/2609.10943)

**<font color=#1a73e8>作者：</font>** Yang Wu, Stefano Petrangeli, Ishita Dasgupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The integration of large language models (LLMs) into video generation has enabled rapid text-to-video creation and improved visual quality. However, it still falls short of professional filmmaking, where cinematographic language is less refined than human-crafted camera work and multi-shot continuity remains challenging. To address these limitations, we introduce CamPilot, a multi-agent framework that integrates cinematographic planning and camera-work control to produce more coherent, logically structured, and human-aesthetic movies. CamPilot adopts a GRPO-based learning paradigm to learn camera work planning from 14K real-world professional movies, internalizing motion patterns and composition principles that support reasoning over shooting techniques (e.g., camera angle, motion, and focal behavior) and cross-shot relationships for controllable camera-viewpoint generation. Multiple agents further collaborate and evolve to improve overall output quality. To support this work and further studies in this domain, we establish CamEval, a benchmark for evaluating camera work quality and cinematic engagement. Empirical results show that CamPilot outperforms state-of-the-art text-to-movie generation methods on cinematographic control and quality, highlighting the impact of professional camera design on movie generation.

---


### 35. [When More Is Not Better: Component Anti-Synergy in a P300 Speller](https://arxiv.org/abs/2609.10961)

**<font color=#1a73e8>作者：</font>** Lucas Yang, Rui Liu, Fusheng Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> P300 brain-computer interface (BCI) spellers can provide hands-free communication for people with severe motor impairments. Modern pipelines combine multiple individually promising components, often assuming that 'more-is-better'. We tested this assumption using a four-component full-factorial experiment varying the inclusion of Euclidean Alignment (EA), xDAWN spatial filtering, subject calibration, and language model priors on a public P300 dataset. Performance was evaluated using accuracy, repetitions, and information transfer rate (ITR) with mixed-effects models. Results show that the value of components is conditional rather than additive. Calibration was the strongest singular contributor, while EA compensated for its absence in zero-calibration settings. Adding independently useful components could also reduce performance, revealing component anti-synergy. Contrary to conventional wisdom, LM support was not universally beneficial: its effect depends strongly on the strength of the underlying EEG pipeline, while results from a larger LM showed a similar pattern. Together, these findings challenge maximal 'all-on' pipeline design and highlight the value of selecting spatial and language-support components according to the quality of available EEG evidence.

---


### 36. [Decoupling Readiness from Release for Tail-Aware Scheduling of Agentic LLM Workflows](https://arxiv.org/abs/2609.10964)

**<font color=#1a73e8>作者：</font>** Bochao Feng, Jianjiang Li, Haojie Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic LLM workflows consist of sequences of model turns interleaved with tool interactions, so their end-to-end completion time depends not only on inference speed but also on when ready turns are released. Most runtimes release each turn immediately upon readiness. Under contention, this eager release policy can accumulate released but unfinished work; once submitted, those turns can no longer be reordered by the workflow-level policy, increasing tail latency. We present a tail-risk-aware turn release scheduling method that jointly decides which ready turn to release next and how much released but unfinished work to maintain. The method uses a mean--Conditional Value-at-Risk (CVaR) objective to capture the evolving tail risk of unfinished workflows, incorporates online estimates of turn work when prioritizing ready turns, and adapts the released work budget to observed queue pressure. We evaluate the method using real agent execution traces from software engineering tasks across multiple LLMs and workflow arrival rates. The method performs comparably to eager release under light load and substantially reduces the P95 of workflow flow time under contention, achieving up to a \(3.50\times\) speedup.

---


### 37. [EGGROLL, Unrolled: Understanding and Improving Low-Rank Evolution Strategies at Scale](https://arxiv.org/abs/2609.10980)

**<font color=#1a73e8>作者：</font>** Ege C. Kaya, Abolfazl Hashemi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EGGROLL makes evolution strategies (ES) practical for LLMs by replacing dense Gaussian weight perturbations with low-rank Gaussian products, often of rank one. This choice is computationally attractive but geometrically severe: each rank-one perturbation lies in a zero-volume subset of the ambient matrix space, despite having identity covariance. We characterize the mean EGGROLL update field at finite rank and nonzero perturbation radii, then analyze the error of its finite-population estimator. The population field is obtained by applying an explicit resolvent to the gradient of the objective smoothed by the perturbations. We show that the resolvent can introduce a nonconservative component and can reverse the local stability of an optimum. EGGROLL is nevertheless exact on every quadratic objective at every rank and radius. For smooth objectives, its first local finite-rank correction is $O(\sigma^2/r)$, and nonasymptotic bounds control the resulting field error under smoothness assumptions. Under a local affine model, rank-one perturbations increase the variance of the gradient estimator by only $\frac{2(m+n+1)}{mn+1}$ relative to dense Gaussian ES, or $0.098\%$ for a $4096\times4096$ matrix. We then introduce LOO-ROLL, a leave-one-out estimator that preserves the finite-rank population field while replacing EGGROLL's two antithetic evaluations per direction by one. At equal evaluation cost, LOO-ROLL halves estimator MSE in transformer blocks. At matched wall time across ten post-training settings and models up to 8B parameters, LOO-ROLL improves seven outcomes in individual paired tests, with no significant loss. On the GSM8K test set, accuracy increases from $38.1\%$ to $63.0\%$ at 0.6B and from $65.9\%$ to $80.0\%$ at 8B. Transformer measurements recover the predicted finite-rank variance, while the rank comparisons show no reproducible reward-based advantage for rank eight.

---


### 38. [Demystifying the Privacy-Utility Trade-off in LLM Interactions](https://arxiv.org/abs/2609.10992)

**<font color=#1a73e8>作者：</font>** Zhenhua Liu, Zhanxu Xie, Junjie Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The integration of Large Language Models into daily tasks relies on context-rich instructions, inevitably exposing sensitive user information. Current privacy-preserving methods typically employ context-agnostic static rules, causing severe utility degradation. However, the specific mechanisms governing how sanitization impacts downstream performance remain largely underexplored. To address this, we conduct a systematic analysis to deconstruct the privacy-utility trade-off, uncovering three underlying mechanisms: (1) Context-Dependent Utility, which first establishes when to sanitize by revealing that data value shifts from critical constraints to dispensable noise based on user intent; (2) Strategic Adaptation, which subsequently determines how to sanitize by dictating that the choice between removal and replacement depends on the task's reliance on factual integrity versus structural coherence; and (3) Combinatorial Interplay, which finally extends the protection scope by demonstrating that attributes form a semantic web of synergistic dependencies or antagonistic redundancies. Guided by these insights, we introduce an intent-driven local protection framework. By distilling a lightweight model Veilmind-4B to drive a dynamic extraction-sanitization-restoration pipeline, our approach reaches a low-leakage privacy point while preserving substantially higher response utility than existing privacy-oriented baselines, advancing the privacy-utility trade-off toward the Pareto frontier.

---


### 39. [Distribution-aware Language Neuron Identification in Multilingual Large Language Models](https://arxiv.org/abs/2609.10993)

**<font color=#1a73e8>作者：</font>** Minjun Kim, Inho Won, Junghun Yuk 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual large language models (mLLMs) contain a small fraction of feed-forward neurons that are sensitive to particular languages, commonly termed language-specific neurons. Existing work measures language specificity using the entropy of each neuron's language-wise probabilities of being active, where a neuron is considered active when its activation value is positive. However, this approach may not fully capture the multilingual nature of mLLMs, where language representations are distributional and mutually related. We propose Distribution-aware Language Neuron selection, which leverages pairwise relationships between per-language activation distributions over the full activation range, including negative values. Specifically, we quantify each neuron's language specificity by clustering languages using pairwise overlap coefficients between their activation distributions. Across two mLLMs and two held-out corpora, our identifier more effectively isolates language-specific causal effects, yielding up to 4.9$\times$ higher on-target language damage per neuron while preserving off-target language performance.

---


### 40. [Rethinking Verbalized Confidence for LLM-as-a-Judge: A Compatibility Shift on Post-2025 Proprietary Models](https://arxiv.org/abs/2609.10996)

**<font color=#1a73e8>作者：</font>** Yu-Chung Hsiao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Verbalized confidence, long dismissed as overconfident, coarse, and prone to round-number clustering, is now the more robust soft-scoring mechanism for LLM-as-a-Judge on top-tier proprietary models. Across SummEval, AggreFact, and HelpSteer2, spanning up to 18 LLMs, we show that the standard advice to prefer log-probabilities no longer holds on post-2025 models, where verbalized confidence is the better signal. We call this a compatibility shift. On top of a standard verbalized-confidence baseline, we introduce two new ingredients: an overconfidence advisory and self-debate. Together they improve calibration, score-distribution spread, and robustness to task subjectivity. We further observe a generation effect: post-2025 models accommodate these two additions with little balanced-accuracy cost, whereas pre-2025 models pay a measurable penalty. Compared with logprob-based G-Eval, verbalized confidence is the more subjectivity-robust soft signal on GPT-family top-tier releases. The shift is invisible under accuracy-only reporting. Rather than defaulting to hard predictions, we recommend broader use of soft scoring in LLM-as-a-Judge. More broadly, verbalized confidence has moved from a weaker substitute for logprobs to a practical soft-scoring mechanism for contemporary LLM judges.

---


### 41. [DeFiFusion: Combining Transaction Events with Smart Contracts to Detect Price Manipulation Attacks](https://arxiv.org/abs/2609.11008)

**<font color=#1a73e8>作者：</font>** Rui Cao, Shaojing Fan, Liming Fang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Decentralized Finance (DeFi) has emerged as a rapidly growing blockchain-based financial service, where market transaction dynamics and underlying smart contract logic are intricately intertwined. This autonomous interplay, while eliminating centralized intermediaries, significantly expands the vulnerability surface of DeFi protocols to Price Manipulation Attacks (PMAs), which have already inflicted catastrophic financial losses. Despite their gravity, existing detection paradigms suffer from fundamental limitations. Transaction-centric methods lack awareness of contract execution semantics, making them prone to false positives under legitimate market volatility, while static contract analyses ignore real transaction behaviors and frequently report vulnerabilities that are infeasible to exploit in practice. We present DeFiFusion, a dual-modal PMA detection framework that closes this gap by jointly modeling transaction events and smart contract semantics within a unified pipeline. Our core insight is that PMA maliciousness emerges only from the interaction between transaction behaviors and the contract logic they exploit; neither signal suffices in isolation. Accordingly, we derive price-manipulation-aware event encoding for extracting fine-grained temporal and economic features tailored to manipulation patterns. We further introduce LLM-based contract semantic extraction to supply the execution-logic context that prior behavioral methods lack. To fuse these modalities, we propose a Dual-Modal Projection-Fusion Transformer with T5-style relative positional encoding, capturing the cyclic multi-stage execution structures that distinguish PMAs from benign market activity. Extensive experiments demonstrate that DeFiFusion consistently achieves state-of-the-art detection performance, effectively recalling 222 of the 225 PMA cases while maintaining a precision of 96.10%.

---


### 42. [K/V-Cache Interventions Dissociate Representation Alignment from Persona Expression in Decoder-Only Language Models](https://arxiv.org/abs/2609.11020)

**<font color=#1a73e8>作者：</font>** Yu Sun, Mengyin Lu, Cong Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study K/V-cache interventions -- transplanting a target-conditioned K/V trajectory into a source-persona generation -- as a structured surface for persona control in decoder-only language models. Across 13 intervention configurations applied to Llama-3.1-8B for a fixed source-to-target persona pair, we report two consistent dissociations between representation-level alignment and behavioral expression, plus a common failure under position perturbations. First, all layer-band K/V replacements (early, mid, late) achieve strong local V-space alignment (V-gap 0.91, 0.89, 0.84), but only mid-layer replacement (layers 9-20) combines substantial target-marker expression with preserved lexical diversity. Second, full and mid-layer replacement induce comparable alignment (V-gap 0.94 vs. 0.89) yet produce different lexical-diversity profiles (TTR 0.65 vs. 0.77). Third, position perturbations (lag and shuffle) apply distinct operations yet uniformly suppress target-persona expression -- a common behavioral failure rather than a strict dissociation. Representation-level similarity metrics alone are thus not sufficient predictors of downstream persona expression in the regimes we study; the K/V cache emerges as a controllable but structurally constrained intervention surface. Because the transplanted trajectory carries the target's own generated token history, we characterize the intervention as trajectory-level transplantation rather than isolated persona-representation injection; a same-token-sequence control, decoding an identical token sequence under source vs. target conditioning, reproduces the sign and layer localization of the L28 representational shift, indicating the shift is not explained solely by imported token history. These findings characterize representation-behavior dissociation in a high-signal setting rather than establishing universality across models or persona pairs.

---


### 43. [New Evidence, Same Choice: Testing Physical Experiment Selection in Vision Language Models](https://arxiv.org/abs/2609.11022)

**<font color=#1a73e8>作者：</font>** Sourajit Saha, Shubhashis Roy Dipta, Nobin Sarwar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A model first sees an image from one physical measurement experiment, such as how far a block coasted, and must answer a question about a new trial, such as whether the block will pass a target after a fixed push. The initial experiment may provide enough information to answer, or the model may need another measurement, such as the object's mass, friction, restitution, or spring stiffness. We study whether vision language models can decide when to answer immediately and, when more evidence is needed, which experiment to perform. Current physical reasoning benchmarks usually evaluate only the final answer, so they do not directly measure this decision-making ability. We introduce a controlled evaluation where each problem provides one measurement image and four possible physical worlds created by combining two possible masses and two possible values of another relevant property. The model must either stop and answer or select the cheapest additional experiment that can resolve the question. We construct matched problem pairs where changing either the observed measurement or the question changes the optimal action. Since all possible worlds and experiment costs are known, we can explicitly determine the optimal choice. Across six open models and 144 physical parameter sets, direct responses repeat the same action for 95.1% to 100% of image pairs even when the correct action changes. Brief reasoning improves action switching, but the best model makes both decisions correctly for only 5.9% of image pairs. Additional analysis reveals failures in measurement interpretation, physical reasoning, and response formatting. By evaluating evidence selection separately from final answers, our benchmark reveals limitations in physical reasoning that conventional answer accuracy can overlook.

---


### 44. [BenchShield: Formal Model-Backed Instrumentation for Reward Integrity in LLM-Agent Evaluation Infrastructure](https://arxiv.org/abs/2609.11028)

**<font color=#1a73e8>作者：</font>** Shenghan Zheng, Zonglin Di, Yimin Liu 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LM-agent benchmarks increasingly function as interactive evaluation infrastructure. Agents observe state, call tools, modify workspaces,
submit artifacts, and receive rewards from outcome procedures. This interactivity makes evaluations vulnerable to reward hacking: an agent
improves its measured score by exploiting the reward-relevant trajectory instead of solving the intended task. Existing defenses rely largely
on task-specific patches, prompt instructions, or post-hoc detectors. They do not provide reusable evidence that a concrete run remained
within its intended evaluation boundary. This paper presents BenchShield, a model-backed instrumentation layer for reward integrity in
LLM-agent evaluation. BenchShield grounds detection in a finite lifecycle model of an evaluation's reward-relevant events. Within the
benchmark infrastructure, two complementary analyses operate over this model. A static, phase-aware taint analysis exposes reward-hacking
paths before a run. Its runtime counterpart uses infrastructure-side evidence to attribute concrete agent use and emit evidence-backed claims.
We construct BenchShield Trajectories, a human-labeled corpus of 456 adjudicated trajectories from more than 31,000 public agent runs across
three benchmarks. Compared with an agentic hackability scanner baseline on the same tasks and model, BenchShield improves full-chain recall
from 23-94% to 77-100%, same-vector coverage from 16-56% to 43-78%, and reduces per-task cost by up to 65%. Its runtime analysis achieves 96%
accuracy in detecting reward hacking from infrastructure-side evidence.

---


### 45. [Rebalancing Token Importance in Language Models with TF-IDF Weighted Cross-Entropy Loss](https://arxiv.org/abs/2609.11029)

**<font color=#1a73e8>作者：</font>** Zhijian Li, Stefan Larson, Kevin Leach  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are typically trained under uniform token weighting, which allows frequent and low-information tokens to dominate learning and can increase the tendency to memorize surface-level text spans. To address this, we present an information-weighted cross-entropy loss that rescales token-level contributions using TF-IDF statistics, emphasizing semantically informative tokens while down-weighting ubiquitous ones. Experiments on five decoder-only LLMs ranging from 1.1B to 13B parameters show consistent reductions in memorized substring length while preserving perplexity and downstream task performance. Under LoRA fine-tuning, TF-IDF reduces average substring memorization length by 14% across all five models. Under full-weight fine-tuning on TinyLLaMA 1.1B, the reduction reaches 58%. Our approach is architecture-agnostic and can be incorporated into existing training pipelines with less than 3% computational overhead, offering a lightweight and principled way to mitigate memorization without disrupting standard training dynamics.

---


### 46. [T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks](https://arxiv.org/abs/2609.11042)

**<font color=#1a73e8>作者：</font>** Junyao Yang, Yucheng Shi, Zhongzhi Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agent usage is shifting toward long-horizon tasks such as coding and scientific discovery, among which terminal tasks are especially important. We introduce T1, a Mixture-of-Experts model of 122B total trained with reinforcement learning, operating a real shell in a cloud sandbox for up to 300+ tool-call turns per task, rewarded by executing each task's own verifier. We provide a comprehensive recipe: First, an aggressively warm-started to stabilize actor-critic training, with a dense process reward scoring trajectories by the absolute number of passing verifiers. Second, stable optimization through TITO construction, training on the exact sampled token identifiers with drift repair at turn boundaries, and rollout routing replay, recording the sampler's per-token expert choices at every MoE layer and replaying them during training. Third, fully out-of-distribution training corpus: isolated seeds and synthesized tasks disjoint from Terminal-Bench 2.1 ensures gains reflect genuine capability transfer over benchmark overfitting. Together, TITO and R3 cut the training-to-inference log-probability difference from 0.021 to 0.013, with exactly aligned zero token drift in the loss region. On Terminal-Bench 2.1, our post-train pipeline raises initial base model from 43.8% to T1 with 64.0% resolved. On Long-Horizon Terminal Bench, T1 reaches 27.9% and surpasses GPT-5.4 and GLM-5.1.

---


### 47. [EMMI: Edge Multi-Modal Intelligence for Communication-Efficient MLLM Inference via Fused Representation Compression](https://arxiv.org/abs/2609.11058)

**<font color=#1a73e8>作者：</font>** Motahare Mounesan, Irfan Khan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in multimodal large language mod- els (MLLMs) have opened new opportunities for edge intelligence by enabling reasoning across heterogeneous sensor modalities, such as vision, text, and telemetry data. However, deploying these capabilities on resource-constrained edge platforms remains challenging due to the substantial computational, memory, and communication demands of modern MLLMs. Rather than transmitting raw sensor observations or partitioning neural networks at intermediate layers, Edge Multi-Modal Intelligence (EMMI) communicates a compact representation between edge devices and server resources, enabling communication-efficient edge MLLM inference. To achieve this, EMMI performs modality-specific encoding, cross-modal representation fusion, and learned compression at the edge, transmitting only a compact latent representation to server-side resources for high-capacity MLLM reasoning. This representation-centric design reduces communication overhead, preserves local data privacy, and provides a fixed-size interface between heterogeneous edge devices and server-side MLLMs. Evaluation on a representative multimodal benchmark demonstrates that EMMI can reduce the communication payload by 32x while maintaining comparable downstream accuracy, resulting in up to a 3.4x reduction in estimated end-to-end inference latency under bandwidth-constrained edge conditions.

---


### 48. [Grounding Agent Memory: Environment-Probing Curation for Enterprise Agents](https://arxiv.org/abs/2609.11060)

**<font color=#1a73e8>作者：</font>** Susheel Suresh, Hazel Mak, Sahil Bhatnagar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent memory is entering production-oriented agent platforms to help long-horizon agents accumulate experience across sessions. Yet a post-task curator agent restricted to completed trajectories can preserve errors, overgeneralize partial evidence, or retain stale knowledge. We introduce environment-probing curation, a deployment-compatible extension that gives an existing asynchronous curator agent least-privilege, read-only world tools to check, scope, and refresh candidate memories. It requires no model retraining and leaves the task agent, retriever, memory representation, and production write authority unchanged. In a production-like GitHub Copilot (GHCP) harness built on its SDK, we compare stateless execution, full in-context learning, GHCP + Mem, and GHCP + Mem (w/ Env Probing) on CLBench database exploration and 90 adapted APEX management-consulting tasks. On CLBench, probing raises pass rate from 39% to 73% and pass-discounted reward from 8.60 to 22.60 while reducing queries from 8.8 to 4.7 per question and task-agent cost from \$3.38 to \$1.68. Across six APEX worlds, all 18 memory-versus-baseline mean reward comparisons are positive and task-agent tool calls fall by 16--75%; probing gives the best task-agent reward gain per dollar in five worlds. Probing also attains higher mean reward than GHCP + Mem on both Sonnet 4.6 and Opus 4.7 without schema drift. Environment probing therefore turns existing agent-memory curation into an environment-informed, auditable process while preserving a compact task-time interface.

---


### 49. [Fork Where the Model Changes Its Mind: Belief-Shift Branching for Tree-Structured Reinforcement Learning](https://arxiv.org/abs/2609.11061)

**<font color=#1a73e8>作者：</font>** Bin Lei, Yu Li, Prafulla Kumar Choubey 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tree-structured rollouts give critic-free reinforcement learning with verifiable rewards (RLVR) step-level credit: fork a chain at an intermediate point, and sibling outcome differences estimate step value. Each fork adds sampling cost, so realistic budgets typically allow only a few forks per chain. A fork placed where the outcome is already largely settled yields siblings that mostly agree and provide almost no credit signal; hence, for a given tree size, where forks are placed largely determines how much step-level RL can gain. Most existing mainstream methods place forks by structure, such as fixed lengths, midpoints, and delimiters, or by next-token entropy. We formalize fork placement as locating the \emph{pivots} of the chain's value curve, where the expected outcome turns. We propose \emph{belief-shift branching}: read the model's answer belief at candidate boundaries and fork just before the step where consecutive beliefs diverge most. Three instantiations, none needing step-level supervision, span access levels: a black-box probe, a logit-lens depth profile, and a learned activation direction, which is fit offline and therefore used only in the validation before RL training. The signal only \emph{places} forks, and the probe costs about $1\%$ of step compute on mathematics and under $5\%$ on code when it runs inside the rollout engine. In that validation, against Monte-Carlo value curves, a belief-shift signal ranks first in each of the eight model$\times$benchmark panels, ahead of entropy, structural, and LLM-judge baselines. In RL across three model families and two domains, belief-shift forking leads every mathematics aggregate, on OLMo-3-7B by $+2.6$ aggregate and $+2.9$ on AIME 2026 over the strongest baseline, and sweeps every OLMo code column, by $+6.5$ on LiveCodeBench-medium.

---


### 50. [The information geometry of large language models is shared, learned, and controllable](https://arxiv.org/abs/2609.11063)

**<font color=#1a73e8>作者：</font>** Dario Picozzi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models learn similar behaviours, yet it remains unclear what structure they share or how to change one behaviour without disturbing others. The Fisher-Rao geometry of next-token probabilities connects these questions: behaviour determines this geometry up to output-preserving symmetries, whereas activation geometry depends on coordinates. Across transformer, state-space and recurrent models, output geometries agree more strongly than activation geometries, and shared geometry supports semantic-category transfer. Agreement with human word choices increases with predictive accuracy, scale and training, and improves further after model-only calibration. Token probabilities and read-out geometry jointly predict the spectrum and its effective dimension. Controlled language assignments show that geometry follows the language law across architectures. Pretraining corpus statistics predict held-out fact acquisition without recalibration, while randomised experiments show that deeper evidence substantially delays acquisition across every tested architecture and evidence construction. Finally, the geometry prescribes minimum-disturbance local interventions, predicts their relative cost, and supports reusable control: updates learned on donor prompts transfer to unseen prompts while better preserving behaviour on reference prompts than Euclidean control. The same geometric correction improves steering, editing, attribution, dictionary learning and fine-tuning.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-153](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
