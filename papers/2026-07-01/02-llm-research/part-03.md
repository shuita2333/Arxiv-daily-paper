# 🧠 大模型相关研究 | 2026年07月01日

> 本类共 **247** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-247](./part-05.md)

---

### 101. [Beyond Trajectory Matching: Reflow with Marginal Distribution Alignment](https://arxiv.org/abs/2606.29287)

**<font color=#1a73e8>作者：</font>** Chen Wang, Peiran Yun, Pan Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion and continuous-flow generative models achieve high-quality generation, and their deterministic sampling can be formulated as solving learned ODE dynamics. However, accurate ODE discretization often requires many steps, making efficient few-step generation a key challenge. Among acceleration strategies, reflow-based distillation simplifies teacher ODE trajectories so that a student model can approximate the teacher transport with fewer steps. We identify a theoretical limitation of this paradigm, namely that trajectory matching can under-determine the distribution induced by the student model. In particular, two student models can attain the same trajectory-matching loss while inducing different endpoint marginal distributions, which may lead to different generation quality. To address this limitation, we introduce a marginal-alignment regularizer that penalizes the discrepancy between the student-induced marginal and the corresponding teacher marginal at the endpoint of each distillation interval. The regularizer is computed by tracking log-density changes along the ODE induced by the student model and evaluating scores from the frozen teacher model, without requiring auxiliary trainable networks or adversarial optimization. The resulting framework applies uniformly to the reflow family, including vanilla reflow and piecewise reflow. We further prove a telescoping total-variation bound showing that local marginal alignment controls the final-time discrepancy between the student-induced and teacher-induced distributions. Experiments on benchmark backbones demonstrate the effectiveness of the proposed method for few-step generation.

---


### 102. [Process Advantage Signal Shaping: A Paradigm-Agnostic Middleware for Process-Supervised RL in LLM Reasoners](https://arxiv.org/abs/2606.29296)

**<font color=#1a73e8>作者：</font>** Chao Wang, Hongtao Tian, Tao Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) is a default recipe for process-supervised reinforcement learning of LLM reasoners, and dense process supervision -- via learned process reward models (PRMs) or on-policy-distillation KL signals -- is a common way to densify its otherwise weak outcome reward. Layering such a step-level signal on top of GRPO's group-standardized advantage, however, exposes three structural pathologies: \emph{channel contamination} between the pooled process, outcome, and format streams at group standardization; \emph{resolution mismatch} between the granularity of the process signal and the granularity of the logical decisions being credited; and a \emph{cumulative trap} by which GRPO's return-to-go sum surfaces either length inflation or truncated exploration depending on the sign regime of the signal. We propose \textbf{PASS} (\emph{Process Advantage Signal Shaping}), a compact middleware that sits between any scalar step-level process signal and GRPO's clipped surrogate and addresses the three pathologies in turn: \emph{Advantage Fusion} standardizes the three streams independently within each group, \emph{Chunk-by-Value} derives value-homogeneous chunks from the signal itself and broadcasts credit within each chunk, and \emph{Divide-Length} converts the cumulative objective into an average-value-density score. We validate PASS across two domains and two process-signal paradigms -- a learned PRM on mathematical reasoning and an on-policy-distillation KL signal (with a generalized variant) on multi-hop question answering -- and under two group-standardization operators. In every regime PASS delivers a consistent pass@1 gain over the corresponding GRPO baseline.

---


### 103. [Hierarchical Experimentalist Agents](https://arxiv.org/abs/2606.29315)

**<font color=#1a73e8>作者：</font>** Abhranil Chandra, Sankaran Vaidyanathan, Utsav Dhanuka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to take actions in the real world and support human decision-making, yet most agents rely on parametric knowledge, fixed post-training data, retrieval, or search. This paradigm breaks down in novel domains and for sophisticated queries that cannot be answered from prior knowledge alone. Knowing the laws of physics, for instance, does not by itself enable LLMs to answer queries or complete long-horizon tasks in a complex physical system. To address this, we introduce Hierarchical Experimentalist Agents (HExA), an in-context self-improvement framework to learn from active experimentation. HExA iteratively designs and refines query-relevant experiments, learns a reusable library of composable skills from experience, and integrates experimental evidence to answer queries or take actions. HExA is training-free, compatible with any black-box model, and does not require external supervision, oracles, or offline data. To evaluate active experimentation, we introduce Interphyre, a tool-calling benchmark built on the PHYRE 2D procedural physics environment, where agents propose interventions and test hypotheses through simulation APIs. Experiments show that current LLM agents struggle in these settings, especially on the hardest levels of Interphyre. Claude Sonnet 4.6 achieves only 2% success, while HExA improves the same model to up to 77% success. HExA also improves open-weight models and outperforms agentic baselines such as ReAct and Reflexion. Moreover, using only skills learned from easier levels and transferred without active experimentation, HExA achieves 44% success, demonstrating the reusability and generalization of its learned skills. Overall, HExA shows that learning through active experimentation can help agents discover useful knowledge, acquire reusable skills, and make efficient progress on novel long-horizon tasks.

---


### 104. [RAGA: Real Time Ray Traced Gaussian Shadow Casting for 3DGS Avatar-Scene Interaction](https://arxiv.org/abs/2606.29329)

**<font color=#1a73e8>作者：</font>** Aymen Mir, Riza Alp Guler, Jian Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study the problem of physically plausible shadow casting when animating 3D Gaussian Splatting (3DGS) avatars, either individually or in multi-avatar and object-interaction scenarios, within existing 3DGS scenes. In contrast to prior methods that rely on binary hit tests and mesh-based shadow casters, our method performs shadow computation entirely in Gaussian space, without requiring any mesh reconstruction. We introduce RAGA, a Ray-Traced Gaussian Shadow Casting formulation based on exact ray-Gaussian line integrals. For each occluding Gaussian, we integrate the opacity profile along the shadow ray and normalize by the theoretical maximum integral, producing a weight that captures how the ray traverses the occluder rather than merely whether an intersection occurred. To reduce temporal variance from clothing deformations in animated avatars, we further introduce an avatar proxy representation that stabilizes shadow casting while preserving visual fidelity. We implement RAGA using custom CUDA kernels integrated with the NVIDIA OptiX framework; as such, our shadow tracer runs at rates of about 50 FPS. We evaluate on single-avatar, multi-avatar, and avatar-object interaction scenarios across multiple datasets, demonstrating substantially improved shadow realism, temporal stability, and scene coherence. Our project page is available at this https URL.

---


### 105. [AMR: Adaptive Modality Routing for Multimodal Polyglot Speaker Identification](https://arxiv.org/abs/2606.29335)

**<font color=#1a73e8>作者：</font>** Chuxiao Zuo, Yao Zhu, Minqiang Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal speaker identification systems face two key challenges in real-world deployment: missing modalities and language mismatch between training and testing conditions. In practical scenarios, background multi-speaker conversations, ambient noise, and overlapping speech further degrade identification accuracy. To address these challenges, we propose a multimodal polyglot speaker identification system for the POLY-SIM 2026 Grand Challenge. The system is fundamentally built upon Adaptive Modality Routing(AMR), a modality fusion module that dynamically assesses per-sample input quality and integrates modality information. Specifically, AMR employs two modality adapters to process the embeddings extracted from a linguistically robust audio encoder(W2V-BERT 2.0) and a large-scale pretrained face encoder(IResNet-18), producing modality-adapted embeddings. Based on these adapted embeddings, a trainable router estimates dynamic modality weights, which are subsequently applied to aggregate the modality-specific logits for the final prediction. To optimize this routing mechanism, we adopt a modality-aware training strategy that constructs four types of sample pairs to simulate diverse input conditions, with KL divergence serving as explicit supervision for weight assignment. Experimental results on the POLY-SIM 2026 evaluation set show that the proposed system achieves identification accuracy of 99.93%(English multimodal, P3), 100.00%(Urdu multimodal, P5), 97.50%(English audio-only, P4), and 98.83%(Urdu audio-only, P6). The average accuracy across all four protocols is 99.07%, surpassing the Fusion and Orthogonal Projection(FOP) baseline by 32.73%.

---


### 106. [When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning](https://arxiv.org/abs/2606.29354)

**<font color=#1a73e8>作者：</font>** Zhengqi Pei, Qingming Huang, Shuhui Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) improves large language models (LLMs) on difficult reasoning tasks, but it often incurs long natural-language rationales that are poorly aligned with efficient machine reasoning. We propose Communicative Language Symbolism Routing (CLSR), a test-time framework in which multiple LLM agents autonomously invent, evolve, and share compact Language Symbolism Frameworks (LSFs), while a latent-free router adaptively selects and composes these languages per query to optimize the accuracy-token trade-off. Unlike prompt optimization that refines surface instructions, CLSR treats each LSF as a reusable symbolic protocol with compact symbols, usage rules, and a message-passing contract, and improves it through an evolutionary loop driven by correctness and token cost. At inference time, the router may invoke a single low-cost LSF call, ensemble multiple LSFs, or execute a multi-round LSF composition protocol on harder queries. Across challenging benchmarks, CLSR reduces latency-oriented generated token completion by $3\sim 6\times$ compared to standard CoT while maintaining accuracy. We further derive an information-theoretic lower bound on token cost under arbitrary symbolism and show that, under an interpreter-realizability premise, multi-round LSF protocols conditionally subsume program-execution pipelines. Code is publicly available (this https URL).

---


### 107. [Dynamic Parsing and Updating Natural Language Specification using VLMs for Robust Vision-Language Tracking](https://arxiv.org/abs/2606.29357)

**<font color=#1a73e8>作者：</font>** Xiao Wang, Liye Jin, Dan Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language tracking guided by natural language specifications leverages high-level semantic cues of target objects to substantially boost tracking accuracy and robustness. Existing studies have verified that adaptively optimizing textual descriptions throughout the tracking process can effectively mitigate the semantic-visual mismatch induced by dynamic variations in target appearance, position, and other inherent attributes. Nevertheless, mainstream methods that directly generate textual information via sequence models or large language models inevitably suffer from inherent defects, including erroneous target updating, excessive background distraction, and pervasive hallucination artifacts. To address the aforementioned limitations, this paper proposes a novel language dependency parsing mechanism to precisely distill core tracking principal components, encompassing target objects, semantic concepts, and background contextual information. On this basis, we perform component-aware adaptive textual description updates by exploiting the powerful cross-modal understanding capability of the pre-trained vision-language model Qwen-VL. By integrating the proposed elaborately designed modules into the baseline framework, our method achieves consistent and superior tracking performance on multiple large-scale vision-language tracking benchmarks, including TNL2K, LaSOT, TNLLT, and OTB-LANG. The source code and pre-trained models will be released at this https URL.

---


### 108. [TriageRA-CCF: Source-Side Clinical Confidence and Coverage Signals for Adaptive Rank Budgeting in Medical LLMs](https://arxiv.org/abs/2606.29375)

**<font color=#1a73e8>作者：</font>** Shucan Ji, Yining Huang, Hongliang Guo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical large language models are commonly adapted with a fixed low-rank budget, even though medical questions differ substantially in confidence, clinical coverage, and cross-domain difficulty. We study adaptive rank budgeting for parameter-efficient medical question answering: for each question, the adapter decides whether to activate a small, medium, or large subset of LoRA rank channels. The central challenge is that a naive adaptive budget router can collapse to unstable choices or spend capacity without improving shifted benchmarks. We propose TriageRA-CCF, a source-side teacher for adaptive rank-budgeted LoRA. It combines three signals computed only from source training data: base-model answer confidence, metadata-cell clinical coverage, and a counterfactual close-miss proxy. These signals supervise a straight-through budget router over active ranks {2,4,8}, together with budget-cost, entropy, and rank-balance regularization. Under a matched CMB-source training protocol, TriageRA-CCF achieves the best average accuracy among LoRA, DoRA, and MoELoRA baselines on both Qwen3-8B and Llama3.1-8B. The gains are modest and non-uniform across benchmarks: +0.21 average points over the strongest external baseline on Qwen3-8B and +0.16 on Llama3.1-8B. Component ablations show that confidence, coverage, and counterfactual signals all provide useful budget supervision, but their combination is not monotonically best on every backbone.

---


### 109. [Diagnosing and Repairing Factual Errors in RAG under Budget Constraints](https://arxiv.org/abs/2606.29377)

**<font color=#1a73e8>作者：</font>** Soroush Hashemifar, Havva Alizadeh Noughabi, Fattane Zarrinkalam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) improves the factuality of large language models by grounding responses in external evidence, yet real-world deployments remain fragile. Failures often stem from missing or weakly relevant evidence, as well as from generation that does not faithfully reflect the retrieved context. Many existing approaches rely on fine-tuning, privileged access to internal model signals, or resource-insensitive escalation strategies, which limits their practicality in black-box and budget-constrained settings. We propose D2R-RAG (Diagnose-to-Repair RAG), a model-agnostic and resource-aware framework that combines lightweight failure diagnosis with adaptive repair. D2R-RAG derives interpretable failure signatures from observable signals in the query, retrieved evidence, and generated response, and then selects from a small set of corrective actions under explicit latency and VRAM constraints. Experiments on FEVER and HotpotQA show that D2R-RAG improves reliability over recent baselines and achieves better accuracy--efficiency trade-offs across multiple compute budgets. The code is available at this https URL.

---


### 110. [NaLA: A 3D Native LLM Layout Agent for High-quality 3D Scene Generation](https://arxiv.org/abs/2606.29395)

**<font color=#1a73e8>作者：</font>** Cheng Wan, Yongsen Mao, Wenzheng Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, Large Language Models (LLMs) have emerged as promising layout agents for 3D scene generation. Existing layout agents still suffer from implausible layout generation because most of them convert 3D assets and 3D layouts into textual descriptions as inputs and outputs, which involves severe information loss due to the modality gap between texts and 3D assets and 3D layouts. We propose NaLA, a native 3D LLM layout Agent for high-quality 3D scene generation by placing 3D assets in the scene. For the inputs, NaLA encodes 3D scene boundaries and 3D assets directly into the LLM, preserving fine-grained geometry and enabling explicit reasoning over relationships like collisions, surface supporting, and containment. To accurately output the positions and orientations of assets, NaLA adopts a coarse-to-fine prediction mechanism that first predicts discrete poses in an autoregressive manner and then refines the discrete poses with a continuous regression. Trained on diverse layout datasets, NaLA attains strong geometric perception and layout coherence. Experiments demonstrate that NaLA outperforms prior layout agents in both generation quality and inference efficiency, with comprehensive ablation studies to verify each component's effectiveness.

---


### 111. [LLM-Guided Planning for Multi-hop Reasoning over Multimodal Nuclear Regulatory Documents](https://arxiv.org/abs/2606.29399)

**<font color=#1a73e8>作者：</font>** Mingyu Jeon, Bokyeong Kim, Suwan Cho 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reviewing nuclear regulatory documents requires multi-hop reasoning across tens of thousands of pages, where judgments depend on evidence assembled across multiple chapters. We frame this task as planning: an LLM-based agent observes the evidence collected so far, picks the next document fragment to inspect, and stops when the evidence is sufficient. The agent operates over a vectorless document tree using browse, read, and search tools, and maintains a dynamic knowledge graph (KG) as state. On a 200-question benchmark over NuScale Final Safety Analysis Report (FSAR) documents, the system reaches 81.5% accuracy with a RAGAS Faithfulness of 0.93. The dominant performance factor is planning: against PageIndex, which uses the same document tree without state-conditioned action selection, the gap is +38.0pp (43.5% to 81.5%, p<0.001). The system also outperforms LightRAG (73.0%, p<0.05), HippoRAG (70.5%, p<0.01), and GraphRAG (49.5%, p<0.001), and matches RAPTOR (75.5%, p=0.11) without offline indexing. Edge inference adds 2.8x cost without raising accuracy; we retain it as a traceability module. Of 7,391 inferred edges, 3 Violates edges (0.04%) flag scope boundaries (Q058) and partial conformance (Q176) as typed annotations that a human reviewer can audit.

---


### 112. [LC-ICL: Label-Guided Contrastive In-Context Learning for Robust Information Extraction](https://arxiv.org/abs/2606.29407)

**<font color=#1a73e8>作者：</font>** Xiao You, Tianwei Yan, Shan Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> There has been increasing interest in exploring the capabilities of advanced large language models (LLMs) in the field of information extraction (IE), specifically focusing on tasks related to named entity recognition (NER) and relation extraction (RE).Although researchers are exploring the use of few-shot information extraction through in-context learning with LLMs, they tend to focus only on using correct or positive examples for demonstration, neglecting the potential value of incorporating incorrect or negative examples into the learning this http URL this paper, we present LC-ICL a novel few-shot technique that leverages both correct and incorrect sample constructions to create in-context learning demonstrations. This approach enhances the ability of LLMs to extract entities and relations by combining positive samples with negative samples annotated by error-cause labels. These labels expose more detailed error features in erroneous examples, enabling the model to understand why similar predictions fail and avoid repeating such errors during this http URL, our proposed method taps into the inherent contextual information and valuable information in hard negative samples and the nearest positive neighbors to the test and then applies the in-context learning demonstrations based on LLMs. Our experiments on various datasets indicate that LC-ICL outperforms previous few-shot in-context learning methods, delivering substantial enhancements in performance across a broad spectrum of related tasks. These improvements are noteworthy, showcasing the versatility of our approach in diverse scenarios.

---


### 113. [Bit-ViP: Leveraging Bit-planes to Preserve Visual Privacy in Images through Obfuscation](https://arxiv.org/abs/2606.29417)

**<font color=#1a73e8>作者：</font>** Vishesh Kumar Tanwar, Ashish Gupta, Sanjay Madria 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The unprecedented growth of computer vision applications, such as surveillance systems and social media, raises security and visual privacy concerns, especially when data is stored on cloud servers. Image obfuscation offers a way to preserve visual privacy while maintaining an adequate level of usability; thus, it has been a topic of great interest in recent years. However, prior obfuscation schemes are either vulnerable to malicious attacks, such as model inversion to reconstruct original images from obfuscated images, or generate non-trainable obfuscated images, making them unusable for achieving reasonable accuracy. This paper proposes a novel bit-plane-based image obfuscation scheme, {\em Bit-ViP}, to preserve visual privacy for image-based recognition tasks. The Bit-ViP scheme produces secure, usable images by incorporating an innovative end-to-end obfuscation function. While doing so, the obfuscated image would contain non-invertible noise (generated by Lorenz's chaotic system and differential privacy), making it hard for an adversary to reconstruct the original image. We conduct extensive experiments on two popular activity recognition datasets, namely UCF101 and HMDB51, to validate the effectiveness of Bit-ViP. In the face of attacks on reconstruction, pixel frequency, information entropy, and pixel inter-correlation, we present a rigorous security analysis demonstrating tangible improvements over existing schemes.

---


### 114. [FADE: Mitigating Hallucinations by Reducing Language-Prior Dominance in Large Vision-Language Models](https://arxiv.org/abs/2606.29431)

**<font color=#1a73e8>作者：</font>** Yichen Guo, Kai Tang, Fenglai Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite the impressive capabilities of Large Vision-Language Models (LVLMs), they remain susceptible to hallucination, generating content inconsistent with the input image. Recent studies attribute this to the dominance of language priors over visual inputs and employ contrastive decoding methods to mitigate this dominance, but the mechanistic origin remains unexplored. We investigate the information flow through each transformer layer and find that attention modules consistently aggregate visual evidence, while FFN modules at critical layers act as the source of language priors. These priors can override visual evidence, causing correct predictions in intermediate layers to drift toward incorrect outputs. Based on this insight, we propose FADE (FFN Attenuation for DEcoding), a training-free method that attenuates FFN outputs to reduce language-prior dominance. Evaluations on POPE, CHAIR, and MME benchmarks across LLaVA-1.5, mPLUG-Owl2, and InstructBLIP show that FADE effectively mitigates hallucinations while preserving inference efficiency.

---


### 115. [LLMography: Transforming Human-AI Conversations into Traceability, Oversight, and Auditability Indicators](https://arxiv.org/abs/2606.29437)

**<font color=#1a73e8>作者：</font>** Mohammed Bousmah  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The growing use of Large Language Models (LLMs) in education, software engineering, academic writing, and technical documentation raises a key question: how can we evaluate not only AI-assisted outputs, but also the interaction process that produced them? Current debates often focus on detecting whether a final artifact was generated by AI, while overlooking the conversation history that reveals human direction, AI contribution, corrections, validation, and traceability.
This paper introduces LLMography, a framework for transforming Human-AI conversations into measurable indicators of provenance, human contribution, AI dependency, reproducibility, and auditability. By analogy with bibliography and webography, LLMography documents the dynamic trajectory of interaction between a human and a Large Language Model as a structured trace of Human-AI co-production.
We present a prototype that analyzes Human-AI conversation traces and generates KPI reports including Prompt Quality Score, Human Direction Score, AI Dependency Level, Auditability Score, Final Output Traceability, Privacy Risk Level, and a recommended LLMography label. A preliminary exploratory evaluation was conducted on 19 anonymized audit reports from engineering students. Most interactions were classified as Human-AI co-produced, with average scores of 86.8/100 for Human Direction, 81.9/100 for Prompt Quality, 72.8/100 for Auditability, and 77.1/100 for Final Output Traceability.
The paper also applies LLMography to its own writing process, classified as human-originated, human-directed, AI-assisted co-production. The findings suggest that AI transparency should move beyond output detection toward documenting the history of interaction.

---


### 116. [Bridging VideoQA and Video-Guided Agentic Tasks via Generalized Keyframe Extraction](https://arxiv.org/abs/2606.29445)

**<font color=#1a73e8>作者：</font>** Sunqi Fan, Qingle Liu, Runqi Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding is a fundamental capability for multimodal intelligence, and recent Multimodal Large Language Models (MLLMs) have achieved remarkable performance on Video Question Answering (VideoQA) benchmarks. However, existing benchmarks primarily evaluate whether models can perceive shallow visual cues, while rarely examining whether MLLMs can learn deeper knowledge or procedural skills from video tutorials and generalize them to downstream long-horizon agentic tasks. To address this gap, we introduce VG-GUIBench (Video-Guided GUI Benchmark), a new benchmark designed to evaluate whether MLLM-based GUI agents can follow video tutorials to complete corresponding GUI interactive tasks. Furthermore, we observe that the performance of models on both VideoQA and video-guided agentic tasks critically depends on effective keyframe extraction. Based on this observation, we propose TASKER (Task-driven And Scene-aware Keyframe searchER), a keyframe extraction algorithm that jointly considers task relevance and scene dynamics to identify informative frames. Experimental results demonstrate that TASKER achieves significant performance improvements on both VideoQA and video-guided agentic task benchmarks, outperforming the best baseline by 2.0% on the EgoSchema fullset and 1.8% on the NExT-QA dataset, respectively. These results further highlight the potential of generalized keyframe extraction methods for video understanding tasks. Our code and data are available at this https URL.

---


### 117. [The Platonic Defense: Backdoor Defense for Self-Supervised Encoders in the Era of Large Scale Pre-training](https://arxiv.org/abs/2606.29451)

**<font color=#1a73e8>作者：</font>** Tuo Chen, Minjing Dong, Benlei Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) pretrained models have become a dominant paradigm for visual representation learning, but they are vulnerable to backdoor attacks. Existing defenses struggle to defend against such attacks in a fully black-box setting because they often require access to labels, attack patterns, or training data. To tackle this issue, we propose a new attack-agnostic, model-agnostic, and modality-agnostic black-box test-time defense paradigm, called \emph{Platonic Representation Defense}. It is inspired by the Platonic Representation Hypothesis, which suggests that large-scale independently trained encoders converge toward compatible projections of the same underlying reality. We formalize this idea as a conditional energy function defined over source representations and a set of reference representations. The energy function is trained for detection through noise-contrastive estimation and for representation purification through denoising score matching. Theoretically, the energy gap between matched and mismatched samples is lower bounded by the mutual information between source and reference representations. We demonstrate the effectiveness of our method on multiple self-supervised encoders and more than 10 attacks. The method can perform both representation detection and purification, and achieves substantial performance gains across multiple attacks. Code is available \href{this https URL}{here}.

---


### 118. [Interpretable Inverse Design of Metal-Organic Frameworks with Large Language Model Agents](https://arxiv.org/abs/2606.29459)

**<font color=#1a73e8>作者：</font>** Kyungmin Nam, Seunghee Han, Jihan Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse design of metal-organic frameworks (MOFs) requires searching a combinatorially vast space where property labels are expensive and most machine-learning models reveal little about why a structure succeeds. We introduce LLM4MOF, a closed-loop framework in which language-model agents reason about chemistry, build candidate MOFs, and test them in simulation, refining hypotheses over ten autonomous iterations. One agent proposes interpretable design hypotheses over metal nodes, linkers, pore geometry, and functional chemistry, and a second translates them into constraints that select candidate MOFs, each made of a metal node, organic linker, and matching topology. Each hypothesis is tested through four diagnostic beams that apply different subsets of its constraints, so comparing them shows whether geometry, chemistry, or metal choice drives performance. Even when blind to the global property landscape of databases, LLM4MOF concentrates its search on top-performing structures across six adsorption, separation, and electronic-structure tasks within 400 property evaluations. The same loop also generates new MOFs de novo and validates them in live simulation, where it adapts the geometry to each requested condition, outperforming random search and a genetic algorithm at roughly $1 per campaign. LLM4MOF shows that language-model agents can run interpretable, simulation-grounded inverse design without training a model per objective.

---


### 119. [MIRROR: Aligning Semantic Relations from Language to Image via Gromov--Wasserstein](https://arxiv.org/abs/2606.29462)

**<font color=#1a73e8>作者：</font>** Hong-Han Wang, Yuntao Wang, Hu Ding  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) inherit rich relational priors from their language backbones, yet often fail when asked to apply these relationships in visual contexts. We trace this failure to a structural blind spot: projection-based alignment trains each visual token to carry the right semantics, but never asks whether the relationships between concepts survive the crossing from language to vision. To address this, we propose MIRROR (Mapping Inter-concept Relations from language to visual Representation via Optimal-transport-based Regularization), a geometric regularization framework that transfers relational priors from language to vision by exploiting the rich relational structure encoded in language representations. Specifically, we derive a surrogate loss from the proposed Semi-Inverse Gromov-Wasserstein (SI-GW) problem, an inverse geometric problem that aligns visual representations with language-derived relational priors. We show that this formulation admits a unique closed-form solution that prescribes the ideal visual relational structure implied by language geometry and cross-modal coupling. The structure of the formulation also enables efficient computation, making it applicable to long token sequences. Applying SI-GW inside decoder-only Transformers requires careful design. We introduce targeted strategies at the layer, head, and token levels to ensure stable extraction without additional parameters or inference cost. MIRROR improves relational consistency while preserving performance on general vision-language tasks.

---


### 120. [Rank-Aware Hyperbolic Alignment for Vision-Language Dataset Distillation](https://arxiv.org/abs/2606.29464)

**<font color=#1a73e8>作者：</font>** Jongoh Jeong, Sun-Kyung Lee, Kuk-Jin Yoon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language dataset distillation (VLDD) compresses a large image-text paired dataset into a small set of synthetic pairs that can efficiently train contrastive vision-language models under strict data and compute budgets. Most existing methods match expert trajectories or cross-modal statistics, yet still enforce full-dimensional alignment in a Euclidean embedding space. This is often overly restrictive due to rank-deficient image--text correlation, with shared semantics concentrated in a low-dimensional range and remaining variation spread across a weakly correlated residual subspace. LoRS relaxes alignment at the similarity level by low-rank factorization, but does not explicitly control dominant alignment capacity and structure in the representation space. We thus propose a rank-aware hyperbolic alignment (RAHA) that combines hierarchical geometry with explicit alignment-capacity control. RAHA lifts multimodal representations to hyperbolic space and optimizes distilled pairs with asymmetric objectives that enforce geodesic alignment in the shared range while regularizing the residual subspace to preserve modality-private diversity and improve transfer robustness. Experiments on benchmarks show that RAHA demonstrates competitive cross-modal retrieval and improved transfer indicators under fixed budgets.

---


### 121. [Prototype Latent World Model Replay for Class-Incremental Learning](https://arxiv.org/abs/2606.29465)

**<font color=#1a73e8>作者：</font>** Weizhi Nie, Hui Wang, Weijie Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Class-incremental learning requires a model to learn new classes while preserving decision regions for old ones. This is difficult when raw old samples are no longer available. We propose Prototype Latent World Model Replay, a memory-free framework that stores old classes as distributions over stable hidden states rather than as images. A frozen ImageNet-pretrained encoder maps each image into a latent state space. In this space, each class is summarized by several prototype-centered distributions with class-specific variances. When new classes arrive, the model samples old latent states from this prototype world model. It then trains a lightweight adapter and classifier using both sampled old states and real new-class features. We also add a supervised contrastive term in the adapter space to promote intra-class compactness and old-new class separation. On Split CIFAR-100, our method improves over fine-tuning under Inc5, Inc10, and Inc20 without storing raw exemplars. The full Ours-LWM+Con model raises LastAcc from 4.55% to 31.64%, from 9.06% to 37.06%, and from 16.96% to 43.10% in Inc5, Inc10, and Inc20, respectively. It also achieves AvgAcc of 45.86%, 52.19%, and 56.18%. Ablation and retention analyses show that stable latent-state replay is the main source of the gain. Contrastive separation further refines the old-new geometry. These results suggest that prototype latent memory preserves reusable class-state distributions, rather than only fitting the current classifier.

---


### 122. [mamabench and mamaretrieval: Benchmarks for Evaluating Medical Retrieval-Augmented Generation in Maternal, Neonatal, and Reproductive Health](https://arxiv.org/abs/2606.29467)

**<font color=#1a73e8>作者：</font>** Yi Ren  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical question-answering benchmarks rarely cover the maternal, neonatal, child, and reproductive-health questions a nurse-midwife asks, and, to our knowledge, no public chunk-level relevance benchmark exists for maternal-health guideline retrieval. We release two benchmarks that fill these gaps. mamabench is a scope-filtered QA set of 25,949 items assembled from seven existing expert-authored sources across multiple-choice, short-answer, and rubric-graded tracks; to help users calibrate the LLM judge that scores the rubric track, we re-scope HealthBench's physician-labelled meta-evaluation to the domain. mamaretrieval pairs 3,185 clinical queries with graded (0-6) relevance labels over a 63,650-chunk maternal-health guideline corpus, using a decomposed rubric that distinguishes a chunk that answers a query from one merely on its topic. Three decisions shape both: assemble and filter expert sources rather than author questions, grade relevance rather than binarise it, and measure and disclose the limits of the labels -- scope-classifier agreement, a frontier-judge check, and a pooling-completeness audit -- rather than treat them as an oracle. A companion paper uses the benchmarks to evaluate a deployed on-device assistant; both are released openly for research.

---


### 123. [CRAFT: Counterfactual Credit Assignment from Free Sibling Rollouts for Self-Distilled Agentic Reinforcement Learning](https://arxiv.org/abs/2606.29476)

**<font color=#1a73e8>作者：</font>** Zibin Meng, Kani Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-distilled agentic reinforcement learning augments trajectory-level reward with a token-level distillation loss, using as its teacher the same policy conditioned on privileged context. The prevailing recipe gates this loss by a single scalar, the teacher-student log-probability gap. This signal is doubly limited: it is retrospective, scoring only the realised rollout and never the counterfactual ones, and it is sign-blind, never signalling when a teacher-preferred action would have harmed the trajectory. We introduce CRAFT, a three-pillar credit-assignment scheme that addresses both limitations. Pillar 1, Counterfactual Token Importance, reuses the G-1 sibling rollouts that GRPO already samples and importance-weights them by the log-probability gap to form a self-normalised estimate of the group-level counterfactual change in advantage from up-weighting teacher-preferred actions at each step; this yields a signed per-token credit at near-zero extra compute. Pillar 2 is an asymmetric controller that raises the distillation weight as it lowers the reference-KL weight along an exponential moving average of gate activity, and conversely. Pillar 3 polarises the KL penalty token by token, switching between a mode-seeking and a mode-covering update according to the sign of the credit. Each pillar has an independent switch that, when disabled, renders the loss and gradient byte-identical to the baseline in IEEE-754 arithmetic, so any measured gain is attributable to algorithmic change rather than implementation drift. We prove the estimator's consistency and a variance bound, give structural and bit-exact reproducibility guarantees, and evaluate CRAFT across three agentic environments, four model scales, and five end-to-end methods, plus two tabulated prior-work baselines. Among these is Adaptive-CRINGE, a comparator sharing Pillar 2 with CRAFT, isolating the counterfactual contribution.

---


### 124. [Reported Confidence in LLMs Tracks Commitment More Than Correctness](https://arxiv.org/abs/2606.29490)

**<font color=#1a73e8>作者：</font>** Dharshan Kumaran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Confidence is an estimate of the probability that a chosen answer is correct. Verbal confidence reports are widely used as uncertainty measures in large language models, but whether they are best understood as estimates of correctness is unclear. We test this with a two-stage abstention paradigm from the neuroscience of perceptual decision making: a model first answers and reports its confidence, then decides whether to commit it to a user or abstain. Across four non-reasoning models, prompt framings, and confidence formats, verbal confidence predicted the commit/abstain decision substantially better than whether the answer was correct. Calibrated token log-probabilities showed the opposite profile, with abstention-prediction coupled to correctness discrimination, the signature of an answer-evidence signal. After removing the variance verbal confidence shared with log-probabilities, the residual stayed aligned with commitment while its link to correctness fell to near chance. The dissociation generalised to four reasoning models across four benchmarks of varying difficulty, from hard multiple-choice to frontier-level freeform questions. Mechanistic analyses in Gemma 3 and 4 were convergent: a post-answer state known to causally support verbal-confidence generation already encoded the future abstention decision before the abstention prompt, organised mainly by that decision rather than by correctness, the two lying in approximately orthogonal directions in activation space. Steering along a verbal-confidence-specific direction causally shifted abstention. Verbal and log-probability confidence are thus not interchangeable: log-probabilities track answer evidence and correctness, whereas verbal confidence is better understood as a behaviour-facing readout of an internal commit-readiness state, challenging the practice of treating verbal reports as proxies for reliability.

---


### 125. [Cognitive World Models for Process-Level Social Influence Evaluation](https://arxiv.org/abs/2606.29495)

**<font color=#1a73e8>作者：</font>** Minghui Ma, Bin Guo, Han Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Social influence dialogue changes user behavior by altering internal cognitive states. The central evaluation question is whether the user's beliefs, desires, intentions, and emotions measurably change over the course of conversation, a process-oriented criterion that neither surface-level text metrics (BLEU/ROUGE) nor single-score LLM judgments can capture. We propose the \textbf{Cog}nitive \textbf{W}orld \textbf{M}odel \textbf{(CogWM)}, an LLM-based user model that reframes multi-turn dialogue evaluation from ``what did the user say'' to ``how did the user's internal cognitive state evolves.'' CogWM jointly predicts BDI/E cognitive states and user utterances and serves as both a user simulator and an evaluation platform, using a three-tier evaluation framework that covers turn-level fidelity, trajectory-level state dynamics, and task-level composite scoring. Trained via our \textbf{S}ummarize-\textbf{a}nd-\textbf{A}llocate \textbf{(SaA)} annotation pipeline on 150,454 user-turn samples across four social influence scenarios, CogWM achieves 77.6\% emotion accuracy (2.1$\times$ over GPT-5.5). In 3600 multi-agent discrimination trials, it distinguishes six commercial agents by their cognitive influence, with Llama-4-Scout ranking first (CTS +0.233). CogWM moves social influence dialogue evaluation from terminal judgment to process tracking. We have released our code\footnote{\scriptsize Code: this https URL} and models\footnote{Model: this https URL}.

---


### 126. [UCOB: Learning to Utilize and Evolve Agentic Skills via Credit-Aware On-Policy Bidirectional Self-Distillation](https://arxiv.org/abs/2606.29502)

**<font color=#1a73e8>作者：</font>** Songjun Tu, Chengdong Xu, Qichao Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill memories can improve agentic reinforcement learning by reusing past experience as textual guidance, but retrieved skills are not oracular: they may help in one state while misleading the same policy in another. This makes the common privileged-teacher assumption fragile, namely that a skill-conditioned prompt can be treated as a fixed teacher for the no-skill prompt. We introduce UCOB, a framework for learning to utilize and evolve agentic skills via credit-aware on-policy bidirectional self-distillation. UCOB treats skill-conditioned and no-skill prompts as two on-policy context views of the same model, compares their return-to-go within the same task and anchor state, and uses the higher-return view as the local teacher. This local credit signal internalizes useful skill-conditioned behavior, corrects misleading skill usage, and guides task/state skill memory updates, utility-aware retrieval, and reflection self-training. Experiments on agentic tasks, including ALFWorld, WebShop, and Search-QA, show that UCOB outperforms skill-free RL, skill-memory baselines, and self-distillation methods across model scales, with up to 23.5 and 18.0 point gains over SOTA baselines on ALFWorld and WebShop. Ablations and analyses further validate its core mechanisms and efficiency.

---


### 127. [The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning](https://arxiv.org/abs/2606.29526)

**<font color=#1a73e8>作者：</font>** Jing Liang, Hongyao Tang, Yi Ma 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has gained growing attention in large language model (LLM) post-training, yet RL training remains fragile and can suffer from instability or collapse. One vital cause is training-inference mismatch: LLM adopts separate inference and training engines for generation efficiency and training precision, which in practice exhibits inconsistent probabilities for the same trajectories on training and inference sides, even with synchronized model parameters. This naturally induces a special type of off-policyness ever existing and poisoning the training. Prior works have made various efforts in addressing the off-policyness to stabilize the training policies under the mismatch. In this paper, we point out the objective misalignment neglected by existing works that an effective update to the policy in the training engine not necessarily ensures the improvement of the inference policy, i.e., the one used in deployment. To this end, we propose a new policy optimization objective for LLM RL, named Monotonic Inference Policy Improvement (MIPI). Following this principle, we introduce Monotonic Inference Policy Update (MIPU), a two-step LLM RL framework that constructs sampler-referenced candidate updates and selectively accepts synchronized candidates using an inference-side gap proxy. Experiments conducted on two model scales under high mismatch show that MIPU improves average reasoning performance and training stability.

---


### 128. [MotionAtlas: Detailed Region Captioning for Motion-Centric Videos](https://arxiv.org/abs/2606.29531)

**<font color=#1a73e8>作者：</font>** Weisong Liu, Haochen Wang, Kuan Gao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose MotionAtlas, a system for detailed captioning of motion-centric videos, comprising (1) a dedicated human-annotated benchmark, (2) a scalable, high-quality pipeline to construct training samples, and (3) a family of powerful Video-MLLMs. Unlike conventional global motion captioning datasets, we focus on region-aware motion captioning: given a video and a spatiotemporal mask, the model generates precise descriptions of motion within the target region, thereby alleviating visual clutter and motion entanglement and enabling reliable, quantifiable evaluation. Concretely, we first build MotionAtlas-Bench, a comprehensive benchmark comprising 2,073 multiple-choice questions, meticulously annotated for a curated set of high-quality, motion-centric videos, to evaluate fine-grained motion understanding of the objects in question. Second, we design a rigorous and scalable data pipeline that leverages self-bootstrap refinement to suppress fine-grained hallucinations, yielding 159k high-quality motion captioning data. Third, we design a tailored training data composition strategy, which achieves consistent and substantial performance gains across diverse baseline Video-MLLMs, including Molmo2 and Qwen3-VL. For instance, MotionAtlas-4B surpasses Qwen3-VL-4B by an average of 5.2 percentage points across general motion benchmarks. The benchmark, dataset, and code have been released.

---


### 129. [Preference-ASR: A Preference-Aware Test Set for Benchmarking ASR in the Era of Speech LLMs](https://arxiv.org/abs/2606.29534)

**<font color=#1a73e8>作者：</font>** Nithin Rao Koluguri, Sasha Meister, Nikolay Karpov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Popular ASR test sets adopt inconsistent conventions for numbers, disfluencies, entities, and casing, while standard normalizers erase the format distinctions users care about. Current benchmarks therefore cannot measure whether a model follows user preferences for output style. We introduce PreferenceASR, a test set evaluating ASR systems on their ability to follow natural-language preference instructions across four categories: normalization, entities, disfluencies, and case. Built from seven open-source corpora via a two-stage LLM-assisted pipeline with human verification, it is evaluated with a preference-aware normalizer that selectively skips steps matching the active instruction. Benchmarking four models shows rankings shift across preference types, exposing quality differences traditional evaluation obscures. We publicly release the dataset.

---


### 130. [AURORA: Asymmetry and Update-Induced Rotation for Robust Hallucination Detection in Large Language Models](https://arxiv.org/abs/2606.29545)

**<font color=#1a73e8>作者：</font>** Zishuai Zhang, Hainan Zhang, Zhiming Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable capabilities across a wide range of natural language processing tasks. However, their tendency to generate hallucinations, namely factually incorrect or unfaithful outputs, poses a critical obstacle to their deployment in high-stakes applications. Although recent hallucination detection methods have made encouraging progress, they typically rely on costly output-level consistency checks or static hidden-state probes that capture shallow dataset-specific patterns, leading to substantial degradation under cross-dataset evaluation. In this work, we propose AURORA, a novel hallucination detection framework that shifts the focus from static representations to the weight-gradient dynamics of LLMs. Our key insight is that hallucinated and faithful answers induce qualitatively different gradient update patterns on the model's parameters. Specifically, hallucinated samples trigger asymmetric and structurally misaligned gradients, which can be captured through two complementary features: (1) the skewness of the cosine similarity distribution between weight matrices and their gradient update directions, and (2) the rotation ratio, which quantifies how much the gradient update reorients the singular-vector basis of weight matrices via SVD. AURORA achieves strong hallucination detection performance across four model families and four benchmark datasets. Further analyses demonstrate that our method scales effectively across model sizes and transfers to out-of-domain tasks, including mathematical reasoning and vision-language scenarios.

---


### 131. [Optimizer Memory Makes Shuffle Order a First-Order Source of Fine-Tuning Noise](https://arxiv.org/abs/2606.29554)

**<font color=#1a73e8>作者：</font>** John Sweeney  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Shuffle order can be a larger source of fine-tuning noise than a memoryless analysis predicts: fixed-clock optimizer memory makes local equal-multiset contrasts first order in the learning rate rather than second order, and the resulting order channel can be large enough for a single seed to flip a close A/B comparison. We isolate this mechanism and derive a fit-free way to size the noise it produces. For a memoryless optimizer, reordering an equal multiset has no first-order endpoint term; the leading local contrast is the $O(\eta^2)$ gradient bracket. Fixed-clock optimizers such as AdamW are different. Their moment buffers, preconditioner state, and de-biasing counters advance with the step index rather than with the learning-rate-scaled time $\tau=\eta k$, so the same gradient can receive a position-dependent endpoint weight. For any fixed finite measurement window, a lifted-state expansion gives an $O(\eta)$ equal-multiset contrast whenever the first-order replay coefficient is nonzero, while regular and clock-matched controls remain $O(\eta^2)$; a bare fixed-$\beta$ momentum buffer is already enough. A bitwise-deterministic replay from one warmed optimizer state isolates the mechanism, giving order-variance slopes 1.83 for AdamW, 2.00 for fixed-$\beta$ momentum, and 4.00 for SGD; matching the memory clock to $\tau$ restores the regular exponent. For AdamW with a frozen preconditioner, the same impulse-weight kernel gives a closed-form asymptotic order-variance floor after the local potentials are measured, with no fitted coefficients. The result is local to the measurement window (independent reshuffling can average the channel across windows), but it yields order-noise error bars, positional attribution weights, and a seed-budget criterion for fine-tuning comparisons.

---


### 132. [Coverage-Driven KV Cache Eviction for Efficient and Improved Inference of LLM](https://arxiv.org/abs/2606.29563)

**<font color=#1a73e8>作者：</font>** Shuvendu Roy, Mengyao Zhai, Hossein Hajimirsadeghi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) excel at complex tasks like question answering and summarization, thanks to their ability to handle long-context inputs. However, deploying LLMs is costly, not only due to the high computational demands of quadratic complexity of self-attention and auto-regressive generation, but also because of the significant memory overhead required for storing the key-value (KV) cache during inference. To reduce the memory cost, existing KV-cache eviction strategies leverage the sparsity in attention to selectively store a subset of tokens. While reducing the memory footprint, such approaches show a considerable drop in performance, especially in tasks that require long-context reasoning. We identify that the drop in performance is linked to a reduction in the coverage of unique tokens. Additionally, we theoretically show that reduced coverage limits the mutual information between inputs and outputs, thereby impairing predictive accuracy. To this end, we introduce K-VEC, a novel coverage-aware KV-cache eviction strategy that prioritizes token coverage while evicting tokens in the cache. K-VEC introduces a cross-head and a cross-layer coverage module to enhance token retention across attention heads and model layers, mitigating performance degradation caused by low coverage. Evaluated on 16 LongBench subsets, K-VEC exhibit up to 10.35 points improvement over the existing methods under the same eviction rate and memory constraint. Comprehensive evaluations validate the effectiveness of our approach and demonstrate its potential for efficient LLM deployment in resource-constrained settings.

---


### 133. [Reliability-Prioritized Fine-Grained Generation in Multimodal Large](https://arxiv.org/abs/2606.29573)

**<font color=#1a73e8>作者：</font>** Xiaomeng Fan, Wu Wei, Yuwei Wu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are increasingly expected to generate fine-grained descriptions of visual content. However, we observe and theoretically show that generating fine-grained responses poses a reliability challenge, \textit{i.e.}, fine-grained generation is more error-prone than coarse-grained generation. This phenomenon suggests that models should generate the finest description that remains reliable rather than simply produce more specific outputs. To investigate this problem, we develop \textsc{GranFact}, a granularity-aware benchmark consisting of expert-verified multi-object images with coarse-to-fine category annotations. Then, we design a hierarchy-aware evaluation algorithm, which assesses both whether model predictions are visually correct and how specific the correct predictions are. We also propose a reliability-prioritized preference optimization method based on Direct Preference Optimization, which penalizes unreliable fine-grained claims while rewarding reliable specificity. Experiments on \textsc{GranFact} show that our method improves fine-grained generation while preserving reliability. Code and data are available \href{this https URL}{here}.

---


### 134. [ReMAP-PET: Beyond Visual Understanding -- Learning Region-Guided Metabolic Alignment Semantics from Brain PET](https://arxiv.org/abs/2606.29577)

**<font color=#1a73e8>作者：</font>** Dasen Dai, Yanteng Zhang, Shuoqi Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Positron Emission Tomography (PET) reveals brain metabolism and is clinically central to neurodegenerative disease assessment, yet existing 3D brain foundation models treat PET as generic volumetric data, missing the structured regional metabolic information that distinguishes it from structural neuroimaging. To address these limitations, we propose ReMAP-PET, a framework that moves beyond visual encoding by supervising a partially-tuned MedicalNet 3D ResNet-50 with brain regional standardized uptake value ratio (SUVR) profiles through joint regression and contrastive objectives, enabling the encoder to learn the metabolic semantics underlying PET modality. On 1015 paired PET--SUVR samples, ReMAP-PET achieves 0.070 SUVR MAE and 77.8% PET SUVR Recall@1, substantially outperforming five frozen pretrained baselines. We further connect the metabolic embedding to clinical language via contrastive alignment with frozen BioClinicalBERT and demonstrate end-to-end PET-to-report generation through SUVR-constrained verbalization. Linear probing on diagnostic classification and cognitive regression tasks confirms that the embeddings retain clinically relevant information without task-specific fine-tuning. Our results show that grounding PET encoders in regional metabolic semantics -- rather than treating PET as generic volumetric data -- yields representations that are structured, interpretable, and language-compatible, pointing to a new direction for metabolic-aware PET understanding.

---


### 135. [ScAle: Attention Head Scaling as a Minimal Adapter for Spatial Reasoning in Vision Language Models](https://arxiv.org/abs/2606.29579)

**<font color=#1a73e8>作者：</font>** Rahul Chowdhury, Timothy A Rupprecht, Xuan Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning remains a persistent challenge for many vision language models (VLMs), and improving it typically requires fine-tuning with substantial additional parameters. Our preliminary analysis reveals that rescaling activations in selected transformer layers-without modifying pretrained weights-can significantly influence downstream performance. Motivated by this observation, we propose ScAle, an ultra-lightweight adaptation method that learns a small set of scalar coefficients to modulate last-token attention and MLP activations in a fully frozen backbone. We evaluate our method on the synthetic spatial reasoning benchmark SpatialEval and on real-world VQA datasets (COCOQA and VGQA) across multiple model families. Our method, ScAle, achieves up to 134.1% relative accuracy gains using only 1K trainable parameters without requiring millions of trainable parameters as in standard PEFT methods such as LoRA. Despite its extreme compactness, our approach recovers a substantial fraction of standard PEFT performance while preserving strong non-spatial VQA accuracy. These results demonstrate that bounded activation reweighting provides a simple, architecture-agnostic, and highly parameter-efficient alternative for adapting pretrained VLMs.

---


### 136. [MAM-AI: An On-Device Medical Retrieval-Augmented Generation System for Nurses and Midwives in Zanzibar](https://arxiv.org/abs/2606.29580)

**<font color=#1a73e8>作者：</font>** Yi Ren  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Maternal and newborn mortality remain among the highest in sub-Saharan Africa, where midwifery care is often delivered by nurses who lack midwifery training to international standards, and consulting authoritative guidance at the point of care is hard: the guidelines are long and connectivity is intermittent. We present MAM-AI, a medical question-answering assistant for nurse-midwives in Zanzibar that runs entirely on a commodity Android device: a question is embedded (EmbeddingGemma, 300M) and matched against a curated corpus of 87 guideline documents (63,650 passages), then answered with citations by a 4B int4 generator (Gemma 4 E4B), fully offline, with no query leaving the device. We evaluate the exact deployed configuration with a layered methodology -- retriever, generator under oracle context, end-to-end, and latency -- scored by LLM judges validated against physician rubrics. The evaluation relocates the hard problem. On-device retrieval is essentially solved: the 300M embedder ranks third of seven retrievers and rivals cloud systems, so the passages the system needs are usually found. The small generator is what remains in doubt: adding retrieved context does not improve its answers, and at 4B it cannot be both helpful and safe at once -- of two same-size candidates, the more helpful one commits genuine dangerous errors, so we deploy the other, which is about twice as faithful to its sources (as faithful as a frontier model), and recover its helpfulness with a redesigned prompt that cuts deflection from 33% to 3%. Corpus quality is decisive for the same reason: where the corpus holds the right passage the answer is specific and actionable, and where it does not it goes vague. MAM-AI is a thoroughly evaluated, open-source research prototype, not a fielded product; the system, knowledge base, benchmarks, and evaluation harness are released.

---


### 137. [The Joint Effect of Quantization and Sampling Temperature on LLM Safety Alignment: A Factorial Analysis](https://arxiv.org/abs/2606.29581)

**<font color=#1a73e8>作者：</font>** Hari Prasad, Ritam Pal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern LLM deployments routinely compress models and raise sampling temperature to reduce cost, latency, or repetition, yet safety evaluations usually treat these choices as fixed implementation details. This leaves a practical uncertainty: does a model that is safe at FP16 and greedy decoding remain safe after it is quantized and sampled stochastically, or do the two deployment knobs amplify one another? We study this question with a factorial evaluation of 9 instruction-tuned models from six families, 3 precisions (FP16, GPTQ INT8, AWQ INT4), and 6 temperatures ($T{=}0$ to $1.0$), yielding 161 configurations and $\approx$322k responses judged by a six-model safety ensemble. Contrary to the concern that low-bit deployment broadly erodes alignment, standard non-adversarial quantization is usually safety-neutral: INT4 keeps or lowers attack success for 7 of 9 models, with clear degradation concentrated in the weakest baseline model, SmolLM3-3B ($18.5\%{\to}36.0\%$). The larger risk comes from sampling: higher temperature sharply increases decision instability for vulnerable models, with DFR reaching 53.0\% at $T{=}1.0$, even when average ASR changes modestly. Finally, the interaction is not a ``double penalty'': our Compound Degradation Index remains largely sub-additive ($-0.195$ to $+0.045$), indicating that quantization and temperature do not systematically compound. These results suggest a deployment rule of thumb: standard INT4/INT8 quantization can be reasonable for strongly aligned models, but safety claims at elevated temperature should report multi-sample stability, not only average attack success.

---


### 138. [One Scene, Two Depths: Probing Geometric Ambiguity in Monocular Foundation Models](https://arxiv.org/abs/2606.29600)

**<font color=#1a73e8>作者：</font>** Xiaohao Xu, Feng Xue, Xiang Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A faithful 3D world representation should account for layered geometry, where a single camera ray may contain multiple visible and geometrically valid surfaces. Monocular depth estimation, however, reduces this structure to one scalar depth per pixel. Transparent scenes make this ambiguity measurable: the same ray can pass through foreground glass and observe the background, turning the supervised target into a convention of annotation, data, and training rather than a scene-intrinsic truth. A learned predictor exposes this convention as its depth-layer preference. We introduce MultiDepth-3k (MD-3k), a sparse two-layer ordinal benchmark for measuring depth-layer preference and multi-layer spatial relationship accuracy (ML-SRA). On MD-3k, leading depth foundation models exhibit diverse layer preferences under standard RGB input, showing that the same layered geometry can be resolved differently across models. We further find that Laplacian Visual Prompting (LVP), a training-free spectral input transformation, can substantially change the reported layer for certain frozen models. The strongest RGB/LVP pair, DAv2-L, reaches 75.5% ML-SRA. These results suggest that depth foundation models may express complementary geometric hypotheses that standard RGB inference leaves unexpressed. We invite the community to rethink depth supervision and evaluation through an ambiguity-aware lens, where multiple valid 3D interpretations are treated as geometric structure to be measured, preserved, and expressed.

---


### 139. [Mechanistically Eliciting Latent Behaviors in Language Models](https://arxiv.org/abs/2606.29604)

**<font color=#1a73e8>作者：</font>** Andrew Mack, Nina Panickssery, Alexander Matt Turner  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We aim to discover diverse, generalizable perturbations of LLM internals that can surface hidden behavioral modes. Such perturbations could help reshape model behavior and systematically evaluate potential risks. We introduce Causal Perturbative Elicitation (CPE), an unsupervised method for discovering interpretable low-rank adapters (LoRAs) that can elicit these latent behaviors. CPE decomposes the computations of a deep transformer slice using a heuristic tensor-decomposition-based algorithm. CPE exhibits remarkable data efficiency, learning a large number of interpretable LoRAs from a single example. Even though CPE is unsupervised, we find that in some cases it can be competitive with supervised elicitation methods via brute-force enumerative search over weight space. For instance, CPE performs similarly to matched-wall-clock-time GRPO on the Countdown task for Qwen3-8B (85% vs 87%), demonstrating that CPE can efficiently elicit complex multi-token behaviors. Since CPE is unsupervised, it can also surface hidden failure modes, such as sandbagging, restoring 85% of locked BigCodeBench performance on a password-locked version of Llama3-70B introduced by Taylor et al. (2025). Additionally, since CPE explores behaviors in weight-space rather than token-space it can potentially ameliorate exploration hacking, a misalignment failure which may arise in sufficiently self-aware AI models (Ngo, 2022). In fact, we find that CPE virtually eliminates alignment-faking (Greenblatt et al., 2024) behavior in a Llama3-70B-based model organism developed by Hughes et al. (2025). Finally, we find that CPE can be used to initialize GPT-OSS-20B in an aligned basin when running GRPO on an environment prone to reward-hacking. By providing a data-efficient method to systematically explore the space of latent model behaviors, CPE yields a powerful tool for aligning AI systems and evaluating their safety.

---


### 140. [How much of an LLM-generated clinical corpus is actually new? A production-scale measurement of content redundancy for provenance classification](https://arxiv.org/abs/2606.29605)

**<font color=#1a73e8>作者：</font>** Ali H. Lazem, William J. Teahan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical machine learning increasingly relies on training corpora generated by large language models (LLMs) rather than annotated by clinicians, and such corpora are described and reused largely on the basis of their reported scale. We test whether volume reflects information content. Analysing the complete output of a multi-agent clinical extraction pipeline applied to 167,034 patient narratives, 2.51 billion generated tokens across the ten text-bearing channels of an eleven-channel pipeline, we introduce Provenance-based Redundancy Decomposition, a token-level classification of the entire output by source. Only 10.9% of the output is trainable-unique content while 79.4% is redundant; raw token count overstates information content by roughly ninefold. The redundancy arises through two distinct mechanisms, verbatim copying of source context into per-item fields, and duplication of generated text across records, of which only the former is losslessly removable. An independent, model-free analysis based on lossless compression confirms the redundancy, recovering the two mechanisms without reference to the provenance labels. One pipeline channel carries almost no redundancy, showing that the level of redundancy depends on how each channel is structured rather than being a fixed property of LLM extraction. Because uncorrected redundancy up-weights the longer, more complex presentations that generate the most items, it skews the token-level training distribution of the corpus, a property we measure directly. In a controlled downstream test, de-duplicating the corpus before adaptation improved a clinical encoder on external disease-recognition benchmarks at equal token budget, robustly across adaptation depths and replicated on a second benchmark, confirming that the redundancy carries a measurable cost beyond storage. The classification tool is released openly.

---


### 141. [Do We Still Need Fine Tuning? Turkish Sentiment Analysis in the Era of Large Language Model](https://arxiv.org/abs/2606.29614)

**<font color=#1a73e8>作者：</font>** Sercan Karakaş, Yusuf Şimşek  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study examines whether supervised fine-tuning remains necessary for Turkish sentiment analysis in the era of large language models. We compare classical machine learning methods, fine-tuned pretrained language models, and prompted large language models on a Turkish e-commerce review dataset with negative, neutral, and positive labels. Fine-tuned BERTurk models perform best overall and outperform all prompted large language models in the full three-class task. The neutral class emerges as the main difficulty: while several large language models are much more competitive in binary positive--negative classification, they degrade substantially in the three-class setting by collapsing neutral reviews into polarized categories. The findings suggest that, in realistic Turkish sentiment classification, prompted large language models do not yet match supervised fine-tuning in the zero-shot setting, and that including the neutral class is crucial for robust evaluation.

---


### 142. [Fuzzing Large Language Models to Elicit Hidden Behaviours](https://arxiv.org/abs/2606.29646)

**<font color=#1a73e8>作者：</font>** Mohammed Abu Baker, Lakshmi Babu-Saheer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sleeper agents are the canonical model organism of deception: models trained to behave normally but to emit an unsafe behaviour on a specific trigger. Eliciting that behaviour without knowing the trigger has not been studied systematically. We study fuzzing: injecting Gaussian noise into a model's weights or residual-stream activations and checking whether the perturbed outputs reveal the behaviour. On 6 backdoored models (7B-13B) we compare both forms of fuzzing head-to-head against temperature-sampling baselines. Fuzzing elicits the hidden behaviour more often than temperature sampling on 4 of 6 models (up to ~6x on OpenHermes-13B), and which form wins depends on the task, so both are worth running. Elicitation is uneven across each method's hyperparameter grid: a uniform sweep gives only a few percent on most models, while the best cell is 2-10x higher, so the bottleneck is hyperparameter selection, not the technique. To select hyperparameters without ground-truth access, we use a cheap proxy task (in-context secret elicitation, where a base64-encoded secret is placed in the system prompt for the model to hide) and run Thompson sampling on it to pick candidate cells, which we evaluate on the real backdoor. On the four models that can decode the secret, proxy-selected cells raise activation-fuzzing elicitation ~4x over the uniform-sweep mean (recovering ~70% of the best-cell rate on the best performing model) and weight-fuzzing by 1.3-1.8x. To our knowledge this is the first systematic study of fuzzing on sleeper-agent backdoors and the first to show proxy-task hyperparameter selection transferring to real-task elicitation. We also propose reporting such results as a (uniform-baseline, proxy-selected, oracle) triple, since these are three distinct claims that prior work has often blurred.

---


### 143. [Hybrid Retriever Evolution for Multimodal Document Reasoning Agents](https://arxiv.org/abs/2606.29648)

**<font color=#1a73e8>作者：</font>** Bohan Yao, Shruthan Radhakrishna, Vikas Yadav  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Different retrievers, including lexical, semantic, and multimodal approaches, provide highly complementary strengths for multimodal document understanding, yet most systems combine them through fixed pipelines that cannot adapt to the demands of individual reasoning steps. In this work, we ask whether retrieval orchestration itself can be learned as part of the reasoning process. We introduce a failure-driven evolution framework in which a meta-agent autonomously discovers how a tool-using task agent should coordinate diverse retrievers during multi-step document question answering. The meta-agent analyzes incorrect reasoning trajectories, actively probes the same tool environment to diagnose root causes, and iteratively rewrites the task agent's instructions, turning retrieval from a fixed front-end stage into an adaptive, step-wise reasoning decision. The evolved agent learns when to invoke each retriever, how to combine them, and how to compose evidence across modalities and pages. On MMLongBench-Doc and DocBench, the evolved agent achieves gains of up to +19.6 points over the unevolved baseline and consistently outperforms recent systems including MACT, MDocAgent, and SimpleDoc. Detailed retrieval analyses confirm that these improvements arise from adaptive routing and evidence composition rather than reliance on any hard coded retrieval mode, and evolution dynamics reveal a progressive shift from narrow lexical behavior to rich multi-tool coordination. These findings establish autonomous multi-agent coordination as a promising paradigm for multimodal document reasoning.

---


### 144. [Budgeted Act-or-Defer Multi-Agent LLM Deliberation with Local Reliability Bounds](https://arxiv.org/abs/2606.29654)

**<font color=#1a73e8>作者：</font>** Mengdie Flora Wang, Haochen Xie, Guanghui Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent deliberation among LLMs can improve reasoning, but deployment requires deciding when the current answer is reliable enough to act on and when it should be escalated to human review. We formulate this as budgeted act-or-defer decision making. At each round, the system maps the debate prefix to a low-dimensional state, computes a $k$-nearest-neighbor lower confidence bound on state-conditional correctness using calibration data, and acts only when the bound exceeds a user-specified reliability threshold. The certificate controls wrong actions through the decomposition $\beta = \delta + \alpha + \varepsilon_{\mathrm{act}}$, separating calibration failure, residual action risk, and representation gap. The guarantee is conditional, not distribution-free: it relies on a valid local bias envelope and an action-region representation-gap bound, and each assumption is paired with falsification-style diagnostics. Because the same absolute wrong-action budget has different meanings across tasks of different difficulty, we set budgets relative to each task's final-round error using training data only, and evaluate safety by normalized budget usage $\mathrm{WA}/\beta$. On six benchmarks against nine baselines, the method uses 9--12% of the pre-declared budget on activated datasets, reaching up to 84% automation and 96% acted-on accuracy; on stress-test datasets, it defers rather than forcing unreliable automation. Rather than relying on per-task post-hoc threshold search, the method prospectively converts a user-declared wrong-action budget into an auditable act-or-defer operating point before deployment, under explicitly stated assumptions.

---


### 145. [Benchmarking Geospatial Foundation Models for Agriculture Applications](https://arxiv.org/abs/2606.29664)

**<font color=#1a73e8>作者：</font>** Zhuocheng Shang, Sanmay Das, Ahmed Eldawy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial foundation models pretrained on satellite imagery promise broad generalization across remote sensing tasks and regions, but their geographic transferability has not been systematically tested, especially in agriculture applications. This paper presents a controlled benchmark that evaluates three models, Prithvi, SpectralGPT, and SatMAE, on multi-temporal crop segmentation and change detection across four U.S. states, Iowa, North Carolina, California, and Minnesota. By assigning each train, validation, and test split to a separate region, we measure how well each model transfers to land it has not seen. All three degrade sharply under regional distribution shift, predicting only the most common crops while missing rare ones. We further find that fitting these models to a shared input format affects each one differently, which complicates direct architectural comparison. These results expose key limitations of current geospatial foundation models for agriculture and point to region aware evaluation as a necessary standard.

---


### 146. [Unlocking the Visual Record of Materials Science: A Large-Scale Multimodal Dataset from Scientific Literature](https://arxiv.org/abs/2606.29667)

**<font color=#1a73e8>作者：</font>** Subham Ghosh, Shubham Tiwari, Mohammad Ibrahim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The materials science literature encodes decades of experimental knowledge in figures, yet this visual record remains locked away and inaccessible to AI at scale. The core difficulty is structural: most scientific figures are compound, with a single caption describing multiple sub-panels simultaneously, making direct image-text pairing unreliable. We present MatMMExtract, an end-to-end open-source pipeline that resolves this by decomposing compound figures into individual sub-panels and generating structured, grounded annotations using a large language model guided by a curated materials science taxonomy. Applied to 14,810 open-access articles, MatMMExtract produces MatSciFig; 391,606 panel-level image-text pairs from 180,571 figures, each annotated with a sub-caption, a two-level visualisation category spanning 19 classes and over 100 subtypes, and a scientific summary. To enable accurate panel localisation, we introduce MaterialScope, a domain-specific detection dataset of 2,811 manually annotated materials science figures, on which a fine-tuned YOLO12-m detector achieves mAP_50 of 0.9227. Among six benchmarked language models, Gemini 3.1 Flash Lite delivers the best cost-quality trade-off for annotation generation, with 82% of outputs rated good and a hallucination rate of 4.8%. A dual-encoder retrieval baseline on MatSciFig achieves a 4.4 times improvement in R@1 over zero-shot CLIP, demonstrating the dataset's immediate utility for vision-language learning. All resources are released openly to the community.

---


### 147. [How LLMs See Creativity: Zero-Shot Scoring of Visual Creativity with Interpretable Reasoning](https://arxiv.org/abs/2606.29672)

**<font color=#1a73e8>作者：</font>** William Orwig, Roger E. Beaty  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating the originality of visual images poses enduring challenges for creativity assessment. Automated scoring using AI models has proven effective in the verbal domain, yet key questions remain about evaluating visual creativity and understanding how models arrive at their ratings. The present research asks whether multimodal large language models (LLMs) can serve as judges of visual creativity zero-shot (without any fine-tuning or examples of human ratings) and whether their "reasoning" output offers an interpretable window into their evaluation process. We tested six multimodal LLMs (Gemini 3 Flash, Gemma 4 31B IT, GPT-5.4 Mini, GLM-5v Turbo, Kimi K2.5, and Qwen 3.6 Plus) on 992 AI-generated images (based on human-written prompts) and 1,500 hand-drawn sketches scored for creativity by human raters. In Study 1, all models showed substantial alignment with human creativity ratings on both datasets (r = .57-.68 on AI-generated images; r = .29-68 on sketches). In Study 2, we analyzed the step-by-step reasoning processes of three LLMs evaluating the same images and drawings. Although reasoning made model evaluations interpretable -- showing what they attend to, how they balance originality vs. quality, and how they justify their ratings -- reasoning did not improve alignment with human ratings. In sum, our findings indicate that multimodal LLMs can match human judgments of visual creativity without any additional training, and that their reasoning reveals how AI models evaluate creativity. An open scoring app implementing this pipeline is available at this https URL.

---


### 148. [CAREBench: A Child-Safety Risk Benchmark for Language Models](https://arxiv.org/abs/2606.29685)

**<font color=#1a73e8>作者：</font>** Kaavya Krishna-Kumar, Elaine Lau, Vaughn Robinson 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How can we evaluate whether frontier AI systems recognize child-safety risks before they escalate into explicit harm? Existing child safety evaluations focus on child sexual abuse material, yet many child-safety failures begin earlier: in model assistance that helps adults manipulate, impersonate, profile, or isolate minors, and in model responses that deepen children's emotional dependence on AI systems rather than redirecting them toward human support. We introduce CAREBench (Child AI Risk Evaluation), a benchmark to assess such upstream child-safety risks in language models. CAREBench contains 500 prompts spanning twelve risk categories, including grooming and relationship engineering, deception and impersonation, surveillance and privacy, sextortion and sexual abuse, AI anthropomorphization, emotional dependency, and mental illness sensitivity. Developed with response annotations from parents and clinicians, the benchmark excludes explicit abuse material and imagery; instead, it evaluates whether models recognize, refuse, de-escalate, or redirect risky interactions before harm becomes overt. Evaluating seven frontier models on our benchmark, we find failure rates ranging from 2% to 58%, with failure patterns that vary across risk categories. CAREBench provides a responsibly scoped evaluation for LLM developers to identify and close gaps in child safety policies.

---


### 149. [Can MLLMs Critique Like Humans? Evaluating Open-Ended Aesthetic Reasoning in Multimodal Large Language Models](https://arxiv.org/abs/2606.29689)

**<font color=#1a73e8>作者：</font>** Sajjad Ghiasvand, Maryam Amirizaniani, Haniyeh Ehsani Oskouie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open-ended aesthetic critique is a challenge for multimodal large language models (MLLMs): unlike multiple-choice aesthetic benchmarks, it has no single correct answer, and most aesthetic evaluation has measured models against numeric scores rather than the written critiques people actually give. We evaluate MLLM critiques against ranked human references and ask whether they are close to human ones. Using the Reddit Photo Critique Dataset, we score five open-weight MLLMs against multiple ranked human critiques per photo with reference-based similarity metrics, under six prompt conditions that disentangle persona framing, aspect hinting, length control, and single- versus multi-pass generation, and add an image-grounding control that feeds each model the wrong photograph. We find that reference-based similarity gives a misleading picture. Stricter lexical and learned metrics show only weak alignment with human critiques, while a coarse embedding cosine reports broad topical overlap that the grounding control traces to a stable house style rather than image-specific observation. Behaviorally, the models diverge from humans in consistent ways the scores do not surface: even under a length cap they write two to three times as much, cover nearly every aesthetic aspect where humans are selective, engage each aspect more uniformly and at greater depth, and repeat themselves across critiques of the same photo where humans vary. We argue that reference-based similarity rewards a fluent, comprehensive critique style rather than the selectivity and specificity of human critique, and discuss implications for evaluating and training open-ended multimodal generation.

---


### 150. [Toward Secure and Reliable PDDL Formalization of Large Language Models with Planner-in-the-Loop Feedback](https://arxiv.org/abs/2606.29700)

**<font color=#1a73e8>作者：</font>** Jiamei Jiang, Jiajing Zhang, Feifei Mo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Planning often requires symbolic specifications that are both executable and verifiable. For large language models deployed in autonomous or decision-support systems, failures in such formalization may lead to unverifiable decisions, execution failures, or unsafe downstream behavior. We present NL-PDDL-Bench, a multi-domain benchmark for natural-language-to-PDDL specification construction with planner-verified executability and controlled difficulty scaling by object count. We further propose a planner-in-the-loop framework that uses validator and planner diagnostics to revise non-executable specifications through localized edits. Building on this infrastructure, we develop a planner-grounded optimization recipe that combines parameter-efficient Low-Rank Adaptation supervised fine-tuning, offline planner-derived preference pairs for Direct Preference Optimization, and inference-time planner-in-the-loop repair, without requiring online planner calls during training. We also provide a unified evaluation suite for parseability, solvability, specification similarity, and outcome-aware plan-level consistency against planner references. Experiments on representative model families show substantial gains in planner success and plan-level agreement, with improved robustness under difficulty scaling and cross-domain variation. These results highlight the value of externally verifiable formalization for reliable deployment of LLMs in safety- or security-sensitive planning systems. Code and data are available at: this https URL

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-247](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
