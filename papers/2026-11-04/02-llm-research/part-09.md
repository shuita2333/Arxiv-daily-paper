# 🧠 大模型相关研究 | 2026年11月04日

> 本类共 **515** 篇论文：已确认 **481** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 401. [Action Verification through Conjecture and Refutation for Language Model Agents](https://arxiv.org/abs/2611.02950)

**<font color=#1a73e8>作者：</font>** Minhyeon Oh, Chiyeong Heo, Geonwoo Noh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language model agents increasingly act on users' behalf by manipulating external environments through tools, often from high-level instructions that leave critical task- and environment-specific context unstated. To prevent resulting misaligned actions, recent work verifies proposed actions before execution, largely by establishing whether the conditions supporting them hold. We argue that this confirmation-oriented view leaves a fundamental blind spot: a wrong action often passes every check that asks whether it is right. This motivates a different question for verification: rather than asking what evidence supports an action, can the agent find evidence that refutes it? We pursue this direction with BlackSwan, a refutation-oriented, expect-suspect-test procedure that predicts the intended effect of each state-mutating action, formulates specific and empirically testable hypotheses for how it could be wrong, and tests them using existing observations or additional non-mutating actions, executing the action only if none survives testing. On challenging AppWorld tasks, BlackSwan improves success rate over the strongest baseline by 14.9 and 25.2%p with and without the backbone model's thinking mode, respectively. Even without thinking or in-context demonstrations, it outperforms stronger baselines equipped with them. The gains also transfer beyond AppWorld, with BlackSwan improving WebShop performance by 12.7%p. More broadly, our results suggest that language model agents have an underused capacity to recognize and self-correct misaligned actions, which can be systematically elicited through active conjecture and refutation before execution.

---


### 402. [Cyber-JEV: Matched Contrastive Fine-Tuning of Language Models for Fast Source-Code Vulnerability Triage](https://arxiv.org/abs/2611.02957)

**<font color=#1a73e8>作者：</font>** Zhuyi Zhao, Shengjie Yuan, Shengyu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Single-pass scoring models such as Jev give each code function a vulnerability probability, so that security teams can rank many functions for review without generating written explanations. Training an open-weight model for this task is limited by data. Benchmarks with both vulnerable and non-vulnerable labels keep few vulnerable functions once examples related to the test data are removed, while larger public vulnerability records mostly contain vulnerable functions only. Mixing the two lets the data source predict the label, and training on the labeled data alone leaves a model that often scores a fixed function above its vulnerable original. We present Cyber-JEV, a fine-tuning method that uses fix commits to turn these records into comparison groups. Each group holds a vulnerable function, its patched version and up to two unchanged functions from the same file, so the model sees the change that removed a recorded defect. One shared model learns two tasks: classifying functions from the labeled reference data, and ranking the vulnerable function above the other members of its group. At test time the input is one function and the output is a vulnerability score. On a test benchmark of 7,270 functions, an ensemble of five fine-tuned Qwen3.5-4B models reaches an area under the receiver operating characteristic curve of 0.814, compared with 0.743 for Jev 1.13. With the 4,031 alerts of Jev as the review budget, it misses 16 of 322 vulnerable functions instead of 39. Compared with training on the reference data alone, it ranks the vulnerable version above the patched version 14.8 to 29.2 percentage points more often on three sets of real fixes. Such scores can order the changed functions of a pull request or a release for review under a fixed budget.

---


### 403. [SHq: Learnable Grids for LLM Weight Quantization](https://arxiv.org/abs/2611.02966)

**<font color=#1a73e8>作者：</font>** Michael Helcig, Earl Killian, Dan Alistarh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Block-scaled lookup-table (LUT) formats, which represent weights as indices into a small value set (the grid), have become standard for low-bit LLM quantization, ranging from NF4 and BOF4 to the 3-bit LUT instruction in NVIDIA Rubin. While these formats leave the grid definition flexible, existing implementations rely on fixed grids derived either from numerical data types (INT, FP) or assumed weight distributions (NF, BOF). We demonstrate that no single fixed grid is universally optimal; the best fixed grid varies with bit-width: BOFS at 2 bits, NF at 4 and 5 bits, and INT at 6 bits. We introduce SHq, a closed-form family of grids parameterized by two critical degrees of freedom: a companding strength {\alpha} that interpolates level spacing from uniform to floating-point-like, and an offset c that introduces asymmetry. This offset allows the sign bit of the FP8 block scale, otherwise unused, to select between the grid and its mirror image, up to doubling the number of distinct values available per block. SHq modifies only the lookup table contents and serves as a drop-in replacement for the grid in any such format. Across five models ranging from 3B to 35B parameters, including a mixture-of-experts architecture, evaluated at 2-6 bits using RTN and GPTQ, SHq achieves the lowest KL divergence in every setting at 3 and 4 bits and in most settings at 2, 5 and 6 bits. It outperforms the best fixed grid by up to 34% and remains superior under mixed-precision configurations. At 4.5 bits per weight, the SHq format reduces the KL divergence of NVFP4 by 41-67% while improving downstream accuracy. Grid families incorporating both spacing and offset parameters perform comparably, whereas those lacking an offset exhibit clearly higher error, confirming that these two degrees of freedom drive the observed gains. We therefore propose SHq as the standard grid for block-scaled lookup-table formats.

---


### 404. [CAREFUL-Bench: Effect-Aware, Judge-Free Evaluation of Multi-Turn LLM Function Calling](https://arxiv.org/abs/2611.02978)

**<font color=#1a73e8>作者：</font>** Alexander Kovalenko, Artem Redchych  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The multi-turn checker of the Berkeley Function Calling Leaderboard (BFCL) evaluates final state correctness but ignores the effects of intermediate calls: extra calls are free, function documentation does not describe side effects, and the scripted user never responds to proposals. Consequently, models asking for confirmation before destructive actions are penalized; 260 of 734 reference turns in the base category perform destructive actions without confirmation. We make BFCL effect-aware without replacing it. We infer effect declarations for all 128 functions by executing them in BFCL simulators and comparing state changes, with destructive writes identified by three annotators. A judge-free replay scorer reproduces official results across all 800 reference trajectories while reporting unrequested destructive calls, duplicate writes, redundant reads, surplus steps, and their token costs. We also introduce a confirmation-aware protocol with a deterministic simulated user. Across 11 open models, effect-aware scoring preserves the official ranking but reveals substantial differences in execution quality: the leading model loses 14.0 points due to unrequested destructive calls, while surplus steps consume up to 28% of input tokens. Adding effect hints to function documentation has no impact on eight evaluated models. Allowing the simulated user to respond recovers up to four points for models that seek confirmation. However, the best model completes only six of 576 conversations requiring destructive actions with explicit confirmation. These results expose a key limitation of current function-calling benchmarks: they cannot distinguish between asking for clarification and obtaining permission before potentially destructive actions.

---


### 405. [Distilling Literary Sentiment from LLM Annotations into an Ordinal BERT Model](https://arxiv.org/abs/2611.02985)

**<font color=#1a73e8>作者：</font>** Artem Suslov, Takehiro Hashimoto  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The scarcity of human-annotated literary corpora limits the development of domain-specific sentiment analysis models. This study investigates whether LLM-generated annotations can supervise smaller models for literary sentiment analysis. We fine-tune five BERT models using ordinal regression on 10,889 literary sentences annotated by Gemma 4 31B on a ten-point sentiment scale. The models are evaluated against 1,923 human-annotated sentences from Hemingway's "The Old Man and the Sea", alongside the teacher model and conventional baselines.
BERT-large achieves a Kendall's $\tau$ of 0.589, approaching the teacher's 0.604. Although a constant-neutral predictor achieves the lowest overall mean absolute error (MAE), BERT-base outperforms the teacher on non-neutral sentences, achieving an MAE of 0.726 versus 1.116. These findings demonstrate the potential of LLM-generated supervision for developing smaller literary sentiment models, while highlighting the limitations of aggregate error metrics on predominantly neutral datasets.

---


### 406. [Can You Predict the Next Mind? Toward Multi-Turn Multi-Party Mental World Modeling](https://arxiv.org/abs/2611.02988)

**<font color=#1a73e8>作者：</font>** Jiahao Huang, Zheng Lian  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While multimodal foundation models have achieved remarkable progress in physical world modeling, generation, and embodied reasoning, their capacity for dynamic mental world modeling remains underexplored. Existing benchmarks predominantly focus on static mental state perception or short-horizon decision-making, overlooking the dynamic mental trajectories inherent in multi-party, multi-turn interactions. To bridge this gap, we introduce M$^3$WME-Bench, a benchmark designed to evaluate mental world modeling conditioned on the evolving actions of interactants. Specifically, models are tasked with forecasting a target subject's future mental states and behaviors over extended social interactions. In addition to the benchmark suite, we construct M$^3$WME-23K, a dedicated training dataset, and establish a competitive baseline named MindNext-7B. Extensive evaluations across four representative paradigms (general MLLMs, emotion-specialized MLLMs, agentic frameworks, and World Foundation Models) reveal that current systems consistently struggle to anticipate forward-looking mental states. Mechanistic analyses further reveal that existing architectures fundamentally lack forward mental state transition dynamics. Our findings highlight a pivotal challenge in advancing agents from physical to mental world modeling, charting new directions for socially adaptive AI.

---


### 407. [Finding Errors Is Not Enough: Selective Model Escalation for Entity-Targeted Sentiment Analysis](https://arxiv.org/abs/2611.02989)

**<font color=#1a73e8>作者：</font>** Nishan Chatterjee, Matthew Purver, Antoine Doucet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Improving a sentiment classifier with limited resources involves more than simply deciding how much data to collect or which model to train. A labelled collection may lack examples of an important class. Once trained, a classifier may benefit from another model even when that model is weaker on its own. We study these decisions in document-level Entity-Level Sentiment Analysis (ELSA), primarily using South Slavic news. We first compare acquisition orders as collections grow. We then use uncertainty to choose which predictions to revisit, how many to process, and whether an alternative encoder or local LLM can correct them. Finally, we select complete routing policies on development data for held-out evaluation. Minority-prioritised acquisition helps at some very small training sizes, but not consistently thereafter. On SentiCoref, an oracle correcting all errors in the least-confident 10% without harming correct predictions would add 9.14 Macro-F1 points; however the best evaluated action gains only 0.90. Encoder averaging helps on AspectBench and NewsMTSC but harms SentiCoref, where selective LLM assistance is more promising. Both development-selected policies route 30% of records to the encoder-assisted LLM, yielding observed gains of 1.02 points on SentiCoref (interval includes zero) and 1.71 on NewsMTSC, at substantially different inference costs.

---


### 408. [BLPO: Beyond-Local Policy Optimization for Long-Horizon LLM Agents](https://arxiv.org/abs/2611.03005)

**<font color=#1a73e8>作者：</font>** Xuanren Chen, Chongyang Tao, Wenpeng Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon tasks require large language model (LLM) agents to coordinate interdependent actions, a capability central to automating complex workflows. Stepwise group-based reinforcement learning provides finer credit than trajectory-level supervision, but reliable comparisons must account for differences in interaction history. Enforcing this consistency within the limited rollouts of each task can leave insufficient support for estimating action preferences. We propose Beyond-Local Policy Optimization (BLPO), which estimates task-progress advantages from experience shared across tasks and training updates. We summarize trajectory prefixes into task-progress states and abstract actions by their function, allowing corresponding decisions from different tasks to contribute to shared estimates. To control bias and noise from heterogeneous tasks, we accumulate context-relative returns in a global memory with balanced aggregation and reliability weighting. These global advantages complement local comparisons over normalized actions and trajectory-level credit without a learned critic or additional rollouts. Experiments on ALFWorld and WebShop with 1.5B and 7B policies show improved task success over the evaluated baselines under matched training budgets. Further analyses show faster learning and shorter trajectories with little computational overhead.

---


### 409. [Q-CamTuning: A Multimodal Large Language Model for Fine-Grained Quality Reasoning in Livestreaming Camera Tuning](https://arxiv.org/abs/2611.03007)

**<font color=#1a73e8>作者：</font>** Yanchao Bi, Pengfei Chen, Yulong Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the popularization of livestreaming applications, automatic camera tuning has become indispensable for ordinary users to enjoy high Quality of Experience (QoE). However, the existing Image Quality Assessment (IQA) methods face two challenges in camera tuning. First, they struggle to identify subtle quality difference between images, which is common in camera tuning. Second, the ability to explain fine-grained differences and to provide suggestions for camera tuning are even more lacking. To address these challenges, we first construct FGLive-Comments, an instruction tuning dataset with rich annotations of both preferences for fine-grained image pairs and quality reasoning from global and local visual evidence, which supports selective adjustment recommendations of camera parameters. Based on FGLive-Comments, we develop Q-CamTuning, a multimodal large language model for livestreaming camera tuning. Its progressive perception-evidence-guidance framework learns quality-aware visual representations, enhances fine-grained reasoning with global-local evidence, and maps quality issues to camera-parameter adjustment directions. Extensive experimental results demonstrate that Q-CamTuning outperforms existing IQA models in both quality scoring and fine-grained image pair ranking. User study also validates its ability to recommend camera tuning suggestions.

---


### 410. [VizDAGuide: Misleading Chart Question Answering in Compact Vision Language Models via DAG-Structured Supervision](https://arxiv.org/abs/2611.03023)

**<font color=#1a73e8>作者：</font>** Haiyang Zhang, Sicheng Song, Zixin Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Misleading charts can lead vision-language models to conclusions that conflict with underlying data. Existing work focuses on inference-time strategies, while training-time supervision remains less explored. We present VizDAGuide, a DAG-structured supervision method for misleading-chart question answering. The method represents intermediate reasoning states and their dependencies as a directed acyclic graph, assigns supervision weights according to their roles, and serializes the graph into a unified training target for open-ended and multiple-choice QA with single-pass inference. Experiments on two benchmarks across Qwen3-VL and InternVL3.5 models show improvements over a content- and weight-matched Linear CoT-SFT baseline on both answer formats. Process-level evaluation shows gains in grounding and operation execution, while ablations indicate that dependency structure and weighted supervision are most effective when combined. These results support DAG-structured weighted supervision for misleading-chart question answering.

---


### 411. [VLM-as-a-Judge for Person Re-Identification](https://arxiv.org/abs/2611.03027)

**<font color=#1a73e8>作者：</font>** Bessie Dominguez-Dager, Miguel Cazorla, Vincent Lepetit  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cloth-changing person re-identification (CC-ReID) is still very challenging, and no method clearly dominates: methods that lead on one benchmark collapse on the others, because they rest on different identity cues. We show that a general-purpose vision-language model (VLM), used zero-shot as a judge for reranking a short candidate list, beats the expert retrieval models it reranks by a wide and consistent margin. On the four scenarios of CHIRLA, a long-term CC-ReID benchmark that no publicly released Re-ID model is trained on, reranking the candidates of two frozen experts raises rank-1 on every scenario, by 12.9 points on average over the best expert and 9.4 over the best naive ensemble of the two, with no component fine-tuned on the target data. Merging both experts' shortlists matches or beats reranking the stronger expert's shortlist alone, at lower cost. Introducing a VLM does, however, come at a cost: almost all of the pipeline's FLOPs are spent on it. We therefore borrow a criterion from ensembling and invoke the VLM judge only where the two experts disagree at rank 1. This threshold-free gate removes 40% of the calls, and a comparable share of total compute, with no significant drop in rank-1, trading 1.8 to 3.8 points of mAP. Judging remains the dominant cost, but on a benchmark where dedicated experts stall, we find a frozen general-purpose model to be the strongest judge of identity. The code is available at this https URL.

---


### 412. [VERS: Steering Reasoning Models by Editing Their Activation Explanations](https://arxiv.org/abs/2611.03040)

**<font color=#1a73e8>作者：</font>** Ihor Vitenko  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning language models write a chain of thought before they answer, and many checks in it do not change the final answer. Natural language autoencoders (NLAs) explain a model's activations in text and rebuild activations from text, and editing an explanation can steer a model at a single token. We study whether such edits can also steer how a model reasons. We build VERS (Verbalize, Edit, Reconstruct, Steer): it turns explanation edits at the doubt points of one reasoning trace into one fixed direction, and adds this direction at paragraph breaks. On the full GSM8K test, VERS cuts generated tokens by 45.8% at an accuracy change of -0.82 percentage points (pp); on MATH-500 it saves 31.3% at -3.05 pp. At half strength, its trade-off between tokens and accuracy lies between those of the published methods SEAL and DEER. With fitted affine maps and a strength tuned for each model, the direction transfers to larger Qwen3 models, up to 235B-A22B, and saves 30-35% of tokens. On competition problems, however, VERS loses 3-7 pp at every model size, and a fixed direction did not separate necessary checks from unneeded ones.

---


### 413. [VideoEditor-MoE: Scaling Complex Video Editing with Mixture of Experts](https://arxiv.org/abs/2611.03043)

**<font color=#1a73e8>作者：</font>** Xiao Cao, Fuchen Long, Yansong Qu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Complex video editing requires understanding complex instructions while jointly fulfilling multiple editing requests. Meeting these demands through dense model scaling substantially increases computational cost. We introduce VideoEditor-MoE, the first open-source mixture-of-experts framework for video editing. Beyond sparse MLP-MoE layers, MoE-Attention expands attention capacity through routed key--value experts while preserving global interactions among video tokens. Initialized from a 5B video editing model, VideoEditor-MoE scales to 14B and 56B parameters, with approximately 8B parameters activated per token in both variants. Comparisons with existing methods and two complementary baselines, Explicit-MoE and MLP-MoE, assess its benefits over explicit expert guidance and MLP-only expert architectures. Further analyses demonstrate that all experts remain active and reveal that learned routing responds more strongly to sample content and diffusion noise levels than to human-defined editing categories. Spatial analysis further indicates sensitivity to object-level semantic features. We also identify decoupled weight decay as a strategy for stabilizing expert scaling.

---


### 414. [Unlocking Criminal Court Decisions: Flexible Information Extraction for Empirical Legal Research](https://arxiv.org/abs/2611.03051)

**<font color=#1a73e8>作者：</font>** Tomáš Knap, Ivana Kvapilíková, Jan Černý 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Criminal verdicts contain descriptions of criminal behavior that can support quantitative legal research, but structuring them requires attributes and extraction rules that cannot always be fully specified in advance. We present an LLM-based pipeline that builds a structured dataset through attribute exploration, text span extraction, and value normalization, guided by annotation instructions that legal experts can refine. We evaluate it on two traffic offenses: driving under the influence (DUI) and driving despite a ban (DDB). For DUI, revising the instructions was associated with higher extraction accuracy (from 52% to 70% of correctly extracted values) and higher agreement between human annotators. Repeated runs of the same model agreed with each other more than with the gold annotations, showing that consistent output is not necessarily correct, while disagreement between annotators and between models helped reveal unclear instructions. For DDB, where the instructions defined fixed categories and output formats, agreement was high for most attributes.

---


### 415. [PRIME: Predictive Routing of Interventions by Modeling Effects for Scientific Ideation](https://arxiv.org/abs/2611.03055)

**<font color=#1a73e8>作者：</font>** Fengxian Ji, Xie Yu, Zhexuan Cui 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Feedback-driven iteration is widely used to improve LLM-generated scientific ideas, but existing systems either leave revision decisions implicit in generation, align revisions with feedback-localized weaknesses, or restrict action selection to system-specific operations. This is problematic because problems, hypotheses, and solutions are interdependent: the location where a weakness manifests does not itself determine the revision scope that will produce a better successor. We term this phenomenon diagnosis-intervention mismatch. We introduce Predictive Routing of Interventions by Modeling Effects (PRIME), a plug-and-play feedback-to-revision decision layer for existing scientific ideators. PRIME operates in three stages: (1) Structural Attribution interprets feedback over the problem-hypothesis-solution structure without fixing a revision target; (2) Counterfactual Routing constructs alternative scope-conditioned interventions and compares their projected successor utility and risks through lightweight rollouts; and (3) Intervention Execution compiles the selected intervention into an ordered generator-facing plan with semantic actions, preservation constraints, and dependency requirements for successor generation. We validate diagnosis intervention mismatch on 112 human-annotated idea-feedback pairs. Across four benchmarks, two ideators, and fixed- and open-problem settings, PRIME improves successor quality and routing reliability over strong baselines; removing counterfactual routing reduces quality from 3.463 to 1.960 and increases route regret from 0.426 to 1.929, confirming cross-scope effect modeling as the primary source of its gains.

---


### 416. [Towards a Trustworthy and Governable Internet of Agentics: An Architectural Perspective on Protocols, Systems, and Services](https://arxiv.org/abs/2611.03066)

**<font color=#1a73e8>作者：</font>** Haoyi Xiong, Yi Liu, Jiang Bian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model applications are increasingly being organized as tool-using and multi-agent workflows rather than as isolated chat interfaces. This perspective paper examines the architectural problem that follows from that shift: agents may reason, invoke tools, and delegate work, but dependable deployment still requires interoperability across frameworks, runtimes, data boundaries, and organizational control domains. We study this problem through the lens of the \emph{Internet of Agentics} (IoA), an emerging service-computing view in which heterogeneous agents are treated as governable service participants rather than only as stand-alone model endpoints. The paper organizes the landscape as a three-layer progression: from today's fragmented agent ecosystem, to interoperable agents, and ultimately to trustworthy and governable autonomy. First, it examines the protocol stack centered on the Agentic AI Foundation, including MCP for agent--tool interaction; A2A for agent--agent coordination; this http URL and Skills-style procedural manifests; and discovery, transport, and trust mechanisms such as AGNTCY and SLIM. Second, it reviews the systems abstractions that make agents deployable as service components, including logical agent architectures, orchestration patterns, gateways, registries, runtime control loops, and hardware-aware inference infrastructure. Third, it situates these developments within services computing, arguing that agentic systems reinterpret classical concerns from SOA and microservices---discovery, composition, governance, pricing, and trust---at the level of cognitive capabilities rather than deterministic functions.

---


### 417. [VL-Dedup: Graded Multimodal Entity Resolution for Image-Text Data Deduplication](https://arxiv.org/abs/2611.03080)

**<font color=#1a73e8>作者：</font>** Zhenxi Liu, Guanze Chen, Dehui Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-text corpora contain copies of one image, captions that describe one image in different ways, captions reused for different images, and captions that do not match their images. Each case calls for a different curation action. Deduplication and multimodal entity resolution (ER) only decide whether records are the same, and they are evaluated on labeled pairs. Yet pair scores do not tell which records end up in the same cluster or which useful captions get deleted. We therefore formulate image-text deduplication as graded multimodal ER, which decides visual identity, caption handling, and mismatches for each pair, and we evaluate it at three levels: pairs, clusters, and the retained set. Our method, VL-Dedup, groups records of the same visual entity into clusters and caps the size of each cluster. Within each cluster, a vision-language model (VLM) and CLIPScore decide which captions to keep and which to flag. We also build VL-DedupBench, with 50,000 COCO and SOP records and 66,788 labeled pairs. On it, a classifier that selects no false edge among the labeled pairs still joins millions of record pairs from different entities. Spending VLM calls on the pairs inside clusters, rather than on pairs with uncertain scores, gives better caption decisions from the same model. Even when almost all clusters are correct, keeping one record per cluster loses facts in many deletions, while the deletions of VL-Dedup lose much less information.

---


### 418. [An Experimental Study of Hybrid Retrieval, NLI and Open-source LLMs for Scientific Claim Verification](https://arxiv.org/abs/2611.03093)

**<font color=#1a73e8>作者：</font>** Lakshmi Narayanan P, Narenkarthik K, Naren Kumar C  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Claim verification is the task of deciding whether a source text supports a claim, contradicts it, or lacks sufficient evidence. Natural Language Inference (NLI) models can judge whether a single sentence supports or contradicts a claim, but they struggle when the evidence is spread across several sentences. Conversely, Large Language Models (LLMs) can reason across sentences, but may draw conclusions the text does not support. In this experimental study, we test whether a conservative fusion rule, labeling a claim Support or Contradict only when both models agree and defaulting to Not Enough Evidence otherwise, combines their strengths. We construct a benchmark of 2,035 claims from SciFact and CliniFact (858 Support, 152 Contradict, 1,025 Not Enough Evidence). We retrieve the top five most relevant sentences per claim using a hybrid of semantic and lexical (BM25) retrieval, which slightly outperforms either method alone. These retrieved sentences are then provided to every verification model. We then compare a DeBERTa-v3-base-mnli-fever-anli NLI baseline against Llama 3.1 8B, Qwen3 8B, and Mistral 7B. Qwen3 achieves the highest Macro-F1 (0.7937), followed by Llama 3.1 (0.7204) and Mistral (0.6388), while the NLI baseline reaches only 0.3157. Contrary to our hypothesis, fusion degrades performance, dropping Macro-F1 to 0.7392, 0.6730, and 0.5991, respectively. To understand this decline, we analyze agreements, disagreements, and common error patterns between the NLI and LLM verifiers. Our error analysis shows that NLI and LLM disagreements often result in correct LLM predictions being overturned.

---


### 419. [A Fine-Grained Hierarchy and Benchmark for State Tracking in Language Models](https://arxiv.org/abs/2611.03094)

**<font color=#1a73e8>作者：</font>** Jackson Petty, William Merrill, Ashish Sabharwal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Theoretical limitations of transformers on state tracking---the ability to track information about entities or variables over long contexts---have motivated new recurrent language modeling (LM) architectures such as Gated DeltaNet (GDN). These architectures have, in particular, been benchmarked against the $S_5$ word problem, a theoretically hard state-tracking task that captures abilities such as code evaluation under arbitrary variable assignment. It, however, remains open whether other, simpler forms of state tracking might both be more relevant in practice and already explain observed differences between these architectures. We propose evaluating state tracking using a hierarchy of word problems with four increasing levels of difficulty: r-trivial, corresponding to immutable assignment to variables in programming; aperiodic, where assignments are mutable; soluble, where assignments are self-referential; and general finite state tracking. Theoretically, we show that the class of problems transformers are thought to length-generalize on does not even contain all aperiodic state tracking. On the other hand, we prove that GDN with positive eigenvalues expresses all aperiodic problems, and the regular languages recognized by certain transformers are precisely all soluble ones, thus providing a fine-grained picture of state tracking capabilities of various architectures. Taking these ideas to practice, we construct StateBench, a 4-tier long-horizon state-tracking benchmark. Our systematic direct training experiments across architectures largely align with theoretical expectation, albeit with interesting observations at very large scale length-generalization. Additionally, we also evaluate pretrained models---both open hybrid and closed frontier ones---on StateBench, finding that none of them robustly solves even soluble state tracking, suggesting a direction for future improvement.

---


### 420. [DR Pixel: Page-Native Deep Research with Vision-Language Models](https://arxiv.org/abs/2611.03097)

**<font color=#1a73e8>作者：</font>** Tiansheng Hu, Yichuan Wang, James V. Talwar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Complex documents such as scientific papers contain rich information in tables, figures, and equations; however, existing deep research (DR) agents typically reduce papers to OCR-extracted text. We instead ask whether vision-language models (VLMs) can enable page-native deep research: directly retrieving and reasoning over rendered document page images. We introduce DR Pixel, the first open-source end-to-end multimodal DR agent that uses rendered page images as its sole retrieval and reasoning unit, operating over a corpus of 1.06M pages. To evaluate this setting, we construct DRPixelBench, a benchmark on scientific papers requiring reasoning over text, figures, tables, and equations. Surprisingly, page-native DR already works well without training, outperforming OCR-based baselines across state-of-the-art models like GPT-5.4, Gemini-3.5-Flash, and Qwen3.6-27B, while requiring fewer tool calls. We next turn to DR training. A key challenge is that teacher trajectories for agentic supervised finetuning are noisy, mixing critical reasoning and action steps with redundant or failed attempts. To address this, we introduce counterfactual credit reweighting, a fine-grained credit assignment method that weights individual reasoning and action steps by their counterfactual contribution to the final answer. Our training improves retrieval recall by about 15 points and final accuracy by over 10 points on DRPixelBench, and likewise outperforms the untrained baseline on four existing benchmarks. On out-of-distribution ViDoRe-V3, DR Pixel comes within 1.8 points of an oracle that is given the gold pages directly. Our results suggest that the conventional OCR-then-retrieve pipeline is not only unnecessary but suboptimal: directly retrieving and reasoning over visual document pages makes complex DR both more effective and more efficient.

---


### 421. [LUCA: A Synthetic World for Experimental Reasoning](https://arxiv.org/abs/2611.03100)

**<font color=#1a73e8>作者：</font>** Anna Gogleva, Thomas Charman, Martin Balla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An experimental agent can succeed for the wrong reasons. Evaluations, however, often focus on the outcome, not the experiments, evidence, and inferences that produced it. We introduce LUCA, a configurable synthetic world for evaluating this process under fully known ground truth. Agents learn unknown regulatory systems through budgeted experimentation, then predict unseen interventions, diagnose hidden faults, and attempt rescues. This setup allows us to evaluate experiment selection, prediction, diagnosis, and intervention separately.
Across seven frontier LLMs and three baselines, these capabilities dissociate sharply. Agents frequently rescue malfunctioning systems while diagnosing the wrong fault; diagnosis varies 7x across models while prediction varies only 1.4x. Models also adopt surprisingly different experimental strategies, and greater exploration does not reliably yield better performance. In one failure mode, agents often perform the experiment needed to distinguish competing causes, but still fail to use the resulting evidence. LUCA turns these hidden failures into measurable behaviours, providing a controlled environment to study where experimental agents succeed and fail. Code: this https URL.

---


### 422. [Diagonal Equivalence in State Space Models: Characterization, Retrieval Rank, and Selective Extensions](https://arxiv.org/abs/2611.03101)

**<font color=#1a73e8>作者：</font>** Dennis Rochau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We classify real and complex state-space models (SSMs) with linear transitions, distinguishing fixed-basis diagonal equivalence from input-output equivalence and tracking coefficient-conditioning windows under coordinate changes. We characterize diagonal equivalence through commuting transition families whose members are diagonalizable over the chosen field. With time-shared token-local matrix maps, we identify this class's state-mediated kernels with unnormalized scalar-mode linear attention with multiplicative masks. Mamba 3's multiple-input, multiple-output (MIMO) construction lifts one value per local interface; SSD-MIMO routes independent values for local retrieval rank above one. HybridMamba combines Mamba 1's per-coordinate decay, Mamba 2-style heads and Mamba 3's complex rotations and two-endpoint writes, mixing real and rotating state blocks with different decay laws. They recover Mamba 1-3 single-input, single-output (SISO) configurations as exact special cases. On five large H100 bfloat16 workloads, our fused GPU kernels improve geometric-mean training time over official Mamba 1/3 in matched SISO recoveries, with Mamba 2 near parity at SSM-core scope. Memory tradeoffs depend on the baseline and metric: saved-for-backward versus peak allocation. In small-model multi-token recall experiments, both designs outperform Mamba 1-3 on the hardest tier; higher routing ranks perform best in gated or phase-diverse configurations. In single-seed language models with about 500M parameters, both improve on Mamba 1/2 in test loss at 2B tokens, but the routing gains do not translate into lower language-model loss. Our best configurations approach Mamba 3 SISO through 10B tokens while remaining behind it and Mamba 3 MIMO in language-model loss.

---


### 423. [From Local Skills to Long-Horizon Web Tasks: Progressive Skill Exploration for LLM Web Agents](https://arxiv.org/abs/2611.03116)

**<font color=#1a73e8>作者：</font>** Xueyang Feng, Xiaohe Bo, Xu Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are driving autonomous agents toward real-world environments, with the Web emerging as one of the most representative interaction scenarios. However, training Web agents with naive exploration remains challenging: successful trajectories are rare, and the sparse terminal rewards make it difficult for agents to obtain useful feedback from failed trajectories. Inspired by skill acquisition theory, we propose Skill-Composed Progressive Exploration (SCOPE), a short-to-long learning framework for long-horizon Web agents that decomposes complex task exploration into a gradual expansion process from local skills to complete task-solving capability. Specifically, SCOPE iteratively explores around local skills: Skill Discovery extracts reusable local skills and failure experiences from historical rollouts; Skill Orchestration composes discovered skills into high-level skill chains; and Skill Expansion leverages failure experiences aligned with the current skill chain to guide the agent toward exploring new subskills. Through this process, SCOPE progressively constructs task-completing skill chains across rollouts and internalizes them into the policy parameters through agentic on-policy distillation. Extensive experiments on WebArena, WebVoyager, and WebShop show that SCOPE consistently improves exploration dynamics and achieves 3.9% to 18.6% relative gains over the strongest baselines in each setting.

---


### 424. [SurgPace: Complexity-Aware Progressive Distillation for Surgical Multimodal Large Language Models](https://arxiv.org/abs/2611.03125)

**<font color=#1a73e8>作者：</font>** Zhicheng He, Xiaohan Xing, Hongqiu Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have shown strong potential in robotic surgery for question answering, scene understanding, and grounded assistance, but their high computational cost limits real clinical deployment. Knowledge distillation provides a practical way to build compact surgical MLLMs, yet direct distillation is not well suited to surgical data because surgical samples vary greatly in difficulty, visual ambiguity, and required clinical context, making uniform teacher-student transfer unstable. In addition, the role of supervision changes during training: early stages require stronger teacher guidance for multimodal alignment, while later stages rely more on task supervision for effective optimization. To address these challenges, we propose SurgPace, a complexity-aware continuous curriculum framework for progressive distillation of surgical vision-language models. SurgPace estimates sample complexity using predictive confidence and Lorentz geometric consistency, and uses the fused score to guide a continuous easy-to-hard training process. We further introduce hierarchical representation alignment, which aligns the student with the teacher at the feature, logit, and probability levels, while gradually shifting the training focus from teacher imitation to task supervision. This design separates sample-level curriculum from objective-level scheduling, leading to more stable and effective distillation. We evaluate SurgPace on Surg-396K, a benchmark built from four public surgical datasets and covering five dialogue paradigms. SurgPace consistently outperforms strong MLLM distillation baselines, demonstrating its effectiveness for building compact, memory-efficient surgical MLLMs with faster decoding under controlled benchmarks. Code is available at this https URL.

---


### 425. [CUA-Master: Scaling Computer-use Agents through Open-World Recursive Improvements](https://arxiv.org/abs/2611.03126)

**<font color=#1a73e8>作者：</font>** Xinlei Yu, Gen Li, Ji Zhao 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite recent advances in CUAs, their development remains constrained by the limited diversity, controllability, and reliability of interaction data. Moreover, conventional optimization pipelines lack iterative feedback, while existing recursive improvement approaches often rely on self-generated experiences, limiting ability expansion and yielding diminishing returns. To address these challenges, we introduce CUA-Master, a nested double-loop recursive improvement framework. At the system level, an outer world-data-model flywheel continuously incorporates open-world corpus and leverages evolving model weaknesses to guide subsequent data construction and optimization iterations. At the data level, an inner flywheel couples open-world seeding and autocatalytic propagation. The former mines authentic workflows as seed tasks from instructional videos, and employs visual-semantic dual-path trajectory reconstruction; The latter transforms these seeds into reusable primitives for controllable synthesis of diverse, complex, and verifiable tasks. To enable efficient and reliable trajectory collection, we further introduce a feedback-guided snapshot-rollback retry mechanism in various real environments. Extensive experiments demonstrate that CUA-Master-27B achieves competitive performance across GUI-only and GUI-CLI hybrid benchmarks, scoring 80.2 on OSWorld Verified, 36.9 on OSWorld 2.0, 43.9 on WeaveBench, and 25.0 on Agents' Last Exam. Our framework also substantially improves the quality and efficiency of data synthesis, and exhibits continuous gains across recursive iterations.

---


### 426. [Behavioral Affinity Transduction for Zero-Shot Vision-Language Classification](https://arxiv.org/abs/2611.03132)

**<font color=#1a73e8>作者：</font>** Junxi Huang, Wenshuo Chen, Xiucheng Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An image that is hard to classify on its own may have a helpful neighbor in the same unlabeled batch. Zero-shot vision-language models (VLMs) score images independently and leave this evidence unused. We study small unlabeled query batches with no labeled examples. Visual similarity can reflect pose or background, so it may connect images from different classes. Each image's scores over the class vocabulary offer another way to choose neighbors. We introduce Behavioral Affinity Transduction (BAT), which builds a sparse graph from these class-response profiles. The graph supplies neighbor evidence during prediction. For EM-Dirichlet, it also screens candidate classes and initializes assignments. BAT plugs into direct and iterative readouts of a frozen VLM. Across diverse datasets, BAT improves the mean accuracy of every tested readout. In the main RN50 comparison, soft and hard EM-Dirichlet gain $4.22$ and $2.72$ percentage points.

---


### 427. [Meet Students Where They Are: Student-Prefix Teacher Adaptation for On-Policy Distillation](https://arxiv.org/abs/2611.03133)

**<font color=#1a73e8>作者：</font>** Xue Zhang, Songming Zhang, Yunlong Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) mitigates the student's exposure bias by optimizing on student-generated trajectories. However, student-generated prefixes may contain reasoning errors or follow patterns unfamiliar to the teacher, undermining the reliability of its token-level supervision. This degradation becomes more pronounced as prefixes grow longer. To address this teacher-side distribution mismatch, we propose Student-Prefix Teacher Adaptation (SPTA), which adapts the teacher to the states on which it is queried during distillation. Specifically, before OPD starts, we collect student rollout prefixes with random lengths and continually train the teacher to continue from the prefixes using reinforcement learning with verifiable rewards (RLVR). By treating each prefix as context and rewarding correct final answers, the teacher learns to recover from student-induced states rather than imitate the student's reasoning. Then, the adapted teacher is used for standard OPD, with no changes to the distillation objective. Experiments on mathematical reasoning benchmarks show that our SPTA improves average student performance over standard OPD and OPD with task-level RLVR-adapted teachers. These results highlight the importance of adapting teachers not only to solve problems independently, but also to provide reliable guidance on the states their students actually visit.

---


### 428. [DepthGraft: Structural Regularization through Hierarchical Cross-Layer KV Reconstruction](https://arxiv.org/abs/2611.03142)

**<font color=#1a73e8>作者：</font>** Xiaohan Qin, Xiangdong Zhang, Yu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scaling depth is a key route to stronger large language models, but Pre-LN architectures often suffer from depth-wise information dilution, limiting the effective use of deep layers. While cross-layer connectivity has proven effective at mitigating this problem, existing designs usually introduce additional computation or memory access. We revisit cross-layer KV sharing as an efficient form of such connectivity. Beyond cache compression, each KV reuse edge creates a direct gradient path from deep layers to source KV projections, turning KV sharing into an implicit structural regularizer for KV representation geometry. We provide a systematic analysis of this mechanism, showing that proper sharing topologies sharpen key retrieval directions while enriching the value content subspace, whereas existing adjacent or global-anchor designs do not fully exploit this effect. Motivated by this, we propose DepthGraft, a hierarchical KV-sharing architecture that reconstructs deep-layer KV from stride-aligned shallow-middle source pairs. DepthGraft distributes non-local gradient flow across source layers, while preserving prefill early completion and reducing KV cache by roughly one third. Experiments on dense and MoE models from 0.5B to 16B parameters show consistent downstream improvements under both GQA and MLA. Notably, on the 16B MoE model, DepthGraft achieves a 7.0% absolute improvement on MMLU-Pro, along with gains of 6.6% on CMMLU and 6.4% on C3. These results validate the potential of DepthGraft as a scalable design for large-scale pretraining. The project page is available at this https URL.

---


### 429. [Controlling Sharpening in LLM Post-Training](https://arxiv.org/abs/2611.03146)

**<font color=#1a73e8>作者：</font>** Simon Matrenok, Nicolas Menet, Nicolas Flammarion 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM post-training via reinforcement learning has shown consistent improvements in accuracy at the cost of reducing behavioral coverage - a phenomenon known as sharpening that can stall progress on difficult tasks. Repeated sampling objectives such as $\mathrm{pass@k}$ and $\mathrm{max@k}$ are known to mitigate sharpening, but the mechanism behind it remains poorly understood. Moreover, existing approaches for $\mathrm{@k}$ optimization use dedicated algorithms, and no general framework exists for adapting established policy optimization methods from $\mathrm{@}1$ to $\mathrm{@k}$. We derive the optimal policies for KL-regularized $\mathrm{pass@k}$ and $\mathrm{max@k}$ objectives in closed form. Our explicit solutions reveal that $\mathrm{@k}$ optimization naturally redistributes learning pressure based on prompt difficulty, directing it toward harder problems. Crucially, we show that standard $\mathrm{@}1$ objectives achieve these exact same optimal policies through prompt-adaptive regularization or reward transformation. Ultimately, this yields an optimizer-independent explanation for why $\mathrm{@k}$ objectives reduce sharpening on easy tasks while prioritizing success on harder ones. Building on these insights, we introduce $\mathrm{@k}$ Adaptive Pressure for Policy Optimization (KAPPO). Following a one-time reference calibration, KAPPO seamlessly adapts existing $\mathrm{@}1$ methods to $\mathrm{@k}$ via prompt-adaptive regularization or reward transformation, without otherwise altering their training procedures. Experiments with several RL methods on mathematical reasoning and code generation demonstrate that KAPPO provides direct control over sharpening. Crucially, we demonstrate that $\mathrm{@k}$ pressure can be fully realized with single completion training, matching the performance of multi-completion $\mathrm{@k}$ optimizers at a fraction of the cost.

---


### 430. [Toward Knowledge-Centric AI: Discovering, Internalizing, and Using Explicit Knowledge Across Agents and Generations](https://arxiv.org/abs/2611.03157)

**<font color=#1a73e8>作者：</font>** Yisen Gao, Haoyu Huang, Zhongwei Xie 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge is how understanding accumulates across people and generations: durable records that outlive their producers and that others can check, combine, teach, and correct. AI agents are now built and run by many independent users and organizations, and each agent is upgraded, replaced, or retired within months. Yet what an agent learns stays trapped in model parameters, a transient context window, or a system-specific memory store that is appended to and retrieved from rather than processed. We argue that the next generation of AI should be knowledge-centric, built around an explicit, continuously evolving knowledge layer independent of any single agent. In this loop, agents discover knowledge from their environments and trajectories; the layer internalizes it by turning fragmented, heterogeneous records and experience into composable, revisable understanding; and agents across systems and generations use the result and return new outcomes for revision. While discovery and use have advanced rapidly with large language model agents, internalization remains the bottleneck. We argue that internalization should become a persistent object of training and maintenance-centered on condition-preserving conceptualization of events and deductive, inductive, and abductive reasoning across noisy, heterogeneous representations (text, tables, graphs, rules, and programs). To power this layer, we call for knowledge foundation models that provide shared neural capacity for knowledge computation, and outline a research agenda showing how an explicit knowledge layer delivers reuse, cost efficiency, auditability, and continuity across agent generations.

---


### 431. [LaBraM at Scale: Scaling Data and Models for EEG Pretraining](https://arxiv.org/abs/2611.03165)

**<font color=#1a73e8>作者：</font>** Jun-Yu Pan, Ruicheng Yin, Bao-Liang Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LaBraM, an early EEG foundation model, demonstrated that large-scale EEG pretraining can yield strong representations for diverse downstream tasks. Building on this foundation, we expand pretraining data and model capacity while retaining its core encoder and objective. We train ten encoders with 5.8 million to 1.97 billion parameters on three EEG collections spanning 25,067 to 79,910 hours, adapting signal preparation and training to heterogeneous recordings. Across 23 tasks, Atom-L* reaches 59.05% mean balanced accuracy at its best evaluated full fine-tuning (Full-FT) checkpoint, 3.61 percentage points above the strongest baseline EEG foundation model. Quark-G leads linear probing (LP) at 54.33%, a 1.24-point margin. Both also lead average task rank. At the last evaluated checkpoints, larger encoders improve Full-FT more consistently than LP, and stronger LP does not guarantee stronger Full-FT. Preserving patch structure improves LP over average pooling. Data-fraction experiments suggest capacity-dependent saturation, while checkpoint trajectories show that downstream performance can decline as pretraining loss falls. Joint classification with a shared Qwen3 readout reaches 50.50% with Molecule-H and Qwen3-8B; increasing language-model size provides no consistent gain. These results demonstrate the value of scaling LaBraM and the importance of matching pretraining scale to downstream adaptation.

---


### 432. [CoworkOS:Scaling Agent Coworkers for Real-world Automation](https://arxiv.org/abs/2611.03178)

**<font color=#1a73e8>作者：</font>** Jiajie Jin, Guanting Dong, Chengjun Pan 等 40 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rapid advances in cowork agents are shifting human-AI collaboration toward real-world automation, delivering software, designs, and other artifacts. However, such productivity work demands both high-quality delivery on complex productivity tasks and continued monitoring and decision-making over long horizons, a combination that remains an open challenge. We introduce CoworkOS, a general-purpose harness for long-horizon work that separates task strategy from execution management: the model decides actions, delegation, and acceptance, while the runtime maintains state and feedback. Its three-layer architecture enables direct execution or delegation to Subagents, synchronously or asynchronously, under stable responsibilities. Through a shared application layer, humans and agents inspect and revise the same evolving documents, presentations, CAD models, and Blender scenes, so human-in-the-loop participation can enter both through conversation and through direct modification of the work itself. To sustain continuity across agents and sessions, CoworkOS further introduces hierarchical workspaces and persistent semantic memory, so working files, key decisions, and long-running Job logs remain shareable, reusable, and resumable after interruption. Across 12 benchmarks and 6 categories of real-world applications, CoworkOS proves highly competitive with frontier agent applications such as Codex and DeepSeek Harness. As a sustained-work case study, CoworkOS uses GLM-5.3 as its backbone to conduct RSI-driven automated post-training on Qwen3.6-35B-A3B. Over five rounds, the model's average score across eight benchmarks rose from 33.19 to 42.95 (+9.76). Looking ahead, we believe CoworkOS opens a meaningful path toward general cowork-agent intelligence.

---


### 433. [ACTOR: Action-Centered Temporal Organization for Literary Role-Playing Agents](https://arxiv.org/abs/2611.03184)

**<font color=#1a73e8>作者：</font>** Yuxiang Gao, Tianjie Ju, Zheng Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language agents for literary role-playing are typically modeled around dialogue generation, leaving characters' non-dialogue behaviors and their dynamic evolution over story time underrepresented. In this paper, we propose ACTOR (Action-Centered Temporal Organization for Literary Role-Playing Agents), an automated framework for constructing such behavior trajectories from raw novel texts. ACTOR extracts dialogue and persona-relevant non-dialogue behaviors, represents each behavior using a Thought-Action-Observation structure, and organizes behavior trajectories according to the internal temporal order of the story. We build a behavior dataset from 143 diverse literary works. For each source behavior, we generate counterfactual behaviors that are contextually plausible yet inconsistent with the character's persona. We find that existing models struggle to reliably infer character-consistent actions from historical behaviors and evolving character states. Using these behavior pairs, we train models with Regularized Preference Optimization (RPO), which augments DPO with a negative log-likelihood loss on the source behavior to jointly optimize behavior preference and generation. We further design a four-way next-behavior selection task to evaluate the model's ability to faithfully mimic character actions. Across 17,560 evaluation instances, the model trained on ACTOR's preference pairs achieves substantially improved accuracy. This result demonstrates that structured, temporally organized supervision enables models to leverage character profiles and prior behaviors to infer subsequent actions, greatly advancing literary role-playing beyond mere dialogue imitation. Code and data are available at this https URL.

---


### 434. [Written Once, Read Differently How Language Models Own Answers Steer Their Next Ones](https://arxiv.org/abs/2611.03198)

**<font color=#1a73e8>作者：</font>** Marcus Armstrong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a language model answers a yes/no question, that answer changes how it answers a different question about the same entity. We study this \emph{self-commitment} in 22 open-weight models from four families (0.5B--72B parameters), fixing the model's first answer and measuring the shift in its second across 3,600 question pairs about 120 entities. Each answer writes a \emph{commitment direction} into the residual stream. The similarity of two questions' directions predicts their coupling on held-out entities ($\rho = 0.43$--$0.85$), and ablating a single direction shared across topics leaves at most 17\% of the effect in every model. How this direction is read is far less stable: the reading circuit spreads across more attention heads as models grow, instruction tuning makes more questions read it in the opposite sense, and in one model changing only the system prompt reverses the circuit's sign. Ablating the direction while sparing the attention sink removes most of the coupling at under 1.3\% perplexity cost in 18 of 19 instruction-tuned models, though it shifts standalone answers in two. Without the sink spared, the direction's alignment with the leading principal component of ordinary text predicts which models pay a high cost. Written once, the commitment is read differently across scale, training and prompt.

---


### 435. [CISA: Retrofitting Dense Attention Models with Chunk-Indexed Sparse Attention](https://arxiv.org/abs/2611.03200)

**<font color=#1a73e8>作者：</font>** Mohammed Dabbah, Izhak Golan, Oren Tropp 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context LLM inference is costly because attention repeatedly reads a growing key-value (KV) history. We introduce Chunk-Indexed Sparse Attention (CISA), which retrofits pretrained dense attention models without gradient updates. CISA selects fixed-size KV chunks using compact summaries of existing keys, avoiding token-level indexing and a separate full-length index cache. It uses one indexing query per KV group and shares selected chunks across queries in that group. During prefill, QShare reuses selections across adjacent queries to reduce indexing cost and improve KV reuse and GPU utilization. We evaluate CISA on NVIDIA Nemotron 3 Nano and Ultra, and Inkling-Small. In one-layer BF16 benchmarks at batch size 32 using Ultra's per-device attention dimensions, core attention is 11.7x faster for prefill queries near the end of a 1M-token prompt and 13.0x faster during decode. Including chunk scoring, selection, and all other measured GPU work, speedups are 8.6x and 3.0x. On Ultra NVFP4 with a 4,096-chunk budget, aggregate scores stay within 1.5 percentage points of dense attention on MRCR, LongBench v2, and GraphWalks. RULER sweeps on Nano and Ultra BF16 up to one million tokens show scores within 2.05 percentage points of dense attention with 8-16x fewer KV reads. Serving million-token prompts with 32 concurrent requests and 4K output tokens per request, CISA achieves 2.29x the end-to-end throughput of dense attention using Nemotron 3 Ultra NVFP4 on four NVIDIA B300 GPUs. Selecting fewer chunks increases throughput to 2.61x; in separate GraphWalks evaluations, the smaller budget widens the aggregate score gap from 1.49 to 3.59 percentage points. These results expose a practical quality-speed tradeoff without sparse training.

---


### 436. [Do Agents Still Follow the Rules? Benchmarking Rule Compliance under Agent Context Compaction](https://arxiv.org/abs/2611.03223)

**<font color=#1a73e8>作者：</font>** Yiwei Zha, Qingyu Meng, Herbert Bos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents compact long histories to fit their context windows, but the compacted context must still carry the operating rules that govern later actions. Prior work shows that violations rise after compaction, but measures compliance outside a complete agent harness and does not identify where each violation comes from. We introduce ARCBench(Agent Rule Compliance Benchmark), a configurable benchmark built on the open-source pi agent harness. Its tool-calling agent loop lets us measure rule compliance from actions taken during execution, bringing the evaluation closer to deployed agent workflows. Using ARCBench, we examine where violations after compaction come from, and how different compaction configurations and adversarial settings change their sources. We find that compaction rarely deletes the rule: most violations after compaction occur while the rule is still in the compacted history, with the agent treating a later request as permission, ignoring the rule, and proceeding anyway. Where violations come from depends on the configuration: how the rule is delivered decides whether the agent would break it even without compaction, while the compaction strategy and budget decide whether the rule survives. The strongest compactor-targeted attack more than doubles violations by corrupting the rule in the summary and changing how the agents behave, whereas the strongest defense restores the rule in most summary but still violates. Finally, retaining a rule does not guarantee compliance: compacted runs that retain the rule violate more than twice as often as runs with the full history.

---


### 437. [ScienceCUA: Resource-to-Skill Construction and Execution-Guided Skill Evolution for Scientific Computer Use Agents](https://arxiv.org/abs/2611.03238)

**<font color=#1a73e8>作者：</font>** Daiqiang Li, Jingyi Peng, Rui Hu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents for scientific software require application-specific expertise. Much of this expertise is documented in human-authored software manuals and web pages. However, turning these resources into executable, reusable skills remains challenging due to mismatches between documented and deployed software versions and differences in scope between documentation coverage and task requirements. We introduce ScienceCUA, a two-stage framework combining resource-to-skill construction with execution-guided skill evolution. First, ScienceCUA identifies tasks supported by the software from its documentation, infers operational trajectories, and generalizes them into reusable Skills. Command catalogs, syntax constraints, and shortcuts are organized separately as References for on-demand lookup. Then, ScienceCUA uses execution feedback to drive skill self-evolution by contrasting successful and failed trajectories for the same task, identifying deficiencies, revising existing skills or adding new ones, and updating the skill library only after repeated validation in real environments. To enable reliable evaluation without benchmark noise or task leakage, we introduce two improved benchmarks. ScienceBoard-Verified provides an audited and corrected basis for measuring task performance, while ScienceBoard-VE separates skill evolution from final testing through disjoint evolution and test tasks and further supports native-agent evaluation. Experiments show that the initial Skills and References improve average task success rate by up to 7.23 percentage points over the base model, while skill self-evolution increases the total gain over the baseline to as much as 17.12 percentage points. ScienceCUA turns software documentation into an evolving set of executable skills and queryable references, offering a practical way for general-purpose agents to use scientific software reliably and at scale.

---


### 438. [Forecasting How RLHF Responds to Reward-Model Edits Before Training](https://arxiv.org/abs/2611.03244)

**<font color=#1a73e8>作者：</font>** Zixiao Wang, Duzhen Zhang, Xingbo Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Responses with headers, lists and greater length receive high scores from reward models (RMs), and RLHF policies learn to produce these features even when true quality does not improve. Practitioners therefore edit their RMs, but they learn whether an edit works only after an RL run. We show that the response of a policy to an RM edit can be forecast before training, from samples of the current policy and the scores of the old and new RM. If we read the RM as a set of prices, the first-order theory of KL-regularized RL implies that each feature moves in proportion to its within-prompt covariance with the change in reward. We implant controlled price changes into retrained RMs under a 2^(4-1) fractional factorial design with a self-distilled placebo, run 54 RL runs from six parent policies, and fix every forecast before the runs. With the covariance predictor, we predict the direction of all 20 changes in supply whose forecast has the same sign at every parent and explain 82% of the standardized change. With counterfactual prices, the classical alternative, we explain 50%. The forecast also holds under GRPO and for real RM upgrades, where we explain 66% out of sample with a coefficient frozen from the factorial runs. For rent, the gap between the proxy reward and a gold reward from stronger judges, we rank RM edits correctly with the same covariance over the first 30 steps (Spearman 0.94). This measures the horizon of the forecast: by step 200, the ranking of the factorial edits reverses under both RLOO and GRPO, while the real upgrades keep their order. When we vary the KL coefficient beta, the initial response does not depend on beta, and the response saturates below the KL equilibrium. In one experiment, the long-run response to a price rise is consistent with an additional implicit regularizer beta_0 of about 0.003 to 0.007.

---


### 439. [R$^2$-Omni: Reducing Structural and Precision Redundancy in Omni-LLMs for Long-Form Generation](https://arxiv.org/abs/2611.03247)

**<font color=#1a73e8>作者：</font>** Bolong Feng, Pengfei Zhou, Zhenglin Wan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni-modal large language models (Omni-LLMs) typically process large numbers of multimodal tokens from audio-visual inputs, incurring substantial computational costs and a large memory footprint for the key-value (KV) cache. Aggressive token pruning can alleviate this problem while maintaining competitive performance on multiple-choice tasks, which require only a single option as output. However, we observe substantial quality degradation when generating long-form, open-ended responses. We attribute this gap to query-guided selection, which can retain sufficient evidence for answer selection while discarding details needed for comprehensive generation. This motivates reducing overlapping information across tokens, termed structural redundancy, while preserving diverse content. However, the retained representations may still contain precision redundancy due to unnecessarily high numerical precision in their cached values. To address these two levels of redundancy in token representations, we introduce a training-free framework named R$^2$-Omni. First, Structure-Aware Token Consolidation (STC) consolidates redundant representations using spatiotemporal similarity in video and local continuity in audio. Then, Semantic-Sensitivity Guided Precision Allocation (SSPA) allocates value precision to the retained representations according to the estimated reduction in attention-output error under quantized keys, with query attention and audio-visual alignment providing a semantic prior. Extensive experiments on long-form generation benchmarks demonstrate an average 5.0$\times$ reduction in the memory footprint while preserving 97.98% of baseline generation quality and achieving a 1.48$\times$ end-to-end speedup, highlighting the benefits of jointly reducing structural and precision redundancy.

---


### 440. [The Cost of Mismatch: Noise Amplification in Zeroth-Order Reinforcement Learning](https://arxiv.org/abs/2611.03260)

**<font color=#1a73e8>作者：</font>** Lianmin Chen, Junbin Qiu, Chenxing Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-order (ZO) optimization has emerged as a promising approach for memory-efficient large language model (LLM) post-training, yet its reliable application to reinforcement learning with verifiable rewards (RLVR) remains largely unexplored. Motivated by the distinct data regimes of on-policy RL and fixed-data optimization, we develop a generic variance-theoretic framework to investigate what limits the reliability of ZO gradient estimation. Our analysis reveals that estimation reliability is structurally determined by whether the two finite-difference evaluations are performed on matched data. On-policy reinforcement learning (RL) under the mismatched-data regime produces a $1/\mu^2$ oracle-noise amplification that sets an irreducible noise floor as the perturbation scale $\mu$ decreases, whereas Boltzmann Targeted SFT (BOLT) under the matched-data regime eliminates this amplification via noise cancellation. We further derive convergence guarantees with explicit constants that cleanly separate the two regimes. These results naturally lead to ZO-BOLT, which applies ZO optimization to BOLT's RLVR-aligned weighted-SFT objective. Controlled perturbation-scale sweeps and matched-versus-mismatched end-to-end comparisons validate the predicted effect of data matching. Experiments across three model variants and two mathematical reasoning benchmarks further show that ZO-BOLT consistently improves over the pretrained baseline while retaining a near-inference memory footprint. The code is publicly available at this https URL.

---


### 441. [Specificity Bias and the Wikipedia Paradox: An xAI Analysis of AI Text Detectors under Domain Shift](https://arxiv.org/abs/2611.03280)

**<font color=#1a73e8>作者：</font>** Nico Morloher, Johannes Reschke, Mohamed Mady  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of Large Language Models (LLMs) demands reliable detection of human-authored versus synthetic text. However, current Transformer-based detectors often experience severe performance degradation during domain shifts and operate as opaque classifiers. This paper investigates the robustness and interpretability of fine-tuned Transformer models (DistilBERT, RoBERTa) by evaluating them against a custom out-of-distribution (OOD) dataset of hyper-local news synthesized via open-source LLMs (Llama 3, Mistral, Gemma). To analyze model decision boundaries, we apply a tripartite Explainable AI (xAI) framework using SHAP. Our analysis reveals three key phenomena: First, detectors often rely on a "Call-to-Action" syndrome inherent to instruction-tuned LLMs rather than generic machine text. Second, we observe a "Specificity Bias," where LLMs successfully bypass detection by hallucinating specific named entities and mimicking conversational imperfection. Finally, we illustrate the "Wikipedia Paradox," wherein formal, objective human writing is frequently misclassified as AI due to its low statistical burstiness. These findings demonstrate that purely statistical detection paradigms face systematic limitations in highly structured human domains, emphasizing the critical need for semantically-aware, interpretable detection architectures.

---


### 442. [ENGINE: Endogenous Variational MultiScale Optimization for Zeroth-Order LLM Fine-Tuning](https://arxiv.org/abs/2611.03293)

**<font color=#1a73e8>作者：</font>** Zhuoli Ouyang, Changxi Chi, Siyuan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-order (ZO) optimization enables memory-efficient large language model (LLM) fine-tuning, and recent methods incorporate curvature-aware strategies. However, in the high-dimensional parameter space of LLMs, these methods inherently suffer from exploding gradient variance and prohibitive costs. Conversely, confining updates to a low-dimensional subspace reduces variance but discards critical high-dimensional information, degrading performance. This creates a fundamental dilemma: full-space optimization is informative but has high variance, while subspace optimization has low variance but loses information. To break this trade-off, we propose ENGINE (Endogenous Variational MultiScale). Inspired by computational mechanics, we adapt static Variational MultiScale (VMS) theory to dynamic optimization, treating low- and high-dimensional spaces as resolved coarse and unresolved fine scales. Through a multigrid-style V-cycle, ENGINE alternates between spaces, dynamically probing fine-grained information in the high-dimensional space and injecting it to correct the efficient low-dimensional sampling process. Under appropriate assumptions, statistical analysis characterizes variance reduction and correction of curvature-induced bias, and convergence analysis establishes a stationarity bound for the corrected coarse updates. Evaluations on standard LLM benchmarks show that ENGINE achieves higher accuracy and faster convergence than existing ZO methods, achieving up to a $2.61\times$ speed-up in forward passes with zero additional peak memory overhead. Code is available at this https URL.

---


### 443. [LLMs Depend on Specialist Tools for Out-of-Distribution Generalization in MS/MS Structural Elucidation](https://arxiv.org/abs/2611.03308)

**<font color=#1a73e8>作者：</font>** Gabriel Asher, Cailum M. K. Stienstra, Tomo Oga 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A frontier language model was recently reported to solve 1D NMR structural elucidation without tools. We ask whether this capability transfers to tandem mass spectrometry (MS/MS) in the de novo setting, where the model must propose a structure directly from the spectrum without a candidate list or reference library. To separate reasoning from recall, we build a 100-analyte benchmark from MassSpecGym, split by each analyte's textual footprint into in-distribution (well documented in literature) and out-of-distribution (essentially undocumented) arms. We hold the model, harness, and output format fixed and vary only the LLM's access to domain-specific tools. Without tools, a frontier LLM reaches 52% Top-1 accuracy in-distribution but only 2% out-of-distribution. Only access to de novo structure generators improves out-of-distribution accuracy, raising it to as much as 38% Top-1, and the resulting agent outperforms the standalone de novo models both in and out of distribution. These results suggest that LLMs are not effective at de novo MS/MS structural elucidation on their own, and that further gains depend on the specialist tools available to the agent rather than on the LLM itself.

---


### 444. [MultiInpaintCOCO: Fine-Grained Visual Understanding in Multiple Languages](https://arxiv.org/abs/2611.03309)

**<font color=#1a73e8>作者：</font>** Andrei-Alexandru Manea, Jindřich Libovický, Philipp J. Rösch  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Previous research shows that vision-language (VL) models struggle to understand fine-grained image details and tend to focus on the overall layout. Moreover, any weakness in English tends to be further amplified in the multilingual setting. To study that, we extend InpaintCOCO, an English dataset focused on fine-grained visual details, to 13 typologically diverse languages across five language families, creating MultiInpaintCOCO - a new multilingual benchmark of 953 minimal-pair examples. We further test several state-of-the-art models in multilingual multimodal retrieval, considering both light VL CLIP-like encoders and large language models. Our results show that performance degrades substantially for lower-resource languages, with the strongest predictor being the data resources available for the languages rather than typological similarity to English. In cross-lingual retrieval, most models exhibit a systematic bias toward English: when given a correct caption in a non-English language and an incorrect one in English, models preferentially select the English caption. This bias varies considerably across architectures. Among the tested models, Gemma 3 shows the strongest English preference while Qwen 3 is the least biased, despite both reaching similar monolingual accuracy across languages. The code is available at this https URL.

---


### 445. [TrafficInstruct: A Multi-Task Network Traffic Dataset and Benchmark for Instruction Tuning](https://arxiv.org/abs/2611.03319)

**<font color=#1a73e8>作者：</font>** Zhengdao Li, Hui Wen, Zixuan Wan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Instruction tuning for multi-task network traffic analysis requires data with clearly defined sources, supervision targets, and evaluation conditions. We introduce TrafficInstruct, a newly collected dataset comprising raw packet captures and 55,000 structured supervised fine-tuning records across ten tasks: malware traffic detection, botnet detection, malicious DNS-over-HTTPS detection, Web attack detection, advanced persistent threat detection, encrypted VPN detection, Tor behavior detection, encrypted application/service classification, website fingerprinting, and application classification under concept drift. An automated workflow captures traffic from controlled software executions, attack experiments, and application activities. Labels are supported by task-specific collection evidence, including process or socket attribution, activity records, and execution outcomes. Filtering, sanitization, and task-specific transformations produce instructions, traffic observations, and structured answers. We verify sample sources and partition the dataset by complete collection sessions, keeping all samples from the same session within one partition. The benchmark defines allowed inputs, deterministic label mappings, fixed training/validation/test partitions, and task-wise scoring rules. We evaluate majority-class, random-forest, and ET-BERT baselines, an unadapted 27B language model, and independently trained task-specific LoRA adapters on a shared frozen base. Adapters are selected using validation data and evaluated on the corresponding test sets. Task-specific adaptation improves classification performance, supporting instruction tuning across diverse traffic-analysis tasks.

---


### 446. [A Symbolic-Neural Framework for Context-Aware Evidence Extraction from Mobile SQLite Databases](https://arxiv.org/abs/2611.03323)

**<font color=#1a73e8>作者：</font>** Jeel Piyushkumar Khatiwala, Divyangkumar Patel, Dianxiang Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reliable forensic evidence extraction from mobile SQLite databases is challenging because application schemas are undocumented, evolve across releases, and differ across operating systems, making schema-specific methods brittle and difficult to maintain. We present SNEEF, a symbolic-neural framework for context-aware evidence extraction that encodes each SQLite row as context-value pairs with standardized provenance metadata and column labels, uses a language model to recognize nine forensic entity types, and binds each accepted entity to its source table and row through the PA-EEP provenance protocol. We evaluate SNEEF against examiner-verified ground truth from five corpora built from public Android and iOS device images, spanning multiple application versions. SNEEF achieves an F1 score of 0.967 for evidence entities extracted from SQLite row content, excluding application names, compared with 0.728 for a context-free configuration, with consistent gains across all corpora. We also introduce an Evidence Failure Mode taxonomy to characterize why extraction errors occur.

---


### 447. [The SIMPLE Law for Energy Cost of LLM Inference](https://arxiv.org/abs/2611.03330)

**<font color=#1a73e8>作者：</font>** Hiari Pizzini Cavagna, Andrea Proia, Daniele Cesarini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI is billed per token, yet tokens are not equally expensive. Each token enters the KV-cache and raises the cost of those that follow, so energy grows non-linearly along a sequence whose tokens look identical. No analytical model states what a token costs, and the most accurate SOTA model is a fit, not a law: it absorbs architecture into fitted coefficients, requiring per-LLM fitting. We derive closed-form expressions of the computational and memory-access complexity of LLM inference in terms of architectural hyperparameters, covering MHA and GQA, and compare a family of analytical models of increasing granularity. From these, we obtain the SIMPLE Inference Model to Predict LLMs Energy (SIMPLE), a four-parameter law that separates prefill from decode, and decode into KV-cache cost and next-token computation. Over traces of 13 dense LLMs from six families on NVIDIA H100 GPUs, it attains R2 = 0.969 and 11.97% MAPE, 3.1-3.5x below the SOTA, without per-LLM calibration. The SIMPLE law explains as well as predicts: prefill energy grows quadratically with the hidden dimension, so larger LLMs suffer most from long inputs; and more aggressive GQA KV grouping reduces the per-token energy by up to 3x relative to standard MHA. Increasing the reasoning token budget pushes output length beyond the analytically derived energy minimum, driving super-linear energy growth; although accuracy grows with the budget, energy grows faster, so Intelligence per Joule peaks at an intermediate budget and falls by up to 3.14x across a 4.0x reasoning-budget range. Agentic serving raises energy per request by 13.0x relative to non-agentic ones, driven by the growth of both the prefill and the KV-cache terms with input length; while prefix caching removes most of the prefill cost (-93%), the KV-cache term is unaffected, so even a cached agentic request costs 4.8x more.

---


### 448. [ArabGeoText: Tool-Augmented Vision-Language Models for Arabic Geospatial Text Spotting](https://arxiv.org/abs/2611.03339)

**<font color=#1a73e8>作者：</font>** Yakoub Bazi, Sarah Alsaleh, Mohamad M. Al Rahhal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial text spotting involves locating and transcribing geographic labels, such as road names, district names, and landmarks, in raster maps. These labels are often small, densely arranged, and arbitrarily oriented. Although Arabic text recognition has been studied extensively in documents and natural scenes, Arabic geospatial text spotting remains underexplored. We introduce ARABGEOTEXT, an Arabic-centric benchmark covering 970 geographic locations in Riyadh and Jeddah, with 17,875 manually annotated text instances per view type. For each location, we pair an OpenStreetMap (OSM) rendering with a composite created by overlaying that rendering on the corresponding remote sensing (RS) imagery. The paired views preserve label content and pixel geometry, allowing evaluation across different backgrounds. Geographic partitions support in-city and city-disjoint evaluation of detection, recognition, and end-to-end spotting. Experiments with direct Qwen3.5-4B spotting show difficulties in recovering all labels within a tile. We therefore propose a tool-augmented vision-language framework that combines YOLO26 localization and crop rectification with Qwen3.5-4B recognition adapted through low-rank adaptation (LoRA). The framework outperforms direct LoRA-adapted Qwen3.5-4B spotting across both image views and test cities. With localization held fixed, reader adaptation further improves recognition over the pretrained zero-shot reader. The dataset and code will be made publicly available at this https URL.

---


### 449. [FLAMIA: FLAsh MIcroscaling Attention for Fast and Causally Safe Training on Blackwell](https://arxiv.org/abs/2611.03344)

**<font color=#1a73e8>作者：</font>** Fedor Velikonivtsev, Mikhail Koltakov, Denis Kuznedelev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention remains a substantial computational cost in Transformer training, particularly at long context lengths. NVIDIA Blackwell GPUs provide high-throughput low-precision matrix multiplication, but exploiting it in attention requires addressing quantization overhead, causal information leakage through shared scales, and numerical inconsistencies between the forward and backward passes. We present FLAMIA, a family of attention kernels for Blackwell with MXFP8 and mixed NVFP4/FP8 training paths. Our design combines token-block scaling that reuses quantized operands across matrix orientations, targeted safeguards against scale-induced leakage, and consistent forward and backward computations. Fused quantization and architecture-specific kernel optimizations reduce overhead, while document-local scaling and workload-aware scheduling support variable-length documents directly in packed layouts without repacking. Across various causal packed-document workloads, the MXFP8 path accelerates the combined forward and backward attention call, including quantization, by factors of $1.10$--$1.40\times$ on B200 and $1.06$--$1.42\times$ on B300 relative to the fastest evaluated baseline for each workload. We validate training stability and quality preservation on pretraining Llama-style models. These results show how jointly designing quantization, training numerics, and document scheduling translates low-bit hardware throughput into practical attention acceleration.

---


### 450. [NormMoX: A Normative Mixture of Experts for Explainable Autism Classification from Structural and Functional MRI](https://arxiv.org/abs/2611.03349)

**<font color=#1a73e8>作者：</font>** Muhammad Hasan Masrur, Fani Deligianni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While structural and functional magnetic resonance imaging (sMRI, fMRI) offer profound potential for researching autism spectrum disorder (ASD) and understanding individual neurodivergence, current classifiers lack the explanatory power needed for scientific study, clinical use and personal-level insights. Most models learn from imaging features that also vary with age, sex, scanner site and head motion. They fuse the two modalities without a common reference and explain decisions against arbitrary reference inputs rather than a typical brain. We present NormMoX, a normative mixture of experts that makes the typical brain the shared reference for prediction, fusion and explanation. Normative models trained on large healthy cohorts give the value each brain measure is expected to take for a person's age and sex. NormMoX learns from each person's deviations from these expected values. For each modality, a neural network expert turns the deviations into a score of evidence for ASD. A fusion head, MoX, compares each score with those of typical controls before combining them. It therefore needs no imputation when a modality is missing and shows in which modality each person is atypical. On 1,035 participants of ABIDE I, NormMoX reached an AUROC of $0.728 \pm 0.004$ in repeated cross-validation, above linear, single-modality and deep fusion baselines. NormMoX thus shows not only whether a person is likely to have ASD, but where, and in which modality, their brain departs from typical. The implementation is available at this https URL.

---


> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
