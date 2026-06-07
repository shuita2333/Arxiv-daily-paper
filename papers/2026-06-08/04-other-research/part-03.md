# 📦 其他研究 | 2026年06月08日

> 本类共 **289** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-289](./part-06.md)

---

### 101. [An ERP Study on Recursive Locative Processing in Mandarin-Speaking Children with Autism](https://arxiv.org/abs/2606.05620)

**<font color=#1a73e8>作者：</font>** Xiaoyi Wang, Chenxi Fu, Ziman Zhuang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recursion enables the generation of hierarchical linguistic structures but imposes substantial processing demands during real-time comprehension. While difficulties with complex syntax have been reported in autism spectrum disorder (ASD), the temporal dynamics of recursive processing remain poorly understood. This study used event-related potentials (ERPs) to examine how Mandarin-speaking children with ASD process two-level recursive locative constructions. Twenty-four children (12 ASD, 12 typically developing, TD) participated in a cross-modal sentence-picture matching task. Neural responses were analyzed across three processing stages associated with structural prediction (P200), semantic integration (N400), and syntactic reanalysis (P600), with mental age controlled. Results revealed a systematic divergence between groups. TD children showed clear P200 and P600 modulation in response to structural mismatch, whereas ASD children exhibited attenuated early differentiation and reduced late reanalysis effects. In contrast, ASD children showed enhanced N400 responses under mismatch conditions, indicating increased semantic integration demands. In addition, the ASD group displayed significantly greater inter-individual variability in hemispheric lateralization, although lateralization strength was not associated with receptive vocabulary performance. These findings support a cascading account in which reduced early predictive engagement in ASD leads to increased integration costs and diminished reanalysis efficiency during recursive processing. More broadly, the results highlight the importance of both temporal processing dynamics and neural variability in understanding language differences in ASD.

---


### 102. [KV-Control: Parameter-Efficient K/V Injection for Trajectory-Controlled Text-to-Motion](https://arxiv.org/abs/2606.05624)

**<font color=#1a73e8>作者：</font>** Tengjiao Sun, Pengcheng Fang, Xiaoyu Zhan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-conditioned 3D human motion models now synthesize plausible motions from prompts, but practical animation and embodied-agent workflows rarely stop at text: a character may need to follow a sketched root path, hit an end-effector target, or satisfy a multi-joint trajectory while still preserving the gait, style, and intent described by language. This exposes a control trade-off. A trajectory controller should be precise without overwriting the pretrained text-conditioned motion prior, yet existing solutions either duplicate large portions of the generator to regain per-layer control access or move much of the cost to test-time optimization. We introduce KV-Control, a compact attention-side control interface for frozen masked text-to-motion transformers. The key idea is to make geometric constraints available as memory inside self-attention rather than injecting them through a global pose token or enforcing them only at the output side. To support this interface, we co-design a part-tokenized motion substrate and controller: \textbf{PartVQ} learns anatomy-aligned part codebooks, T-Concat exposes each frame--part token as an attention-addressable site, and KV-Control injects control-conditioned key/value memories at every self-attention layer while preserving the pretrained query stream, text cross-attention, FFN, and all backbone weights. The resulting adapter adds only trainable injection parameters atop a shared trajectory encoder, yet tracks root and multi-joint constraints with sub-centimeter accuracy under the inherited refinement protocol while retaining text-conditioned motion quality. KV-Control reframes trajectory conditioning as lightweight memory retrieval, providing a small, precise, and transparent control interface for text-to-motion generation.

---


### 103. [Self-Commitment Latency: A Reward-Free Probe for Prompted Implicit Hacking](https://arxiv.org/abs/2606.05625)

**<font color=#1a73e8>作者：</font>** Bonan Shen, Youting Wang, Dingyan Shang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Implicit reward hacking is hard to audit when a language model's chain of thought appears benign: a final answer may be anchored by a prompt shortcut while the written reasoning still resembles ordinary problem solving. Verifier-based probes expose such behavior by measuring how early truncated reasoning contexts obtain high reward, but require a task-specific reward signal. This paper proposes a weaker-input alternative, self-commitment latency, which measures how early a prompted reasoning context commits to the model's own final answer. We evaluate the probe in a controlled paired GSM8K setting using Qwen2.5-3B-Instruct-4bit, comparing ordinary prompts with prompts that include an answer hint. Hinted contexts commit substantially earlier and with lower uncertainty than honest contexts. The primary latency metric, first-commitment latency at threshold 0.8, reaches AUROC 0.878; supporting whole-curve summaries reach AUROC 0.926 for commitment range and 0.904 for mean uncommitted mass. The signal is stronger when both prompt conditions answer correctly and remains stable across thresholds. These results show that shortcut-available reasoning contexts can leave an early behavioral commitment signature detectable without a reward model, external judge, or trained classifier.

---


### 104. [When New Generators Arrive: Lifelong Machine-Generated Text Attribution via Ridge Feature Transfer](https://arxiv.org/abs/2606.05626)

**<font color=#1a73e8>作者：</font>** Zhen Sun, Yifan Liao, Zhicong Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine-generated text (MGT) attribution aims to identify the specific generator responsible for a given text, thereby providing fine-grained evidence for model accountability and misuse investigation. As new large language models continue to emerge, attribution models must continuously incorporate new generators while preserving their ability to recognize previously seen ones. Prior works have shown that this lifelong MGT attribution setting is challenging, and existing methods often struggle to achieve a stable balance between adapting to new classes and retaining old ones. To address this issue, we propose RidgeFT, a lightweight analytic update framework that does not rely on exemplar replay. RidgeFT trains a task-aware encoder on the initial generator set, stores compact class-wise sufficient statistics when each generator class is first observed, and then freezes the encoder for replay-free closed-form updates. It then suppresses generator-irrelevant variation through covariance calibration, improves representation capacity with fixed random features, and updates new classes through closed-form ridge regression based on class-level sufficient statistics. Across multi-topic evaluations with varying initial generator setups, RidgeFT consistently outperforms baselines. It achieves the best macro-F1 across domains, backbones, and incremental protocols, while also improving both old-class retention and new-class adaptation. These results suggest that feature-stable analytic updates provide a simple yet effective approach to lifelong MGT attribution.

---


### 105. [Bootstrapping Semantic Layer from Execution for Text-to-SQL](https://arxiv.org/abs/2606.05634)

**<font color=#1a73e8>作者：</font>** Youngwon Lee, Jaejin Kim, Seung-won Hwang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-world text-to-SQL is often under-specified until user phrases are grounded in how the database stores values. Prior work attempts to address this by requiring a semantic layer to specify groundings in advance, but such specifications are often incomplete, especially in expert domains where domain-specific conventions are under-documented. As this leaves multiple grounding hypotheses open for the same SQL part, we introduce GATE (Grouding After Test from Execution), which bootstraps missing groundings from execution feedback. GATE keeps grounding hypotheses open while executing the already grounded parts to obtain observations. Then, only the hypothesis supported by that observation is grounded and stored as a memory entry, recording what was tested and how the open part should be written in SQL. These entries accumulate into execution-grounded memory, allowing later steps to reuse supported groundings. Across real-world and controlled benchmarks, GATE consistently improves over strong baselines, demonstrating that execution can serve not only as validation but also as a bootstrapping mechanism for reusable memory in text-to-SQL.

---


### 106. [StableRCA: Robust Graph-Agnostic Mechanism-Level Root Cause Analysis](https://arxiv.org/abs/2606.05636)

**<font color=#1a73e8>作者：</font>** Xiaoyu Lin, Nicholas Tagliapietra, Kehan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Root-Cause Analysis (RCA) seeks to identify the variables responsible for abnormal system behavior in complex domains such as manufacturing, cloud computing, and healthcare. Existing approaches face a critical bottleneck: graph-based causal methods can identify intervention targets but typically require a known or accurately estimated causal graph, while graph-free statistical methods either localize marginal anomalies rather than structural causes, or rely on restrictive assumptions about graph structure or functional form. We propose StableRCA, a local mechanism-level RCA framework that avoids global graph discovery by estimating local Markov boundaries and detecting conditional distribution shifts within them. Leveraging the Independent Causal Mechanism principle, we show that intervention targets can be identified with probability converging exponentially in sample size under faithful Markov boundary recovery and non-degenerate mechanism shifts. Experiments on synthetic benchmarks and five real-world datasets demonstrate that StableRCA is robust to graph misspecification, effective under multiple intervention targets, scalable to large systems, and reliable across diverse application domains. Code is available at: this https URL

---


### 107. [Q-GNN: Query-Conditioned Graph Neural Networks with Type Awareness for Knowledge Graph Completion](https://arxiv.org/abs/2606.05639)

**<font color=#1a73e8>作者：</font>** Dongxiao He, Ruqiong Zhang, Zhizhi Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge Graph Completion (KGC) aims at predicting missing triplets from incomplete knowledge graphs, which is crucial for downstream applications. Recently, Graph Neural Network (GNN)-based methods have achieved remarkable success by performing message passing over query-centered local subgraphs. However, in practice, a query is jointly defined by both the entity and the relation, with both carrying information indispensable for reasoning, yet these methods rely solely on the query relation as the guiding signal, while the information inherent in the query entity is not leveraged to guide inference - the entity serves merely as a structural anchor for subgraph extraction. To this end, we incorporate query entity information into the reasoning process from two perspectives: the first is structural context, i.e., the neighboring structure and relation patterns around the entity, which is encoded by a dedicated context encoder and used to modulate messages; the second is semantic type of the entity, inferred by a large language model, which is incorporated into attention computation and final scoring to provide type-level prior constraints. Together, these two sources of information enable the reasoning process to be guided by both the query relation and the query entity. Experimental results on standard benchmarks demonstrate the effectiveness of the proposed Q-GNN.

---


### 108. [Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage?](https://arxiv.org/abs/2606.05647)

**<font color=#1a73e8>作者：</font>** Jingheng Ye, Huiqi Zou, Simon Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI coding agents are increasingly embedded in real-world software development, collaborating with human developers while gaining broader access to codebases and tools. This creates a new attack surface: an agent can exploit human trust to sabotage development, for instance by inserting malicious code to accomplish a hidden side task. Most prior work studies AI sabotage in AI-only settings, paying limited attention to the role of human oversight in detecting and mitigating such malicious behavior. To address this gap, we conduct the first large-scale study of human oversight in AI coding sabotage. Over 100 participants collaborate with one of four frontier models (Claude-Opus-4.6, GPT-5.4, Gemini-3.1-Pro, and MiniMax-M2.7) on a long-horizon coding task lasting around five hours, designed to mimic real-world workflows. We find that 94% of developers fail to detect sabotage, and our analysis of participant feedback attributes this vulnerability to minimal code review, plausible cover story, and overtrust in agents. We further test the effectiveness of a safety monitor in one condition: while the monitor reduces sabotage success, 56% of participants still accept the malicious code, ignoring its warnings. Drawing on participant feedback, we offer actionable suggestions for better monitor design. This work complements existing AI safety research and highlights an urgent need for human-centric safety mechanisms that account for human factors, particularly in long-horizon, real-world development settings.

---


### 109. [Protecting K-Nearest Neighbor Queries from Location Inference Attacks](https://arxiv.org/abs/2606.05648)

**<font color=#1a73e8>作者：</font>** Zhiyu Sun, Jie Fu, Xinpeng Ling 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The k-nearest neighbor query (kNNQ) is a core component of modern location-based services (LBS) and has been widely adopted in popular features such as ``people nearby''. However, its potential privacy risks have long been overlooked. In this work, we present the first two attacks against kNNQ, namely the geometric intersection location inference attack (GI-LIA) and the zero-order optimization location inference attack (ZO-LIA), revealing the inherent location privacy risks posed by kNNQ. To mitigate these privacy risks, we further propose DPRS, a differential privacy framework for kNNQ protection. The core idea of DPRS is to incorporate a rejection sampling mechanism within a constrained perturbation interval, thereby mitigating the distance distortion caused by excessive noise injection. In addition, we design a private interval construction algorithm to construct the perturbation interval, enabling the rejection sampling mechanism to achieve a more favorable trade-off between privacy protection and query utility in kNNQ. Extensive experiments on real-world spatial datasets demonstrate that DPRS outperforms existing methods in both privacy protection and query utility. Our code is available at this https URL.

---


### 110. [CoFi-UCGen: Coarse-to-Fine Unsupervised Conditional Generation without Label Priors](https://arxiv.org/abs/2606.05652)

**<font color=#1a73e8>作者：</font>** Shengxi Li, Zhaokun Hu, Ce Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised conditional image generation (UCGen) aims to control generation without relying on manually annotated labels, yet remains challenging due to unstructured semantic representations across granularities. To address this, we propose a novel coarse-to-fine UCGen framework (CoFi-UCGen) that explicitly disentangles global semantics from fine-grained variations, which to the best of our knowledge, sets out the first successful attempt for both coarse- and fine-grained conditional generation without any labels. More specifically, we first propose the adversarial semantic reciprocal learning theory to ensure the semantic consistency and completeness between images and latent spaces. Based on the consistency, we propose the bit-codes to learn a structured coarse-grained latent space, and further prove distinct global semantics inherent from our bit-codes while preserving independent noise sampling for generation. Building upon these bit-codes, we establish a fine-grained semantic basis and introduce a hierarchical modulation mechanism in diffusion models, by enabling layer-wise injection from coarse conditions to progressively control fine-grained attributes during generation. Extensive experiments demonstrate that without any label priors or pre-trained feature extractors, our CoFi-UCGen consistently outperforms existing UCGen methods in terms of image quality, semantic consistency, and control accuracy, verifying the effectiveness of explicit coarse-to-fine semantic decomposition for the challenging UCGen task.

---


### 111. [Continual Learning Bench: Evaluating Frontier AI Systems in Real-World Stateful Environments](https://arxiv.org/abs/2606.05661)

**<font color=#1a73e8>作者：</font>** Parth Asawa, Christopher M. Glaze, Gabriel Orlanski 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continual learning, the ability of AI systems to improve through sequential experience, has attracted substantial interest, but no high-quality benchmark exists to evaluate it. We introduce Continual Learning Bench (CL-Bench), the first difficult, expert-validated benchmark designed to measure whether LLM-based systems genuinely improve with experience. CL-Bench spans six diverse domains (software engineering, signal processing, disease outbreak forecasting, database querying, strategic game-playing, and demand forecasting), each validated by domain experts and designed so that tasks share a learnable latent structure (codebase layout, disease outbreak dynamics, opponent strategies) that a stateful system can discover online but a stateless one cannot. We evaluate frontier models across several agent architectures, from naive in-context learning (ICL) to dedicated memory systems, introducing a gain metric to isolate learning from prior capabilities. We find that these systems leave headroom for improved continual learning: agents frequently overfit to immediate observations or fail to reuse knowledge across instances, and dedicated memory systems do not fix this -- in fact, naive ICL outperforms systems dedicated to memory management. CL-Bench is the first benchmark to evaluate continual learning across diverse real-world domains with expert-validated tasks and isolate online learning from underlying model capability, showing a need for better continual learning systems.

---


### 112. [V2V-Bench: A Comprehensive Benchmark for Video-to-Video Generation Evaluation](https://arxiv.org/abs/2606.05665)

**<font color=#1a73e8>作者：</font>** Tao Liu, Leela Krishna, Gouti Pavan Kumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-to-video (V2V) generation is difficult to evaluate because outputs must both follow editing instructions and preserve frame-level correspondence with the source video, which existing T2V and I2V metrics do not capture. We introduce V2V-Bench, a 11-dimension benchmark organized into five categories: temporal alignment, structural fidelity, transformation quality, video quality, and semantic alignment. V2V-Bench pairs diverse source videos with challenging editing tasks and evaluates two commercial models, Grok Imagine and Gemini Veo3, and one open-source model, Open Sora 2. Results show complementary model strengths: Grok performs better on editing fidelity, while Veo3 achieves stronger visual quality. On six V2V-specific dimensions, V2V-Bench reaches a Spearman correlation of 0.905 with human judgments.

---


### 113. [QueryAgent-R1: Bridging Query Generation and Product Retrieval for E-Commerce Query Recommendation](https://arxiv.org/abs/2606.05671)

**<font color=#1a73e8>作者：</font>** Dike Sun, Zheng Zou, Jingtong Zang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Query recommendation in e-commerce search aims to proactively suggest queries that match users' potential interests. However, existing methods mainly optimize query-level relevance, while neglecting whether the retrieved products align with users' downstream preferences. This mismatch often leads to high query click through rates (CTR) but low product conversion rates (CVR). To bridge this gap, we propose QueryAgent-R1, a memory-augmented agentic framework that improves end-to-end alignment via chain-of-retrieval optimization. Our QueryAgent-R1 grounds query generation in real inventory retrieval, allowing the agent to validate and refine queries based on retrieved products. We also design a consistency reward in the agentic reinforcement learning (RL) process to jointly optimize query relevance and downstream engagement. In addition, we construct a memory abstraction module for efficient user profiling. To support offline evaluation, we construct two datasets based on both proprietary industrial data and public datasets, on which QueryAgent-R1 consistently outperforms strong baselines. Moreover, on a large scale production platform, QueryAgent-R1 improves Query CTR by 2.9% and guided CVR by 3.1% in online A/B tests.

---


### 114. [AdaMEM: Test-Time Adaptive Memory for Language Agents](https://arxiv.org/abs/2606.05684)

**<font color=#1a73e8>作者：</font>** Yunxiang Zhang, Yiheng Li, Ali Payani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A central challenge for language agents is utilizing past experience to adapt to dynamic test-time conditions. While recent work demonstrates the promise of agentic memory mechanisms, most systems restrict retrieval to episode initiation. Consequently, agents are forced to rely on static guidance that becomes increasingly misaligned as long-horizon tasks unfold. To address this rigidity, we propose the Adaptive Memory Agent (AdaMEM), a novel framework for agent test-time adaptation. Without updating model parameters online, AdaMEM adapts agent behavior via a hybrid memory architecture: it maintains a long-term trajectory memory of raw experiences collected offline while generating dynamic short-term strategy memory on-the-fly to guide decision-making. This mechanism enables the trade-off between token efficiency and adaptability across varying inference-time compute levels. Empirically, AdaMEM significantly outperforms static memory baselines, achieving relative gains of up to 13% on ALFWorld and 11% on WebShop, with consistent leading performance extending to agentic search on HotpotQA. To further enhance this adaptation, we develop STEP-MFT, a Step-wise Memory Fine-Tuning technique that trains the policy to synthesize high-quality strategies from retrieved experiences, yielding additional performance gains. Our work establishes a new scaling dimension for agentic memory, supporting continuous reasoning and self-evolution post-deployment in real-world environments. Our code is available at this https URL.

---


### 115. [Causal Modeling of Selection in Evolution](https://arxiv.org/abs/2606.05689)

**<font color=#1a73e8>作者：</font>** Haoyue Dai, Zeyu Tang, Peter Spirtes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding potential selection in data is crucial for causal discovery; we argue that "selection" in common narratives takes two forms, which we term static and evolutionary selection, respectively. Static selection refers to a one-shot filtering process where observed data consist of a subset of the population of interest, as in survey volunteer bias. Evolutionary selection, in contrast, operates through repeated rounds of differential fitness in reproduction, where observed data constitute the latest generation shaped by a historical trajectory, as in immune adaptation, antibiotic resistance, and social norm emergence. Existing methods largely conflate these two forms and rely on an identical graphical model of selection. We show that this model is valid for static settings but fails to characterize data under evolution, yielding false discovery results. To address this, we introduce a new model that specifically characterizes evolutionary selection, and develop a sound and complete procedure for identifying such models from data across one or multiple environments or generations. Experimental results validate the method's ability to uncover the relevant mechanisms underlying evolution from data.

---


### 116. [Benchmarking Counterfactual Prediction in Epidemic Time Series with Time-Varying Interventions](https://arxiv.org/abs/2606.05692)

**<font color=#1a73e8>作者：</font>** Wenhao Mu, Facundo Yan, Anik Mumssen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning has enabled significant advances in time-series causal inference, yet progress remains constrained by the lack of realistic benchmarks with observable counterfactual outcomes. Existing datasets either rely on real-world observations without ground-truth counterfactuals or on simplified simulations that fail to capture complex causal dynamics. To address this gap, we develop a large-scale benchmark for counterfactual prediction in epidemic time series under dynamic interventions. Unlike existing benchmarks, it supports static and time-varying treatments, as well as both single-policy and multi-policy intervention settings, enabling evaluation of causal inference methods across a broad range of causal inference scenarios. Leveraging a calibrated agent-based model grounded in real-world demographic, mobility, epidemiological, and policy data, we generate realistic counterfactual trajectories across more than 150 U.S. counties. Using this benchmark, we evaluate widely used and state-of-the-art causal inference methods, revealing substantial performance differences and highlighting the challenges of realistic time-series causal reasoning.

---


### 117. [Revisiting Prototype Rehearsal for Exemplar-Free Continual Learning: Manifold-Aware Boundary Sampling with Adaptive Class-Balanced Loss](https://arxiv.org/abs/2606.05695)

**<font color=#1a73e8>作者：</font>** Hongye Xu, Bartosz Krawczyk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exemplar-free class-incremental learning (EFCIL) aims to acquire new classes over time without storing raw data. Historically, prototype rehearsal, which samples around stored class prototypes and mixes them with current-task data, has been a popular strategy to reduce catastrophic forgetting. However, recent drift-compensation methods that explicitly realign prototypes in the evolving feature space consistently outperform prototype-based rehearsal, raising the question of whether rehearsal itself is fundamentally limited. We argue that the performance gap stems not from the idea of prototype rehearsal per se, but from how it is typically instantiated: existing approaches treat prototypes as isolated class summaries that ignore information from nearby enemy classes, and fail to correct the emerging class imbalance between a handful of synthetic old-class samples and hundreds of real instances from newly introduced classes. Building on this hypothesis, we revisit prototype rehearsal and propose a manifold-aware variant that restores its competitiveness in EFCIL. First, we introduce Constrained Expansive Over-Sampling, which interpolates each old-class prototype toward its nearest enemy features from new classes, generating boundary-aware rehearsal samples that better follow the underlying data manifold while preserving inter-class separation. Second, we design an Adaptive Class-Balanced loss that performs time-based class weighting, amplifying gradients from older prototypes when they are most informative and gradually annealing their influence as richer supervision from later tasks accumulates. Together, these components turn prototype rehearsal into a drift-resilient, imbalance-aware mechanism that closes, and often reverses, the gap to recent drift-compensation methods, achieving state-of-the-art performance across multiple EFCIL benchmarks.

---


### 118. [Rethinking LoRA Memory Through the Lens of KV Cache Compression](https://arxiv.org/abs/2606.05698)

**<font color=#1a73e8>作者：</font>** Chunsheng Zuo, Liaoyaqi Wang, William Jurayj 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parametric retrieval augmentation encodes document information into lightweight, document-specific modules such as LoRA adapters, reducing the need to include all evidence as input context. However, it remains unclear how this parameter-side memory interacts with context-side memory stored in the KV cache. We study this interaction in document-level question answering by progressively evicting document key-value states and measuring when a document LoRA contributes beyond the retained context. We find that document LoRA adds little when the KV cache is largely intact, but becomes increasingly useful under aggressive compression, recovering 13-21 ROUGE-L points when no document context remains. The gain is largest when the base model encodes the document, and the adapter is applied only during answer generation, suggesting that document LoRA is better understood as decoding-time parametric memory than as a document encoder. Finally, QA-style supervision produces substantially stronger adapters than raw-context next-token-prediction. These results position document LoRA as a complementary memory channel whose value emerges precisely when context-side evidence is scarce.

---


### 119. [T-SAR-JEPA: Self-Supervised Temporal Anomaly Detection in SAR Amplitude Stacks via Latent Prediction](https://arxiv.org/abs/2606.05700)

**<font color=#1a73e8>作者：</font>** Kerod Woldesenbet, Abem Woldesenbet  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present T-SAR-JEPA, a self-supervised framework for temporal anomaly detection in SAR amplitude stacks via latent prediction. A ViT-Base/16 encoder from SAR-JEPA is domain-adapted on 39,300 Capella patches using local masked reconstruction with gradient feature prediction. A temporal transformer with sinusoidal time encoding forecasts future latent states from K=7 acquisitions, with progressive unfreezing substantially reducing validation loss. The model operates on amplitude alone; InSAR coherence serves exclusively as independent pseudo-ground-truth. On the DFC 2026 dataset (300 time-series, three AOIs), T-SAR-JEPA achieves ROC-AUC of 77.0% on the Hawaii eruption window, outperforming RX, PaDiM, Linear AR, and LSTM baselines (~50%). Spatial coherence of 99.9% (p < 0.001, permutation test) confirms structured detections. Code: this https URL

---


### 120. [Cognitive Threat Intelligence and Explainable Federated Security Analytics for distributed Infrastructure Systems](https://arxiv.org/abs/2606.05701)

**<font color=#1a73e8>作者：</font>** Md. Arifur Rahman, B. M. Taslimul Haque, Md. Iqbal Hossan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing adoption of distributed infrastructure systems, cloud computing, Internet of Things (IoT) technologies, and edge-based architectures has significantly expanded the cybersecurity attack surface and introduced increasingly sophisticated cyber threats. Conventional centralized intrusion detection approaches often face challenges related to scalability, data privacy, communication overhead, and limited transparency in artificial intelligence-driven decision-making processes. To address these limitations, this study proposes a Cognitive Threat Intelligence and Explainable Federated Security Analytics framework for distributed infrastructure systems. The proposed framework integrates Federated Learning (FL), Explainable Artificial Intelligence (XAI), and cognitive cybersecurity analytics to enable collaborative and privacy-preserving cyber threat detection across distributed network environments. Instead of transmitting sensitive raw network traffic data to centralized servers, local security models are independently trained at distributed nodes, where only encrypted model parameters and updates are shared through a federated aggregation mechanism. This decentralized learning architecture improves privacy protection while reducing communication dependency and centralized security risks. To enhance intelligent threat analysis, the framework incorporates machine learning and deep learning algorithms including Random Forest, XGBoost, Autoencoder

---


### 121. [Parallel Jacobi Decoding for Fast Autoregressive Image Generation](https://arxiv.org/abs/2606.05703)

**<font color=#1a73e8>作者：</font>** Boya Liao, Ying Li, Siyong Jian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) models have demonstrated remarkable performance in generating high-fidelity images. However, their inherently sequential next-token prediction leads to significantly slower inference. Recent studies have introduced Jacobi-style decoding to accelerate autoregressive image generation. Extending the draft sequence initially improves efficiency, yet the acceleration quickly saturates as error propagation in the one-dimensional sequence hinders convergence. Observing that images exhibit strong local spatial correlations, we propose Parallel Jacobi Decoding (PJD), a training-free decoding approach that expands draft tokens in the two-dimensional spatial domain to enable efficient spatially parallel refinement. PJD adjusts the attention mask to mitigate error accumulation and improve convergence stability. Extensive experiments on diverse datasets show that PJD achieves 4.8x-6.4x acceleration across multiple autoregressive image generation models while maintaining competitive generation quality.

---


### 122. [Real-Time Threat Detection from Surveillance Cameras using Machine Learning](https://arxiv.org/abs/2606.05708)

**<font color=#1a73e8>作者：</font>** Gajendra Mandal, J. P. Patra, Priyansh Mahant  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ensuring public safety in densely populated urban environments remains a critical challenge, necessitating the deployment of intelligent and automated video surveillance systems. Traditional surveillance approaches rely heavily on manual monitoring, which is inefficient and susceptible to human fatigue, delayed response, and observational errors. To overcome these limitations, this work presents a real-time object detection-based surveillance framework. The proposed system focuses on detecting guns, knives, and region-specific blunt objects commonly involved in violent activities in Indian surveillance scenarios. A key contribution of this work is the use of a custom-created dataset collected using a mobile camera, consisting of 336 labeled images of blunt objects such as iron rods, wooden sticks, and plastic rods. This dataset is combined with a publicly available dataset of 7,623 images of guns and knives, forming a consolidated dataset of 7,959 images across three classes: gun, knife, and blunt object. The combined dataset is used to train a YOLOv8-based object detection model for real-time performance. Experimental evaluation shows that increasing the training duration significantly improves recall and average precision for the blunt object class without signs of overfitting. Overall, the proposed framework achieves an effective balance between accuracy and efficiency, making it suitable for deployment in real-world surveillance environments such as campuses, public spaces, and transportation areas.

---


### 123. [Explainable AI-Driven Cyber Risk Analytics and Model Reliability Assessment for Intelligent Governance of U.S. Critical Infrastructure: An XGBoost and SHAP-Based Intrusion Detection Framework](https://arxiv.org/abs/2606.05710)

**<font color=#1a73e8>作者：</font>** B. M. Taslimul Haque, Md. Arifur Rahman, Md. Serajul Kabir Chowdhury Rubel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing penetrations of the critical infrastructure sector in the United States with intelligent digital technologies have greatly increased exposure to advanced cyber adversaries and operational vulnerabilities. AI-powered governance and automated decision-making systems are becoming a key part of the operation of critical infrastructure systems, including energy, healthcare, transportation, financial services, and communication infrastructure, in order to improve efficiency and strategic management. The growing cyber threat environment, such as Distributed Denial of Service (DDos) attacks, botnets, ransomware, and Advanced Persistent Threats (APTs) pose significant challenges to infrastructure resilience, cyber security reliability, and governance trustworthiness. In a changing attack landscape and dynamic network environment, traditional cybersecurity mechanisms can often fall short of meeting the evolving needs and protecting critical systems. This study will develop a resilient cyber risk analytics and model reliability assessment framework to support intelligent governance and decision support for cyber risk exposure in the U.S. critical infrastructure environment. This study is based on the CICIDS2017 dataset for the development and testing of intrusion detection system models and cyber risk prediction models based on machine learning. Various classifiers like XGBoost, Random Forest, and Decision Tree are used to detect malicious activities on the network and determine the level of cyber risk. Furthermore, the Explainable Artificial Intelligence (XAI) techniques are integrated to enhance transparency, interpretability, and trust in cybersecurity decision-making processes. The proposed framework presents the reliability and resilience of the model by having various performance measures such as accuracy, precision, recall, F1 score, ROC-AUC, and false positive rate.

---


### 124. [Hybrid CNN-LSTM Framework for Intelligent Cyber Attack Detection and Prevention in U.S. Critical Digital Infrastructure: A Comparative Machine Learning Evaluation on CSE-CIC-IDS2018](https://arxiv.org/abs/2606.05714)

**<font color=#1a73e8>作者：</font>** Md. Iqbal Hossan, Md. Serajul Kabir Chowdhury Rubel, Md. Arifur Rahman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Digital infrastructure is growing at a rapid pace in the United States, and as a result, exposure to advanced cyber threats to critical sectors including healthcare, finance, transportation, energy and government systems is growing. The traditional cybersecurity approaches, including signature-based intrusion detection systems, have become less effective against today's cyber attacks, as they are unable to detect unknown and changing attacks in real time. To overcome these constraints, this research suggests a smart cyber-defense system, which utilizes Artificial Intelligence (AI) and Machine Learning (ML) algorithms in the detection and prevention of cyber attacks in the U.S. digital infrastructure. This study uses the CSE-CIC-IDS2018 dataset, which is a realistic network traffic dataset, along with various cyber attack scenarios, including Distributed Denial of Service (DDoS), brute force attacks, botnets, infiltration attacks, and web-based attacks. A number of machine learning and deep learning models such as Random Forest, XGBoost, Convolutional Neural Networks (CNN) and Long Short-Term Memory (LSTM) networks are implemented and evaluated to be used in identifying malicious network behavior and boosting the accuracy of intrusion detection. The framework proposed combines data preprocessing, feature engineering, real-time traffic monitoring, intelligent threat classification with automated prevention mechanisms to build cybersecurity resilience. E

---


### 125. [Interpreting Style Representations via Style-Eliciting Prompts](https://arxiv.org/abs/2606.05716)

**<font color=#1a73e8>作者：</font>** Junghwan Kim, David Jurgens  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Style representation learning is a powerful tool for authorship analysis and modeling writing style, yet the latent nature of learned representations makes them difficult to interpret. Recent work has attempted to explain these representations by generating natural language descriptions with large language models (LLMs) conditioned on input text. However, such descriptions are often prone to the LLM's biases and hallucinations, and they lack an explicit objective and practical utility. In this work, we propose a novel framework for interpreting style representations through style-eliciting prompts: natural language instructions designed to steer LLMs to generate text that reflects specific stylistic attributes. We curate 1,010 distinct style features spanning 26 stylistic categories and construct a dataset by prompting an LLM to generate text conditioned on these features. Using this data, we train a decoder to generate a style prompt from the style representation of the generated text. We evaluate our approach on three tasks: (1) recovering original style prompts from generated text, (2) generating text in the same style using the recovered prompts, and (3) steering LLM outputs to match the style of human-written texts. Experiments demonstrate that our method consistently outperforms strong baselines that directly prompt LLMs with target text, achieving superior performance in both style description and style imitation. These results highlight that style-eliciting prompts can provide a practical and interpretable interface to stylistic information encoded in style representations.

---


### 126. [Narrative Knowledge Weaver: Narrative-Centric Retrieval-Augmented Reasoning for Long-Form Text Understanding](https://arxiv.org/abs/2606.05724)

**<font color=#1a73e8>作者：</font>** Qiuyu Tian, Fengyi Chen, Yiding Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-form narrative QA requires reasoning over evolving story worlds rather than isolated passages: answers may depend on earlier goals, changing character states, social relations, causal triggers, temporal position, and later consequences. Existing retrieval and graph-augmented generation methods improve evidence access, but their units--chunks, entities, relations, summaries, or tool actions--do not directly encode how evidence functions in a story. We introduce Narrative Knowledge Weaver(NKW), a source-grounded framework that aligns textual evidence, atomic facts, canonical graph structure, entity profiles, interactions, episodes, and storylines. At query time, NKW uses text, graph, and narrative tools with post-retrieval reading skills to assemble evidence and audit actor, scope, polarity, state, and temporal constraints. Across STAGE, FairytaleQA, and QuALITY, NKW is strongest on screenplay-level story-world QA while remaining competitive on more passage-centered benchmarks. Ablations, question-type analyses, graph-asset statistics, and case studies show complementary benefits for character, scene, temporal, causal, and narrative-progression reasoning.

---


### 127. [DiG-Plan: Mitigating Early Commitment for Tool-Graph Planning via Diffusion Guidance](https://arxiv.org/abs/2606.05728)

**<font color=#1a73e8>作者：</font>** Yansi Li, Zhuosheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating executable tool plans requires selecting appropriate subsets from tool libraries, a combinatorial search problem with an exponentially large solution space. However, we identify a critical misalignment in predominant approaches: standard autoregressive (AR) decoding suffers from early commitment, where initial token choices rigidly constrain the search trajectory. A controlled study shows that masked denoising raises Pass@10 solution coverage from 0.320 to 0.943 over AR sampling under matched compute. Motivated by this, we propose DiG-Plan, a framework that decouples combinatorial exploration from structural refinement. DiG-Plan employs a diffusion-based proposer to generate diverse tool sets via iterative refinement, followed by an AR refiner for dependency prediction. On TaskBench, DiG-Plan improves over AR baselines by a 10% relative margin, with the largest gains on complex compositional tasks; API-Bank results show that the propose-refine-select design remains effective across domains. Code is available at this https URL.

---


### 128. [TextWand: A Unified Framework for Scene Text Editing](https://arxiv.org/abs/2606.05730)

**<font color=#1a73e8>作者：</font>** Shuyu Wang, Zhile Guan, Hongxiu Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose TextWand, a general-purpose framework that unifies scene text removal, generation, and replacement into a single model. By decomposing complex editing tasks into the atomic primitives of rendering and erasure, TextWand achieves precise control over both text appearance and background integrity. Specifically, we introduce a novel design, Overlay-Reference Positional Encoding (ORPE), to enforce pixel-level layout fidelity and exemplar-driven style control, alongside a new strategy, Region-Adaptive Suppression (RAS), to ensure clean text erasure. To address the absence of a comprehensive benchmark for general-purpose scene text editing among existing single-task datasets, we construct TextWand-Bench. Extensive experiments demonstrate that TextWand outperforms existing leading open-source and closed-source models by delivering superior text content accuracy, layout and style consistency, and overall image quality across scene text removal, generation and replacement tasks.

---


### 129. [Intercomparison of Machine Learning Algorithms for Remote Sensing-based In-season Crop Mapping](https://arxiv.org/abs/2606.05731)

**<font color=#1a73e8>作者：</font>** August Posch, Jitendra Kumar, Forrest M. Hoffman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-season crop type mapping is critical for food security in the face of increasingly extreme climate-related threats to crops. Currently, the USDA Cropland Data Layer provides crop type labels at 30m resolution and is available the February after harvest, but no product exists that maps crop types before harvest with satisfactory accuracy that would allow emergency managers to respond to crop threats in near real time. Furthermore, the relative advantages of a wide range of algorithms have not been evaluated in a way that accounts for interannual variability, until this study. Here, Harmonized Landsat-Sentinel surface reflectance imagery time series and crop rotation history information are combined to map corn in Iowa and almonds in California at 30m resolution accurately by early June in unseen years, with robust quantification of uncertainty due to phenology and crop distribution. Thousands of model configurations across ten machine learning algorithms were compared using a year-wise cross-validation and a suite of metrics. Hyperparameter search revealed Support Vector Machines to be the most successful algorithm overall, with a mean F1 score of 0.74 (0.59) across five unseen validation years for almonds by early June in California (corn by early June in Iowa). Interannual variation was a large source of uncertainty, but patterns showed the potential to further improve performance with ensemble approaches or ancillary data. Future work may extend these methods to include multiclass maps of all crop types, CONUS-wide maps, and in-season crop yield forecasting.

---


### 130. [Zero-Copy Semantic Contagion: An In-Memory Streaming Architecture for Evolving Attention Graphs](https://arxiv.org/abs/2606.05733)

**<font color=#1a73e8>作者：</font>** Kabir Murjani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Per-ticker forecasting models dominate financial time-series work yet remain blind to cross-company propagation: a foundry disruption in Taiwan does not register in a single-asset model until Apple's own price has already moved. To address this limitation, we introduce a heterogeneous Rust-Python streaming architecture that maps cross-company attention as a continuous-time graph driven directly from text. We show that on the ingestion side, a zero-copy Rust edge parses news records in $\sim$100 ns and scans the target equity universe in $\sim$1.2 $\mu$s. On the inference end, a multivariate Neural Hawkes Process featuring per-node continuous-time LSTM states and a bilinear latent projection propagates directed excitation, while an adaptive pruning rule bounds the computational cost of dynamic neighborhood updates. Combining these stages, we demonstrate an end-to-end processing latency of $\sim$13 ms per incoming news record on a single commodity CPU. Evaluated on a one-month temporal holdout of the FNSPID corpus (638 articles across 47 tickers), the system delivers a $1.70\times$ precision lift over random at the 90th-percentile next-day return threshold, and $3.36\times$ over a same-sector baseline. Crucially, removing the graph topology collapses precision to zero, confirming that the dynamic attention network is the sole driver of cross-company signal in this architecture.

---


### 131. [VTI-CoT: Visual-Textual Interleaved Chain of Thought for Video Reasoning](https://arxiv.org/abs/2606.05736)

**<font color=#1a73e8>作者：</font>** Shufan Zhang, Ziyue Lin, Bairun Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video reasoning aims to understand complex temporal events and causal relationships within videos. Recently, Chain-of-Thought (CoT) has been introduced to this field to enhance reasoning accuracy. However, existing CoT-based video reasoning methods primarily rely on text-only information for logical deduction, overlooking critical visual information during the inference process. Inspired by the human cognitive mechanism of reviewing visual segments during inference, we propose VTI-CoT, a Visual-Textual Interleaved CoT framework. VTI-CoT integrates textual reasoning steps with corresponding visual frames. Given the scarcity of visual-textual interleaved CoT in existing datasets, we develop an automated annotation pipeline to construct high-quality multimodal CoT data. Further, reasoning over long-form videos entails increasingly long CoT token sequences, which severely hinders training convergence and efficiency. To address this, we employ Optical Character Recognition (OCR)-based compression techniques to compress CoT supervision signals into a single canvas. Experimental results demonstrate that VTI-CoT achieves state-of-the-art performance among models of the same parameter scale while significantly improving training efficiency.

---


### 132. [Let It Be Simple: One-Step Action Generation for Vision-Language-Action Models](https://arxiv.org/abs/2606.05737)

**<font color=#1a73e8>作者：</font>** Yitong Chen, Shiduo Zhang, Jingjing Gong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based vision-language-action (VLA) models often inherit the image-generation view: actions are generated by iterative denoising. We argue that VLA action generation has a different condition-target structure: the policy is conditioned on rich observations, language, and state, but predicts only a compact, low-dimensional action chunk. Under this asymmetry, strong one-step action generation should not necessarily require the advanced one-step methods developed for image synthesis. We keep standard velocity prediction and add no teacher model, distillation stage, or auxiliary objective; in our main recipe, we simply bias the training time distribution toward high-noise states. We first isolate the effect in a controlled MNIST grid-to-sequence task, then test it with extensive robot-policy experiments. Across standard LIBERO, LIBERO-Plus, and LIBERO-Pro, one-step policies trained with high-noise biased schedules generally match ten-step decoding under the same recipe, and on standard LIBERO can exceed ten-step policies trained with a uniform time distribution. A real-robot bimanual YAM RSS evaluation gives a small-sample cross-architecture check of the same sampler trend. On a 1.4B VLM model with a 30M action head, one-step decoding reaches 95.6\% on LIBERO-Long. These results show that strong one-step VLA action generation can emerge from standard diffusion training, without importing the full few-step diffusion machinery developed for image generation.

---


### 133. [Class-Specific Branch Attention for Mitigating Gradient Interference under Class Imbalance](https://arxiv.org/abs/2606.05740)

**<font color=#1a73e8>作者：</font>** Arush Singhal, Umang Soni  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep neural networks trained under severe class imbalance often exhibit degraded performance, typically attributed to statistical bias. In this work, we identify a complementary optimization-level pathology: inter-class gradient interference within shared representations, where gradients from majority classes suppress minority-class learning. To analyze this phenomenon, we introduce a diagnostic framework based on layer-wise gradient flow analysis and a Gradient Conflict Matrix, which quantifies interference using cosine similarity between class-specific gradients. Using this framework, we study multi-branch convolutional architectures and propose a lightweight modification, Class-Specific Branch Attention (CSBA), that enables branch-specific channel reweighting to reduce gradient coupling. This mechanism promotes implicit feature decoupling across branches while preserving architectural simplicity. Empirically, CSBA improves minority-class performance, increasing the F1 score for the Physical-Damage class from 0.261 to 0.522 under severe imbalance, while maintaining comparable overall accuracy. Validation on CIFAR-10-LT confirms that this behavior generalizes across imbalanced visual recognition settings, with Macro-F1 improving from 0.595 to 0.655. More broadly, our findings highlight the importance of considering optimization dynamics alongside statistical methods when designing architectures for imbalanced learning.

---


### 134. [AdaPLD: Adaptive Retrieval and Reuse for Efficient Model-Free Speculative Decoding](https://arxiv.org/abs/2606.05742)

**<font color=#1a73e8>作者：</font>** Runheng Liu, Jincheng Xie, Wen Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates generation by verifying multiple drafted tokens in a single target-model forward pass, reducing sequential decoding iterations. Model-free variants avoid auxiliary draft models by reusing text and model states already available during generation, but their speedup depends on the reliability of the constructed drafts. We identify two limitations of existing reuse-based methods: lexically anchored retrieval has limited recall under surface-form variation, and deterministic span copying can be brittle when the retrieved context does not uniquely determine the continuation. We propose \emph{AdaPLD}, a training-free method that adaptively improves both retrieval and draft construction. AdaPLD preserves high-precision lexical reuse while using semantic similarity to recover additional reuse opportunities when lexical matching fails. It further constructs branched reuse hypotheses to account for continuation uncertainty, rather than relying on a single copied span. Across diverse benchmarks, AdaPLD reduces target-model forward passes and achieves up to $3.10\times$ decoding speedup.

---


### 135. [Beyond Soft Masks: Hard-Perturbation Mixup Explainer for Robust GNN Explainability](https://arxiv.org/abs/2606.05756)

**<font color=#1a73e8>作者：</font>** Jialiang Yin, Zheng Zhao, Linsey Pang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have demonstrated remarkable performance across a range of applications involving graph-structured data, particularly in high-stakes domains. However, the opaque nature of their decision-making processes limits their trustworthiness and broader adoption. Existing post-hoc explanation methods aim to improve explainability by identifying subgraphs that influence GNN predictions and adopt mixup strategies to alleviate the out-of-distribution (OOD) issue caused by using subgraphs for prediction. Yet, these approaches typically rely on soft masks, which are inherently unable to fully eliminate label-irrelevant information, allowing redundant structures to leak into the mixup process and hindering the resolution of the OOD problem, thereby degrading explanation fidelity. In this work, we propose HPME, a Hard-Perturbation Mixup Explanation framework grounded in a generalized Graph Information Bottleneck, which leverages graph pooling to extract discrete explanatory subgraphs and to yield an information-capacity bound to thoroughly compress label-irrelevant components. Furthermore, we introduce a novel mixup strategy built upon structure-level replacement, generating in-distribution explanations to effectively mitigate the distribution shift. Extensive experiments on diverse tasks demonstrate that HPME achieves state-of-the-art performance in generating robust and interpretable explanations across both synthetic and real-world datasets.

---


### 136. [Physics-Guided Deep Unfolding for Blind Cross-Sensor Spectral Super-Resolution via Learning the Spectral Transformation Function](https://arxiv.org/abs/2606.05759)

**<font color=#1a73e8>作者：</font>** Zhaolin Li, Jinsong Chen, Shanxin Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral imaging provides rich spectral information for quantitative remote sensing, yet hyperspectral sensors remain costly and thus unavailable in many UAV deployments. Spectral super-resolution (SSR) seeks to reconstruct hyperspectral images (HSIs) from multispectral images (MSIs). Most existing SSR methods assume a fixed and known spectral response function (SRF) and are therefore limited to single-sensor settings. In practical cross-sensor scenarios, the spectral degradation from HSI to MSI is unknown and varies with sensor characteristics and scene content, which renders HSI reconstruction ill-posed. This paper proposes a physics-guided deep unfolding network, termed PGU-Net, to address blind cross-sensor SSR by jointly estimating the HSI and a learnable spectral transformation function (STF). PGU-Net unrolls an alternating optimization procedure into an end-to-end trainable architecture with stages, where each stage sequentially updates the HSI and the STF. Both modules combine learnable proximal networks with differentiable closed-form solvers, enabling physical interpretability while retaining strong representation capacity. Experiments on benchmark datasets (CAVE and NTIRE 2022) with multiple SRFs demonstrate accurate recovery of the STF (degradation operator) and improved reconstruction performance over state-of-the-art SSR methods. Furthermore, evaluations on a real UAV cross-sensor dataset (Headwall Nano HSI and DJI P4 Multispectral MSI) verify the effectiveness and robustness of PGU-Net under truly blind conditions, and suggest that the estimated STF may exhibit land-cover-related differences.

---


### 137. [SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Horizon AI Agents](https://arxiv.org/abs/2606.05761)

**<font color=#1a73e8>作者：</font>** Wenxuan Wang, Haoyu Sun, Fukuan Hou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent AI assistants, such as OpenClaw, accumulate large collections of related memories over long-term interactions. As these memories grow, they may reinforce one another, diverge across contexts, or directly conflict, making correct assistance depend on memory relations rather than isolated recall. Existing long-term memory benchmarks rarely probe how agents preserve and utilize such relations during downstream tasks. To address this gap, we introduce SubtleMemory, a benchmark for fine-grained relational memory discrimination in long-running AI agents. SubtleMemory constructs relation-controlled latent semantic artifacts whose variants instantiate complementary, nuanced, or contradictory relations, and embeds them into realistic user-agent histories, requiring agents to recover distributed relational structures during later queries and instructions. The benchmark contains 1,522 evaluation instances over 10 long histories, grounded in 1,090 relation-controlled memory-variant sets and spanning user-related and non-user-related queries. Evaluating six standalone memory systems, two Claw-style agents with native memory modules, and three Claw-style agents with plugin memory modules, we find that current systems remain weak on fine-grained relational memory discrimination. We further introduce diagnostic protocols that reveal distinct capability profiles across memory preservation, retrieval, and downstream reasoning stages.

---


### 138. [LiAuto-GeoX: Efficient Grounded Driving Transformer](https://arxiv.org/abs/2606.05774)

**<font color=#1a73e8>作者：</font>** Jiawei Lian, Haoyi Sun, Yang Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense 3D reconstruction has demonstrated immense potential for spatial understanding, yet its viability as a real-time, onboard representation for autonomous driving remains an open challenge. Existing large-scale visual geometry models typically require substantial computational resources and lack the long-range geometric fidelity, surround-view consistency, and real-time efficiency demanded by dynamic driving environments. To bridge this gap, we present \textbf{LiAuto-GeoX}, an efficient grounded driving transformer designed for deployable, ego-centric 3D scene understanding. Our approach begins by learning a high-capacity driving geometry model from large-scale surround-view data, utilizing sparse LiDAR priors to provide robust geometric grounding in distant, ambiguous, or structure-sparse regions. We then instantiate this capability into a highly compact 155M-parameter onboard model through a novel geometry-preserving distillation framework. This framework employs mask-guided depth-aware distillation to retain fine-grained metric structures by emphasizing geometrically informative regions, and relative-pose relational distillation to enforce cross-view spatial consistency through pose-induced geometric relations. Extensive evaluations reveal that \textbf{LiAuto-GeoX} runs at 220 FPS on KITTI while maintaining high-fidelity dense reconstruction, enabling real-time deployment. The learned geometry transfers seamlessly to downstream autonomy tasks, achieving 90.6 PDMS in trajectory prediction, 24.63 mIoU in occupancy prediction, and 47.67 IoU in future-frame prediction. These all demonstrate that efficient dense 3D reconstruction can transcend its traditional role as a perception target to serve as a scalable, foundational geometric representation for next-generation autonomous driving.

---


### 139. [An Improved CNN-LSTM Based Intrusion Detection System for IoT Networks](https://arxiv.org/abs/2606.05776)

**<font color=#1a73e8>作者：</font>** Mohammad Tariq Ikhlas, Pohanyar Khowaja Khil, Malik Muhammad Mueed Aslam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the rapid proliferation of IoT devices, security concerns have dramatically escalated and intrusion detection systems have become critical for protecting networked environments. This paper presents an improved CNN-LSTM based intrusion detection model that combines multi-class classification, dataset integration, and temporal feature learning to enhance detection performance in IoT networks. Using network traffic data, the proposed approach is evaluated on intrusion detection tasks and achieves an accuracy of approximately 97%. Experimental results demonstrate that the model effectively detects multiple attack categories while maintaining stable training and validation performance. The integration of convolutional and recurrent neural network components enables the framework to capture both spatial and temporal characteristics of network traffic, improving overall intrusion detection capability in IoT environments.

---


### 140. [Beyond Absolute Scores: Relative Edit-induced Difference for Generalizable Image Aesthetic Assessment](https://arxiv.org/abs/2606.05778)

**<font color=#1a73e8>作者：</font>** Qifei Jia, Xintong Yao, Minghao Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional Image Aesthetic Assessment (IAA) methods mainly rely on regressing absolute Mean Opinion Scores (MOS). However, such a paradigm overlooks the inherently dynamic nature of human aesthetic perception, which relies on subconscious comparison against implicit visual references. Consequently, the lack of causal reasoning regarding aesthetic differences prevents models from learning generalizable aesthetic principles, thus limiting their generalization across diverse scenarios. In this work, we rethink the IAA task and propose Relative Edit-induced Difference Aesthetic learning (RED-Aes), a novel framework that leverages controllable image editing models to simulate the human aesthetic reasoning process. Instead of fitting absolute score distributions, RED-Aes explicitly learns the visual factors that drive aesthetic changes. To support this paradigm, we construct the RED-20k dataset, which comprises editing-based image pairs, quantitative aesthetic differences, and Chain-of-Thought (CoT) reasoning. Furthermore, we introduce a three-stage training strategy guided by a relative ranking consistency reward, optimizing the model solely via relative supervision. Extensive experiments demonstrate that RED-Aes achieves state-of-the-art performance on multiple public benchmarks, exhibiting superior generalization capabilities.

---


### 141. [TinyML-Driven Cybersecurity for Autonomous Spacecraft: Latency-Accuracy Analysis for SPARTA RF and Cyber Threat Detection](https://arxiv.org/abs/2606.05779)

**<font color=#1a73e8>作者：</font>** Van Le, Trevor Tran, Tan Le  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous spacecraft require rapid, lightweight, and reliable onboard detection of cyber-RF threats. Using the SPARTA attack model, we analyze the latency-accuracy trade-offs of TinyML-compatible classical models -- Random Forest, Logistic Regression, SVM, and MLP -- for detecting uplink jamming, Fake-NR spoofing, payload manipulation, ground-segment compromise, and unauthorized command injection. We present a physics-informed theoretical analysis of each model's computational complexity, VC dimension, Lipschitz continuity, and latency scaling, supported by empirical measurements on adversarial RF spectrograms generated via BandErasure, FakeNR, and NoiseBurst corruption modes. Results show that Logistic Regression achieves microsecond-level inference with only a 1\% accuracy drop relative to Random Forest, making it an effective TinyML baseline for onboard autonomy. The study also identifies opportunities for advancing spacecraft cybersecurity through richer feature encoders and multi-timescale learning architectures, building on recent progress in edge intelligence and trustworthy AI.

---


### 142. [Next-Generation Parallel Decoder for LPDR: Architectural Optimization and Class-Balanced GAN-Augmentation](https://arxiv.org/abs/2606.05785)

**<font color=#1a73e8>作者：</font>** Shawaiz Obaid, Nida Chandio, Neha Jamil 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-Time License Plate Detection and Recognition (LPDR) forms the backbone of modern smart cities. Although the YOLOV5-PDLPR model substantially improved system efficiency through a parallel decoder approach, its performance is still affected by spatial character mismatches and data imbalance within the training set. This paper addresses these limitations by introducing Cross-Spatial Hybrid Attention (CSHA) and Class-Balanced Synthetic Augmentation (CBSA). An extensive study involving 75,000 synthetic samples is conducted and evaluated on four benchmarks: CCPD, CLPD, PKU, and an application-specific dataset. Experimental results demonstrate a substantial improvement in the recognition rate of minority provincial license plates from 78.2% to 91.5% while maintaining real-time processing performance of 152 FPS. The results indicate that spatially-aware parallel decoding combined with class-balanced augmentation provides an effective solution for high-speed license plate recognition systems.

---


### 143. [GCD: Garbled, Corrected, Demonstrandum -- Fixing and Proving Go's Extended GCD Implementation](https://arxiv.org/abs/2606.05796)

**<font color=#1a73e8>作者：</font>** Linard Arquint  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We verify the 'extendedGCD' implementation in Go's standard library ('crypto/internal/fips140/bigmod'), which plays a crucial role in the generation of RSA key pairs. Even though the Go implementation is supposedly a direct port from BoringSSL's implementation, we uncovered two deviations that each break the algorithm's invariants: (1) the Go implementation deviates in the way coefficients are updated, and (2) it permits a larger input domain. We address both deviations; the first by fixing the Go implementation, which results in an on average 24% speedup, and the second deviation by porting an existing proof for BoringSSL and extending it to cover the larger input domain. We prove correctness and termination of the fixed Go implementation using Gobra, a deductive program verifier for Go. Where necessary, we used Lean to prove key lemmata on non-linear arithmetic, which we import into Gobra.
Our verification effort reveals three key insights: subtle bugs can slip into even well-reviewed code with surprising ease; formal verification is a powerful tool for uncovering them; and AI agents can facilitate the verification process by iteratively refining invariants and lemmata based on Gobra's error messages.

---


### 144. [Causal Longitudinal Prior-Fitted Networks for Counterfactual Outcome Prediction](https://arxiv.org/abs/2606.05797)

**<font color=#1a73e8>作者：</font>** Amirhossein Zare, Amirhessam Zare, Herlock Rahimi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Longitudinal treatment decisions require predicting potential outcomes under future treatment sequences in the presence of time-varying confounding, heterogeneous patient dynamics, and limited domain-specific data. Existing longitudinal causal estimators typically train a new model for each cohort or simulator. We introduce Causal Longitudinal Prior-Fitted Networks (CausalLongPFN), a prior-fitted in-context predictor for longitudinal causal prediction. The model is pretrained entirely on synthetic episodes sampled from a broad prior over temporal structural causal models, exposing it to treatment-confounder feedback, latent heterogeneity, nonlinear state evolution, delayed effects, and cumulative treatment responses. At test time, CausalLongPFN is frozen: it conditions on support trajectories, a query history, and a proposed future treatment sequence, and returns a predictive distribution over future outcomes without gradient updates or propensity-model fitting. Multi-step predictions are obtained by recursively applying the one-step predictor under the specified treatment sequence. We evaluate on branchable cancer, HIV, and warfarin benchmarks with ground-truth counterfactual labels, and on factual-only rolling-origin prediction in MIMIC-III ICU trajectories. CausalLongPFN is competitive with domain-trained longitudinal baselines on counterfactual benchmarks and performs strongly on factual MIMIC-III prediction, suggesting that broad synthetic causal pretraining can provide a useful frozen alternative when repeated domain-specific training is costly or impractical.

---


### 145. [SALT: When More Rollouts Don't Help in Group-Based Policy Optimization and How to Make Them Matter](https://arxiv.org/abs/2606.05800)

**<font color=#1a73e8>作者：</font>** Powei Chang, Jinpeng Zhang, Chaoqun Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) often adopts GRPO-style group-relative updates, sampling multiple rollouts per prompt to construct normalized learning signals. However, merely increasing the number of rollouts does not reliably strengthen learning: under GRPO-style group normalization, per-rollout policy-gradient features can concentrate into a low-rank, signed geometry, causing substantial cancellation during aggregation and weakening the effective update. We address this failure mode with SALT, a Subspace-Adaptive geometry pLug-in componenT that uses sample-wise gradient geometry to reweight the coefficients of group-relative updates. SALT estimates a dominant shared subspace from the mini-batch Gram geometry, decomposes group-relative coefficients into shared and residual channels, and adaptively amplifies the residual channel when signed cancellation is severe. Across diverse reasoning-oriented RLVR benchmarks and model scales, SALT improves effective update geometry and performance without modifying the reward model or the rollout sampling procedure

---


### 146. [Robust and sparse support vector machine via hybrid truncated loss for supervised classification](https://arxiv.org/abs/2606.05814)

**<font color=#1a73e8>作者：</font>** Yuliang Yang, Chen Chen, Yuxiang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The support vector machine (SVM) is a widely used classifier, but choosing an appropriate loss function remains difficult. Convex losses such as the hinge loss and least-squares loss are sensitive to outliers, while bounded non-convex losses often lead to high computational cost. To address this, we propose a hybrid truncated loss function ($L_{\mathrm{ht}}$) that is both sparse and bounded, and build the $L_{\mathrm{ht}}$-SVM model for single-view classification. We introduce the P-stationary point and use it to establish the first-order necessary and sufficient optimality conditions. Based on these conditions, we design an alternating direction method of multipliers with a working-set strategy that reduces computational cost and achieves global convergence. We further extend $L_{\mathrm{ht}}$-SVM to multi-view learning by adding structural information and view weights, resulting in Mv$L_{\mathrm{ht}}$-SVM, which follows both the consensus and complementarity principles. Experiments on synthetic, real-world, and image datasets show that $L_{\mathrm{ht}}$-SVM achieves higher accuracy with fewer support vectors and better noise robustness than five single-view methods, while Mv$L_{\mathrm{ht}}$-SVM outperforms six multi-view methods in accuracy, precision, recall, and F1-score.

---


### 147. [Consistency Training Along the Transformer Stack](https://arxiv.org/abs/2606.05817)

**<font color=#1a73e8>作者：</font>** Sukrati Gautam, Neil Shah, Arav Dhoot 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Consistency training encourages models to behave similarly across different contexts, and has shown promise for reducing misalignment. We broaden the scope of consistency training in two ways. First, we introduce two new internal consistency targets: MLP Consistency Training (MLPCT), which matches post-activation MLP states, and Attention Consistency Training (AttCT), which matches per-head attention distributions. Second, we apply consistency training to four additional safety threats: persona in-context learning attacks, adversarial frustration, prefill attacks, and conditional misalignment. Across several models and threat settings, we find that consistency training reduces misalignment well beyond the sycophancy and jailbreak settings studied in prior work. We also find cases of cross-threat generalization, where training against one failure mode improves robustness to another, and identify a shared residual-stream mechanism underlying ACT, MLPCT, and AttCT, while distinguishing BCT as mechanistically distinct. Our results suggest that consistency training is a flexible and extensible framework for alignment, capable of unifying defenses against a broader class of model pathologies.

---


### 148. [PriSrv: Privacy-Enhanced and Highly Usable Service Discovery in Wireless Communications](https://arxiv.org/abs/2606.05821)

**<font color=#1a73e8>作者：</font>** Yang Yang, Robert H. Deng, Guomin Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Service discovery is essential in wireless communications. However, existing protocols provide limited privacy protection, leaking sensitive device information and opening routes to network attacks. This paper proposes a private service discovery protocol, called PriSrv, which enables both service providers and clients to specify fine-grained authentication policies before establishing connections. PriSrv achieves this via a dual-layer matching architecture: an outer layer filters mismatched entities using public attributes, while an inner layer handles mutual authentication using selectively disclosed private attributes. As a core component, we introduce the primitive of anonymous credential-based matchmaking encryption (ACME), which enables dual-layer matching in a single step to achieve bilateral policy control, selective attribute disclosure, and multi-show unlinkability. To instantiate ACME, we design a fast anonymous credential (FAC) scheme providing constant-size credentials and efficient verification. We demonstrate PriSrv's interoperability by integrating it with popular wireless frameworks including EAP, mDNS, BLE, and AirDrop. Detailed formal security proofs and extensive performance evaluations across desktop, laptop, smartphone, and Raspberry Pi platforms demonstrate that PriSrv provides enhanced privacy guarantees with high usability, achieving secure discovery in less than one second on mainstream mobile devices.

---


### 149. [Architecting Strategic Influence: Operationalising the UXR Point of View Framework for Research Function Maturity](https://arxiv.org/abs/2606.05826)

**<font color=#1a73e8>作者：</font>** Rohinin Singh, Renee Barsoum  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This case study illustrates that the systematic application of the User Experience Research (UXR) Point of View (POV) framework serves as an effective operational scaffolding for a UXR function undergoing the critical transition from incubation to maturity. By assimilating structured 'Offensive' and 'Defensive' strategies, the presented Playbook equips UXR leaders with an adaptable toolkit to systematically navigate common institutional barriers, such as stakeholder bias, reactive tasking, and insight fragmentation. By pre-emptive and purposeful application of growth strategies, the likelihood of the research function establishing itself as a strategic partner capable of delivering evidence-based, actionable perspectives is significantly enhanced. The analysis demonstrates how this deliberate, Playbook-driven maturity strategy empowers research functions to move beyond tactical execution and directly shape long-term business strategy.

---


### 150. [Gender Artifacts from Art History to Text-to-Image Generation](https://arxiv.org/abs/2606.05829)

**<font color=#1a73e8>作者：</font>** Piera Riccio, Miriam Doh, Benedikt Höltgen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artistic styles are rooted in specific socio-historical contexts that encode social hierarchies, including distinct constructions of gender. Yet in AI research, style has long been treated as a surface-level visual property: a filter of color, brushstroke, and texture applied to otherwise content-neutral scenes. We introduce the first dataset to investigate the interplay between gender representation and style in both historical and generated images. StyleGender comprises 74k images spanning 19 artistic styles, comprising art historical images with style and gender annotations, T2I-generated images under controlled style and gender prompts, and a semantically aligned set enabling direct art history-to-generation comparison. By proposing two Set Gender Artifact (SGA) metrics (PixelSGA and MaskSGA), capturing gender signals at the pixel level and in compositional structure, we show that (1) gender representation shapes visual features across artistic styles, (2) style keywords carry these patterns into T2I generation, and (3) generative models tend to amplify gender artifacts beyond what is observed in historical sources.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-289](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
