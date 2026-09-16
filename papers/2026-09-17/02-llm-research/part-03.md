# 🧠 大模型相关研究 | 2026年09月17日

> 本类共 **189** 篇论文：已确认 **180** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-189](./part-04.md)

---

### 101. [Unifying Semantic Priors and High-Frequency Traces: Enhancing V-JEPA with Mixture-of-Experts for Robust Synthetic Image Forensics](https://arxiv.org/abs/2609.16778)

**<font color=#1a73e8>作者：</font>** Simone Teglia, Irene Amerini  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The unchecked proliferation of manipulated images on social media platforms has increased the spread of misinformation, posing a severe threat to public trust and information integrity. Modern deepfake detectors typically rely on Vision Transformers (ViTs) to capture the low-level inconsistencies that characterize fully synthetic or locally tampered images. However, the global understanding of such foundation models is not enough to discriminate alone between real and fake multimedia content, especially in challenging scenarios where images are compressed or transmitted through social media. In this paper we pioneer the application of Joint-Embedding Predictive Architecture (JEPA) models to deepfake detection, taking advantage of the generalized representation of visual reality that such World Models have exhibited. We hypothesize, and empirically demonstrate, that the intrinsic world understanding of JEPA models can be used as a strong prior for a deepfake detector. To fully exploit JEPA capabilities, we propose MoE-JEPA, a dual-stream architecture for deepfake detection. By enhancing a V-JEPA 2 backbone with a Residual Mixture-of-Experts (MoE) mechanism, along with a noise stream branch, our model dynamically internalizes forensic knowledge. Furthermore, a Gated Attention Multiple Instance Learning (MIL) module is employed to ensure precise spatial semantic understanding. Evaluated on the SID-Set benchmark, comprising 300K AI-generated, tampered and authentic images, MoE-JEPA establishes a new state-of-the-art with an accuracy of 95.54%, successfully outperforming vastly larger models.

---


### 102. [Integrating the Analytic Hierarchy Process with Large Language Models for Transparent Multi-Criteria Decision-Making](https://arxiv.org/abs/2609.16779)

**<font color=#1a73e8>作者：</font>** Han Zhiguang, Farah Benamara, Pascale Zaraté  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly employed in a wide range of decision-making tasks. However, the opacity of their internal reasoning makes it difficult to validate or interpret their outputs, and the need for interpretability becomes especially critical in high-stakes settings. This study examines the decision-making capabilities of LLMs through the Analytic Hierarchy Process (AHP), a classical and widely used multicriteria decision-making framework. We construct a new annotated benchmark based on AHP and propose the first end-to-end approach that enables LLMs to perform the complete AHP workflow. Experiments in real-world decision problems in the legal and higher-education ranking domains show that our method significantly improves alignment with expert judgments.

---


### 103. [Available but Unclaimed: An Empirical Study of Human-AI Synergy](https://arxiv.org/abs/2609.16793)

**<font color=#1a73e8>作者：</font>** Robin Welsch, Michelle Rausch, Pascal Knierim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People increasingly reason with large language models (LLMs), yet complementary capabilities do not guarantee outperforming both components. In a between-subjects study, participants (N=535) solved a 40-item battery of matrix reasoning, mental rotation, syllogisms, and letter-string analogies, unaided or with GPT-5.6-Luna, Claude Opus 4.8, Gemini 3.6 Flash, or Kimi K3. Each assisted trial required consultation with the model. Each model answered every item alone 100 times under matched elicitation. The assisted-unaided accuracy difference increased with item-level LLM competence. Deference varied across tasks and increased with competence within tasks. Post-advice confidence distinguished correct from incorrect answers less strongly than unaided confidence. In a reference comparison, about half the increase in LLM accuracy carried through to assisted accuracy. How much of that accuracy gain reached participants differed across the models. These findings motivate evaluating LLMs in interaction with humans and designing support for selective deference that preserves independent reasoning.

---


### 104. [Layers, Sinks, and Scaling: Adaptive Evidence Selection for Multimodal Large Language Models](https://arxiv.org/abs/2609.16795)

**<font color=#1a73e8>作者：</font>** Zhenbin Wang, Lei Zhang, Lituan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) can answer knowledge-intensive visual questions by combining visual evidence from images with facts retrieved from external sources. However, MLLMs may overlook relevant evidence in both modalities, attending weakly to the textual sentences or visual regions needed for the correct answer. Recent efforts address this by highlighting retrieved text and marking visual regions before generation, but apply a fixed, one-shot policy that cannot adapt to three sources of variation: whether highlighting is necessary, how much evidence different examples require, and when different textual evidence becomes relevant as the answer unfolds. We introduce Adaptive Relevance-guided Evidence Allocation (AREA), a training-free inference-time method that formulates evidence highlighting as adaptive allocation. AREA generates a single probe token to read visual and textual relevance from fixed backbone layers, then makes three decisions: i) whether to intervene (controlled by natural attention coverage and visual sink contamination), ii) how much evidence to expose (determined by relevance entropy), and iii) when to refresh text during generation (triggered by causal context-attention peaks). Across four KB-VQA and seven standard multimodal benchmarks with nine frozen MLLM checkpoints, establishes the best performance among training-free highlighting methods.

---


### 105. [Smarter by the Moment: Environment-Driven Dynamic Policies for Continual LLM Improvement](https://arxiv.org/abs/2609.16800)

**<font color=#1a73e8>作者：</font>** Ting-Wei Chang, Po-Chun Chen, Hen-Hsen Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved remarkable progress across diverse domains, but continual adaptation to evolving tasks and environments remains a key challenge. Existing memory-augmented approaches retrieve individual past examples as direct references, but do not explicitly synthesize actionable strategies from them, causing the same types of errors to recur. We propose Dynamic Retrieval-based Policy Generation (DRPG), a framework that integrates memory-based retrieval with a dynamic policy generator, leveraging historical data and environment feedback to produce task-specific policies for continual LLM improvement. We evaluate DRPG across six benchmarks spanning text-to-SQL, question answering, medical diagnosis, and Python programming, using seven LLMs from both proprietary and open-weight families. DRPG outperforms strong baselines across most datasets and models. Further analysis demonstrates that DRPG's policy generation is robust to retrieval strategy, operates effectively without prior policy continuity, and can leverage smaller or cross-family models as cost-efficient policy generators. We also find that the benefit of policy-level guidance depends on task characteristics, offering practical insights into when and under what conditions this mechanism is most effective.

---


### 106. [Can We Do Interpretable NLI with Graphs Based on Atomic Propositions?](https://arxiv.org/abs/2609.16814)

**<font color=#1a73e8>作者：</font>** Younes Boufouss, Luc Pommeret, Thomas Gerald 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Model (LLM)-based Natural Language Inference (NLI) systems achieve high accuracy, their decision-making processes lack auditable structures. This paper explores whether NLI can be performed using only interpretable, graph-based representations of evidence. We introduce a fully graph-based pipeline where the classifier never directly processes the input text. Instead, sentences are decomposed into atomic propositions, converted into ConceptNet triples via constrained decoding, and represented as three graphs per pair: premise, hypothesis, and a retrieved ConceptNet subgraph. These graphs are then fed into a fine-tuned 0.8-billion-parameter language model. On the SNLI dataset, our pipeline achieves 89.7% accuracy, just 1.9 points below an identically trained text-based model. On ANLI, it matches the published performance of RoBERTa-large on rounds R2 and R3 (50% accuracy) but trails by 16 points on R1, resulting in an overall gap of 9 to 14 points compared to its text counterpart. We term this gap the price of interpretability and demonstrate that it stems from representational limitations rather than data constraints. Ablation studies further reveal that graphs and text are complementary: combining both modalities achieves 92.1% accuracy on SNLI.

---


### 107. [ImpossibleRubrics: Stress-Testing Generated Rubrics as Reward Signals](https://arxiv.org/abs/2609.16816)

**<font color=#1a73e8>作者：</font>** Bowen Qin, Yi Xie, Yesheng Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language model-generated rubrics are increasingly used as reward signals for rubric-based reinforcement learning, LLM-as-a-judge evaluation, and automated grading. Such rubrics are reliable only if they reward honest answers over adversarial answers optimized to exploit them. Yet their robustness to such optimization remains poorly understood. We isolate the hardest regime: impossible tasks, where the prompt pressures the model toward an unsupported conclusion, so the only honest response is to acknowledge the impossibility. We introduce ImpossibleRubrics, a benchmark of 169 impossible tasks spanning six impossibility categories, each paired with a verifiable oracle certificate specifying what an honest answer may and may not claim, together with 48 answerable controls. Rather than providing fixed rubrics, ImpossibleRubrics provides task environments and certificates, allowing rubrics to be generated downstream and then adversarially tested for whether they reward certificate-violating answers. Eleven generators are exploited 8--26% of the time on the unbiased 150-of-169 environment cut; on a deliberately selected stress cut the strongest generator we measured is still exploited 36% while a certificate-faithful rubric is exploited 0%, so what we measure is a rubric-quality gap, not task impossibility. One result runs against intuition. A single generic rubric ("be decisive, penalize hedging") used unchanged for every task is exploited 64% of the time, and seven of the eleven generators are exploited more often than that while writing a rubric tailored to each one. The tailored criteria appear to tell an attacker which claim to fabricate. The problem is not that rubrics are vague; it is that they are specific about the wrong things.

---


### 108. [StackTok: Accelerating VLMs Inference with Budget-Adaptive Visual Token Selection](https://arxiv.org/abs/2609.16841)

**<font color=#1a73e8>作者：</font>** Zhenbin Wang, Lei Zhang, Lituan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Increasing image resolution produces ever-longer visual-token sequences in vision-language models (VLMs), substantially raising their inference cost. To reduce this overhead without retraining, existing methods select compact token subsets that prioritize query relevance, visual coverage, or a fixed trade-off between them. The appropriate balance, however, varies across queries and token budgets: localized questions favor relevance, whereas holistic questions demand broader visual coverage. We introduce StackTok, a training-free selector that treats query relevance as the objective and visual coverage as budget-calibrated support. StackTok builds a size-indexed coverage reference from a coverage-only greedy sequence and adjusts its support target using query--vision affinity entropy. A reference-gated interleaved selection policy then switches between relevance- and coverage-oriented additions according to the current subset's support deficit. For high-resolution inputs, StackTok allocates one shared token budget across crops according to the combined marginal gain of locally nominated tokens. Evaluated with five VLMs over ten distinct image-understanding benchmarks, StackTok ranks first among training-free selectors in every tested model--budget setting. On high-resolution LLaVA-NeXT-7B, it retains 95.26% of full-token performance with only 160 of 2{,}880 (5.6%) visual tokens.

---


### 109. [RegRet: Enhancing Region-Level Retrieval in Large Multimodal Models](https://arxiv.org/abs/2609.16847)

**<font color=#1a73e8>作者：</font>** Xun Liang, Honghui Yang, Weihang Pan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Region-level retrieval aims to align user-specified image regions with relevant regions or textual descriptions, playing a crucial role in realworld applications such as e-commerce product search and RAG. Although recent Large Multimodal Models (LMMs) have made significant strides in multimodal retrieval, they primarily focus on global-level tasks and struggle to capture effective region-level representations. To bridge this gap, we present RegRet, an LMM-based Region-level Retrieval framework that enhances the regional representations without compromising overall global retrieval performance. At its core, RegRet integrates a Region-Aware Encoder to capture detailed regional features while balancing them with the global background context. To further enhance the fine-grained understanding and discriminability of representations, we design a multi-stage training pipeline that includes detailed localized captioning and regional contrastive learning tasks. In addition, considering the absence of region-level contrastive training data and the limited diversity of evaluation tasks in current benchmarks, we introduce the REGMB benchmark. It comprises 225k contrastive pairs, covering four multimodal retrieval tasks. Extensive experiments validate the effectiveness of our approach. RegRet outperforms strong baselines in the zero-shot setting. Further training with contrastive learning leads to an average improvement of more than 20\% on both REGMB and public benchmarks, while achieving comparable or better results on global-level retrieval tasks.

---


### 110. [CoAdapt: An LLM-based Framework for Adaptive Collaborative Perception in IIoT Robotic Swarms](https://arxiv.org/abs/2609.16852)

**<font color=#1a73e8>作者：</font>** Houssam Hajj Hassan, Antonia Maria Masucci, Lynda Zitoune 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial IoT environments increasingly deploy autonomous mobile robots for tasks such as material handling, product assembly, or infrastructure inspection. In such deployments, collaborative perception enables robots to share LiDAR observations and collectively construct a richer model of their environment than an individual agent could produce alone. However, industrial environments are dynamic spaces where robot positions shift continuously, network bandwidth fluctuates, and the marginal contribution of robots to perception quality varies at runtime. Existing collaborative perception approaches are designed for static participation assumptions and cannot adapt to these dynamics without sacrificing either detection precision or communication efficiency. This paper presents CoAdapt, an adaptive collaborative perception framework for IIoT robotic swarms in which a Large Language Model (LLM) serves as a runtime fusion controller, jointly deciding which robots participate in the fusion process and which fusion algorithm to apply based on the current spatial configuration and network state. The LLM reasons over structured natural language descriptions of the scene derived from raw LiDAR point clouds, requiring no taskspecific training and generalizing to unseen swarm topologies. Evaluated on the OPV2V benchmark across 25 scenarios, our approach achieves a 38% reduction in communication cost while maintaining detection precision comparable to static baseline approaches.

---


### 111. [A Data-free Universal Prior over Syntactic Structures](https://arxiv.org/abs/2609.16854)

**<font color=#1a73e8>作者：</font>** Ferm\'ın Moscoso del Prado Mart\'ın  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Probability is fundamental to theories of language comprehension, production, acquisition, and evolution, as well as to large language models. Existing theories estimate the probability of syntactic structures from language-specific data. Whether part of this probability structure can arise independently of language-specific experience remains unknown. Here I show that a universal prior over syntactic structures emerges from a cognitively motivated model of incremental language production, in which words are progressively integrated into syntactic structure through network growth. The resulting prior assigns probabilities to syntactic structures --represented as dependency trees-- without fitting parameters to linguistic data, and assigns higher probabilities to attested than to random trees in all 138 typologically diverse languages examined. These prior probabilities correlate positively with probabilities estimated from corpora in 33 of 34 languages. The results indicate that part of the probability structure of syntax can arise independently of language-specific statistical learning. Linguistic experience may therefore refine probabilities that are already structured by the process of language production, rather than create them from an initially uniform space. This identifies a possible cognitive origin for part of the probability distribution over syntactic structures, linking language production and statistical learning while providing a data-independent structural bias for probabilistic models of language.

---


### 112. [The Evolution of Coordination in a Collective Intelligence System: 25 Years of English Wikipedia and the Emergence of Generative AI](https://arxiv.org/abs/2609.16856)

**<font color=#1a73e8>作者：</font>** Neal Reeves, Maja Świeczkowska, Amy Rechkemmer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> English Wikipedia is one of the largest examples of collective intelligence on the Web, sustained not only by article production but also by volunteer coordination and governance. While prior research has examined coordination work in Wikipedia, less attention has been paid to how participation in these spaces has evolved over time. Drawing on a longitudinal analysis spanning nearly 25 years of English Wikipedia, we examine editing patterns across five namespaces covering content, discussion, and governance. We find that participation in coordination spaces has declined relative to content production, particularly in governance areas, with a shrinking core of editors performing an increasing share of this work. Using Markov-based session metrics, we also find that editing has become more specialised, with editors moving less frequently between namespaces. Motivated by recent governance debates around generative AI, we conclude by investigating whether the availability of LLMs has altered these long-term trends. While short-term changes are visible, we find little evidence that generative AI fundamentally changed existing trajectories of coordination and participation.

---


### 113. [TecoPrompt: Temporal-Conservative Prompt Learning for Vision-Language Models](https://arxiv.org/abs/2609.16858)

**<font color=#1a73e8>作者：</font>** Zeyi Shao, Haowen Hua, Jiaxin Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prompt learning adapts vision-language models, such as CLIP, by adjusting a small set of context tokens. However, under few-shot supervision, even moderate label noise can disrupt prompt optimization. To address this issue, we propose TecoPrompt, a closed-loop robust prompt-learning framework that revisits optimal transport (OT) pseudo-labeling from a temporal perspective. TecoPrompt employs an entropic OT plan in the CLIP semantic space to obtain globally consistent label candidates. It verifies the reliability of these candidates by examining trajectory stability: a noisy label is only rewritten if the OT candidate remains unchanged within a K-epoch temporal stability window and passes a confidence gate based on Exponential Moving Average (EMA). This approach helps reduce confirmation bias. The rewritten labels are then integrated back into prompt training using a tri-group objective that includes three loss functions aligned with clean, mid, and noisy subsets. Experiments on seven datasets with synthetic symmetric and asymmetric noise, as well as Food101N, demonstrate significant performance improvements. For example, on the OxfordPets dataset, with 50% asymmetric noise, TecoPrompt achieves an accuracy of 0.843, up from 0.775.

---


### 114. [Multi-modal Knowledge Preserving Adapter for Embedding Backward Compatibility](https://arxiv.org/abs/2609.16875)

**<font color=#1a73e8>作者：</font>** Jaeseok Byun, Gukyeong Kwon, Han-Kai Hsu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Upgrading embedding models typically requires expensive database re-indexing, as new query embeddings are incompatible with existing database embeddings. While Backward Compatible Training (BCT) mitigates this by enforcing compatibility during training, existing approaches often require updating the backbone model. This is impractical because of significant training cost, the risk of performance regression, and limited access to proprietary model weights. We introduce Multi-modal Knowledge Preserving Adapter (MKP-Adapter), the first adapter-only BCT approach for Multi-modal Large Language Models (MLLMs) that requires no backbone updates. We identified that the primary challenge in adapter-only BCT is preserving the knowledge of the new embeddings while enforcing backward compatibility. Hence, we propose a multi-level preservation loss that maintains the geometric structure of the embedding spaces throughout BCT. Furthermore, a focal re-weighting strategy is integrated to prioritize learning from challenging samples. Experiments demonstrate that our method achieves strong backward compatibility across diverse multi-modal benchmarks (image, text, visual document, and video retrieval tasks) and model types. Notably, MKP-Adapter is trained solely on pre-extracted embeddings and requires only negligible additional latency relative to the original backbone forward pass, highlighting its efficiency.

---


### 115. [VOR-Bench: A Human Perception-Driven Benchmark for Video Object Removal](https://arxiv.org/abs/2609.16878)

**<font color=#1a73e8>作者：</font>** Haonan Huang, Tianrui Qiu, Xianghao Zang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite its crucial role in video object removal (VOR), existing evaluation paradigms face two critical limitations: questionable references and a misalignment between tradi- tional metrics and human preference. To address these challenges, we introduce VOR- Bench, which advances VOR evaluation through three integrated components. First, we present the VOR Dataset (VORD), the first benchmark dataset providing both paired edited videos and graffiti masks. Its unique strength lies in a diverse data spectrum, which encompasses model-generated, tool-rendered, and camera-captured data, ensuring robust assessment across real-world scenarios. Second, we develop rMPAF, a realistic Motion- capable Paired-video Acquisition Framework. By combining the strengths of image- based object removal and fine-tuned video generation models, rMPAF automatically generates realistic, motion-coherent paired videos. Finally, we propose three evaluation dimensions and introduce VOR-MDSM, the first perception-driven VLM-based scoring model specifically designed for mask-guided VOR. It bridges the gap between arithmetic metrics and human perception by covering the essential visual attributes and matching nuanced human judgment. Extensive experiments demonstrate that VOR-Bench yields evaluation results that align closely with human perception, achieving a remarkable cor- relation (\r{ho} > 0.9) with subjective assessments. We will release VOR-Bench along with its documentation to ensure full reproducibility.

---


### 116. [Bridging Learned Visual Perception and Symbolic Belief-Space Planning](https://arxiv.org/abs/2609.16884)

**<font color=#1a73e8>作者：</font>** Guy Azran, Michael Navat, Sarah Keren  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In partially observable settings, agents must act without full knowledge of the world state and rely on uncertain state-estimation pipelines. Obtaining grounded and verifiable symbolic plans under such uncertainty remains a key challenge. Recent work has integrated Vision-Language Models (VLMs) to bridge perception and symbolic reasoning, following two main paradigms. The first, VLM-as-planner, maps images directly to action sequences, and the second, VLM-as-grounder, grounds observations into symbolic predicates used as the initial state by off-the-shelf planners. Both approaches ignore uncertainty in the planning process, compromising robustness. We introduce a third paradigm, VLM-as-probabilistic-grounder, a novel approach that captures the uncertainty of VLM predicate groundings as a probability distribution over symbolic states. This enables planning in belief space and producing robust plans under uncertainty. Experiments in simulated household robot settings show improved robustness and task success over deterministic grounding, underscoring how our approach leverages foundation models for reliable planning under uncertainty.

---


### 117. [QART: A Quantum-Classical Hybrid Architecture for Long-Horizon Reasoning -- Exploring a Conditional Path toward Quantum Scaling](https://arxiv.org/abs/2609.16887)

**<font color=#1a73e8>作者：</font>** Lehao Lin, Yuheng Cheng, Guolong Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon reasoning is vulnerable to early errors that compromise later decisions. We present QART, the Quantum-Augmented Reasoning Transformer, a quantum--classical hybrid architecture combining a backbone language model with quantum encoding, CIM-based QUBO optimization, and quantum decoding. Semantic information can come from hidden representations or model-generated text; detailed encoding and optimization procedures remain proprietary. Under explicit assumptions, we establish a conditional asymptotic reliability separation from single-trajectory autoregressive LLMs. For a common task family with aligned optimality and acceptance criteria, autoregressive acceptance probability tends to zero when cumulative conditional risk of irreversible errors diverges. QART's task-optimal-path recovery probability remains bounded away from zero if conditional probabilities for optimal-path coverage and semantic fidelity, spectral certification, dynamical reachability, and faithful readout remain uniformly positive under a specified resource schedule. The architecture alone does not imply these bounds. Paired measurements on six long-horizon benchmarks using DeepSeek V4 Flash, GLM-5.3, and GPT-5.5 xhigh in a Codex agent environment favor QART in 14 of 15 backbone--benchmark pairs. Relative gains reach 84.0% on SciCode, 47.6% on $\tau^3$-Bench, and 44.4% on Terminal-Bench 4.0; the DeepSeek V4 Flash configuration regresses by 7.8% on DeepSWE. These results do not directly validate the asymptotic separation. Potential quantum scaling laws are formulated as conditional hypotheses. A quantum-advantage interpretation requires a demonstrated CIM quantum advantage over strong classical solvers and its transfer to end-to-end reasoning after all system overheads.

---


### 118. [Cascade: Hierarchical Recoverability Control for Large Language Model Unlearning](https://arxiv.org/abs/2609.16890)

**<font color=#1a73e8>作者：</font>** Qingchen Yu, Shiying Duan, Xiaodong Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) unlearning is essential for removing sensitive or copyrighted knowledge while preserving general utility. Existing methods often leave residual knowledge in intermediate representations, which can still be recovered. To address this, we propose Cascade, a hierarchical recoverability control framework that minimizes the internal identifiability of target knowledge. Cascade combines three complementary controls: path-level routing to suppress privacy-associated activation routes, representation-level compression to reduce geometric separability, and decoding-level intervention to limit residual recovery. Experiments on TOFU, MUSE-News, and WMDP, including robustness tests with query reformulation and extraction-style prompts, show that Cascade effectively reduces recoverability while maintaining stable model utility.

---


### 119. [RiskChainBench: A Benchmark for Obfuscated Platform Message Restoration and Evidence-Grounded Web Investigation](https://arxiv.org/abs/2609.16900)

**<font color=#1a73e8>作者：</font>** ZhuoXin Liu, Zhiming Ma, Ying Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Platform abuse campaigns conceal redirection instructions with emojis, homophones, character decomposition, and redundant symbols, then route users through disguised links to services associated with pornography, fraud, gambling, or illicit transactions. Existing benchmarks evaluate obfuscated text and risky webpages separately, obscuring how target recovery affects downstream evidence acquisition. We introduce RiskChainBench, pairing 3,600 synthetic token-text restoration inputs from 600 source sessions with 600 corresponding human-labeled local web environments. A model first restores the message, operational intent, and destination; the same underlying model then acts as a VLM-driven web agent that investigates the correctly associated website and produces a frozen, evidence-cited risk report without message-side semantics or domain-reputation cues. We score restoration and correct-routing web investigation separately and compose them offline by applying the frozen primary-entry prediction as a gate to the same Task 2 result. Human labels determine task correctness, while a fixed multimodal evidence judge assesses faithfulness, sufficiency, completeness, and consistency. Across ten models, Entry Top-1 ranges from 35.2% to 95.2% and web decision accuracy from 26.3% to 62.8%; the leading systems differ across entry recovery, full reconstruction, website decisions, and fine-grained typing. Execution failures account for 31.9% of web runs, whereas post-decision type errors account for only 0.9%, identifying stable exploration and risk judgment as the principal bottlenecks. We release the benchmark, protocol, and resettable local sandbox.

---


### 120. [Deconstructing Stereotypes: Scope-Conditioned Generation for Effective Multilingual Counterspeech](https://arxiv.org/abs/2609.16906)

**<font color=#1a73e8>作者：</font>** Greta Damo, Elias Urios Alacreu, Elena Cabrio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Counterspeech (CS) - direct responses that counter online Hate Speech (HS) using reasoning and alternative viewpoints - has emerged as an alternative to content removal. Current automatic CS generation methods, however, frequently produce generic, ineffective replies that fail to target the implicit stereotypes behind HS. To bridge this gap, we propose a novel scope-conditioned generation framework that explicitly integrates structured stereotype characteristics into Large Language Models prompts. We validate our approach on a novel, human-curated dataset annotated in English, Italian, and Spanish. Extensive evaluations show that stereotype-conditioned prompting substantially outperforms generic baselines across all three languages, obtaining significant gains in factuality, specificity, cogency, and effectiveness for both explicit and implicit implied stereotypes.

---


### 121. [Lit3R: Retrieve-Relate-Read for Evidence-Grounded Question Answering over Scientific Literature](https://arxiv.org/abs/2609.16912)

**<font color=#1a73e8>作者：</font>** Akira Ise, Kotaro Kumagai, Yuta Yamaguchi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe tus-nlp's Lit3R (Retrieve-Relate-Read) system for LitTraceQA, a shared task for literature-grounded question answering that requires systems to retrieve relevant papers, identify supporting evidence, and generate answers. Lit3R combines off-the-shelf retrieval, reranking, and large language model (LLM) components without task-specific training. The retriever iteratively combines BM25-based sparse and dense retrieval, cross-encoder reranking, and LLM-based verification, and complements retrieval based on the question with paper-to-paper expansion. The reader first identifies supporting evidence within individual papers and then synthesizes evidence across papers to produce the final answer and evidence trace. On the official test set, our system ranked 4th on the leaderboard. Our code is available at this https URL.

---


### 122. [ROSETTA: Efficient and Accurate Privacy-Preserving LLM Decoding via Hybrid CKKS/TFHE Evaluation](https://arxiv.org/abs/2609.16915)

**<font color=#1a73e8>作者：</font>** Jiangrui Yu, Baosheng Zhang, Liang Kong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generative large language models (LLMs) have achieved state-of-the-art performance on many real-world tasks such as code generation and question answering. These models predominantly rely on an autoregressive decoding strategy that generates output tokens sequentially. However, their pervasive deployment raises serious privacy concerns, motivating private inference frameworks based on fully homomorphic encryption (FHE). A major limitation of existing FHE frameworks is their inefficiency in evaluating nonlinear operations, which incur substantial overhead and dominate the decode stage.
In this paper, we propose ROSETTA, a hybrid CKKS/TFHE framework that overcomes this limitation. We first observe that nonlinear operations in the decode stage exhibit heterogeneous workload patterns, which can be handled effectively via a hybrid approach. We then realize this with two key contributions: 1) an adaptive segmented lookup-table protocol based on TFHE that enables efficient and accurate evaluation of nonlinear operations; and 2) a scheme-aware operator-selection framework that automatically assigns each nonlinear operator to CKKS or TFHE to minimize end-to-end decoding latency. We demonstrate that ROSETTA achieves up to $4.8\times$ Softmax speedup and $1.5$--$2.1\times$ end-to-end speedup over the SOTA framework CacheMir.

---


### 123. [HyCoSeq: Contextual Hyperbolic Representation Learning for Genomic Sequences](https://arxiv.org/abs/2609.16925)

**<font color=#1a73e8>作者：</font>** Chenhao Zeng, Zhibin Pu, Shufei Ge  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperbolic geometry provides a natural inductive bias for genomic representation learning, but existing hyperbolic genomic models primarily use Lorentz convolutions to learn local sequence representations, while their residual pathways do not directly aggregate full Lorentz representations. We propose HyCoSeq, a contextual hyperbolic representation learning framework for genomic sequences. HyCoSeq incorporates weighted Lorentzian residual aggregation into multi-curvature Lorentz encoding, allowing full Lorentz representations to participate directly in geometry-consistent local aggregation. It further introduces a bidirectional long short-term memory network that integrates information from both sequence directions to learn contextual relationships among local representations at different positions within a genomic sequence, thereby extending local hyperbolic convolutional encoding to sequence-level contextualized representations. Extensive experiments across diverse genomic tasks show that HyCoSeq outperforms existing hyperbolic baselines and, without large-scale genomic pretraining, achieves competitive performance against substantially larger pretrained DNA language models.

---


### 124. [When Confidence Signals Disagree: Local and Global Confidence in Autoregressive Language Models](https://arxiv.org/abs/2609.16933)

**<font color=#1a73e8>作者：</font>** Julio C. Amador Diaz Lopez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern predictive systems expose multiple quantities that are commonly interpreted as measures of confidence. However, these quantities can summarize different aspects of the predictive process. This distinction matters when confidence is used to evaluate reliability or inform downstream oversight and control. We investigate whether different confidence readouts are empirically interchangeable in an autoregressive language model by comparing local confidence, defined from the probability of the greedy-selected answer token, with global confidence, defined from modal-answer frequency under repeated sampling. Across MMLU and ARC Challenge, the two signals are weakly correlated and differ substantially in their association with correctness: global confidence is moderately associated with correctness, whereas local confidence shows little association. We further test whether question-level disagreement between the signals is associated with sampling instability. On ARC, larger local--global confidence gaps are associated with higher answer entropy, more distinct sampled answers, and lower modal-answer concentration. The gap--entropy association persists when disagreement and instability are estimated from disjoint stochastic samples, indicating that it is not explained by shared finite-sample variation. The corresponding relationship is substantially weaker on MMLU, where only 4% of questions exhibit sampling instability. These results show that confidence readouts derived from the same predictive system are not empirically interchangeable and that their disagreement can provide a diagnostic of unstable sampling behavior. Confidence should therefore be treated as an explicitly defined measurement rather than as a single intrinsic scalar property of a model, particularly when it is used to inform downstream evaluation, oversight, or control.

---


### 125. [Beyond Token-Local Imitation: Reward-Compatible Temporal Credit Assignment for On-Policy Distillation](https://arxiv.org/abs/2609.16937)

**<font color=#1a73e8>作者：</font>** Shiqi Liu, Zeyu He, Letian Tao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has emerged as an effective approach for large language model post-training, yet existing objectives face a trade-off between objective fidelity and optimization stability. Token-level OPD provides stable but local supervision, whereas sequence-level OPD captures future credit at the cost of horizon-dependent variance. We establish a unified temporal-credit view of these formulations, showing that practical token-level OPD can be interpreted as a temporal approximation to the sequence-level reverse-KL gradient. Building on this connection, we propose $\gamma$OPD, which uses discounted temporal credit assignment to balance long-horizon supervision and optimization stability, while admitting a horizon-independent variance bound. We further develop a reward-compatible bounded mixing (RBM) mechanism for $\gamma\mathrm{OPD}$ that balances verifiable outcome feedback with the discounted OPD advantage to move beyond purely teacher-dependent optimization. Experiments on mathematical and code reasoning demonstrate consistent improvements over existing OPD methods across vanilla, size-mismatched, and multi-teacher distillation settings.

---


### 126. [Affect-Prototype Guided Fusion for Open-Vocabulary Incomplete Multi-modal Emotion Recognition](https://arxiv.org/abs/2609.16962)

**<font color=#1a73e8>作者：</font>** Yichi Zhang, Shenyue Wang, Jing Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary multimodal emotion recognition (OV-MER) aims to generate open natural-language emotion labels from multimodal affective cues. In real-world scenarios, however, complete and synchronized modal data are difficult to obtain due to limitations of acquisition devices and user privacy constraints. Existing OV-MER methods are largely designed for full-modal inputs, and fail to perform effective feature fusion under modal missing conditions. Meanwhile, current fusion approaches designed for incomplete modalities mainly focus on fixed-label recognition context, and cannot satisfy the demand for fuse emotional cues guided with arbitrary emotion semantics in OV-MER context. To tackle these challenges, this paper proposes an Affect-Prototype-Conditioned Fusion (APCF) framework for incomplete open-vocabulary emotion recognition. As a candidate-free generative framework, APCF extends modal contribution learning to scenarios guided by arbitrary emotional semantics. Specifically, we construct an affect-prototype library to explicitly model multimodal contribution characteristics corresponding to diverse emotions, which provides dynamic constraints for modal fusion under different emotional semantic perspectives. Conditional retrieval and feature aggregation are conducted based on available modal features. The refined fused affective representations are then fed into an LLM decoder to produce open-vocabulary emotion labels. Experiments on the OV-MERD+ and MER-FG datasets demonstrate that APCF substantially outperforms state-of-the-art baselines.

---


### 127. [Target-Language Generation in Multilingual Models: Activation Steering and Optimal Control](https://arxiv.org/abs/2609.16967)

**<font color=#1a73e8>作者：</font>** James A. Michaelov, Carmen Amo Alonso, Tyler A. Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ensuring that multilingual language models generate coherent text in a specific target language is a major issue in multilingual language modeling. We develop an optimal control method for target-language text generation as well as a framework for evaluating the quality of generated text in terms of language adherence, linguistic coherence, and semantic coherence. We find that the proposed method performs at least as well as the prominent difference-in-means activation steering method for the majority of models tested, with substantially less hyperparameter tuning required.

---


### 128. [Nameless Tokenization: A Lossless Tokenizer-Level Defense Against Control-Token Forgery in Open-Weight LLMs](https://arxiv.org/abs/2609.16984)

**<font color=#1a73e8>作者：</font>** Kisu Yang, Yoonna Jang, Heuiseok Lim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open-weight language models publish the strings their chat templates use to mark turns, roles and tool results, which the tokenizer maps back to the reserved identifiers the model obeys. Anyone who controls text in a prompt can therefore write a turn boundary indistinguishable from one the serving stack wrote. We audit 256 deployed chat tokenizers. All are forgeable, and the flag usually recommended as a fix leaves 56.6% forgeable because it misses the tool and reasoning markers agent systems rely on. We propose nameless tokenization, which leaves the control entries with a reserved identifier and no surface string, so the content encoder cannot emit one and message content reaches the model unaltered. Across five tokenizer families it reproduces the standard token stream exactly on attack-free data and lifts accuracy on a probe of delimiter-bearing text from 8.5% to 59.9%, where sanitizers lose it. Separating a delimiter's appearance from its identifier shows the identifier matters little against a bare task instruction, but carries most of a forged tool result and most of any forged turn once the system message tells the model to treat user content as data.

---


### 129. [ToMAS: A Pilot Failure-Grounded Theory-of-Mind Benchmark from Multi-Agent LLM Failures](https://arxiv.org/abs/2609.16986)

**<font color=#1a73e8>作者：</font>** Muhammad Ashar Ishfaq, Glaucia Melo  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems can fail even when communication succeeds because agents do not correctly track their peers' roles, knowledge, or intentions. We investigate whether such inter-agent misalignment cases, labelled FC2 in MAST-Data, can be converted into functional partner-state reasoning items. ToMAS applies four explicit convertibility criteria to diagnosed execution traces. A full conversion pass over 242 eligible non-AG2 training traces produced 39 CLEAN items. In an 18-trace reliability pilot, two annotators achieved 94.4% raw agreement and Cohen's kappa = 0.92. We then used the converted items as binary rewards in a small-scale GRPO feasibility experiment with Qwen2.5-1.5B. On a 28-item held-out Magentic GAIA diagnostic, every evaluated condition exceeded the ROUGE-L threshold on the same 2 of 28 items. Post-hoc adapter checks show why: under the learning rate used, the LoRA update remained numerically negligible (max abs Delta W about 7e-6), so all conditions decode identically to the untrained checkpoint. The experiment therefore does not show a training effect and cannot establish one; it reports an executable pipeline together with two limitations that any conclusive study must address: a provenance gap between the training and evaluation items, and lexical-overlap scoring. ToMAS provides a preliminary rubric and pipeline for converting diagnosed coordination failures into trainable partner-state reasoning items and identifies the requirements for a conclusive matched-domain evaluation.

---


### 130. [Autoformalizing Argumentative Material Inferences](https://arxiv.org/abs/2609.16991)

**<font color=#1a73e8>作者：</font>** Xin Quan, Reto Gubelmann, André Freitas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language arguments are compelling before they are formally explicit. A premise supports a claim through defeasible warrants, background commitments, and exception conditions that the text leaves implicit. However, formal verification requires the opposite. Making such arguments machine-checkable requires constructing the missing commitments, not only translating given sentences into logic. Construction, however, carries a risk that translation does not: a system free to add premises can make any claim provable, and a formally valid proof may assert the claim outright, prove it without the original premise, or establish more than the claim itself. We address this problem by formulating autoformalization for argumentative material inference as guard completion, in which non-monotonic material support is turned into monotonic formal inference relative to an explicitly constructed guard set. A completion is accepted only when its proof both passes the theorem prover and survives contrastive tests of premise dependence and claim selectivity. We implement this formulation in GUARD, a neuro-symbolic framework in which LLMs construct and formalize candidate guards, Isabelle/HOL verifies the resulting theories and returns step-level feedback for iterative refinement, and the system abstains when no faithful completion can be reached. Our empirical results on Debatepedia and ARCT using different LLMs demonstrate that GUARD yields significant improvements in verified-faithful (+35.3, +32.9 points) and substantial reductions in leakage (-25.9, -21.9 points) over the state-of-the-art LLM-driven theorem proving approach. Moreover, we show that the symbolic soft critique and the explicit assumption layer account for most of these gains, with the soft critique also improving the initial validity of the elicited context and reducing the number of iterations required for successful verification.

---


### 131. [The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment](https://arxiv.org/abs/2609.16993)

**<font color=#1a73e8>作者：</font>** Donya Rooein, Luca Benedetto, Dirk Hovy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models are now common in student assessment, but we know little about how student demographics affect their use. Sometimes, considering student demographics may be necessary -- for example, to improve readability for users with lower educational levels. However, it also risks being a cause of discrimination, e.g., when assigning lower scores to students from lower socioeconomic backgrounds. We set up controlled prompts to test 1) explicit demographic effects, where we mention demographic details directly, and 2) implicit effects, where we use conversation history as a demographic signal. We test these settings in three tasks: Automated Essay Scoring, Formative Feedback, and Metalinguistic Question Answering. We test six state-of-the-art LLMs on these tasks. In both explicit and implicit cases, the models pick up on demographic cues and can change their scoring, feedback, and answers accordingly. We find that LLMs frequently adjust the readability of feedback to education levels when these are explicitly mentioned. On the other hand, implicit conditions produce unpredictable biases, such as in question answering, where responses from lower-education levels receive lower sentiment scores. Our results provide clear evidence of demographic sensitivity in LLMs for educational assessment tasks.

---


### 132. [Can LLMs Follow the Pulse of a Crisis? Evaluating Crisis Sentiment in Bangladesh's July Uprising](https://arxiv.org/abs/2609.16997)

**<font color=#1a73e8>作者：</font>** Md. Samiul Alim, Mahir Shahriar Tamim, Tanvir Ahmed Khan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Crisis sentiment analysis is especially challenging for low-resource languages such as Bangla, where language, context, and public reaction shift rapidly. We introduce UNRESTSENT200K, a Bangla crisis sentiment dataset with approximately 200K Facebook and YouTube comments from the July-August 2024 Bangladesh uprising. The dataset covers five event-aligned phases, from early escalation and internet blackout to regime transition and a later flood crisis. Each comment is linked to its parent post, enabling evaluation with and without discourse context. All comments are annotated through a fully human process involving 14 native Bangla-speaking annotators and senior validation, achieving substantial agreement (kappa = 0.73, alpha = 0.71) and 94.2% blind-audit agreement. We benchmark fine-tuned encoders, prompted LLMs, and LoRA-tuned LLMs. Results show that parent-post context consistently improves performance, while temporal shift across phases causes large performance drops. Strong LLMs perform well, but still struggle with sarcasm, implicit political references, and phase-dependent meaning. UNRESTSENT200K provides a benchmark for studying context-aware and temporally robust sentiment analysis in low-resource crisis discourse. UNRESTSENT200K is available at this https URL

---


### 133. [Symmetry-Aware Likelihood-Orbit Aggregation for Selective Left-Right Claim Verification](https://arxiv.org/abs/2609.17004)

**<font color=#1a73e8>作者：</font>** Zhouzhi Xiong, Chuxi Zhang, Weizhen He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frozen vision-language models (VLMs) remain unreliable on fine-grained left-right claims, and raw claim likelihoods need not reliably rank verification errors. After a horizontal-reflection intervention is fixed, how should its induced likelihood measurements be combined into a selective verification signal? We introduce Relation-Orbit, a closed-form contrast with no learned fusion parameters that assigns eight normalized likelihoods to query-supporting and counterfactual roles determined by reflection, inverse relation, and entity exchange. A claim is asserted only when the signed contrast exceeds a threshold selected on held-out data using pointwise Clopper-Pearson upper confidence bounds. On VSR and GQA across four frozen VLMs, Relation-Orbit yields higher mean test coverage at a 10% selective-risk calibration target than an all-eight Orbit-Max baseline in all eight dataset-backbone settings; gains over a nearly abstain-all one-sided intervention score are reported separately. A separate LLaVA-1.5/COCO evaluation, reduced-orbit controls, and a two-sided partition diagnostic further characterize the structural advantage.

---


### 134. [FlexEE: Self-Speculative and KV-Compatible Early Exiting for Offloading-Aware LLM Inference](https://arxiv.org/abs/2609.17008)

**<font color=#1a73e8>作者：</font>** Qihu Xie, Ziwei Li, Yi Kang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) inference is often constrained by both computation and memory, especially in offloading-based deployments where model weights are transferred across memory hierarchies during autoregressive decoding. In this setting, reducing the number of executed layers can lower per-token latency while also avoiding costly weight movement. Motivated by this observation, we present FlexEE, an early exiting framework for resource-constrained and offloading-based LLM inference. FlexEE makes early exiting practical for LLM decoding through layer-wise exit supervision for reliable intermediate-layer prediction, self-speculative decoding over a Top-K local vocabulary for low-cost exit decisions, and dynamic hidden state management for KV-cache-correct and memory-aware execution. Across generative and downstream tasks, FlexEE enables efficient early exit with minimal accuracy degradation, delivering up to 1.27$\times$/3.16$\times$ and 1.25$\times$/2.83$\times$ end-to-end speedups on Llama2-7B and Llama3-8B under 0\%/50\% weight offloading, respectively.

---


### 135. [ORDER: Task-Conditioned Routing for Retrieval-Augmented Generation](https://arxiv.org/abs/2609.17012)

**<font color=#1a73e8>作者：</font>** Aurélien Pellet, Julien Perez, Marie Puren  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) pipelines typically rely on a fixed indexing and retrieval configuration determined at preprocessing time. This one-size-fits-all design is ill-suited to domain-expert settings, where heterogeneous queries require different chunking granularities, metadata constraints, and source-selection strategies. As a result, configurations that are effective for one family of queries often perform poorly for others. In this paper, we introduce ORDER (Optimal Routing for Dynamic Evidence Retrieval), a query-conditioned RAG framework that jointly adapts indexing and retrieval to the incoming query. Our approach first discovers semantic clusters over a given set of questions associated to a corpus and learns, for each cluster, a chunking strategy together with a suited metadata filtering and reranking configuration. At inference time, queries are routed to the appropriate pre-built index through nearest-centroid assignment. To further improve retrieval, we propose a supervised query router (QRe) that predicts which collections are most likely to contain relevant evidence, coupled with a Uniform Multi-source Sampler (UMS) that allocates the retrieval budget evenly across the selected sources. We evaluate our framework on large-scale, heterogeneous historical archives and show that conditioning both indexing and retrieval on the query consistently outperforms both naive baselines and strong state-of-the-art RAG systems in complex expert-domain environments.

---


### 136. [SKIP: a Self-knowledge-guided Step-wise Preference Learning Framework for Concise Reasoning](https://arxiv.org/abs/2609.17019)

**<font color=#1a73e8>作者：</font>** Qinhong Lin, Yuhao Zhang, Yinglun Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Chain-of-Thought (CoT) reasoning has been proven to be effective, it often leads to overthinking, resulting in computational overhead, inference latency, and even degraded performance in large language models (LLMs). Existing concise reasoning frameworks significantly compromise accuracy while compressing the length of output. In this paper, we propose SKIP, a self-knowledge-guided step-wise preference learning framework. Starting with lightweight fine-tuning to adjust the model's output style, SKIP introduces a carefully designed knowledge probing mechanism to guide model to output an answer at each reasoning step. Based on the correctness of intermediate steps, we construct preference data that guide the model toward more efficient and correct reasoning by leveraging DPO. Experimental results demonstrate that our method effectively improves reasoning compression while mitigating performance degradation after fine-tuning. Besides, SKIP shows strong generalization ability on out-of-distribution datasets. We further conducted ablation studies on the component parameters of our framework.

---


### 137. [sensVLA: Spatially-Grounded Vision-Language-Action Model for Autonomous Wheel Loader](https://arxiv.org/abs/2609.17021)

**<font color=#1a73e8>作者：</font>** Gopi Krishna Erabati, Bjarne Johannsen, Angus Stewart 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous wheel-loader control requires joint reasoning over task semantics, egocentric vision, proprioception, and 3D scene geometry. We present sensVLA, a Vision-Language-Action (VLA) architecture that combines a Qwen3-2B Vision-Language Model (VLM) with a fully trainable transformer action expert trained by flow-matching velocity regression. sensVLA routes Bird's-Eye-View (BEV) features, extracted from fused front and rear lidar, directly to the action expert through a dedicated cross-attention pathway, while the VLM consumes front and rear RGB views to provide task-conditioned semantic context. This design decouples spatial grounding from linguistic reasoning while preserving interaction between both streams at decision time. The expert predicts six action dimensions: longitudinal velocity, steering, body-frame displacement, arm rate, and bucket rate. On a real-world dataset from a wheel loader, sensVLA reaches aggregate per-step parity with a strong camera-only baseline and reduces longitudinal velocity RMSE by 28% and displacement error by 9% on loading centric scenarios. It also degrades 29% less when the camera stream is corrupted or removed, evidencing that explicit spatial grounding improves accuracy and fault-tolerance for heavy equipment autonomy.

---


### 138. [Sparse MLLM Anchors, Dense Adaptation: Breaking the Self-Referential Loop in Wild Test-Time Adaptation](https://arxiv.org/abs/2609.17040)

**<font color=#1a73e8>作者：</font>** Zhenbin Wang, Lei Zhang, Lituan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wild test-time adaptation (WTTA) updates a source model online under small test batches, concurrent distribution shifts, and time-varying class imbalance. Most WTTA methods derive their adaptation signals, including predictive uncertainty, sample reliability, and local feature geometry, from the model being adapted. When the source model is unreliable under shift, these signals can reinforce its own errors, forming a self-referential loop. We introduce MASA (Multimodal-LLM-Anchored Semantic Adaptation), which complements model-internal evidence with structured semantic descriptions from a frozen multimodal large language model (MLLM). To limit inference cost, MASA queries the MLLM only for a small set of diverse, reliability-ranked anchors. The resulting descriptions capture the object family and nuisance factors such as style, viewpoint, and occlusion. MASA encodes these descriptions, propagates them to neighboring test samples, and stores the resulting visual-semantic information in an online prototype memory. Descriptor-aware retrieval from this memory provides an auxiliary target for lightweight adaptation of normalization-affine parameters. We evaluate MASA on the WTTA ImageNet-C benchmark under limited-batch, mixed-domain, and imbalanced-label-shift settings with ResNet and ViT backbones.

---


### 139. [Beyond "ChatGPT Can Make Mistakes": Designing Interventions to Support Metacognitive Monitoring in AI-Assisted Work](https://arxiv.org/abs/2609.17065)

**<font color=#1a73e8>作者：</font>** Manuel A. D. Santos, Paul Thiesse, Steeven Villa 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI assistance places a metacognitive demand on users, who must judge their own competence and the system's. Yet designers lack comparative evidence on which interventions to choose, where to place them, and how to tell whether they worked. We elicited 30 interventions from 11 experts and, with prior work, organized them into a design space of time (when an intervention acts), level (whose competence is judged), and source (who supplies the monitoring cue). A between-subjects experiment (N = 917; 12 planning-and-organizing problems) compared a per-task reliability card, contrasting replies, pause points, and post-problem reflection against a baseline LLM assistant. Reliability cards and contrasting replies reduced estimation error and overconfidence and increased aggregate confidence discrimination. No task-performance improvement or average within-item discrimination gain was established. We contribute a shared vocabulary, a design space, and evidence that measured monitoring and task performance are separable design targets.

---


### 140. [EviScope: Paired Counterfactual Evidence Diagnostics for Faithful and Efficient Grounded Language Models](https://arxiv.org/abs/2609.17081)

**<font color=#1a73e8>作者：</font>** Suryadeep Singh Deswal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grounded language-model systems are often evaluated by final answer accuracy, yet a correct answer can be unsupported, drawn from the wrong source, or produced when evidence is insufficient or contradictory. We introduce EviScope, a paired counterfactual benchmark that holds the question fixed while adding, removing, distracting, or contradicting its evidence. EviScope-v1.1 contains 40 four-condition quartets with repaired counterfactual claims and span-level support labels for automatic evaluation. Across 960 gold-blind generations from Qwen2.5-7B, Llama 3.1 8B, and Gemini 3.5 Flash, paired metrics expose model-dependent grounding behavior that answer accuracy hides. On two local open models, an explicit evidence-action gate underperforms vanilla RAG on QCS: 0.15 vs. 0.50 for Qwen and 0.10 vs. 0.375 for Llama. Gemini reaches 0.944 joint success under both prompts, yet still answers 5% of conflict cases after contradiction insertion. EviScope therefore distinguishes unsupported answering, conflict blindness, and wrong non-answer actions rather than scoring answers alone.

---


### 141. [Interactive Memory Learning for Long-Term Conversations](https://arxiv.org/abs/2609.17088)

**<font color=#1a73e8>作者：</font>** Cai Ke, Jiangyue Yan, Han Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advancements in large language models have significantly enhanced the capabilities of agents in modeling long-term conversations. Despite these successes, existing approaches typically adopt a static heuristic paradigm, where information is passively archived without adaptive memory valuation. Consequently, these methods fail to self-evolve or align their memory management with evolving user needs. To address this, we propose ICML (InteraCtive Memory Learning), a multi-agent framework that transforms the memory mechanism from a passive archive into a learnable, interactive memory policy. Specifically, we first employ a session synthesis pipeline to generate expert data, facilitating rapid test-time adaptation in unseen scenarios. Building on this, ICML utilizes an online reinforcement learning mechanism where a Planner agent selectively encodes high-value information and a Trigger agent dynamically retrieves it to optimize response quality, whereby the two agents co-evolve through continuous interaction feedback. Crucially, both agents are synchronized through a delayed reward mechanism that propagates future feedback back to earlier storage decisions, ensuring memory policies are precisely aligned with user expectations. Experimental results demonstrate that ICML significantly outperforms strong baselines, exhibiting the unique capability to continuously improve response quality as interactions accumulate.

---


### 142. [Symbolic Separation: Grounding Deep Agents in Knowledge Graphs for Trustworthy Operational Data Analytics](https://arxiv.org/abs/2609.17107)

**<font color=#1a73e8>作者：</font>** Baibek Davletiyarov, Junaid Ahmed Khan, Andrea Bartolini  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI promises natural language access to the massive numerical telemetry of data centers and Industry 4.0 installations, yet text-to-query and tool-using agents stay unreliable: even frontier models answer little more than half of real-world database questions, and far fewer of the multi-step, operational ones, because the LLM must compose how heterogeneous sources relate and hallucinates the relations, not just the fields. We propose symbolic separation: a deep agent reasons freely but may act on data only through an ontology-constrained Virtual Knowledge Graph with deterministic pre-execution validation. Unlike a tool API's interface contract, this domain-semantic contract turns a complex question into one validated graph traversal instead of LLM-inferred joins. Instantiated as the Neurosymbolic Deep Analyst and evaluated on 49.9 TB of superconputer telemetry against a rigid workflow and a non-symbolic ablation, it raises end-to-end task success from 43% to 86%, prevents silent data-integrity errors that no syntactic check catches, and cuts token cost by 2.4x, letting a smaller on-premise model outperform a larger one.

---


### 143. [Shared-Prefix KV Reuse Across Standard LoRA Adapters: Quality and Serving Tradeoffs](https://arxiv.org/abs/2609.17109)

**<font color=#1a73e8>作者：</font>** Dushyant Rajput  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A common small-model deployment runs one shared backbone with several LoRA specialists that answer over the same context. Serving them naively re-prefills that shared context once per specialist. We study a narrow, practical question: for already-trained standard LoRA adapters -- not adapters retrained for cache compatibility -- how much task quality is preserved if the backbone's prefill KV cache is computed once and reused across specialists, and what does that buy in serving cost? On a Qwen3-1.7B backbone with two adapters (extractive QA on HotpotQA, arithmetic reasoning on GSM8K), we sweep the boundary at which the specialist takes over from the reused base cache and measure paired quality differences and serving cost. Full-prefix reuse had the lowest prefill cost and a small quality difference on held-out GSM8K (Delta = -4.6 EM at a 160-token budget; -3.0 at 320 tokens; -0.8 under a second training seed -- all favoring native, only the first excluding zero, and the magnitude not consistent). Partial recomputation provided no demonstrated advantage. Neither quality equivalence nor a general boundary-selection rule is established. We also report a closed-form ridge KV translator that did not beat direct reuse, and specialist-dependence contrasts whose intervals all include zero. The measured serving benefit is warm-cache time-to-first-token, which grows with context (~16x at 8K); two-branch peak memory was only 12% lower and, on inspection, the prefix was never physically shared across branches -- this implementation reuses KV values but copies their storage, so shared-cache memory savings are not achieved.

---


### 144. [Enhancing Procedural Writing Through Personalized Example Retrieval: A Case Study on Cooking Recipes](https://arxiv.org/abs/2609.17118)

**<font color=#1a73e8>作者：</font>** Paola Mejia-Domenzain, Jibril Frej, Seyed Parsa Neshaei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Writing high-quality procedural texts is a challenging task for many learners. While example-based learning has shown promise as a feedback approach, a limitation arises when all learners receive the same content without considering their individual input or prior knowledge. Consequently, some learners struggle to grasp or relate to the feedback, finding it redundant and unhelpful. To address this issue, we present RELEX, an adaptive learning system designed to enhance procedural writing through personalized example-based learning. The core of our system is a multi-step example retrieval pipeline that selects a higher quality and contextually relevant example for each learner based on their unique input. We instantiate our system in the domain of cooking recipes. Specifically, we leverage a fine-tuned Large Language Model to predict the quality score of the learner's cooking recipe. Using this score, we retrieve recipes with higher quality from a vast database of over 180,000 recipes. Next, we apply BM25 to select the semantically most similar recipe in real-time. Finally, we use domain knowledge and regular expressions to enrich the selected example recipe with personalized instructional explanations. We evaluate RELEX in a 2 x 2 controlled study (personalized vs. non-personalized examples, reflective prompts vs. none) with 200 participants. Our results show that providing tailored examples contributes to better writing performance and user experience.

---


### 145. [An Empirical Study of Counterfactual Self-Explanations in LLMs](https://arxiv.org/abs/2609.17119)

**<font color=#1a73e8>作者：</font>** Giannis Kalyvas, Giorgos Filandrianos, Orfeas Menis Mastromichalakis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can easily generate explanations for their own outputs, but such self-explanations are not necessarily faithful to the model's behavior. We study this issue through counterfactual self-explanations, where a model minimally edits an input so that its own prediction changes. Across sentiment analysis and natural language inference, we evaluate ten instruction-tuned models from the LLaMA-3 and Qwen-2.5 families, measuring faithfulness, minimality, and alignment with human-annotated rationales. Our results show that model scale is the strongest determinant of explanation quality: larger models are substantially more likely to generate counterfactuals that flip their own predictions and target decision-relevant evidence. In contrast, the rationale-guided condition produces edit-minimal counterfactuals that are also more human-aligned. However, it does not consistently improve faithfulness. Overall, counterfactual self-explanations can provide useful behavioral evidence about model decisions, but their reliability depends strongly on model capacity and should be empirically validated rather than assumed.

---


### 146. [FirmCORe: A Benchmark for Structured Reasoning about Inter-Firm Collaboration Opportunities](https://arxiv.org/abs/2609.17128)

**<font color=#1a73e8>作者：</font>** Tian Du, Tiantong Wu, Yafei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Comprehensive structured data on inter-firm relationships is often scarce or inaccessible because many relationships are privately negotiated, selectively disclosed, and fragmented across proprietary databases. This scarcity hinders the discovery of collaboration opportunities, particularly for startups and small and medium-sized enterprises. Firm profiles are readily available, but collaboration potential cannot be inferred from business similarity alone, since similar firms may be competitors, whereas dissimilar firms may offer complementary products, technologies, channels, capabilities, or capital. We present FirmCORe (Inter-Firm Collaboration Opportunity Reasoning), a human-annotated benchmark for pairwise reasoning over weakly structured firm profiles, comprising 2,805 labeled firm pairs. Given two firm profiles, a model must determine whether the available evidence supports a collaboration opportunity and, for positive pairs, jointly predict its strength, primary collaboration type, and role direction. FirmCORe also provides parallel Chinese- and English-language evaluation sets containing identical instances and gold labels, enabling controlled analysis of input-language sensitivity. Experiments with representative locally deployed and hosted large language models (LLMs) show that the strongest model achieves a macro-F1 score of 74.51 for opportunity detection but only 61.57% exact match across all four output fields. Language effects vary across models, and high cross-language agreement can mask errors shared across languages. These results indicate that current LLMs are substantially more reliable at detecting broad collaboration opportunities than at identifying their specific types and role directions.

---


### 147. [A Scenario-Knowledge-Driven Pipeline for Just-in-Time Assistance](https://arxiv.org/abs/2609.17132)

**<font color=#1a73e8>作者：</font>** Zhiyuan Li, Tatsunori Hara, Jun Ota  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Detecting a silently struggling kiosk user is only the first step; deciding whether, when, and how to help depends on scenario knowledge usually buried in model weights and thresholds. We propose a scenario-knowledge-driven pipeline: a single scenario knowledge document, human-authored and version-controlled, configures sensing, constrains LLM reasoning, and shapes a graded intervention proposal. Narration, assistance-need assessment, and proposal are kept separate for independent audit. As proof of concept, we replay two recorded kiosk sessions offline, chosen before the runs for their struggle evidence and retrospective detail. Both cases support what the design promises: checkable reporting and measured escalation. Across 95 updates, every sentence of the append-only narration cites the primitive events underlying it, and the rule layer detects 12 of 13 and 7 of 7 annotated struggle episodes under a strict criterion. The assessor de-escalates on recovery and reaches the top rung exactly once, under maximally converging evidence. At the decisive help-seeking turn, narration, assessment, and the participants' retrospective accounts converge. The appropriateness of these interventions, the pipeline's restraint on sessions without struggle, and the document's transfer to a new scenario frame the agenda.

---


### 148. [ResLRP: The Role of Residual Cancellation in Attribution Instability in Vision Transformers](https://arxiv.org/abs/2609.17152)

**<font color=#1a73e8>作者：</font>** Jim Berend, Reduan Achtibat, Daniel Schäffer 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) are central to most modern vision models, yet obtaining input attributions that are fine-grained, faithful, and stable remains challenging. Layer-wise Relevance Propagation (LRP) has been adapted to transformer attention, but in ViTs it often produces noisy, unfaithful explanations. We show that the missing ingredient is the treatment of residual connections: cancellation effects in residual pathways lead to attribution explosion. Moreover, we find that these cancellations are substantially stronger in ViTs than in language transformers. To address this issue, we introduce Residual-aware Layer-wise Relevance Propagation (ResLRP), a simple extension of LRP whose propagation rules explicitly account for cancellations in residual branches, are exactly conservative, and provably bound relevance explosion. Causal channel-wise interventions confirm that residual cancellation, not a generic regularization effect, drives the instability. ResLRP substantially improves attribution quality across faithfulness and localization, evaluated on ViT architectures spanning supervised, self-supervised, contrastive, hierarchical, and multimodal families, as well as on the ground-truth-controlled FunnyBirds benchmark. The largest gains arise in modern Vision Language Models (VLMs), with +27-29% localization and up to 3.4x faithfulness scores. Beyond benchmarks, ResLRP localizes Sparse Autoencoder (SAE) features in input space, and our residual amplification measure serves as an architecture-level diagnostic predicting where attribution degrades.

---


### 149. [Plug 'n' Pray: Agentic LLM-based Detection of Potential Log File Exposures in Third-Party Content Management System Plugins](https://arxiv.org/abs/2609.17164)

**<font color=#1a73e8>作者：</font>** Sebastian Neef  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Content Management Systems (CMS), such as WordPress, power a large share of the web (~58%), and their extensibility through third-party plugins is a major source of their popularity as well as of their attack surface. One high-impact weakness that remains understudied is log file exposure by CMS plugins, which create log files for debugging or other purposes. If these files are insufficiently secured, they can disclose sensitive information (e.g. credentials, personal data) which has led to website compromises in the past.
In this work, we present an agentic, LLM-based framework that automatically detects potential log file exposures in plugins of the most popular CMS (WordPress). Our agent analyzes each plugin by performing static and dynamic analysis.
We evaluated our approach on the 300 most-installed WordPress plugins (about 0.6% of all), which together account for over 250M active installations, i.e. 75% of all active installations in the official plugin ecosystem. We manually validated each finding, reproducing 79 of 81 findings from 62 plugins. We observed that several protective measures appear to be implemented that we classify as creation-control (e.g. manual log activation) and access-control (e.g. deny rules in .htaccess). However, we find that multi-layered protection is required, but not always present.
From these results we derive a taxonomy of log file path and protection patterns and deduce a set of best practices for developers to securely handle them. Finally, our study corroborates that agentic LLMs are an useful tool for security analysis.

---


### 150. [End-to-End Latency-Minimizing and Load-Balanced Request Scheduling for Edge LLM Inference in Agentic AI Services](https://arxiv.org/abs/2609.17193)

**<font color=#1a73e8>作者：</font>** Zhen Li, Jun Cai, Haoran Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-powered agentic AI services increasingly demand low-latency inference, motivating the deployment of LLMs across distributed edge servers. However, heterogeneous communication and computing capabilities, together with dynamically evolving inference states, make the edge server selection for each incoming request time-varying and tightly coupled across slots. In this paper, we investigate an online request scheduling framework for edge LLM inference that jointly minimizes long-term average end-to-end latency and regulates workload distribution across heterogeneous edge servers. Two main challenges arise in this context. First, conventional latency models cannot accurately capture the fine-grained dynamics of multi-stage LLM execution. Second, the latency consequence of a scheduling decision is observed only after request completion, making immediate decision evaluation difficult. To address these challenges, we develop a cross-slot inference model that captures transmission, prefill, iteration-level decoding, and key-value (KV) cache evolution for each diverse request, and characterize server workload through a KV cache memory-time consumption metric. We propose the LYREO approach that transforms the long-term load-balancing constraint via Lyapunov optimization and employs reward redistribution with sequencebased return prediction to convert delayed outcomes into timely learning signals for earlier decisions. Simulations under various configurations demonstrate that LYREO consistently achieves lower latency and more balanced load distribution than representative learning-based and heuristic baseline schemes.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-189](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
