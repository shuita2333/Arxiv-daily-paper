# 🧠 大模型相关研究 | 2026年06月05日

> 本类共 **137** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-137](./part-03.md)

---

### 51. [Hyper-ICL: Attention Calibration with Hyperbolic Anchor Distillation for Multimodal In-Context Learning](https://arxiv.org/abs/2606.04434)

**<font color=#1a73e8>作者：</font>** Niloufar Alipour Talemi, Hossein Kashiani, Fatemeh Afghah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal In-Context Learning (ICL) has emerged as a practical inference paradigm for Multimodal Large Language Models, where a small set of interleaved image-text In-Context Demonstrations (ICDs) conditions the model to solve new tasks. Despite its flexibility, multimodal ICL incurs high inference latency and suffers from instability due to sensitivity to demonstration formatting, ordering, and content. To address these limitations, we propose Hyper-ICL, a lightweight, training-based framework for demonstration-free multimodal ICL that reconstructs demonstration effects directly without requiring ICDs at inference time. Hyper-ICL learns a parameter-efficient low-rank logit-level adapter that calibrates attention distributions to better match demonstration-induced attention redistribution. To capture how demonstration influence varies across queries, we introduce a query-adaptive modulation mechanism that adaptively controls intervention strength at token level across layers and heads based on the current query. Finally, we propose a layer-wise hyperbolic anchor distillation loss that aligns intermediate student features to a demonstration-conditioned teacher via Lorentz geodesic distance. This loss encourages the student to reconstruct the demonstration-query relationships induced by ICDs. Extensive experiments across six different multimodal benchmarks (including VQAv2, OK-VQA, and COCO Caption) demonstrate that Hyper-ICL consistently improves accuracy and stability over vanilla ICL and existing state-of-the-art methods.

---


### 52. [Cascading Hallucination in Agentic RAG: The CHARM Framework for Detection and Mitigation](https://arxiv.org/abs/2606.04435)

**<font color=#1a73e8>作者：</font>** Saroj Mishra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-step agentic retrieval-augmented generation (RAG) pipelines have demonstrated significant capability for complex reasoning tasks, yet remain vulnerable to a class of failure that existing hallucination detection mechanisms systematically miss: cascading hallucination, where errors introduced at early pipeline stages propagate and amplify across successive reasoning steps, producing confident but factually incorrect final outputs. To address this vulnerability, we formalize cascading hallucination as a distinct failure mode in agentic RAG systems, present a four-type taxonomy of cascade patterns, and introduce CHARM (Cascading Hallucination Aware Resolution and Mitigation), an architectural framework for detecting and interrupting error propagation in multi-step reasoning pipelines. CHARM comprises four components - stage-level fact verification, cross-stage consistency tracking, confidence propagation monitoring, and cascade resolution triggering - that operate alongside standard agentic RAG pipelines without requiring architectural replacement. We evaluate CHARM on HotpotQA, MuSiQue, 2WikiMultiHopQA, and a custom adversarial dataset across LangChain agentic pipeline configurations, achieving an 89.4% cascade detection rate with a 5.3% false positive rate and 215 ms +/- 18 ms average latency overhead per stage, achieving an error propagation reduction of 82.1%, compared to 18.5% for output-level detectors. Component ablations confirm that each detection module contributes meaningfully to overall cascade coverage. CHARM integrates with human-in-the-loop oversight frameworks to provide a complete reliability and governance stack for production agentic AI deployment.

---


### 53. [LoopMoE: Unifying Iterative Computation with Mixture-of-Experts for Language Modeling](https://arxiv.org/abs/2606.04438)

**<font color=#1a73e8>作者：</font>** Wenkai Chen, Tianshu Li, Wenyong Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) and looped architectures scale models along two orthogonal axes, namely parameter capacity and effective depth. However, mainstream looped architectures rely on dense backbones that couple parameter count with per-token FLOPs, which makes it impossible to isolate the effect of iterative computation under matched budgets. To this end, we present LoopMoE, a looped MoE language model that integrates sparse routing with iterative weight-shared computation through two designs. The first is IterAdaLN, which resolves weight-sharing symmetry via a modulation signal jointly conditioned on the iteration index and the per-token hidden state. The second is a capacity-balancing strategy that recovers the attention-to-FFN active parameter ratio of well-tuned non-looped references. Together, these designs enable the first strictly controlled, head-to-head evaluation of a looped MoE against a Vanilla MoE under identical total parameters, per-token FLOPs, and active sublayer ratios. At the 3B scale, LoopMoE outperforms the Vanilla MoE on 8 of 9 downstream benchmarks with an average improvement exceeding 1 point. At the 9B scale, LoopMoE continues to outperform the matched Vanilla MoE, indicating that the architectural gain persists at larger scale. Our work establishes a controlled synthesis of sparsity and recurrence, and suggests a promising direction for looped language models.

---


### 54. [Listening to the Workforce: Measuring Construction Worker Safety Attitudes from Social Media Discourse Using LLMs](https://arxiv.org/abs/2606.04450)

**<font color=#1a73e8>作者：</font>** Farouq Sammour, Yuxin Zhang, Zhenyu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Worker safety attitudes are key determinants of whether protective practices are applied or bypassed on construction sites. Yet measuring them at scale has remained out of reach. Safety attitudes are multidimensional, vary across topics, and surface most candidly in workers' own conversations. This study created and validated the Construction Safety Attitude Framework (CSAF), which integrates two components: a theory-grounded structure that characterizes safety attitudes along eight dimensions, and an operational codebook for measuring them in worker naturalistic discourse. Applying CSAF to 250 posts and comments from the r/Construction community on Reddit, trained coders reached strong agreement (Krippendorff's {\alpha} = 0.85). Pairwise lift and conditional probability confirmed that the eight dimensions are related yet distinct. To apply the framework across large volumes of discourse, CSAF was operationalized through a large language model (LLM) classifier. On 450 r/Construction contributions, the classifier reproduced expert human coding (Cohen's \k{appa} = 0.90, precision = 0.98, recall = 0.98), and on 400 contributions from r/Roofing it retained that accuracy after transfer to a different trade community (\k{appa} = 0.89, precision = 0.98, recall = 0.97). A proof-of-value case study then applied the validated classifier to 10,346 contributions from r/Roofing, demonstrating that CSAF can distinguish multidimensional attitudes by safety topic, track how they shift over time, and trace the reasoning behind unfavorable ones. The study therefore provides a theoretically grounded, empirically vetted instrument for examining safety attitudes, offering a basis for targeted interventions that address the attitudes underlying unsafe practices.

---


### 55. [Stepwise Reasoning Enhancement for LLMs via External Subgraph Generation](https://arxiv.org/abs/2606.04454)

**<font color=#1a73e8>作者：</font>** Xin Zhang, Yang Cao, Baoxing Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have shown strong performance in natural language generation and downstream reasoning tasks, but they still struggle with logical consistency, factual grounding, and interpretability in complex multi-step reasoning. To address these limitations, this paper proposes SGR, a stepwise reasoning enhancement framework that integrates large language models with external knowledge graphs through query-relevant subgraph generation. Given an input question, SGR first extracts key entities, relations, and constraints to construct a structured schema, then retrieves compact subgraphs from a knowledge graph using schema-guided querying. The generated subgraphs provide explicit relational evidence that guides the language model through step-by-step reasoning. In addition, SGR combines direct Cypher-based reasoning with collaborative reasoning integration, allowing candidate answers from multiple reasoning paths to be validated and aggregated according to both model confidence and graph consistency. Experiments on benchmark datasets including CWQ, WebQSP, GrailQA, and KQA Pro demonstrate that SGR improves reasoning accuracy and Hits@1 performance over standard prompting and several knowledge-enhanced baselines. Ablation studies further show that schema guidance and Neo4j-based retrieval are both crucial to the effectiveness of the framework. These results indicate that dynamically generated external subgraphs can improve the accuracy, robustness, and interpretability of LLM-based reasoning.

---


### 56. [Learning What to Learn: Stage-Specific Data Sets for SFT-then-RL in Small Language Model Reasoning](https://arxiv.org/abs/2606.04466)

**<font color=#1a73e8>作者：</font>** Chongyang He, Rui Zhang, Zixuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training Small Language Models (SLMs) for reasoning typically follows an SFT-then-RL pipeline, yet existing work rarely considers what data should be learned at each stage. We argue that data strategy should be aligned with the distinct roles of SFT and RL: SFT is better suited for acquiring not-yet-mastered reasoning skills, while RL is better suited for consolidating skills that the model can already partially access. Based on this principle, we propose a difficulty-aware SFT-then-RL framework that organizes training data into stage-specific sets. For hard samples in the SFT stage, we introduce a Bridge mechanism that transforms raw teacher-generated reasoning traces into more learnable supervision for SLMs. For hard samples that remain unsolved during RL, we apply Critique Fine-Tuning by converting all-zero-reward failures into diagnostic, repair, and new reasoning trace supervision for the next SFT stage. Experiments on two SLMs across five reasoning benchmarks show that our method consistently improves over representative SFT, distillation, and RL baselines. Our results highlight the importance of coordinating data difficulty across SFT and RL for effective SLM reasoning post-training.

---


### 57. [Entity Binding Failures in Speech LLM Reasoning: Diagnosis and Chain-of-Thought Intervention](https://arxiv.org/abs/2606.04474)

**<font color=#1a73e8>作者：</font>** Ming-Hao Hsu, Xiaohai Tian, Jun Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech Large Language Models (SLLMs) underperform their text counterparts on complex reasoning. We reveal that this modality gap is not a uniform cognitive deficit. Evaluating three diverse SLLMs, we show speech-to-text (S2T) matches or exceeds text-to-text (T2T) on spatial, syntactic, and factual tasks. However, on logical tasks requiring entity tracking, S2T accuracy collapses to chance. We diagnose this localized degradation as an entity binding failure: continuous speech features cause models to lose precise entity-property associations during implicit reasoning. To resolve this, we propose Entity-Aware Chain-of-Thought (EA-CoT), forcing SLLMs to explicitly enumerate entities and bind them to claims before reasoning. Strikingly, EA-CoT bridges the gap, even when spoken names are misrecognized, yielding up to a 24.4% absolute accuracy improvement. Ablations confirm these gains stem entirely from explicit semantic binding, reframing the gap as a resolvable bottleneck.

---


### 58. [Off-Distribution Voices: Fanfiction Subgenres as Universal Vernacular Jailbreaks for Aligned LLMs](https://arxiv.org/abs/2606.04483)

**<font color=#1a73e8>作者：</font>** Zhongze Luo, Ruihe Shi, Zhenshuai Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing jailbreaks against aligned LLMs are discrete artifacts whose surface forms are easy to fingerprint and patch. We argue that the real failure mode is not any specific prompt, but an entire register of natural human writing that safety training has under-covered. Building on this insight, we introduce the first jailbreak family that uses real fanfiction subgenres as universal attack carriers: a creative-writing meta is conditioned on passages from one of twelve Archive of Our Own (AO3) subgenres, and the harmful behavior is embedded as the climax of the resulting scene. The construction requires no attacker LLM and no per-target adaptation. On eight aligned LLMs over the union of HarmBench and JailbreakBench, this attack lifts mean ASR from 0.278 to 0.731 under a four-judge ensemble; a factorial decomposition shows the gain is carried by register rather than length or structure. Two active defences widen rather than narrow the vernacular-to-baseline ratio, indicating that template-targeting defences merely steer attackers toward register-based attacks like ours. We also propose SAGA-A4, a static four-turn extension that attains mean ASR 0.924, substantially exceeding three existing multi-turn methods.

---


### 59. [AgentJet: A Flexible Swarm Training Framework for Agentic Reinforcement Learning](https://arxiv.org/abs/2606.04484)

**<font color=#1a73e8>作者：</font>** Qingxu Fu, Boyin Liu, Shuchang Tao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present AgentJet, a distributed swarm training framework for large language model (LLM) agent reinforcement learning. Unlike centralized frameworks that tightly couple agent rollouts with model optimization, AgentJet adopts a decoupled multi-node architecture in which swarm server nodes host trainable models and run optimization on GPU clusters, whereas swarm client nodes execute arbitrary agents on arbitrary devices. This design provides capabilities that are difficult to support in centralized frameworks: (1) heterogeneous multi-model reinforcement learning, enabling the training of heterogeneous multi-agent teams with multiple LLM as brains; (2) multi-task cocktail training with isolated agent runtimes; (3) fault-tolerant execution that prevents external environment failures from interrupting the training process; and (4) live code iteration, which allows agents to be edited during training by replacing swarm client nodes. To support efficient RL in multi-model, multi-turn, and multi-agent settings, AgentJet introduces a context tracking module with timeline merging, which consolidates redundant context and achieves a 1.5-10x training speedup. Finally, AgentJet introduces an automated research system that takes a research topic as input and autonomously conducts long-horizon, multi-day RL studies on large-scale clusters. By leveraging the swarm architecture, this system reproduces key exploratory workflows of RL researchers without human intervention during execution.

---


### 60. [LimiX-2M: Mitigating Low-Rank Collapse and Attention Bottlenecks in Tabular Foundation Models](https://arxiv.org/abs/2606.04485)

**<font color=#1a73e8>作者：</font>** Yuanrui Wang, Xingxuan Zhang, Han Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) increasingly rival tree ensembles, but their performance is often compute-inefficient: with standard affine scalar tokenization, each feature injects value variation through an essentially one-dimensional channel, and feature IDs/positional signals cannot increase within-feature value degrees of freedom, yielding weak early-layer value sensitivity and redundant hidden states. We present a unified \emph{tokenize-and-route} framework for strong TFMs: \textbf{RaBEL} expands each scalar into compact localized RBF features (optionally exponent-gated) to improve conditioning and shallow-layer effective rank, while a reordered bidirectional block \textbf{S$\rightarrow$N$\rightarrow$F} aligns computation with the readout by aggregating cross-sample context before feature mixing and using attention pooling. Together, these changes yield \textbf{LimiX-2M}, a 2M-parameter model that outperforms larger TabPFN-v2 and TabICL baselines on widely used tabular benchmarks while reducing training and inference costs. These results highlight value-aware tokenization and readout-aligned routing as key levers for improving the accuracy--efficiency trade-off in TFMs. Model checkpoints and inference code are available at this https URL.

---


### 61. [Simulate, Reason, Decide: Scientific Reasoning with LLMs for Simulation-Driven Decision Making](https://arxiv.org/abs/2606.04505)

**<font color=#1a73e8>作者：</font>** Yuhan Yang, Ruipu Li, Alexander Rodríguez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific simulators are increasingly being integrated into LLM-driven systems for high-stakes simulation-driven decision-making. However, existing frameworks primarily use LLMs to generate, calibrate, or execute simulators, treating them as black-box interfaces rather than as structured mechanistic systems that can be reasoned about. As a result, current approaches lack the ability to identify, represent, and reason about the assumptions and mechanisms underlying simulator behavior, limiting transparency, auditability, and decision justification. We introduce MechSim, a mechanism-grounded neuro-symbolic reasoning framework for executable scientific simulators. Unlike prior neuro-symbolic approaches that primarily reason over static symbolic structures, MechSim enables LLM agents to reason about the mechanisms, assumptions, and execution behavior of scientific simulators. Our framework represents simulators through a shared structured schema capturing assumptions, variables, mechanism dependencies, and execution traces. On top of this representation, LLM agents operate as constrained reasoning engines that generate structured, evidence-grounded explanations linking simulator outcomes to their underlying mechanisms. We evaluate our approach across multiple high-stakes domains and show that it improves mechanism-level explanation quality, simulator analysis, and downstream decision-making reliability.

---


### 62. [Self-Evolving Deep Research via Joint Generation and Evaluation](https://arxiv.org/abs/2606.04507)

**<font color=#1a73e8>作者：</font>** Han Zhu, Chengkun Cai, Yuanfeng Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have become increasingly adopted in daily applications, with deep research standing out as a particularly important capability. Unlike traditional question-answering (QA) tasks, deep research report generation lacks definitive ground-truth, making reward design inherently unverifiable and limiting effective reinforcement learning. Existing approaches mitigate this challenge with LLM-as-a-judge and query-dependent evaluation rubrics, but they still rely on static evaluators that cannot adapt their standards as the solver improves, leading to insufficient and eventually saturated optimization pressure. We address this limitation with a \textbf{s}elf-evolving \textbf{co}-evolutionary training framework for deep \textbf{re}search evaluation and generation (SCORE), which tightly couples an evaluator and a solver in a shared-parameter learning process. Rather than treating generation and evaluation as isolated modules, we leverage their intrinsic connection to enable joint improvement within a single shared-parameter model. To restrict this process, we introduce a meta-harness, which dynamically controls the evaluation environment based on solver performance, encouraging valid evaluation dimensions and sufficiently deep evaluator search. Extensive experiments on deep research benchmarks demonstrate consistent improvement in report generation quality, showing that co-evolving evaluation and generation is a promising direction for training open-ended research agents.

---


### 63. [SparDA: Sparse Decoupled Attention for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2606.04511)

**<font color=#1a73e8>作者：</font>** Yaosheng Fu, Guangxuan Xiao, Xin Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse attention reduces compute and memory bandwidth for long-context LLM inference. However, two key challenges remain: (1) KV cache capacity still grows with sequence length, and offloading to CPU memory introduces a PCIe transfer bottleneck; (2) the sparse selection step itself retains $O(T^2)$ complexity and can dominate attention cost at long contexts. We propose SparDA, a decoupled sparse attention architecture that introduces a fourth per-layer projection, the Forecast, alongside Query, Key, and Value. The Forecast predicts the KV blocks needed by the next layer, enabling lookahead selection that overlaps CPU-to-GPU prefetch with current-layer execution. Because Forecast is decoupled from the attention query, our GQA implementation uses one Forecast head per GQA group, reducing selection overhead versus the original multi-head selector. SparDA adds $<$0.5% parameters and trains only the Forecast projections by matching the original selector's attention distribution. On two sparse-pretrained 8B models, SparDA matches or slightly improves accuracy and delivers up to 1.25$\times$ prefill speedup and 1.7$\times$ decode speedup over the sparse-attention offload baseline. By enabling larger feasible batch sizes on a single GPU, SparDA further reaches up to 5.3$\times$ higher decode throughput than the non-offload sparse baseline. Our source code is available at this https URL.

---


### 64. [MapAgent: An Industrial-Grade Agentic Framework for City-scale Lane-level Map Generation](https://arxiv.org/abs/2606.04513)

**<font color=#1a73e8>作者：</font>** Deguo Xia, Zihan Li, Haochen Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Lane-level maps are critical infrastructure for autonomous driving and lane-level navigation, yet constructing and maintaining standardized lane networks for hundreds of cities remains highly labor-intensive. Recent end-to-end vectorized mapping methods can predict lane geometry and topology directly from sensor data, but they typically treat mapping specifications and traffic regulations as implicit, dataset-dependent supervision. Moreover, in complex scenes (e.g., worn or missing markings and occlusions), correct lane configurations are often under-determined by visual evidence alone, making specification violations a major source of human post-editing. We propose MapAgent, an industrial-grade agentic architecture that augments a vectorization backbone for specification-compliant lane-map production. Rather than merely adding an agent loop to map prediction, MapAgent couples backbone perception with explicit specification verification, constraint-aware reasoning, and deterministic map editing under a bounded, verification-driven Judge-Planner-Worker loop. A vision-language Judge diagnoses errors by jointly inspecting visual evidence and draft vectors, while a tool-calling Planner generates minimal corrective edits with post-edit re-validation. To remain scalable for city-scale production, MapAgent is selectively triggered only on tiles with low backbone confidence, adding modest overhead while preserving throughput. Experiments on real-world datasets show consistent gains over strong production baselines, especially in complex and long-tail scenarios. Additionally, MapAgent has been integrated into Baidu Maps, supporting lane-level map generation for over 360 cities nationwide and elevating the overall production automation to over 95%, demonstrating MapAgent's practicality and effectiveness for large-scale lane-level map generation.

---


### 65. [Dynamic Infilling Anchors for Format-Constrained Generation in Diffusion Large Language Models](https://arxiv.org/abs/2606.04535)

**<font color=#1a73e8>作者：</font>** Boyan Han, Yiwei Wang, Yi Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) offer bidirectional attention and parallel generation, enabling them to exploit global context and naturally support format-constrained tasks like parseable JSON or reasoning templates. While straightforward fixed anchors can enforce such constraints, they often impose rigid spans, leading to truncated reasoning or redundant content. To overcome this, we propose Dynamic Infilling Anchors (DIA), a training-free method that dynamically estimates end-anchor positions to adjust generation length before iterative infilling. This flexible mechanism ensures structural correctness and semantic coherence, avoiding the inefficiencies of fixed-span methods. Experiments on reasoning benchmarks demonstrate that DIA substantially improves format compliance and answer accuracy, achieving significant zero-shot gains on GSM8K and MATH. These results establish DIA as a robust pathway toward reliable, structure-aware generation.

---


### 66. [Impostor: An Agent-Curated Benchmark for Realistic AIGC Manipulation Localization](https://arxiv.org/abs/2606.04545)

**<font color=#1a73e8>作者：</font>** Zhenliang Li, Yutao Hu, Qixiong Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative image editing have improved the realism and controllability of localized image manipulation, raising new challenges for image manipulation detection and localization (IMDL). However, existing IMDL benchmarks still have limitations in visual realism, manipulation diversity, and generator coverage, making it difficult to reflect recent trends in image manipulation. To address these limitations, we introduce Impostor, a high-quality AI-edited image manipulation localization dataset containing 100K manipulated images. Impostor is constructed by CraftAgent, a closed-loop agent framework that integrates scene perception, editing planning, manipulation execution, quality validation, and iterative reflection to automatically generate diverse and visually realistic manipulated images. Moreover, Impostor contains images generated by seven recent AIGC models across three manipulation types and includes multiple manipulated regions, providing a more comprehensive benchmark for AIGC-based IMDL. Furthermore, we propose PhaseAware-Net (PANet), a semantic-forensic framework that introduces local phase modeling and semantic-forensic consistency learning to better localize semantically plausible yet forensically disrupted manipulated regions. Extensive experiments show that Impostor poses significant challenges to existing large vision-language models (LVLMs) and specialized IMDL methods, while PANet achieves superior performance on Impostor and multiple public benchmarks.

---


### 67. [Temporal Order Matters for Agentic Memory: Segment Trees for Long-Horizon Agents](https://arxiv.org/abs/2606.04555)

**<font color=#1a73e8>作者：</font>** Yifan Simon Liu, Liam Gallagher, Faeze Moradi Kalarde 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon conversational agents need to interact with users through evolving events, tasks, and goals. Such histories are naturally temporal, yet many existing memory systems organize information primarily by topical similarity and may ignore the order in which events occur. We introduce Segment Tree Memory, or SegTreeMem, a memory architecture that represents conversation history as a temporally ordered Segment Tree over utterances. SegTreeMem incrementally inserts new utterances through an online rightmost-frontier update rule, preserving chronological order while forming hierarchical memory segments. For retrieval, SegTreeMem propagates relevance scores through the tree to combine local semantic matching with hierarchical temporal context. Across three long-horizon memory benchmarks and two LLM backbones, SegTreeMem improves answer quality over flat retrieval, graph-structured memory, and tree-structured memory baselines. Additional temporal-order permutation analysis shows that the performance gain depends on preserving temporal order during memory construction, supporting the claim that temporal order is a key structure for agentic memory.

---


### 68. [Cartridges at Scale: Training Modular KV Caches over Large Document Collections](https://arxiv.org/abs/2606.04557)

**<font color=#1a73e8>作者：</font>** Momchil Hardalov, Gonzalo Iglesias, Adrià de Gispert  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models can reason over long contexts, yet prefilling millions of tokens is wasteful as much of the content remains static across queries. Cartridges address this by distilling document collections into reusable key-value (KV) caches that eliminate prefilling while preserving accuracy. A critical limitation of this approach is that cartridges are monolithic and non-compositional: encoding an entire collection into a single KV block does not scale, and naively mixing cartridges trained in isolation collapses performance to near chance. We introduce Cartridges at Scale (CAS), a training framework for scalable multi-cartridge learning with dynamic distractor mixing and a memory-efficient budget manager that rotates hundreds of per-document cartridges between GPU and persistent storage. Our approach scales to collections exceeding a million tokens, improving over a monolithic cartridge by 10-31 points at comparable token budgets. Oracle cartridge accuracy falls within 2-6 points of full in-context learning even at high compression. When paired with retrieval for cartridge selection, CAS matches or exceeds conventional RAG accuracy while consuming 3-4x fewer prompt tokens.

---


### 69. [Rollout-Level Advantage-Prioritized Experience Replay for GRPO](https://arxiv.org/abs/2606.04560)

**<font color=#1a73e8>作者：</font>** Gyeongtae Yoo, Sanghyeok Park, Soohyuk Jang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from verifiable rewards with GRPO is a standard approach for post-training reasoning LLMs. It remains sample inefficient. Each rollout is used for a single gradient update and then discarded. Naive replay is not well suited in this setting because LLM policies drift quickly per gradient step. Stored rollouts therefore become stale and can destabilize training. We propose a rollout-level replay buffer for GRPO that stores and samples individual rollouts rather than whole groups. The buffer bounds staleness through age eviction. Any rollout older than tau_max training steps is removed. The buffer also preserves on-policy data via fresh-anchored composition. Each batch keeps its fresh on-policy rollouts and then concatenates replay rollouts drawn separately from the buffer. We prioritize replay by per-rollout advantage magnitude and recycle individual rollouts whose advantages are large. Across three Qwen3-Base scales on five math benchmarks, our method outperforms GRPO and naive replay baselines. Gains are positive at every scale and grow with model size. The largest gain is +4.35 pp on the five-benchmark average at 4B. Under an AES metric that jointly measures accuracy and token efficiency, the efficiency margin over GRPO is again largest at 4B, at +0.579.

---


### 70. [SurvPFN: Towards Foundation Models for Survival Predictions](https://arxiv.org/abs/2606.04564)

**<font color=#1a73e8>作者：</font>** Samuel Böhm, Lennart Purucker, Frank Hutter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) have made rapid progress in standard classification and regression, but time-to-event survival prediction tasks have remained largely untouched. Unlike in standard regression tasks, survival prediction models must account for censored data. Standard TFMs cannot handle natively censored data, leading to biased and inaccurate predictions, making them unsuitable for real-world applications. To overcome this fundamental limitation, we propose \texttt{SurvPFN}, a prior-data fitted network (PFN), for survival prediction tasks. We pretrain \texttt{SurvPFN} on millions of synthetic survival prediction tasks to learn survival via distributional regression that accounts for censored data. \texttt{SurvPFN} works by (1) generating data with Weibull event times and a non-informative censoring mechanism; (2) integrating a censored event indicator; and (3) minimizing a censored negative log-likelihood. On SurvSet, a collection of real-world survival tasks, \texttt{SurvPFN} is highly competitive with classical and deep survival baselines without per-dataset fitting, a survival-specific architecture, or feature engineering. We show that survival can be treated as a continuous-time distributional regression problem with censored loss, unlocking the power of PFNs for time-to-event predictions.

---


### 71. [VCIFBench: Evaluating Complex Instruction Following for Video Understanding](https://arxiv.org/abs/2606.04588)

**<font color=#1a73e8>作者：</font>** Huangchen Xu, Yuan Wu, Yi Chang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models have made rapid progress in video understanding, yet existing benchmarks largely rely on simple prompts and provide limited evidence about whether models can satisfy explicit output constraints. We introduce VCIFBench, a benchmark for evaluating complex instruction following in video understanding. VCIFBench constructs constraint-rich instructions from both benchmark-adapted and directly video-grounded prompts, covering content, format, style, and structure requirements, and evaluates model outputs with a hybrid verification pipeline. The benchmark contains 306 satisfiable test instructions, a 540-pair DPO preference dataset, and a 30-item conflict diagnostic subset. Experiments on 10 MLLMs show that joint constraint satisfaction remains challenging. We further show that DPO training on VCIFBench data can improve instruction-following performance.

---


### 72. [Fine-grained Fragment Retrieval in Multi-modal Long-form Dialogues](https://arxiv.org/abs/2606.04591)

**<font color=#1a73e8>作者：</font>** Hanbo Bi, Zhiqiang Yuan, Chongyang Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the widespread adoption of multi-modal communication platforms, long-form dialogues interleaving text and images have become increasingly common. Users often need to retrieve coherent dialogue fragments related to specific topics, rather than isolated utterances. We propose Fine-grained Fragment Retrieval (FFR), which locates semantically relevant multi-utterance, multi-image fragments in multi-modal long-form dialogues. We explore two settings: (1) FFR within Single-Dialogue, retrieving fragments from a given dialogue; and (2) FFR within Dialogue Corpus, retrieving from a large-scale corpus for open-domain scenarios. For (1), we introduce F2RVLM, a generation-based retrieval model trained with reinforcement learning, using multi-objective rewards and difficulty-aware curriculum sampling to enhance fragment coherence. For (2), we develop FFRS, a two-stage system combining offline fragment-level indexing with online retrieval. Specifically, each dialogue is decomposed into minimal semantic fragments encoded by a Fragment Embedding Model (FEM) into a vector database; at inference, FEM rapidly recalls Top-K candidates, and F2RVLM performs fine-grained reasoning to identify the most relevant sub-content. To support FFR, we construct MLDR, the longest multi-modal dialogue retrieval dataset to date, and a WeChat-based real-world test set. Experiments on both benchmarks demonstrate that F2RVLM and FFRS consistently achieve superior performance across single-dialogue and corpus-level FFR.

---


### 73. [A Systematic Evaluation of Positional Bias in Multi-Video Summarization with MLLMs](https://arxiv.org/abs/2606.04596)

**<font color=#1a73e8>作者：</font>** Huangchen Xu, Yuan Wu, Yi Chang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) are increasingly used for video understanding, yet their reliability under multi-video inputs remains poorly understood. We study positional bias in multi-video summarization, where the quality of a per-video summary can change with the video's input slot even when the underlying content is unchanged. We construct a benchmark from ActivityNet and News videos, covering Cooking, Domestic, Leisure, and News settings with two- and four-video inputs. We evaluate nine open-source and proprietary MLLMs and measure position effects with three complementary metrics: Coverage, Directional Positional Bias (DPB), and Middle-Edge Gap (MEG). Our results show that positional effects are domain- and model-dependent: signed directional bias can be small even when middle positions underperform, and increasing visual or generation budget does not uniformly remove the imbalance. We further analyze prompt-level mitigation methods. Together, the results show that multi-video summarization remains sensitive to input protocol and position, motivating more robust order-invariant multimodal systems.

---


### 74. [Plan First, Judge Later, Run Better: A DMAIC-Inspired Agentic System for Industrial Anomaly Detection](https://arxiv.org/abs/2606.04599)

**<font color=#1a73e8>作者：</font>** Yongzi Yu, Ao Li, Le Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents have shown promise in automating complex data-analysis workflows, but their reliable deployment remains challenging in high-stakes industrial scenarios. Industrial anomaly detection (IAD) is essential for manufacturing quality, safety, and efficiency, yet existing LLM-based IAD agents mainly focus on execution while under-exploiting strategy formulation. Consequently, they struggle to handle heterogeneous modalities in a unified and cost-effective manner. Inspired by the DMAIC quality-management framework, we propose DMAIC-IAD (DMAIC-inspired Agentic Industrial Anomaly Detection), a "Plan First, Judge Later" multi-agent system that aligns LLM agents with structured industrial problem-solving. DMAIC-IAD distills heterogeneous references into standardized operating procedures (SOPs) before strategy generation, and introduces a pre-trained execution-free judge model to rank candidate strategies without costly runtime trials. Extensive experiments across four modalities show that DMAIC-IAD improves average detection performance over applicable agentic baselines by 37.76%.

---


### 75. [Beyond Symmetric Alignment: Spectral Diagnostics of Modality Imbalance in Vision-Language Models in the Medical Domain](https://arxiv.org/abs/2606.04613)

**<font color=#1a73e8>作者：</font>** Alessandro Gambetti, Qiwei Han, Cláudia Soares 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) struggle when applied to medical image-text data, yet the tools available to diagnose this failure remain limited. Existing representation alignment metrics are symmetric, collapsing both modalities into a single score and hiding which modality drives cross-modal degradation. We introduce the Spectral Alignment Score (SAS), an asymmetric metric that projects both modalities onto the principal eigenbasis of an anchor modality and computes eigenvalue-weighted per-eigenmode correlations, resulting in directional scores whose difference quantifies modality information imbalance. We embed SAS within a benchmarking framework evaluating 15 VLMs across natural and medical image-text datasets alongside 6 alignment metrics and bidirectional retrieval. Our experiments show that medical images retain richer structural information than their paired clinical reports, a directional asymmetry invisible to all competing metrics, and that SAS achieves the strongest zero-label correlation with retrieval performance in the medical domain, positioning it as a practical diagnostic tool for clinical deployment. Code is available at this URL: this https URL.

---


### 76. [QuBLAST: A Framework for Quantizing Large Language Models with Block-Level Compression Approach and Activation Scaling Strategy](https://arxiv.org/abs/2606.04620)

**<font color=#1a73e8>作者：</font>** Pasindu Wickramasinghe, Achyuta Muthuvelan, Rachmad Vidya Wicaksana Putra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs have become the state-of-the-art algorithms for solving NLP tasks. However, they typically come at huge computational and memory costs, thus making them difficult to deploy on embedded systems. Toward this, state-of-the-art methods typically employ uniform post-training quantization (PTQ) across attention blocks of the network, hence overlooking the potential of applying different quantization levels in the same network. They also employ complex operations to mitigate the negative impact of activation outliers, hence incurring high computational overheads. Moreover, they have not considered evaluation using emerging LLMs with non-conventional attention architectures (e.g., state-space models), which pose different challenges in applying quantization. To address these limitations, we propose QuBLAST, a novel PTQ methodology that employs block-level compression approach with activation scaling strategy for LLMs. Block-level compression approach enables mixed-precision quantization across blocks of the network, while activation scaling strategy efficiently mitigates the negative impact of activation outliers. Specifically, QuBLAST first analyzes the sensitivity of different attention blocks in the pre-trained model through the cross-entropy loss analysis. QuBLAST leverages this sensitivity analysis to determine the weight quantization level for each attention block in the model. Furthermore, QuBLAST employs the activation scaling map for each block to control the range of activation values and mitigate the negative impact of activation outliers, thereby enabling better quantization results. Experimental results show that, QuBLAST reduces model sizes by 40%-45.2% across different model architectures (i.e., Qwen3-8B, Llama3-8B, Mistral v0.1-8B, and Falcon H1R-7B), while maintaining the performance within 5% perplexity increase for the WikiText-2 and WikiText-103 datasets.

---


### 77. [MIRAGE: Mobile Agents with Implicit Reasoning and Generative World Models](https://arxiv.org/abs/2606.04627)

**<font color=#1a73e8>作者：</font>** Zhichao Yang, Yuanze Hu, Haojie Hao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mobile agents are increasingly expected to operate everyday applications from screenshots and language goals, where reliable control requires reasoning over screen affordances, multi-step navigation, and future state changes. However, many agents externalize this computation as long textual chains of thought, which slows interaction, increases supervision cost, and complicates deployment. We introduce MIRAGE, a framework that learns continuous latent reasoning representations from visible textual reasoning traces. MIRAGE transfers explicit reasoning into compact hidden states, enabling the agent to reason internally without decoding long rationales. It also incorporates a generative world-model objective: latent reasoning vectors are aligned with future screenshots, encouraging the agent to anticipate upcoming interface states before acting. This turns hidden computation into both a compressed thought representation and a forward-looking model of environment dynamics. At inference time, MIRAGE reasons in continuous latent space, reducing token generation while improving execution efficiency. On AndroidWorld, MIRAGE matches explicit chain-of-thought supervised fine-tuning in the 4B ablation with a 3-5x lower decoded-token budget and improves a comparable instruction-tuned baseline by 10.2 points; on AndroidControl, it improves action grounding while generating over 75% fewer tokens.

---


### 78. [RAMPART: Registry-based Agentic Memory with Priority-Aware Runtime Transformation](https://arxiv.org/abs/2606.04628)

**<font color=#1a73e8>作者：</font>** Nikodem Tomczak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> RAMPART is a compile-time memory model and pure in-RAM block registry for LLM-based agents. Context assembly is a programmable runtime operation where content is compiled from a structured registry under explicit policy for ordering, inclusion, and eviction. Five composable primitives (promote, gate, write, evict, rollback) act on named addressable blocks before compilation at zero prompt-token cost. Provenance tags and non-evictable authorship flags implement a permissioned memory model with block-level ownership. Controlled probes with Qwen3-8B Q4 show that compile-time placement and the structural relationship between blocks and the task query affect task success, with the cliff falling at roughly the seventh block position when the task follows the registry and the twelfth when it precedes. Grouping the critical block with content-adjacent neighbours and promoting the group as a unit lifts task success by tens of percentage points at positions where single-block placement fails. Cross-model replication on Qwen2.5-7B, Llama-3.1-8B, Mistral-7B-v0.3, and Qwen3-14B shows the content-priming effect appears at the same absolute positions across families, with magnitude varying with model strength. Block grouping raises Mistral's mean pass rate roughly fivefold at the hardest registry size, and a smaller model with the intervention can outperform a larger model without it in the mid-registry zone. Relevance gating reduces prompt cost by 67.8\% while recovering 83% of the promoted-condition success rate. Schema eviction produces 0% invocations against 100% with the schema present, a property policy-based approaches cannot guarantee by construction. Shared-registry coordination reduces inter-agent communication to a method call at zero coordination token cost.

---


### 79. [VentAgent: When LLMs Learn to Breathe -- Multi-Objective Arbitration for ARDS Ventilation](https://arxiv.org/abs/2606.04632)

**<font color=#1a73e8>作者：</font>** Teqi Hao, Yuxuan Fu, Xiaoyu Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanical ventilation for Acute Respiratory Distress Syndrome (ARDS) requires balancing competing physiological goals, including oxygenation, lung protection, and acid-base homeostasis. However, current data-driven methods, especially those imitating retrospective Electronic Health Records (EHR), often suffer from imitation bias. They may capture superficial correlations from inconsistent clinical demonstrations, such as associating passive ventilator settings with survival because such settings are common in stable patients, and thus fail to generalize to volatile or out-of-distribution phenotypes. Standard Reinforcement Learning (RL) methods also struggle with the adversarial trade-offs of critical care and often produce opaque policies with limited clinical interpretability. To address these limitations, we introduce VentAgent, a hierarchical framework in which Large Language Models (LLMs) act as transparent arbitrators for mechanical ventilation. We reformulate ventilation control as a dynamic Multi-Objective Arbitration process rather than single-objective optimization. VentAgent decomposes decision-making into three interpretable stages: Perception, Planning, and Orchestration. By leveraging the semantic reasoning capabilities of LLMs, it synthesizes strategies from heterogeneous experts and resolves conflicting clinical priorities through an explicit coordination mechanism. Evaluations on a high-fidelity physiological simulator show that VentAgent outperforms state-of-the-art RL and classical control baselines. Moreover, it converts control decisions into human-readable reasoning chains, offering a safer, more interpretable, and adaptable paradigm for critical care automation.

---


### 80. [Rethinking Continual Experience Internalization for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.04703)

**<font color=#1a73e8>作者：</font>** Jingwen Chen, Wenkai Yang, Shengda Fan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Experience internalization converts contextual experience from past interactions into reusable parametric capability, offering a promising path toward continual learning in large language models (LLMs). While prior work has predominantly focused on single-iteration transfer, we discover that under multi-iteration experience learning, existing methods suffer from a progressive capability collapse rather than compounding improvement. We systematically examine this failure through three vital dimensions of experience internalization: (1) Experience Granularity: We find that principle-level experience is more durable than instance-level experience, as it effectively abstracts transferable strategies away from trajectory-specific details. (2) Experience Injection Pattern: Our analysis reveals that step-wise injection significantly outperforms global injection by aligning experience with intermediate decision states, a property that is critical for long-horizon tool use. (3) Internalization Regime: We demonstrate that off-policy context-distillation on high-quality teacher trajectories provides a substantially more stable training signal than on-policy context-distillation, which is inherently limited by local corrections on student-induced flawed states. Together, these insights yield a simple yet robust recipe for stable and sustainable experience internalization, providing concrete guidance for engineering self-evolving and continually learning LLMs.

---


### 81. [Query-based Cross-Modal Projector Bolstering Mamba Multimodal LLM](https://arxiv.org/abs/2606.04719)

**<font color=#1a73e8>作者：</font>** SooHwan Eom, Jay Shim, Gwanhyeong Koo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Transformer's quadratic complexity with input length imposes an unsustainable computational load on large language models (LLMs). In contrast, the Selective Scan Structured State-Space Model, or Mamba, addresses this computational challenge effectively. This paper explores a query-based cross-modal projector designed to bolster Mamba's efficiency for vision-language modeling by compressing visual tokens based on input through the cross-attention mechanism. This innovative projector also removes the need for manually designing the 2D scan order of original image features when converting them into an input sequence for Mamba LLM. Experimental results across various vision-language understanding benchmarks show that the proposed cross-modal projector enhances Mamba-based multimodal LLMs, boosting both performance and throughput.

---


### 82. [Physics-Informed Video Generation via Mixture-of-Experts Latent Alignment](https://arxiv.org/abs/2606.04737)

**<font color=#1a73e8>作者：</font>** Cong Wang, Hanxin Zhu, Jiayi Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale video generation models have made remarkable progress in semantic consistency and visual quality, producing videos that are increasingly coherent and visually convincing. Nevertheless, the dynamics induced by pixel-level fitting do not naturally accommodate the regularities that govern real-world motion and interaction, resulting in persistent shortcomings in physical plausibility. To address this limitation, we propose \textbf{PILA} (Physics-Informed Latent Alignment), a framework that injects physics-structured latent guidance into the frozen flow-matching dynamics of pretrained video models. Specifically, PILA first employs anchored field estimation to map frozen-generator latents into an operational physical attribute bank organized by field-proxy slots, using observable motion as a kinematic anchor for constructing less directly observed proxies. To handle the heterogeneity of real-world dynamics, PILA adopts a mixture-of-experts design over physical categories. Label-prior masked expert routing selects category-specific operator experts, whose refinements are regularized by operational residuals abstracted from physical relations. Finally, the refined proxies are fused into the physical attribute bank and decoded into a correction to the flow-matching vector field, injecting physics-aware guidance while preserving the visual prior of the pretrained backbone. With staged adapter training on Wan 2.1-1.3B and direct transfer of the learned adapter to Wan 2.2-14B, PILA achieves state-of-the-art results on VBench-2.0, VideoPhy-2, and PhyGenBench in both visual quality and benchmark-measured physical plausibility.

---


### 83. [FALSIFYBENCH: Evaluating Inductive Reasoning in LLMs with Rule Discovery Games](https://arxiv.org/abs/2606.04751)

**<font color=#1a73e8>作者：</font>** Leonardo Bertolazzi, Katya Tentori, Raffaella Bernardi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as autonomous agents in scientific tasks. Yet whether these systems can effectively engage in forms of inductive reasoning relevant to scientific discovery remains an open question. In this work, we introduce FALSIFYBENCH, an evaluation framework for hypothesis-driven reasoning inspired by the classic Wason 2-4-6 task, in which agents must discover hidden semantic properties by iteratively proposing examples and receiving feedback. This task captures key elements of scientific reasoning: hypothesis generation, evidence gathering, and belief revision in response to both confirming and disconfirming evidence. Our evaluation of 12 LLMs across model families and scales shows that reasoning models are generally stronger scientific reasoners than instruction-tuned models, although no model comes close to optimal performance. The primary driver of success is the capacity for negative testing: models that actively seek to falsify their hypotheses consistently outperform those that primarily seek confirmation. Moreover, a fine-grained turn-level analysis, neglected in previous work, reveals that failure is tied to identifiable patterns in how models navigate the hypothesis space.

---


### 84. [Do Foundation Models See Biology? Evaluating Attention Coherence with Spatial Transcriptomics in Glioblastoma](https://arxiv.org/abs/2606.04764)

**<font color=#1a73e8>作者：</font>** Dilakshan Srikanthan, Amoon Jamzad, Paul Wilson 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whether attention maps from pathology foundation models capture genuine biology remains unknown, yet this question is critical for clinical trust and regulatory approval. We propose a spatial transcriptomics-based framework for orthogonal, hypothesis-free evaluation of attention and apply it to five pathology foundation models (CONCH v1.5, UNI v2, Virchow2, GigaPath, H-Optimus-1) and a ResNet50 baseline. Using attention-based multiple instance learning, we train single-task and multi-task models to predict five molecular alterations in glioblastoma on the CPTAC cohort, validate on an independent TCGA cohort, and evaluate biological coherence of attention maps against 87 transcriptional signatures using co-registered Visium spatial transcriptomics data from 18 samples. Internally, no single encoder dominates across all tasks, and external validation inverts internal performance rankings. Attention maps show a five-fold enrichment gradient from pathways (Cohen's d=0.329) to individual genes (d=0.055), indicating that attention captures emergent multi-gene transcriptional programs rather than individual molecular events. Spatially smooth attention maps do not imply biological coherence, and different encoders attend to distinct biological compartments. Our framework provides objective, quantitative assessment of what foundation models learn from histopathology, moving the field beyond qualitative saliency map review.

---


### 85. [NextMotionQA: Benchmarking and Judging Human Motion Understanding with Vision-Language Models](https://arxiv.org/abs/2606.04773)

**<font color=#1a73e8>作者：</font>** Yong Cao, Chuqiao Li, Xianghui Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable evaluation of human motion understanding is fundamental to advancing embodied AI, robotics, and animation. However, existing benchmarks suffer from coarse semantic granularity, undifferentiated difficulty, limited annotation quality, and pervasive answer ambiguity, leaving them unable to diagnose where current models fail. To bridge this gap, we introduce NextMotionQA, a comprehensive benchmark that leverages vision-language models (VLMs) for semi-automated, expert-verified dataset. NextMotionQA features three complementary tasks: multiple-choice question answering, video captioning, and fine-grained error correction. Each task is systematically structured across three core semantic axes and stratified into three task complexity levels. Our extensive evaluation of twelve representative VLMs uncovers critical capability gaps and weakness that remain invisible under conventional, single-task evaluations. In a complementary direction, recent work has begun using VLMs as judges for text-to-motion evaluation; we ask whether they show the same degradation under harder tasks. We find that VLMs align strongly with expert ratings on coarse criteria (Cohen's \kappa=0.70) but break down on fine-grained, part-level judgment (\kappa=0.10), validating the paradigm in its strong regime while clarifying its limits.

---


### 86. [Inference-Time Vulnerability Beyond Shallow Safety: Alignment Along Generation Trajectories](https://arxiv.org/abs/2606.04778)

**<font color=#1a73e8>作者：</font>** Kyungmin Park, Taesup Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety-aligned Large Language Models (LLMs) remain vulnerable to interventions during inference that redirect generation toward harmful outputs. Recent work attributes this to shallow safety, where alignment concentrates in the first few output tokens. We show that shallow safety is a special case of a broader inference-time vulnerability, in which short token injections at any generation step can substantially alter subsequent safety behavior. We also find that a model's alignment with refusal directions in its hidden states does not predict its robustness to such injection, revealing that internal state alone does not determine generation behavior under perturbation. To address this, we align models directly on generation trajectories constructed by simulating mid-sequence perturbation, and show that this improves robustness to mid-sequence injection and generalizes to attacks that exploit early-token generation. Our work argues that robust safety alignment requires training on the generation process itself, not only its outputs.

---


### 87. [PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents](https://arxiv.org/abs/2606.04780)

**<font color=#1a73e8>作者：</font>** Yubo Hou, Jingwei Song, Hongbo Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persistent LLM agents require memory representations that make the formation of person understanding explicit across long term interaction. Existing agent memory methods emphasize information retention and retrieval, yet give limited account of how accumulated interaction evidence is abstracted into person understanding. We view this process as schema formation, where situated evidence is abstracted into reusable patterns and stable person level claims. We introduce PersonaTree, a structured lifecycle memory framework that realizes this view as a three level persona tree with explicit support paths from evidence to claims. PersonaTree maintains the tree through conservative writing, confidence guided consolidation, and query conditioned path retrieval, returning only the evidence depth required by each query. Across six person understanding and persistent memory benchmarks with three answer backbones, PersonaTree ranks first in 12 of 18 compact scores and reaches the top two in 16 settings. Ablations show that hierarchy improves abstract person understanding on KnowMe, while support path retrieval improves RealPref alignment under a comparable context budget.

---


### 88. [A Pathology Foundation Model for Gastric Cancer with Real-World Validation](https://arxiv.org/abs/2606.04792)

**<font color=#1a73e8>作者：</font>** Ling Liang, Jiabo Ma, Zhengyu Zhang 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gastric cancer remains a major cause of cancer mortality, yet its histological and molecular heterogeneity complicates diagnosis and risk stratification. General-purpose pathology foundation models (PFMs) often plateau on fine-grained endpoints central to gastric cancer care, and few have undergone rigorous prospective validation or clinical reader studies. We present GRACE, a Gastric-specific foundation model for Real-world Assessment and Clinical dEcision support. GRACE was developed from multicenter gastric pathology datasets totaling 48,364 primarily HE-stained whole-slide images from 37,493 patients. When evaluated on 28 clinically relevant tasks, GRACE consistently outperformed representative pancancer PFMs, achieving a macro-AUC of 0.9188, with strong performance for precancerous lesion diagnosis (macro-AUC 0.9322), tumor histopathological assessment (macro-AUC 0.9119), molecular profiling (macro-AUC 0.8682), and prognostic prediction. Beyond benchmarking, GRACE's translational value was substantiated through a rigorous evidence chain. Under safety-gated criteria requiring 100% NPV for rule-out and 100% PPV for rule-in, GRACE streamlined review for up to 69.6% of malignancy-diagnosis cases and triaged 46.8% of MMR-IHC follow-up requests. This translational feasibility was further strengthened by a randomized crossover reader study of pathologist-AI collaboration. With GRACE assistance, diagnostic accuracy improved from 82.0% to 89.9%, yielding nearly twofold higher adjusted odds of a correct diagnosis (OR 1.987) alongside concurrent gains in sensitivity and specificity. AI assistance also reduced diagnostic time by 14.9%, elevated diagnostic confidence by 9.0%, and markedly improved inter-rater agreement. When calibrated to maintain non-inferior performance to senior pathologists, the AI-assisted workflow could triage 60.7% of atrophy and 82.7% of intestinal metaplasia cases.

---


### 89. [NoRA: Evaluating Grounded Reasonableness in Visual First-person Normative Action Reasoning](https://arxiv.org/abs/2606.04806)

**<font color=#1a73e8>作者：</font>** Sichao Li, Sai Ma, Daniel Kilov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LLMs and agentic systems are increasingly deployed in social environments, making normative competence critical for safe and appropriate behavior. However, existing approaches either assess normative judgment in text alone or reduce it to choosing among a fixed set of candidate actions. We argue both are insufficient. In practice, agents are never handed a menu of options; they must identify a reasonable action from scratch, grounded in visible facts and supported by inspectable reasons. We introduce NoRA, a visual first-person video benchmark that requires models to generate candidate next actions and justify each through an explicit fact-reason-action support graph. The benchmark comprises 1,420 annotated video clips, including HumanGold-190 and LLMSilver-1230 splits. Each instance is evaluated through action alignment, factual grounding, and support binding, aggregated into a single grounded reasonableness score. We benchmark 12 multimodal systems under direct, deliberate, and structured prompting regimes, finding that current VLMs frequently recover plausible actions and relevant scene facts, but consistently struggle to construct the full reasonable action space and bind selected actions to the correct local support. NoRA makes this gap measurable, shifting the evaluation question from whether a model can pick an action to whether it can justify an appropriate action for the right visible reasons.

---


### 90. [BiasGRPO: Stabilizing Bias Mitigation in High-Variance Reward Landscapes via Group-Relative Policy Optimization](https://arxiv.org/abs/2606.04807)

**<font color=#1a73e8>作者：</font>** Saket Reddy, Ke Yang, ChengXiang Zhai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mitigating social bias in Large Language Models (LLMs) presents a distinct alignment challenge: unlike verifiable tasks, bias lacks a single ground truth, creating a high-variance, subjective reward landscape. Previous preference-based fine-tuning methods have major trade-offs: Direct Preference Optimization (DPO) is limited by the lack of exploration inherent in offline training, while Proximal Policy Optimization (PPO) can lead to training instability due to potentially unreliable critic estimates. In this paper, we propose BiasGRPO, a framework using Group Relative Policy Optimization (GRPO) to stabilize alignment by normalizing rewards across a group of sampled completions. By substituting the value function with a group-relative baseline, our approach reduces instability while maintaining the exploration benefits of online training. We find that BiasGRPO outperforms DPO and PPO across multiple benchmarks, indicating its effectiveness. To adapt GRPO, we synthetically extend a dataset spanning multiple domains and contexts. We also create and release a custom bias reward model that effectively guides generation while being highly compute-efficient and avoiding knowledge degradation, providing a valuable resource that can be seamlessly integrated into multi-objective RLHF pipelines.

---


### 91. [Learning While Acting: A Skill-Enhanced Test-Time Co-Evolution Framework for Online Lifelong Learning Agents](https://arxiv.org/abs/2606.04815)

**<font color=#1a73e8>作者：</font>** Bo Mao, Jie Zhou, Yutao Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lifelong learning is essential for Large Language Model (LLM) agents operating in dynamic, interactive environments. However, existing lifelong learning agents for long-horizon tasks typically depend on discrete skill or past experiences retrieval with static parameters during inference, which prevents them from continuously internalizing test-time feedback like human learners. To bridge this gap, we propose Skill-enhanced Test-Time Co-Evolution (\texttt{LifeSkill}), a two-stage reinforcement learning framework for Online Lifelong Learning Agents. Specifically, we design Verifier-Guided Skill Learning that addresses the lack of direct supervision for skill extraction by rewarding candidate skills according to the average verifier success of multiple skill-conditioned policy rollouts, encouraging the model to generate skills that are useful for solving tasks rather than merely plausible in text. Furthermore, we introduce Online Skill Internalization, which continuously improves the policy model during test-time interaction by transforming skill-conditioned trajectories into reward signals. This enables the agent to directly internalize reasoning capabilities into its parameters, avoiding the context bloat of experience retrieval. Experiments on LifelongAgentBench show that LifeSkill improves average performance by 7 absolute points by comparing with existing lifelong agent baselines.

---


### 92. [Beyond Objective Equivalence: Constraint Injection for LLM-Based Optimization Modeling on Vehicle Routing Problems](https://arxiv.org/abs/2606.04816)

**<font color=#1a73e8>作者：</font>** Xizi Luo, Changhong He, Dongdong Geng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly translate natural-language optimization problems into executable solver code. Yet for constraint-dense operations research (OR) problems, existing data-filtering and training pipelines largely rely on objective-equivalence signals such as differential testing and answer agreement, which a program can pass while adding spurious constraints or silently omitting required ones, whenever those constraints are non-binding on the tested instance. We propose constraint injection, which uses feasible probes to expose spurious over-constraint and one-constraint-violating probes to reveal silent constraint omission. Combined with differential testing, it forms a dual verifier. We instantiate and evaluate it on vehicle routing problems (VRPs), a representative constraint-dense combinatorial optimization testbed with coupled operational constraints. We develop VRPCoder, an 8B end-to-end model that translates natural-language VRP scenarios into Gurobi scripts, together with an expert-verified VRP benchmark suite covering 21 variants. The verifier is reused as a rejection-sampling filter during data synthesis and as a per-rollout reward in group relative policy optimization (GRPO). Across four VRP benchmarks, VRPCoder-GRPO reaches 93\% average Pass@1, outperforms Gemini-3.1-Pro Preview on three benchmarks, exceeds Claude-Sonnet-4.5 by 28 average points, and surpasses prior OR-LLMs by 78 average points.

---


### 93. [R-APS: Compositional Reasoning and In-Context Meta-Learning for Constrained Design via Reflective Adversarial Pareto Search](https://arxiv.org/abs/2606.04823)

**<font color=#1a73e8>作者：</font>** João Pedro Gandarela, Thiago Rios, Stefan Menzel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are fluent on open-ended tasks, yet in agentic settings, where a system must plan, use tools, and act over extended horizons, fluency does not ensure reliable delivery. We trace this gap to three coupled structural failures: errors propagate without localization, worst-case perturbations go unevaluated, and accumulated knowledge is never invalidated. We argue these share a root cause: abductive, counterfactual, meta-inductive, corrective, and inductive reasoning pull a shared context in incompatible directions. We introduce Reflective Adversarial Pareto Search (R-APS), to our knowledge the first method addressing all three failures jointly via reasoning-mode decomposition, allocating each reasoning mode its own context and orchestrating interaction across three timescales: staged compositional reasoning with a typed validation critic (failure localization), sensitivity-guided counterfactual stress-testing as a first-class Pareto objective (robustness), and meta-inductive rule extraction with explicit invalidation (persistent memory). R-APS requires no fine-tuning and operates on a frozen LLM purely via structured protocol design. We evaluate on planar mechanism synthesis (robotics, prosthetics, mechanical design), with every candidate checked by a kinematic solver. On 32 target trajectories, R-APS delivers robustness certificates 3.5x tighter than uniform-perturbation baselines, 46% faster iterations-to-first-admission, and 2.1x Chamfer-distance reduction over Enum+GA while jointly controlling bar-count and worst-case robustness. Small 4B reasoning-specialized models prove competitive with general-purpose 70B backbones inside the protocol, suggesting structured protocols can partially offset model scale.

---


### 94. [Large Language Models in K-12 Education: Alignment with State Curriculum Standards and Student Personas](https://arxiv.org/abs/2606.04846)

**<font color=#1a73e8>作者：</font>** Lisa Korver, Tomo Lazovich, Sherief Reda  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) become increasingly popular in educational settings, they raise important questions about the ethical implications of their use. Publicly available online chatbots are quickly improving in capability and accuracy leading to more widespread use, including among students looking for help with their homework. This makes it crucial to consider whether these models are aligned with educational standards. Because curriculum standards in the United States are set at the state level, they differ significantly in required content, emphasis, and narrative focus. In this work, we develop an LLM-based pipeline to identify variations in U.S. History curricula across states and evaluate the extent to which different LLMs reflect these state-specific curricular differences. In addition, we conduct controlled experiments that vary user personas by stating user attributes such as geographic location, grade level, gender and race to evaluate the sensitivity of LLM responses to user characteristics. We find that while models are able to adjust their presentation of historical topics, these shifts may come from the perceived political leanings of states and do not necessarily reflect actual curriculum content. Additionally, models successfully adapt to a student's grade level while showing minimal sensitivity to race or gender, suggesting they are capable of useful adaptation to student personas with limited demographic bias. Together, these findings highlight potential risks that open access to LLM chatbots may cause to student learning outcomes stemming from misalignment with state curriculum standards and highlight the need for more robust alignment techniques.

---


### 95. [MusaCoder: Native GPU Kernel Generation with Full-Stack Training on Moore Threads GPU](https://arxiv.org/abs/2606.04847)

**<font color=#1a73e8>作者：</font>** Kun Cheng, Songshuo Lu, Sicong Liao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Native GPU kernel generation turns high-level tensor programs into executable, efficient low-level code. Existing Large Language Models (LLMs) struggle with this task, while execution-based reinforcement learning suffers from sparse rewards, reward hacking, and training instability. We present MusaCoder, a full-stack training framework for native GPU kernel generation on CUDA and MUSA backends. MusaCoder combines progressive kernel-oriented data synthesis, diversity-preserving rejection fine-tuning, and execution-feedback Reinforcement Learning (RL) through MooreEval, a distributed verifier and reward environment. To stabilize RL, MusaCoder introduces PrimeEcho for first-turn-anchored multi-turn rewards, Buffered Dynamic Retry for recovering signals from all-failed hard samples, and MirrorPop for off-policy sequence filtering. Experiments on KernelBench and a MUSA-ported variant show that MusaCoder outperforms strong open-source and proprietary baselines in both correctness and empirical speedup, with the 9B model matching or exceeding frontier closed-source models and the 27B model establishing a new state of the art. These results demonstrate not only the effectiveness of full-stack execution-feedback training for native kernel generation, but also the capability of Moore Threads GPUs to support the complete LLM post-training stack, providing a practical foundation for large-model training and optimization on emerging accelerators.

---


### 96. [AICompanionBench: Benchmarking LLMs-as-Judges for AI Companion Safety](https://arxiv.org/abs/2606.04867)

**<font color=#1a73e8>作者：</font>** Yanjing Ren, Reza Ebrahimi, TengTeng Ma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI companion platforms such as Replika and this http URL rapidly grow, concerns about unsafe human-AI interactions have intensified. This study introduces AICompanionBench, to our knowledge the first publicly available benchmark dataset of human-AI companion conversations annotated with fine-grained safety risk categories. The dataset contains 2,123 real-world Replika conversations collected from Reddit and annotated through human-AI collaboration across nine categories: sexual behavior, antisocial behavior, physical aggression, verbal aggression, substance abuse, self-harm and suicide, control, manipulation, and no-harm. Using this benchmark, we evaluate 20 state-of-the-art open-source and closed-source LLMs under an LLM-as-judge framework for detecting unsafe interactions. Results show substantial variation in model performance, with stronger models achieving high overall accuracy but still struggling with nuanced categories such as manipulation, as well as benign conversations that are incorrectly identified as harmful. Our findings suggest that while current LLMs can effectively detect explicit harmful content, they remain limited in identifying implicit unsafe interactions. Overall, our work contributes a new benchmark dataset for AI companionship safety research and offers insights into monitoring AI companion systems using LLMs. The dataset is publicly available at: this https URL

---


### 97. [Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents](https://arxiv.org/abs/2606.04874)

**<font color=#1a73e8>作者：</font>** Haoyu Sun, Wenxuan Wang, Mingyang Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Planning is central to LLM agents: before acting, an agent must decompose goals, select tools, reason over constraints, and decide when a task is infeasible. Yet existing agent evaluations often report only end-to-end success, making it difficult to determine whether failures stem from planning or execution. We introduce \textbf{Agent Planning Benchmark (APB)}, a planning-specific diagnostic benchmark with 4,209 multimodal cases across 22 domains and five settings, covering holistic planning, feedback-conditioned step-wise planning, and robustness under extraneous tools, broken tools, and unsolvable tasks. Across 12 MLLMs, APB reveals systematic weaknesses in long-horizon planning, tool-noise robustness, calibrated refusal, and inference-time refinement. We further validate APB on 200 ToolSandbox tasks and 200 $\tau^2$-bench tasks, where APB-guided refinement consistently improves plan correctness, plan grade, and downstream execution metrics across three representative models. APB thus serves as an upstream diagnostic complement to execution benchmarks.

---


### 98. [Towards Pretraining Text Encoders for TabPFN](https://arxiv.org/abs/2606.04876)

**<font color=#1a73e8>作者：</font>** Mustafa Tajjar, Alexander Pfefferle, Lennart Purucker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models, such as TabPFN, achieve strong performance on tabular datasets with numerical and categorical data, but do not natively handle high-cardinality text features. Standard pipelines, therefore, embed text with a language model and compress the resulting vectors with PCA into a small number of scalar features before inputting them into TabPFN. This creates an information bottleneck: most embedding dimensions are discarded, and the compressed representation must then be expanded again by TabPFN's feature encoder. End-to-end alternatives can avoid PCA, but they require large amounts of pretraining data containing text cells and usually perform subpar compared to tabular foundation models that were pretrained on large amounts of synthetic data. Inspired by modality-alignment approaches like LLaVA (vision-to-LLM token projection) and TableGPT-style systems (table-to-LLM token projection), we introduce the TabPFN Text Adapter (text-to-TFM token projection). We freeze both the sentence encoder and TabPFN, and train only a lightweight adapter that maps text embeddings into a short sequence of tokens in TabPFN's embedding space. This design removes the PCA bottleneck, preserves TabPFN's numerical strengths, and is more efficient to train than end-to-end text-tabular pipelines.

---


### 99. [MAOAM: Unified Object and Material Selection with Vision-Language Models](https://arxiv.org/abs/2606.04880)

**<font color=#1a73e8>作者：</font>** Jaden Park, Valentin Deschaintre, Jason Kuen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Selection is a core operation in interactive image editing. To be practical, a user should be able to specify and disambiguate the desired selection region through either text or click-based interactions, and the system should support selecting not only objects but also other criteria, such as materials. Material-based selection is valuable for tasks like re-texturing surfaces or editing instances of a specific material. However, existing vision-language-model (VLM) based selection methods are object-centric and typically support a single interaction modality, limiting their applicability. In this work, we thus present Mask Any Object And Material (MAOAM), a unified selection framework that enables precise object and material-level selection across both text- and click-based interactions. MAOAM leverages a VLM with a segmentation head to produce pixel-accurate masks from user prompts: the VLM interprets the user's selection intent (object or material-level) and encodes visual entities, attributes, and spatial relations, while the segmentation head decodes the output token into a mask. A key challenge is the lack of material selection datasets with text annotations. We propose a scalable data generation pipeline: we collect real and synthetic images with material masks, and leverage VLMs to generate material descriptions with rich visual-semantics. We train MAOAM with a multi-task objective over click and text-based selection, along with an auxiliary VQA task derived from the material descriptions to facilitate deeper material understanding. Despite being trained with uni-modal prompts, our model exhibits an emergent improvement in selection when combining text and clicks at inference, enabling flexible image editing workflows. Experiments demonstrate accurate and coherent selections across diverse objects, materials, and interaction scenarios, highlighting robustness in practice.

---


### 100. [DiverAge: Reliable Pluralistic Face Aging with Cross-Age Identity Relation Guidance](https://arxiv.org/abs/2606.04881)

**<font color=#1a73e8>作者：</font>** Yueying Zou, Peipei Li, Qianrui Teng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face aging plays an important role in long-term biometric analysis, cross-age identity verification, and forensic identity analysis. Since the same subject may exhibit multiple plausible appearances at a target age due to genetic, environmental, and lifestyle factors, face aging is inherently a one-to-many generation problem. However, pluralism alone is insufficient for reliable face aging: a model should provide appearance-level candidate diversity within each age group while maintaining sequence-level ordinal reliability across ordered age groups. Existing deterministic aging methods can synthesize visually plausible age-progressed faces, but usually lack stochastic diversity. In contrast, pluralistic aging methods introduce local appearance variations, but often fail to explicitly regulate the identity evolution of the full aging sequence. In this paper, we propose \textbf{DiverAge}, a hierarchical pluralistic face aging framework based on diffusion autoencoding. DiverAge preserves appearance-level diversity through stochastic diffusion decoding and age-conditioned semantic modulation. To improve sequence-level reliability, we introduce a Cross-age Identity Relation Regulator (CARR), an inference-time guidance strategy that jointly denoises multiple target age groups. CARR is guided by a Cross-age Identity Similarity (CIS) prior estimated from real same-identity cross-age pairs, and suppresses excessive cross-age identity drift through one-sided sampling-time guidance without modifying the training objective or introducing extra trainable parameters. Experiments demonstrate that DiverAge improves sequence-level ordinal reliability while maintaining identity preservation, age accuracy, image quality, and appearance-level diversity.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-137](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
