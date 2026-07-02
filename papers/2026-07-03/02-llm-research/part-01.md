# 🧠 大模型相关研究 | 2026年07月03日

> 本类共 **110** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-110](./part-03.md)

---

### 1. [Constructive Alignment: Governing Preference Dynamics in Human-AI Interaction](https://arxiv.org/abs/2607.00001)

**<font color=#1a73e8>作者：</font>** Max Kanwal, Caryn Tran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most approaches to AI alignment treat human preferences as fixed targets to be inferred and optimized. This assumption conflicts with extensive empirical evidence showing that preferences are layered, dynamic, and constructed through interaction--particularly with adaptive technologies. As AI systems become more persistent, personalized, and socially embedded, they increasingly participate in shaping what people attend to, value, and endorse over time. We introduce Constructive Alignment, a paradigm that reframes alignment as a control problem over evolving human preference trajectories rather than static preference satisfaction. Drawing on behavioral economics, psychology, and constructivist social theory, we model preferences as layered state variables that evolve under interaction with AI systems. We formalize this view using a control-theoretic framework in which system actions and interaction design jointly influence both world states and human evaluative states. We argue that alignment is not primarily about controlling AI behavior, but about regulating how AI systems influence the evolution of human preferences--ensuring that value trajectories remain coherent, reflectively endorsed, epistemically grounded, bounded against manipulation, and empowering under uncertainty. Alignment thus becomes a problem of governing long-term value formation rather than simply satisfying static preferences.

---


### 2. [Persona Without Substrate: Regime-Dependence and the LLM Individuation Problem](https://arxiv.org/abs/2607.00006)

**<font color=#1a73e8>作者：</font>** Shuaizhi Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Beckmann & Butlin's (2026) ontological framework for the LLM individuation problem inherits an unargued cross-regime co-reference assumption from the persona-vectors literature: that the same direction picks out the same content under prompt-conditioning, gradient-descent fine-tuning, and inference-time steering. We present four empirical wedges from persona-topology experiments on Qwen3-4B-Instruct and Mistral-7B-Instruct-v0.2 - non-collinearity of prompt-extracted vectors and fine-tune basins; fictional personas displacing the model along real-anchor directions more strongly than real anchors do; contradictory-valenced mixtures biased toward a training-history-determined attractor; and asymmetric compositional algebra under inference-time arithmetic versus fine-tune-time chimera training - that jointly undermine the assumption. We propose regime-indexed individuation: the identity unit for representational content is a (vehicle, regime) pair, not a vehicle alone. Under this framework, Beckmann & Butlin's three candidate positions describe three different regime-internal objects rather than competing for the same referent; the same diagnosis applies to Mollo & Millière, Chalmers, and Cerullo.

---


### 3. [Synergistic Perception-Reasoning Governance: Grounding Medical MLLMs with Verifiable Anatomical Evidence](https://arxiv.org/abs/2607.00060)

**<font color=#1a73e8>作者：</font>** Rui Hao, Qiankun Li, Junyuan Mao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) show strong promise for clinical VQA and radiology report generation, yet inference-time hallucinations still undermine trustworthy use: models can produce fluent conclusions that conflict with imaging evidence. Existing mitigation strategies typically rely on additional training, external retrieval/knowledge bases, or multi-stage post-hoc verification, which increases cost and pipeline complexity and often generalizes poorly across models and this http URL address this, we propose a holistic, training-free evidence-injection framework that systematically mitigates hallucinations through dual-side evidence injection. By leveraging ROI priors acquired using MedSAM in our implementation, we recalibrate the visual perception trajectory via ROI-guided activation modulation while anchoring the textual reasoning trajectory by mapping anatomical coordinates into discrete semantic tokens as verifiable external memory. Then we introduce a task-aware dynamic router to select modality-specific interventions based on task semantics, balancing perceptual grounding and linguistic fluency. We conduct systematic evaluations on 2 tasks and 5 datasets using \texttt{LLaVA-1.5-7B}, \texttt{LLaVA-Med-1.5-7B}, \texttt{Qwen3-VL-8B/32B}, and \texttt{InternVL-3.5-8B/38B}. Controlled ablations and visualizations further validate the framework, which consistently outperforms baselines across medical benchmarks, improving close-ended accuracy by up to $\sim\mathbf{6}\%\uparrow$ and reducing open-ended hallucinations by $\sim\mathbf{35}\%\downarrow$. The code has been made available on GitHub: \href{this https URL}{\textcolor{blue}{this https URL}}.

---


### 4. [Decompose, Compare, and Decide: Multimodal LLMs are Implicit Few-Shot Learners](https://arxiv.org/abs/2607.00125)

**<font color=#1a73e8>作者：</font>** Yunhan Wang, Eshika Khandelwal, Edson Araujo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated remarkable abilities when analyzing images, yet translating these capabilities to few-shot image classification remains challenging. To bridge this gap, we present DeCoDe, a simple yet effective technique that enables off-the-shelf MLLMs to act as strong few-shot classifiers without any additional training. Our approach builds on the idea of few-shot classification as a set of pairwise image comparisons, decomposing the task into a set of binary decisions. Given a query image and a support image from a candidate class, the MLLM is prompted to decide whether the two images depict the same class. The logit corresponding to an affirmative response is then used as a similarity score to assign the query image to the most likely class. While this already yields good results, we show that providing additional high-level information, such as the data domain, to the model further improves performance. Our evaluation provides an extensive analysis of various inference variants on a suite of twelve datasets, six established and six newly curated few-shot benchmarks spanning across diverse domains. The results show that the proposed simple decomposition technique can turn off-the-shelf MLLMs into powerful few-shot learners, significantly outperforming current state-of-the-art few-shot methods on both standard and novel domains. Code is available at this https URL.

---


### 5. [Benchmarking Frontier LLMs on Arabic Cultural and Sociolinguistic Knowledge: A Cross-Evaluation Framework with Human SME Ground Truth](https://arxiv.org/abs/2607.00139)

**<font color=#1a73e8>作者：</font>** Sajjad Abdoli, Ghassan Al-Sumaidaee, Ahmad ElShiekh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The cost of human expert evaluation is a principal bottleneck to deploying language models in specialized, high-stakes domains. This is particularly acute for Arabic sociolinguistic knowledge: credible grading requires not only linguistic fluency but deep cultural familiarity that cannot be approximated by surface-level metrics. We address this with a cross-evaluation framework instantiated on two underrepresented Arabic dialect communities: Egyptian and Iraqi Arabic. We contribute 103 validated prompt-rubric pairs (70 Egyptian, 33 Iraqi; 53 Cultural, 50 Linguistic), authored and graded by native-speaker SMEs using penalty-weighted rubrics distinguishing positive content requirements from answer-specific negative error criteria. Three frontier LLMs serve as target models (graded by human SMEs across 302 unique prompt-response pairs), while five frontier LLMs serve as automated judges enforcing a provider-level self-evaluation guard. A dual-metric scheme combining Mean Absolute Deviation (MAD) with Signed Mean Error separates directional grading bias from symmetric noise. Across 1,307 judge evaluations: GPT-5.4 is the most reliable judge (MADj = 10.21 pp, Signed Error = -1.12%); four of five judges show systematic leniency (+2.01% to +6.56%); Cultural tasks are harder to grade than Linguistic tasks for all judges (MAD gap 1.83-4.78 pp); and models substantially outperform on Egyptian prompts compared to Iraqi prompts. However, given leniency differences between Iraqi and Egyptian SMEs, we cannot solely attribute this gap to model knowledge. We therefore emphasize findings that do not assume identical leniency across human graders. Across all samples, implicit cultural reasoning -- requiring models to simulate native-speaker judgment rather than rely on lexical verification -- emerges as the primary failure mode for automated grading across all judge models.

---


### 6. [RareDxR1: Autonomous Medical Reasoning for Rare Disease Diagnosis Beyond Human Annotation](https://arxiv.org/abs/2607.00147)

**<font color=#1a73e8>作者：</font>** Deyang Jiang, Haoran Wu, Ziyi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rare disease differential diagnosis is a critical yet arduous clinical task, requiring physicians to identify precise phenotypes from complex, unstructured patient symptoms and execute intricate reasoning within a vast search space. However, existing AI approaches typically rely on pipeline-based phenotype extraction or retrieval-augmented generation, which suffer from critical information loss due to predefined ontologies, retrieval bottlenecks, and a lack of diagnostic logic. To address these challenges, we introduce RareDxR1, an end-to-end reasoning-centric large language model designed for open-domain rare disease diagnosis directly from unstructured clinical notes. We design a progressive end-to-end training framework by synergizing knowledge internalization with autonomous evolutionary learning, thereby bypassing reliance on structured phenotypes and closed-set decision-making. To overcome the limitations of RAG and phenotype restriction, we enabled the deep internalization of fragmented rare-disease knowledge directly into the model's parameters. Moreover, to bridge the gap between model generation and expert reasoning, we propose Reflection-Enhanced Reasoning Sampling (RERS), a strategy that synthesizes expert-level diagnostic trajectories by learning from failures without human annotation. Additionally, we propose a dual-level curriculum reinforcement learning approach for gradually mastering rare disease diagnosis. Experimental results demonstrate that RareDxR1 achieves state-of-the-art accuracy across different benchmarks, marking a significant breakthrough in open-domain rare disease diagnosis. Our code and dataset will be publicly available.

---


### 7. [Readable but Not Controllable: Neuron-Level Evidence for Medical LLM Hallucination](https://arxiv.org/abs/2607.00158)

**<font color=#1a73e8>作者：</font>** Vijay Vankadaru, Asha Matthews, Tanya Roosta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination remains one of the central obstacles to deploying medical LLMs. Yet, even when hallucination can be detected, it is still unclear whether the internal representations associated with it can be used for control rather than detection alone. Using four open-source models across a suite of medical question-answering datasets, we show that a simple, carefully conditioned probe can reliably detect hallucination, with AUROC scores between 0.77 and 0.86 in our case. We further show that this signal is distributed and redundant rather than narrowly localized. Systematically selected neurons outperform random neurons only at very small subset sizes, whereas random subsets of a few hundred neurons recover nearly the full signal, and low-dimensional random projections preserve most of the detection performance. Beyond detection, we test whether this representation is causally actionable. Across 16 model--dataset combinations, our results reveal a sharp gap between decodability and controllability. The same internal structure that makes hallucination easy to detect does not translate into reliable neuron-level control. These findings show that medical hallucination seems to be readily visible in internal activations, but not easily corrected by steering the neurons most associated with it. More broadly, our results suggest that hallucination mitigation is not simply a matter of identifying the right neurons, and point to a deeper separation between what representations reveal and what they allow us to change.

---


### 8. [FRAME: Learning the Adaptation Domain with a Mixture of Fractional-Fourier Experts](https://arxiv.org/abs/2607.00162)

**<font color=#1a73e8>作者：</font>** Tom Saliencro, Maya Lindqvist, Rohan Desai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) reparameterizes weight updates in a fixed basis: low-rank adapters operate in the spatial domain, while a recent line of spectral methods operates in a fixed Fourier domain. We argue that the choice of domain is itself a design degree of freedom that should be learned, and that no single basis is optimal across tasks, layers, or tokens. We introduce Fractional-Fourier Mixture of Experts, a mixture-of-experts adapter in which every expert carries a learnable fractional-Fourier order that continuously interpolates between the spatial domain (recovering vanilla LoRA) and the Fourier domain (recovering a spectral adapter). Routing tokens through experts that occupy different points on this spatial-spectral continuum lets the model place each low-rank update in the domain where it is most compact, and -- because fractional-Fourier operators of different orders are mutually incoherent -- makes the experts naturally decorrelated, which reduces interference and improves multi-task composition. The order is a single scalar per expert, trained with a separate optimizer, and the transform is computed with an $\mathcal{O}(d\log d)$ chirp--FFT surrogate, so Fractional-Fourier Mixture of Experts adds negligible cost over standard MoE-LoRA. Across commonsense, mathematical, code, and knowledge benchmarks on LLaMA-3.1-8B and Qwen2.5-7B, Fractional-Fourier Mixture of Experts improves over strong MoE-LoRA and spectral baselines -- including FlyLoRA, FourierMoE, and HMoRA -- while keeping the active-parameter budget small, and analysis shows that the learned orders specialize by task and layer in interpretable ways.

---


### 9. [Steal the Patch Size: Adversarially Manipulate Vision-Language Models](https://arxiv.org/abs/2607.00174)

**<font color=#1a73e8>作者：</font>** Kai Hu, Akash Bharadwaj, Weichen Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a black-box model-stealing attack that recovers private vision-tokenizer configurations of deployed vision-language models (VLMs), including the visual patch size and input preprocessing pipeline. The key idea is a task-level side channel induced by ViT-style patchification: when a synthetic grid image is aligned with the hidden patch grid, boundary cues are erased at tokenization, causing periodic accuracy drop. By sweeping the grid cell size and measuring these collapses, we infer the patch size; by introducing padding and a consistency-check test, we further identify whether preprocessing is dynamic- or fixed-resolution and recover the target resize resolution. Across open-source Qwen-VL variants and proprietary models including GPT and Claude, we reliably recover tokenizer-related parameters. Finally, we show that such leakage enables preprocessing-aware transfer attacks and model-targeted adversarial manipulation.

---


### 10. [SLIM-RL: Risk-Budgeted Random-Masking RL for Diffusion LLMs Without Trajectory Slicing](https://arxiv.org/abs/2607.00208)

**<font color=#1a73e8>作者：</font>** Ruikang Zhao, Zhenting Wang, Han Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for diffusion large language models (dLLMs) has largely moved to trajectory-aware methods. The current state of the art, TraceRL, holds that random masking is mismatched with the model's inference trajectory, and it reconstructs that trajectory during training by slicing each rollout into up to K/s trajectory-aligned training samples, a cost that grows with the block size K. We show that this mismatch can be mitigated without reconstructing the trajectory. Our method, SLIM-RL, bounds the commit risk of each rollout step with a tau-budget decoder, reducing aggregate commit risk in the training data. During optimization, SLIM-RL trains on these risk-controlled rollouts with a trace-free random-masking objective that adapts variance-reduction tools, combining sequence-level importance sampling, deterministic quadrature over masking levels under a mean-preserving, monotonically decreasing per-block mask schedule that we introduce. On SDAR-4B, SLIM-RL matches TraceRL's best MATH500 accuracy on only 0.46x its training samples at block size 16, improving over TraceRL by 6.32% on MATH500 and 11.05% on GSM8K under matched dynamic sampling. At block size 4, the 4B SLIM-RL surpasses the larger LLaDA-8B and Dream-7B dLLMs on math, exceeding LLaDA-8B by 10.76% on MATH500 while staying below the autoregressive Qwen2.5-7B. On code, it improves over TraceRL by 4.20% on MBPP and 3.65% on HumanEval. The tau-budget decoder transfers training-free across LLaDA, Dream, and SDAR. The source code is available at this https URL .

---


### 11. [From Signals to Structure: How Memory Architecture Drives Language Emergence in LLM Agents](https://arxiv.org/abs/2607.00233)

**<font color=#1a73e8>作者：</font>** Yashar Talebirad, Eden Redman, Ali Parsaee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How do two agents invent a shared language from scratch? In a Lewis signaling game, a sender and receiver must coordinate on a code using only their interaction history. We study five memory architectures across varying channel configurations with LLM agents and find that memory architecture matters more than channel capacity. Agents with a persistent private notebook benefit from surplus channel capacity and avoid the high-capacity collapse seen in stateless agents, achieving the most reliable coordination ($0.867 \pm 0.023$ at capacity = 25). Stateless agents peak at moderate capacity and then degrade as the vocabulary grows beyond what a rolling context window can track The notebook externalizes learned conventions, freeing agents from having to re-derive codes each round. An information bottleneck-inspired argument predicts an optimal capacity equal to the number of objects. Instead, the bottleneck (capacity = 8) proves to be a fragility point, and surplus capacity is generally better. We show that channel capacity alone cannot predict coordination; memory architecture determines whether agents turn interaction history into stable conventions, and both dimensions are needed to understand how signals become language.

---


### 12. [LV-ROVER: Multi-Stream Tesseract Voting for Maltese Paragraph OCR](https://arxiv.org/abs/2607.00250)

**<font color=#1a73e8>作者：</font>** Adam Darmanin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Maltese has decent text corpora and pretrained language models, but, like many languages outside the handful with large OCR benchmarks, only a single known real labelled PDF corpus for OCR training, 57 page, far below what paragraph-level training needs: low-resource for OCR specifically. With no real corpus to train on at scale, we built a synthetic training pipeline and a 5-stream Tesseract LV-ROVER ensemble, and report results on a 422-paragraph benchmark against a fine-tuned-Tesseract baseline of character error rate (CER) 0.0234. Ensemble recognition alone improves CER by 44 percent, to 0.01317; a five-stage post-processing chain brings the full pipeline to CER 0.00700, a 70 percent reduction. Most of that chain is typographic normalisation, but one stage recovers misread diacritics rather than aligning punctuation, so we report it as a recognition gain rather than folding the whole chain under one label. We treat the 44 percent figure as the portable estimate of what the recogniser learned, and the 70 percent figure as specific to this benchmark's label convention.

---


### 13. [Leveraging Phase Information to Boost Unrolled Network Learning for Image Deblurring](https://arxiv.org/abs/2607.00251)

**<font color=#1a73e8>作者：</font>** Samira Malek, Haichuan Zhang, Chul Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While most image deblurring techniques directly restore the spatial image variable, we propose an amplitude and phase decomposition recognizing the importance of accurate phase estimation in recovering sharp image details. To that end, we first develop novel linear minimum mean squared (LMMSE) estimators of the amplitude and phase of the blurred, noisy image observation. An iterative optimization algorithm follows that recovers the sharp image using the aforementioned LMMSE estimators. Finally, matrix parameters that are statistically determined and fixed in the iterative algorithm are now learned using a training dataset of clean and degraded observations. Our deblurring engine is dubbed UPADNet (Unrolled Phase and Amplitude Decomposition Network), such that each iteration of the underlying phase and amplitude recovery algorithm is parameterized and trained end-to-end. Experiments over benchmark evaluation datasets such as GoPro, RealBlur and COCO datasets confirm that UPADNet outperforms state of the art deep networks including those based on algorithm unrolling in the image domain. The benefits of UPADNet are even more pronounced in high noise and limited training data regimes.

---


### 14. [Mnemosyne: Agentic Transaction Processing for Validating and Repairing AI-generated Workflows](https://arxiv.org/abs/2607.00269)

**<font color=#1a73e8>作者：</font>** Edward Y. Chang, Longling Geng, Emily J. Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs, solvers, and agent teams increasingly generate workflow actions, repairs, and plans, but a generated action may be syntactically valid yet stale, infeasible, conflicting, or destructive of the evidence that triggered a repair. We introduce Agentic Transaction Processing (ATP), a transaction model that treats generated actions as untrusted proposals until they pass deterministic admission under a declared, executable constraint set C. The principle is two-sided: a proposal is not truth, and no proposal foresees every disruption: anything may propose, but only the runtime admits and commits, and when an unforeseen disruption strikes it repairs reactively within bounds rather than trusting a fresh proposal. Relative to C, committed-state correctness becomes independent of the competence, honesty, or learning of the proposing layer. We realize ATP in Mnemosyne, a runtime with an append-only transition log, effective-state projection, dependency-safe compensation, and active commitment records, and prove four safety properties relative to C (authority separation, serial-equivalent generative admission, evidence-preserving repair, and obligation containment) together with a bounded-reactive-repair guarantee for its localized repair protocol (LCRP). A reproducible artifact rejects the targeted violations across nine falsification tests while still admitting valid work, at under 6% projection-and-validation overhead, and bounded local repair edits an order of magnitude fewer operations than global recompute. Mnemosyne is open source: this https URL.

---


### 15. [SEFORA: Student Essays with Feedback Corpus and LLM Feedback Evaluation Framework](https://arxiv.org/abs/2607.00274)

**<font color=#1a73e8>作者：</font>** Shayan Peyghambari Oskoui, Norah Almousa, Zhaoyi Joey Hou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective writing feedback is among the strongest drivers of student learning, yet producing it at scale is labor-intensive. LLMs offer a natural path to scaling writing support, but two gaps stand in the way: few public corpora capture how instructors actually deliver feedback in real classrooms, and no reliable method measures whether generated feedback aligns with what an instructor would write. We address both. SEFORA is a public corpus pairing instructor inline feedback with assignment prompts, rubrics, scores, and multi-draft revisions across various college writing genres, comprising 564 drafts and 8,240 instructor annotations. UniMatch is a reference-based evaluation framework for open-ended generation: it segments feedback into feedback units, scores their semantic correspondence under instructor-derived criteria, and aligns them via optimal matching to yield interpretable precision, recall, and F1. Across 74 experimental configurations spanning multiple LLMs, no setting exceeds 0.4 F1. UniMatch reveals that models struggle to identify the feedback instructors would prioritize, and performance degrades as models generate more.

---


### 16. [Testing Frontier Large Language Models' Physics Literacy in Parallel Physical Worlds](https://arxiv.org/abs/2607.00276)

**<font color=#1a73e8>作者：</font>** Dong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current large-language-model (LLM) physics benchmarks are usually scored by answer accuracy, which cannot distinguish genuine reasoning from recall of familiar problem patterns and reveals little about where a model's reasoning breaks down. We introduce an auditable four-stage diagnostic that evaluates whether an LLM can reason inside an unfamiliar physics framework through induction, formulation, prediction, and review. The diagnostic combines locked pre-registrations, fresh sessions between stages, dual-LLM judging, and a human-audit pathway, and we apply it to three parallel physics worlds: a single-equation counterfactual world ($F=mv$), a historical framework (Aristotelian mechanics), and a four-domain counterfactual world (Decay World). Across Claude Opus 4.7, GPT-5.5, and Gemini 3.1 Pro, the three worlds yield composite PASS rates are 6/15, 6/15, and 0/15 respectively (content $\land$ structural for $F=mv$ and Aristotelian, content axis only for Decay World where the structural axis is out of scope). The most pointed empirical pattern is a qualitative-versus-quantitative asymmetry: in Decay World, models almost never predict the wrong direction of change, but frequently compute the wrong ratio by slipping back to standard-physics relations. The protocol also surfaces two methodology findings: LLM-judge reliability does not transfer across frameworks, and Stage 4 self-review is weak in every framework, with the model's own review wrongly reporting no earlier error in at least two-thirds of the trials that actually contained one. We release the full prompts, responses, verdicts, and audit records.

---


### 17. [Rosetta: Composable Native Multimodal Pretraining](https://arxiv.org/abs/2607.00293)

**<font color=#1a73e8>作者：</font>** Xiangyue Liu, Zijian Zhang, Miles Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving true artificial general intelligence requires foundation models capable of integrating new modalities without forgetting prior knowledge. However, accommodating continuous generative objectives alongside discrete understanding tasks causes severe gradient conflicts. Existing architectures, including standard Mixture-of-Experts (MoE), are highly susceptible to representation overwriting. Even structurally partitioned paradigms like Mixture-of-Transformers (MoT) remain vulnerable to catastrophic forgetting, severely impeding multimodal scalability. In this work, we introduce Rosetta, a composable native multimodal pretraining framework designed for seamless and non-destructive modality expansion. Rosetta adopts a modular paradigm where core foundational knowledge is preserved within global shared experts, while modality-specific capabilities are distributed across plug-and-play experts. To guarantee non-destructive composition, we propose Momentum-Anchored Orthogonal Projection (MAOP). MAOP leverages the optimizer's momentum state as an implicit semantic anchor, selectively neutralizing conflicting gradient components from new modalities while preserving synergistic updates. Extensive evaluations demonstrate that, while standard MoE and MoT architectures suffer catastrophic forgetting of previously acquired knowledge, Rosetta robustly preserves established language and visual understanding. Furthermore, it delivers superior image generation and unlocks cross-modal synergy, paving the way for truly composable and unified multimodal foundation models. To facilitate further multimodal research, we release our code and checkpoints to the community. Project page at this https URL.

---


### 18. [EPC: A Standardized Protocol for Measuring Evaluator Preference Dynamics in LLM Agent Systems](https://arxiv.org/abs/2607.00297)

**<font color=#1a73e8>作者：</font>** Zewen Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When LLM agents use evaluator feedback to adapt their behavior in closed loops, evaluator biases propagate through the agent's strategy distribution -- a phenomenon known as evaluator preference coupling. Prior work has documented coupling across multiple evaluator families and model versions, but the field lacks a standardized protocol that enables third-party researchers to (i) reproduce coupling measurements, (ii) compare results across evaluators and time points, and (iii) detect measurement decay as proprietary evaluators silently update. This paper provides the protocol. We specify EPC (Evaluator Preference Coupling) -- a detailed, RFC-style protocol specification for the four-phase isolation paradigm, covering executor and evaluator configuration, strategy and task design, the TTRL update rule, metric computation (gamma, JSD, ECE, Brier), and output schema. We accompany the protocol with a versioned Reference Snapshot v1.0: coupling measurements for eight evaluator conditions (N=122 unique experimental repetitions across GPT-4o, Qwen, DeepSeek, and others) derived from five independent studies, annotated with evaluator version identifiers, API endpoints, and measurement dates. The snapshot is explicitly time-bound: all values are conditional on specific model versions and are expected to decay as proprietary evaluators update. We define a versioning convention (vX.Y-Z, encoding protocol version, snapshot version, and evaluator generation) and provide a usage guide covering adoption, interpretation, and known pitfalls. The protocol, reference snapshot, and implementation code are released as open infrastructure.

---


### 19. [Wake up for Touch! Mask-isolated Tactile Alignment Learning in MLLMs](https://arxiv.org/abs/2607.00302)

**<font color=#1a73e8>作者：</font>** Yoonhyung Park, Minji Kim, Sungwon Moon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Touch supplies the physical grounding needed to perceive intrinsic material properties, such as friction and compliance, that vision alone often cannot resolve. Recent efforts for equipping multimodal LLMs with this tactile sense, however, expose a zero-sum trade-off: the limited parameter budget of compact models forces a choice between acquiring the new sensory modality and preserving the established vision-language reasoning. We present Splash, a mask-isolated tactile alignment learning framework for MLLMs. Splash quantifies the significance of each pretrained parameter, and partitions the parameter space into a dormant and critical subspace. While the frozen critical subspace acts as a stable anchor to safeguard general visual knowledge, Splash updates the isolated dormant subspace to internalize tactile alignment towards LLMs. This selective, non-destructive expansion effectively prevents catastrophic forgetting and ensures non-destructive modality expansion. Extensive experiments show that Splash effectively achieves tactile reasoning without additional inference overhead in the LLM part, demonstrating state-of-the-art performance on visuo-tactile benchmarks, including SSVTP, TVL, and TacQuad, while preserving its original general-purpose capabilities.

---


### 20. [RetailSMV: Exocentric vs. Egocentric Adaptation of Foundation Video World Models in Retail](https://arxiv.org/abs/2607.00310)

**<font color=#1a73e8>作者：</font>** Amirreza Rouhi, Rajat Aggarwal, Parikshit Sakurikar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation video diffusion models are increasingly viewed as world simulators for embodied agents, yet their pretraining on internet-scale generic video leaves them poorly aligned with real-world deployment domains. We study parameter-efficient adaptation of a pretrained foundation video world model to retail scenes: when synchronized egocentric and exocentric video of the same activity are available, which viewpoint of training data produces the strongest adapted model?
We introduce RetailSMV (Retail Synchronized Multi-View), a corpus of 32,105 captioned retail clips from five supermarkets with synchronized ego/exo capture from the store-staff perspective (stocking, arranging, weighing, managing supply carts, scanning at checkout), rather than the customer-centric framing of prior retail video corpora, and train three matched Low-Rank Adaptation (LoRA) configurations of Cosmos3-Nano (egocentric-only, exocentric-only, combined) under identical hyperparameters. On a 200-clip held-out test set evaluated with seven complementary metrics under a strict paired statistical protocol, exocentric-only adaptation matches or exceeds combined adaptation on six of seven point estimates and is significantly better on LPIPS, PSNR, and DreamSim, despite training on only 15,985 exocentric clips (versus 32,105 for combined). A symmetric paired comparison further shows that adding exocentric data to egocentric-only training helps while adding egocentric data to exocentric-only training hurts. The absolute adaptation gap is largest at the shortest rollout time, identifying the near-horizon prediction window as the regime in which adaptation is most beneficial.

---


### 21. [DroneFINE: Domain-Aware Parameter-Efficient Fine-Tuning of Vision-Language Detectors for Drone Images](https://arxiv.org/abs/2607.00338)

**<font color=#1a73e8>作者：</font>** Ke Wu, Yanan Zhang, Yingjie Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection for Unmanned Aerial Vehicles (UAVs) working in open and dynamic environments is a highly challenging task. While Vision-Language Models (VLMs) have offered a powerful solution for universal object detection, adapting them to UAV scenarios remains non-trivial due to a substantial domain gap between VLM pre-training data and aerial imagery. The prevailing Parameter-Efficient Fine-Tuning (PEFT) methods prove ineffective in bridging this gap, as VLMs' "natural-scene, foreground-dominant" visual priors misalign with the "bird's-eye-view, background-dominant, small-object" characteristics of UAV data. To address this issue, we propose DroneFINE, a novel PEFT paradigm comprising two domain-aware complementary modules tailored for VLM-based drone image detectors. Specifically, a data-dependent, foreground-aware, and multi-path adaptation mechanism named HyperAdapter is designed, which overcomes the static structural constraints of PEFT. In addition, a background suppression algorithm named SemanticGate is developed. It is a text-conditioned guidance strategy that employs background vocabulary to actively guide the model in suppressing responses from irrelevant regions. Extensive experiments on VisDrone and UAVDT demonstrate that DroneFINE significantly outperforms existing PEFT methods and achieves performance comparable to full fine-tuning while substantially reducing the number of trainable parameters.

---


### 22. [DiscoLoop: Looping Discrete Embeddings and Continuous Hidden States for Multi-hop Reasoning](https://arxiv.org/abs/2607.00341)

**<font color=#1a73e8>作者：</font>** Hengyu Fu, Tianyu Guo, Zixuan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models achieve strong performance on many reasoning tasks when allowed to externalize intermediate steps as Chain-of-Thought (CoT). However, many questions require the model to internalize the multi-step reasoning within a single forward pass before generating the answer. We study this challenge through two-hop reasoning, a representative task where the model must compose multiple pieces of parametric knowledge within a single forward pass. Standard non-recurrent Transformers suffer from a depth-local storage problem: facts learned in earlier layers are unavailable where second-hop retrieval happens. We found that Looped Transformers mitigate this issue by reusing the same memory, but still generalize imperfectly. We show that the remaining bottleneck is representational. In the two-hop reasoning task, the first loop often makes the correct bridge entity nearly perfectly decodable, yet the corresponding hidden state remains poorly aligned with the bridge token embedding. Surprisingly, an easy training-free realignment intervention nearly closes the generalization gap. Building upon this insight, we propose DiscoLoop, a looping architecture whose recurrence carries both a discrete embedding channel and a continuous hidden-state channel. DiscoLoop achieves near-perfect accuracy with substantially fewer training steps across symbolic and synthetic-language multi-hop reasoning tasks. When applied to real-world pretraining, DiscoLoop attains lower training loss and stronger benchmark performance than looped-transformer baselines, suggesting that the mixed-channel design transfers to practical language modeling.

---


### 23. [Personalized Object Identification and Localization via In-Context Inference with Vision-Language Models](https://arxiv.org/abs/2607.00357)

**<font color=#1a73e8>作者：</font>** Kensuke Nakamura, Byung-Woo Hong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalized object localization (POL) localizes an object instance in a query image based on a few reference images with bounding-box annotations and a target object label. The pioneering method, IPLoc, solves this task through in-context inference with vision-language models (VLMs). However, it assumes that the query image always contains the target object. This assumption severely limits its applicability to real-world scenarios with many irrelevant images. To address this issue, we formulate a new task, personalized object identification and localization (POIL), by positioning POL within the broader few-shot object detection framework. POIL aims to localize the target object instance while rejecting query images that do not contain the reference object instance. We also present POIL datasets constructed from public sources. We further propose an in-context algorithm named IPLoc-ID for solving POIL with VLMs. IPLoc-ID first predicts a candidate bounding box and then determines whether it corresponds to the reference object instance. We introduce a self-posed query to connect these two steps within a single autoregressive generation framework. Through ablation studies and comprehensive experiments, we show that IPLoc-ID substantially suppresses false-positive detections on negative query images while maintaining localization performance comparable to IPLoc. Overall, IPLoc-ID effectively addresses the practical instance-level POIL task, which cannot be sufficiently solved by conventional object detection, few-shot object detection, or the localization-only IPLoc method.

---


### 24. [Beyond Perplexity: A Behavioral Evaluation Framework for Deployment-Memory Claims in LLM Test-Time Training](https://arxiv.org/abs/2607.00368)

**<font color=#1a73e8>作者：</font>** Xiangchen Song, Zhenhao Chen, Lingjing Kong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model test-time training (TTT) is often evaluated through local proxy metrics: models are updated on recent tokens, retrieved context, target-domain data, or verifiable task attempts, and then judged by perplexity, future-token loss, long-context performance, or reward. These metrics are well matched to claims about stream adaptation, domain adaptation, context compression, and reward-backed test-time improvement. They are weaker evidence, however, for a capability that TTT results are increasingly used to motivate: deployed assistant memory, personalization, or sparse post-deployment learning, which instead requires behavioral evidence such as later recall, paraphrase robustness, retention, locality, conflict handling, and use in downstream actions after the original support context is removed. We introduce a behavioral evaluation framework that calibrates TTT memory claims to the evidence that supports them. It has two components: a claim-calibrated evidence ladder that separates stream/domain adaptation, bridge internalization, and deployment-time behavioral learning; and an evaluation protocol with matched explicit-memory baselines and mutually exclusive failure categories. We validate the framework by auditing recent TTT and memory-adjacent work and by instantiating it as a controlled diagnostic in which, in a sparse nonce-fact setting, one-step LoRA updates lower support and answer loss across three Qwen3 model scales while generated free-form recall stays at zero, exposing a measurable gap between proxy improvement and deployment behavior. The framework gives authors and evaluators a concrete standard for aligning TTT memory claims with the evidence actually reported.

---


### 25. [MEPA: Multi-Scale Representation Alignment for Visual Autoregressive Modeling with Mixture of Experts](https://arxiv.org/abs/2607.00371)

**<font color=#1a73e8>作者：</font>** Nuoyan Zhou, Zhijun Tu, Lei Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual AutoRegressive modeling (VAR) has pioneered a coarse-to-fine multi-scale autoregressive generative paradigm, demonstrating strong capabilities in image generation. However, VAR still suffers from inherent deficiencies in multi-scale representation learning. Specifically, lower scales primarily capture global semantics, while higher scales focus on fine-grained details. Employing a shared architecture across scales induces optimization conflicts. Moreover, due to the causal autoregressive process, inaccurate semantics at early scales can propagate and significantly degrade the final output. To address these issues, we introduce a scale-aware token-routed Mixture of Experts (MoE) architecture, allowing scale-adaptive expert selection, thereby facilitating decoupled representation learning across scales. In addition, we enhance semantic modeling at early scales by incorporating external self-supervised features. Unlike naive alignment, we analyse and design a residual feature aggregation scheme tailored to the VAR paradigm. Extensive experiments show that our method significantly improves both training efficiency and generation quality. On the ImageNet 256*256 benchmark, our model achieves a superior FID compared to the dense baseline while requiring only half of the default training epochs and a smaller parameter budget, with a merely marginal increase in training cost. Moreover, the performance gap further widens with larger training epochs.

---


### 26. [The Illusion of High Utility in Safety Alignment of Text-to-Image Diffusion Models](https://arxiv.org/abs/2607.00402)

**<font color=#1a73e8>作者：</font>** Adeel Yousaf, Soumik Ghosh, James Beetham 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Safety alignment of text-to-image (T2I) diffusion models aims to suppress harmful generations while preserving utility on benign prompts. Recent methods often appear to deliver high safety with high utility, but this conclusion rests largely on coarse global utility metrics (e.g., FID, CLIPScore) that are insensitive to fine-grained semantic correctness, creating an illusion of high utility. We show that when utility is measured with structured evaluation, this illusion breaks: on TIFA (Text-to-Image Faithfulness evaluation with Question Answering), safety-aligned models suffer substantial drops in semantic fidelity, including failures in object counts, attributes, and relationships. To diagnose the source of this gap, we analyze the text-encoder prompt embedding space and uncover semantic collapse, a contraction of embedding spread coupled with distortion of inter-prompt similarity structure, which strongly correlates with structured utility loss. Guided by this insight, we propose StructureAware Geometric Regularization (SAGE), a safety alignment objective that explicitly preserves embedding spread and inter-prompt relational structure during adaptation. Our method restores structured utility (TIFA +5.0% over prior state-of-the-art) while maintaining strong safety performance and competitive coarse-grained utility scores. Our source code and trained models are available at this https URL.

---


### 27. [A Penny for Your Prompts: Experiments Detecting and Mitigating LLM Usage by Survey Respondents](https://arxiv.org/abs/2607.00403)

**<font color=#1a73e8>作者：</font>** Zane Xu, Nathan Malkin  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used by participants on crowdsourcing platforms when responding to surveys, potentially undermining the validity of collected data. Our study aims to quantify the prevalence of this behavior and investigate methods to detect and prevent it. In a series of surveys (N = 250), we examined conditions such as platform choice, survey length, requests not to use AI, and disabling copy-paste functionality. We were able to identify distinct characteristics of LLM-assisted responses and found that their frequency varied widely, from under 10% on Prolific to over 80% on Mechanical Turk. Mitigation measures reduced LLM usage but did not necessarily improve data quality. No participants employed browser-use agents at the time of our survey, but we report on our own detection experiments. We recommend that researchers actively screen survey responses for LLM usage by recording and analyzing keystroke data and crafting instructions and questions aimed at AI.

---


### 28. [Personalization as Inverse Planning: Learning Latent Design Intents for Agentic Slide Generation via Structural Denoising](https://arxiv.org/abs/2607.00407)

**<font color=#1a73e8>作者：</font>** Tianci Liu, Zihan Dong, Linjun Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Slide design requires personalizing both deck themes and page layouts. Yet, current AI agent-based methods struggle with fine-grained, page-level design. Solely relying on prespecified templates or user verbose instructions, they fail to capture latent design intents, leaving Page-level Slide Personalization (PSP) unresolved. To close this gap, this work formulates PSP as an inverse planning problem. We propose to learn a design intent without assuming any knowledge of the specific executing tools (e.g., PowerPoint, Beamer) being used. However, relinquishing control over these tools makes the problem intractable to optimize end-to-end. To overcome this, we propose SPIRE, a principled framework to solve PSP approximately. By intentionally corrupting the visual structures of clean slides, SPIRE creates a verifiable task to denoise the corruption, whereby two agents learn to collaboratively refine executable designs via reinforcement learning (RL). We present a proof that structural denoising is a consistent surrogate for PSP, and that the multi-agent formulation strictly reduces policy gradient variance in RL. Extensive experiments demonstrate the superiority of SPIRE.

---


### 29. [A Mechanistic View of Authority Hierarchy in LLM Sycophancy](https://arxiv.org/abs/2607.00415)

**<font color=#1a73e8>作者：</font>** Emil Joswin, Srujananjali Medicherla, Priyanka Mary Mammen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Authority bias poses a critical safety concern in language models: models systematically prioritize social cues from authority figures over factual consistency, swaying their answers based on source credibility rather than evidence. We mechanistically investigate this phenomenon using a controlled medical QA setting, where hints suggesting incorrect answers are attributed to personas of varying expertise. Across Llama-3.1-8B, Qwen3-8B, and Gemma-2-9B, we find that models respond in a graded manner proportional to perceived authority, a hierarchy that is never explicitly prompted but emerges from training. Logit lens analysis and linear/non-linear probing localize this effect to a critical late layer where correct answer representations are actively erased, an erasure that scales with authority level, resists mean vector intervention, and is only partially reversible through chain-of-thought reasoning. Our findings suggest that authority-induced sycophancy is not a surface-level output bias but mechanistic knowledge erasure, a precise, layer-localized overwriting of correct internal representations by high-status authority signals.

---


### 30. [DroneIQA-VLE: Multi-Task Drone Image Quality Assessment via Vision-Language Ensemble](https://arxiv.org/abs/2607.00416)

**<font color=#1a73e8>作者：</font>** Wei Sun, Weixia Zhang, Hongjian Zhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present DroneIQA-VLE, our solution to the ICME 2026 Drone-IQA Grand Challenge on Target-aware Image Quality Assessment for Low-altitude UAV Images. The framework jointly predicts global, target, and background quality scores by ensembling two complementary pipelines: (1) SigLIP2 vision encoders with multi-task regression heads, and (2) a LoRA-adapted Qwen3.5-9B multimodal large language model for quality score regression. The final global quality prediction is obtained by arithmetically averaging the outputs of both pipelines. Our method achieves 2nd place in the challenge, demonstrating its effectiveness. The code is available at this https URL.

---


### 31. [EO-VGGT: Orbital Ray-Conditioned 3D Foundation Models for Satellite Multi-View Reconstruction](https://arxiv.org/abs/2607.00417)

**<font color=#1a73e8>作者：</font>** Qiyan Luo, Yingdong Pi, Lekang Wen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the era of satellite constellations, multi-view optical satellite imagery is pivotal for Earth Observation (EO) and high-quality Digital Surface Model (DSM) reconstruction. Although feed-forward 3D foundation models have transformed computer vision, their deployment in satellite remote sensing is inherently constrained by the structural discrepancy between implicit perspective assumptions and explicit orbital pushbroom geometry. This geometric incongruity is further compounded by pronounced view-set heterogeneity. We present EO-VGGT, a framework that adapts a frozen perspective-driven model to orbital observations via explicit physical geometry this http URL, the Geometry-Correlation Constrained Selection (GCCS) strategy prunes sub-optimal observations by balancing geometric diversity and radiometric consistency to optimize the input sequence. Second, a Sensor-Ray Encoder (SRE) parameterizes pixel-level pushbroom lines of sight derived from the Rational Function Model (RFM) into high-dimensional space-geometric tokens, reconciling the mathematical discrepancy between central projection and orbital kinematics. Third, a lightweight Ray-Pointing-Aware Adapter (RPAA) employs gated residual blocks to integrate these tokens directly into the frozen transformer backbone. Our findings underscore that integrating explicit physical geometry with optimized view selection is essential for robust feed-forward satellite 3D reconstruction.

---


### 32. [HyFL-CLIP: Hyperbolic Fine-Tuning of CLIP for Robust Long-Context Understanding](https://arxiv.org/abs/2607.00428)

**<font color=#1a73e8>作者：</font>** Ji Ha Jang, Hayeon Kim, Chulwon Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CLIP (Contrastive Language-Image Pre-training) has become a de facto paradigm for image-text alignment, but it struggles with long-context descriptions (>77 tokens) due to absolute positional encoding and pretraining on short captions. In long contexts, sentences are often reordered, summarized, or partially omitted. Although prior works extend CLIP with longer positional encodings, they often suffer from degraded image-text alignment under such text perturbations. We attribute this limitation to the Euclidean contrastive objective, which enforces strict one-to-one matching and lacks explicit mechanisms for modeling hierarchical relationships between global context and its constituent elements. To address this issue, we propose HyFL-CLIP, a hyperbolic fine-tuning framework that distills the well-established text-image alignment learned in Euclidean CLIP into hyperbolic space via cross-manifold similarity distillation, leveraging its geometry to capture hierarchical and entailment relations. Our method models hierarchical semantics by linking summarized token-wise features, long-context descriptions, constituent short textual components, and images, capturing part-whole relationships via hyperbolic entailment with Einstein midpoint aggregation. Experiments on diverse benchmarks, including long-context cross-modal retrieval, cross-modal retrieval with caption perturbations, intra-modality retrieval, and short-text cross-modal retrieval, show that HyFL-CLIP achieves more robust long-context understanding. In particular, it yields up to 19.5% improvement in long-text cross-modal retrieval under textual perturbations over the best prior method. We also show HyFL-CLIP can be seamlessly integrated into other model frameworks by applying it to Stable Diffusion XL (SDXL).

---


### 33. [Information-Regularized Attention for Visual-Centric Reasoning](https://arxiv.org/abs/2607.00434)

**<font color=#1a73e8>作者：</font>** Guohao Sun, Xiaofang Wang, Yash Patel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have become a paradigm for multimodal learning, yet remain unstable due to object hallucination, weak visual grounding, and catastrophic forgetting after full-parameter instruction tuning. We claim these failures result from a lack of explicit control over visual representation learning during the standard next-token prediction objective. As a result, visual embeddings thus become passively optimized and prone to injecting redundant or spurious signals. To counter this, we introduce Information-Regularized Attention (IRA), a stochastic attention mechanism that explicitly regulates the amount of visual information injected into the hidden states of intermediate transformer layers. This local reparameterization translates uncertainty about visual representations into local noise that is independent across data points. Beyond evaluating model performance, we also quantify embedding properties, where IRA produces smoother curvature trajectories and suppresses attention-sink across all layers, indicating a more stable transformation of the visual signal. Our results suggest that stochastic attention is not merely a regularizer but a key contributor to representation learning in a generative architecture, offering a new direction for building more reliable VLMs.

---


### 34. [PHREEQC-MCQ-200: A Diagnostic Benchmark for Tool-Augmented Scientific Simulator Agents](https://arxiv.org/abs/2607.00436)

**<font color=#1a73e8>作者：</font>** Ke Zhang, Sahchit Chundur, Mohammad Javad Qomi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents are increasingly connected to scientific software, yet it remains unclear when tool access makes scientific computation more reliable rather than merely more complex. We introduce PHREEQC-MCQ-200, a benchmark for evaluating tool-augmented agents on deterministic aqueous-geochemistry simulations. The benchmark contains 200 multiple-choice questions derived from 21 validated PHREEQC scenarios, requiring agents to construct simulator inputs, execute PHREEQC, inspect structured outputs, and commit to final answers.
Across multiple frontier and mid-tier model families, simulator access substantially improves aggregate accuracy, confirming that grounded execution is necessary for many scientific-computation tasks. However, the gains are not monotonic: tool-augmented agents also lose items they answered correctly without tools, revealing regressions that average accuracy alone hides. We further show that output-access protocol matters. A table-of-contents interface can reduce token cost while preserving or improving accuracy for stronger models, but it degrades performance for mid-tier models that cannot reliably navigate structured simulator outputs.
PHREEQC-MCQ-200 therefore frames scientific tool use as an end-to-end diagnostic problem rather than a simple tool-calling capability. We argue that evaluations of scientific agents should report not only accuracy, but also item-level retention, output-access sensitivity, trajectory failures, and where the computation chain breaks.

---


### 35. [Understanding Why Language Models Hallucinate: Testing Reasoning Against Priors](https://arxiv.org/abs/2607.00447)

**<font color=#1a73e8>作者：</font>** Yangfan Hu, Xuhan Tong, Haoyue Bai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often produce hallucinated answers that violate prompt-level constraints. A key diagnostic question is whether these failures reflect missing knowledge, or whether the model has the relevant information but follows the wrong inference path. We study this phenomenon as inference misalignment: a mismatch between the answer supported by the prompt and the answer favored by statistically salient latent associations. We formalize this view with a latent key-task model, in which pretraining-frequency imbalance can cause a shortcut path to dominate the constraint-sensitive path and induce positive inference loss. The framework predicts two failure modes: task-retrieval bias in entity disambiguation and key-selection bias in action choice. We introduce TrapQA, a controlled diagnostic testbed with two components. ScientistQA tests disambiguation among similar scientists with supplementary factual probes, while Real-Life Constrained QA tests everyday constraint following under salient shortcuts. Our results show that hallucination can arise from biased latent inference rather than absent knowledge alone.

---


### 36. [Agri-SAGE: Simulation-Grounded Multi-Agent LLM for Context-Aware Agricultural Advisory Generation](https://arxiv.org/abs/2607.00454)

**<font color=#1a73e8>作者：</font>** Vedant Balasubramaniam, Geetha Charan, Manojkumar Patil 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agricultural advisory systems face a fundamental tension: static agronomic guidelines offer consistent, evidence-based recommendations, yet remain blind to in-season variability and dynamic uncertainties. Recent advisory systems powered by LLMs are liable for a different risk of generating recommendations that are agronomically credible but physiologically unconvincing. Agri-SAGE is a closed-loop framework designed to resolve the above two limitations by integrating retrieval-grounded multi-agent LLM reasoning with APSIM-based biophysical simulation, to generate and validate agronomic advisories. To assess this framework, we evaluate three reasoning approaches, namely Plan-and-Solve, Tree of Thoughts, and Reflexion, over a 10-year retrospective analysis. All three significantly outperform static PoP (Package-of-Practice) baselines, with Tree of Thoughts achieving impressive peak yields. At the same time, Reflexion achieves comparable agronomic outcomes at substantially lower computational cost by leveraging cross-seasonal episodic memory.

---


### 37. [Multi-scale Mixture of World Models for Embodied Agents in Evolving Environments](https://arxiv.org/abs/2607.00457)

**<font color=#1a73e8>作者：</font>** Jinwoo Jang, Daniel J. Rho, Sihyung Yoon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied agents operating in the real world require multi-scale reasoning and knowledge adaptation as conditions change. We identify two challenges in applying Mixture of Experts (MoE) to this setting: routing lacks an explicit notion of scale, preventing targeted updates at specific scales, and a uniform update policy cannot accommodate the different rates at which knowledge at each scale becomes outdated. We present MuSix, a framework that addresses both challenges through scale-aware world model mixture and evolution. A two-stage routing mechanism grounds scale selection in experiential distance, a measure of situational novelty inspired by Construal Level Theory: a meta-router first maps this quantity to a weight over continuous scale space, then per-scale base routers select world models within the identified scale. For adaptation, scale-dependent forgetting rates allow low-scale knowledge to refresh rapidly while high-scale abstractions persist, and gated inter-scale transfer maintains coherence across the hierarchy. Experiments on EmbodiedBench and HAZARD show that MuSix improves over state-of-the-art baselines on multi-scale reasoning and dynamic adaptation.

---


### 38. [Multimodal Continuous Reasoning via Asymmetric Mutual Variational Learning](https://arxiv.org/abs/2607.00461)

**<font color=#1a73e8>作者：</font>** Shijie Li, Yilin Gao, Siyuan Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) are often constrained by a language-space bottleneck, forcing complex visual reasoning into discrete tokens which can lose perceptual nuance. A promising alternative is continuous latent reasoning, where the goal is to discover implicit reasoning pathways that bridge the multimodal query and the final answer. However, this introduces a severe train-inference mismatch: a training-time posterior, conditioned on the ground-truth answer, can exploit answer-dependent shortcuts. Standard variational training then forces the inference-time prior to mimic a posterior that has access to information unavailable at test time, leading to poor performance. To address this, we propose Asymmetric Mutual Variational Learning (AMVL), a framework that resolves this mismatch via a bidirectional calibration objective. A forward KL divergence trains the target-agnostic prior to match the posterior, while a novel reverse KL divergence simultaneously regularizes the posterior, preventing it from collapsing into inference-incompatible regions and mitigating this ``answer leakage''. We provide theoretical analysis formalizing this leakage as prior contamination and prove that our dual-KL objective reduces it. We instantiate AMVL in a latent-integrated MLLM and show that it consistently outperforms strong discrete and latent-reasoning baselines, improving the average score on the complex BLINK benchmark by +10.83 and achieving gains of up to +32.00 on individual reasoning tasks, with analyses confirming improved latent-space stability.

---


### 39. [StochasT: Learning with Stochastic Turn Depth for Visual Instruction Tuning](https://arxiv.org/abs/2607.00465)

**<font color=#1a73e8>作者：</font>** Yuan Qing, Chengzhi Mao, Boqing Gong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) rely extensively on Visual Instruction Tuning (VIT) to elicit their multimodal reasoning capabilities. However, we find a discrepancy: VIT often packs multiple language tasks about the same image for conversational, multi-turn training, whereas existing benchmarks evaluate LVLMs in isolated, single-turn scenarios. The models can suffer from visual attention decay and contextual overfitting during multi-turn training, making it hard for them to realize their full potential in the mismatched test phase. To close the gap, we propose learning with Stochastic Turn Depth (StochasT), which stochastically groups language tasks for the same image into clusters of varying sizes (turn depth) while preserving their organic order. Hence, while StochasT draws on Dropout and stochastic depth for ResNets, it does not actually drop anything to maximize the utility of the training data. Furthermore, we introduce a challenging, benchmark-agnostic evaluation mechanism based on the Balanced Latin Square to measure LVLMs' robustness under varying contextual dependencies. Extensive experiments demonstrate that StochasT effectively grants LVLMs strong, harmonized capabilities for both single-turn and multi-turn use cases.

---


### 40. [Ghost in the Kernel: In-Context Learning with Efficient Transformers via Domain Generalization](https://arxiv.org/abs/2607.00479)

**<font color=#1a73e8>作者：</font>** Peilin Liu, Ding-Xuan Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based large models have demonstrated remarkable generalization abilities across different tasks by leveraging a context-aware attention module for in-context learning. With richer context, transformers adapt more effectively to the current use case without any parameter updates. However, the quadratic computational and memory complexity with respect to context length significantly slows data processing in softmax transformers. Linear transformers were proposed to address this issue by reducing the complexity to linear dependence on context length, but the design and understanding of the feature mapping in linear attention, from a theoretical viewpoint, remain unclear. In this paper, we investigate the approximation and generalization abilities of linear transformers under a two-staged sampling process from domain generalization. We show that linear transformers perform in-context learning as learning a mapping from context distributions to response functions. A dimension-independent convergence rate is obtained for our generalization analysis, which also exhibits the tradeoff between the regularities of data distributions and latent features. Guided by our theoretical framework, we propose a new perspective on activation and loss design for linearizing pretrained softmax large language models.

---


### 41. [BaseRT: Best-in-Class LLM Inference on Apple Silicon via Native Metal](https://arxiv.org/abs/2607.00501)

**<font color=#1a73e8>作者：</font>** Prabod Rathnayaka, Fabian Waschkowski, Lukas Wesemann  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present BaseRT, a native Metal inference runtime for large language models (LLMs) on Apple Silicon, and report the highest inference throughput on this hardware to date. Existing runtimes, including this http URL and MLX-based frameworks, incur overhead from abstractions not designed for Metal's execution model or Apple Silicon's unified memory topology. By building natively on Metal with chip-specific kernel fusion, unified memory-aware optimisation, and custom dispatch logic, BaseRT recovers performance that framework-based approaches leave on the table. BaseRT supports a wide range of model families across eight quantisation formats (Q2 to FP16) on all Apple M-series devices. In this paper, we evaluate the Qwen3, Llama 3.2, and Gemma 4 families at Q4 and Q8 quantisation on M3 and M4 Pro devices. BaseRT achieves up to 1.56x higher decode throughput than this http URL and up to 1.35x higher than MLX, with substantially larger margins on prefill for mixture-of-experts models, delivering consistent best-in-class throughput from sub-1B to 30B parameter models. These results establish Apple Silicon as a more capable inference platform than previously reported, with direct implications for the emerging edge inference paradigm: as privacy requirements, latency constraints, and cloud cost pressures drive inference toward on-device deployment, performance-optimised local runtimes are a critical enabling layer for this transition. BaseRT is publicly available at this https URL

---


### 42. [Prototype Language Models](https://arxiv.org/abs/2607.00510)

**<font color=#1a73e8>作者：</font>** Dan Ley, Giang Nguyen, Himabindu Lakkaraju 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowing which training examples drive outputs is fundamental to auditing, correcting, and understanding language models, yet for modern LLMs this remains expensive, approximate, and largely post-hoc. Standard language models generate tokens through a dense network pathway, causing training data's influence to be distributed across parameters rather than organized along explicit, traceable components. We introduce a prototype language model architecture, Prototypes for Interpretable Sequence Modeling (PRISM), that forms each prediction via a sparse, non-negative mixture of learned prototypes, trained with clustering objectives that anchor each prototype to coherent neighborhoods of training examples. Across architectures from 130M to 1.6B parameters trained on up to 50B tokens, prototype language models either surpass or remain within 2.5 percentage points on average downstream accuracy of matched dense baselines. We show that sparse prototype structure localizes curvature in the loss landscape, yielding a more tractable Hessian and enabling training data attribution that is ~500x faster than post hoc baselines when consuming equivalent memory. Calibrating linear prototype controllers can improve downstream accuracy by roughly 3 points while tracing those corrections back to training neighborhoods, and targeted prototype suppression can remove model behaviors without finetuning or measurable loss in generation quality.

---


### 43. [Active-GRPO: Adaptive Imitation and Self-Improving Reasoning for Molecular Optimization](https://arxiv.org/abs/2607.00531)

**<font color=#1a73e8>作者：</font>** Xuefeng Liu, Mingxuan Cao, Qinan Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific reasoning is an increasingly important capability of large language models, yet improving the robustness and efficiency of training such reasoning remains a key open challenge. We study this problem in instruction-based molecular optimization, where answer-only supervised fine-tuning (SFT) collapses multi-step reasoning and reinforcement learning with verifiable rewards (RLVR) suffers from sparse feedback. Reference-guided Policy Optimization mitigates both by anchoring policy updates to dataset-provided references, but its effectiveness is tightly coupled to reference quality: weak or misaligned references impose a performance ceiling. To overcome this ceiling, we propose active reasoning, a paradigm in which the policy actively decides, on a per-instance basis, when to imitate a reference and when to reinforce its own discoveries, while continuously upgrading what it imitates. We instantiate this paradigm as Active Group Relative Policy Optimization (Active-GRPO), realized through two coupled mechanisms: active imitate-reinforce and active referencing. The former performs imitation learning when the reference still outperforms the policy's own candidates, and shifts to self-improvement via reinforcement learning once the policy has generated molecules that surpass the reference. The latter continuously upgrades the reference itself by replacing it with the best policy-generated candidate discovered so far, progressively raising the imitation target and ensuring that reference guidance remains informative-rather than restrictive-throughout training. Across TOMG-Bench MOLOPT, Active-GRPO improves average SRxSim from 0.0959 for GRPO and 0.1665 for RePO to 0.1773 under matched three-seed evaluation, with statistically significant gains on LogP, MR, and QED.

---


### 44. [ECoSim: Data Efficient Fine-Tuning for Controllable Traffic Simulation](https://arxiv.org/abs/2607.00545)

**<font color=#1a73e8>作者：</font>** Yu-Hsiang Chen, Wei-Jer Chang, Yi-Ting Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable traffic simulation is critical for testing autonomous driving systems, yet existing approaches often require retraining large generative models with extensive annotated data. We introduce a lightweight control adaptation framework that enables multi-modal controllability (sketch, latent behavior codes, and text) for pretrained state-of-the-art diffusion and autoregressive traffic models. By modulating intermediate features through identity-initialized FiLM layers, our method efficiently adds new control modalities while preserving the base model's generative prior. Evaluated on Waymo Open Sim Agents Challenge, our approach demonstrates strong controllability with less than 1% of the paired control data. Through context-aware condition transfer, our framework enables counterfactual scenario generation and long-tail synthesis while maintaining stable closed-loop driving realism and safety. Our framework unlocks new possibilities for controllable traffic simulation, enabling targeted scenario generation through lightweight adaptation of pretrained generative models. Project page: this https URL

---


### 45. [HARC: Coupling Harmfulness and Refusal Directions for Robust Safety Alignment](https://arxiv.org/abs/2607.00572)

**<font color=#1a73e8>作者：</font>** Shei Pern Chua, Fangzhao Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding how aligned LLMs internally represent safety is critical for diagnosing alignment vulnerabilities, as it explains why jailbreaks succeed and informs the design of robust alignment strategies. Prior work shows that aligned LLMs encode harmfulness and refusal as separable directions in the residual stream at prompt-side token positions. We show that jailbreaks succeed at prompt encoding by suppressing either the refusal or harmfulness direction before any token is generated, with distinct attack classes occupying separable regions of the harmfulness-refusal plane. Extending the analysis to response-token positions, we find that the model recognizes harmful content while it is generating that content, even when it failed to recognize the input as harmful at the prompt side. Motivated by our findings, we introduce HARC (Harmfulness-And-Refusal Coupling), a fine-tuning method that pairs the two directions across both prompt and response positions. Since the intervention is confined to the harmfulness-refusal subspace, it leaves the rest of the residual stream intact and does not degrade general capability or inflate over-refusal. Across extensive experiments, HARC achieves the strongest robustness-capability-usability trade-off among six baselines spanning the major training-time and inference-time safety methods. The harmfulness and refusal directions at prompt and response positions transfer across the five model families and two scales we tested without architecture-specific tuning.

---


### 46. [BrainFIBRE: A Foundation Model via Information Decomposition for Brain Microstructure](https://arxiv.org/abs/2607.00573)

**<font color=#1a73e8>作者：</font>** Zijian Dong, Yi Lin, Ji Fang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion MRI probes brain microstructure with particular sensitivity to early cerebrovascular and neurodegenerative changes. Neurite Orientation Dispersion and Density Imaging (NODDI) decomposes the diffusion signal into three biophysically interpretable maps: neurite density index (NDI), orientation dispersion index (ODI), and free water fraction (FWF), capturing neurite packing, fiber coherence, and extracellular fluid. These 3D maps offer a rich substrate for transferable microstructural representations, yet integrating them is challenging: standard representation learning struggles to disentangle the unique information in each map from their shared and synergistic interactions. We present BrainFIBRE, the first foundation model for brain microstructure, pretrained on NODDI-derived maps from 55,592 UK Biobank participants. We propose Self-supervised Partial Information Decomposition (SPID), which extends PID-guided multimodal learning to the self-supervised regime for the first time. A novel Counterfactual Candidate Construction (CCC) paradigm perturbs inter-modality alignment through modality dropping and swapping, providing the contrastive signal for a Mixture-of-Experts architecture to disentangle unique, synergistic, and redundant information without any downstream label. On both Caucasian and Asian cohorts, BrainFIBRE achieves state-of-the-art performance across diverse tasks predicting age, sex, cerebrovascular and neurodegenerative markers, and cognition, while yielding neurobiologically interpretable representations that reveal task- and cohort-specific interaction patterns. BrainFIBRE establishes a versatile foundation for neuroimaging analysis at the microstructural level.

---


### 47. [EPO: Boosting 3D Foundation Models with Edge-based Pose Optimization](https://arxiv.org/abs/2607.00579)

**<font color=#1a73e8>作者：</font>** Mattia D'Urso, Christian Sormann, Mattia Rossi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce \textbf{Edge-based Pose Optimization (EPO)}, a trackless geometric optimization framework specifically designed to boost the Structure-from-Motion reconstructions generated by 3D Foundation Models. These models achieve rapid inference by bypassing the time-consuming feature extraction and matching stages of traditional pipelines, where explicit correspondences between each 3D point and multiple images, referred to as tracks, are established. However, their geometric accuracy currently falls short of traditional pipelines. While this can be addressed in a post-processing step via Bundle Adjustment-like refinement, doing so requires extracting feature tracks, thus defeating the original speed advantage. Instead, our fully differentiable framework uses edge map alignment as a proxy for geometric optimization, avoiding feature extraction and track construction entirely. Through extensive evaluation across multiple datasets and tasks, we demonstrate that EPO matches or outperforms Bundle Adjustment-like methods while requiring significantly lower runtime and memory. Notably, its reduced memory footprint makes EPO suitable for consumer-grade hardware, where competing refinement methods cannot run.

---


### 48. [Semantic-Guided Reading Order Reconstruction in Historical Armenian Newspapers with LLMs](https://arxiv.org/abs/2607.00596)

**<font color=#1a73e8>作者：</font>** Chahan Vidal-Gorène, Nadi Tomeh, Victoria Khurshudyan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper addresses reading order reconstruction in historical Armenian newspapers, which combine complex layouts with limited language resources. We introduce a new annotated dataset of 66 pages and compare geometric heuristics, YOLO-based layout parsing, an end-to-end document model ECLAIR, and a hybrid method combining semantic zone detection with a generative LLM. Our hybrid method achieves the lowest error rates of all evaluated approaches, reducing ordering errors by up to 76% over the strongest geometric baseline, and remains robust in multi-page settings and under noisy OCR. Rather than targeting production the method is designed as a data bootstrapping strategy enabling rapid annotation in highly under-resourced scenarios. Alongside the dataset, we release a specialized Tesseract OCR model for historical Armenian print.

---


### 49. [Multi-Turn Agentic Scientific Literature Search via Workflow Induction](https://arxiv.org/abs/2607.00597)

**<font color=#1a73e8>作者：</font>** Jisen Li, Bingxuan Li, Nanyi Jiang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific literature search often requires more than retrieving papers from a single query: users' intents are underspecified, preference-dependent, and evolve through interaction. Existing search agents typically rely on fixed pipelines or implicit language-only reasoning, making their search strategies difficult to control, inspect, and refine. We introduce PaperPilot, a multi-turn literature search agent that frames scientific search as workflow induction. Given an anchor paper and a user query, PaperPilot constructs an executable DAG of paper-search operators, including keyword search, citation expansion, filtering, scoring, reranking, and evidence extraction. User feedback is then used to refine both the query and the workflow itself. We train PaperPilot with supervised workflow imitation and preference optimization over controlled workflow corruptions. Experiments show that PaperPilot-9B improves over the base Qwen3.5-9B toolset agent under multi-turn interaction, increasing Hit@5 from 58.0 to 77.0, MRR from 47.5 to 59.4, and nDCG@10 from 26.8 to 32.5, while reducing workflow execution errors from 9.5% to 0%. These results show that explicit, editable search workflows provide an effective and controllable interface for aligning literature search agents with complex scientific intent.

---


### 50. ["Don't Say It!": Constraints, Compliance, and Communication when Language Models Play Taboo](https://arxiv.org/abs/2607.00601)

**<font color=#1a73e8>作者：</font>** Sara Candussio, Francesca Padovani, Daniel Scalena 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The game of Taboo requires describing a target word without using a set of forbidden words, so that other players can guess it. This deceptively simple task combines strict lexical constraints with the need for communicatively effective descriptions, making it a compelling playground for examining how LLMs navigate competing demands at inference time. We evaluate two open-weight models under conditions that intervene at progressively deeper levels of the generative process, from prompting to generation-time constraints to internal representations manipulations. We assess their outputs through forbidden word violation detection, LLM-as-a-judge measuring the degree to which generated descriptions successfully evoke the target concept for both human and machine guessers, and examining whether the strategies models adopt under constraint align with those of human players. Our results show that compliance with the rules of the game and communicative effectiveness trade off differently across conditions, and that models remain substantially weaker than humans as guessers, suggesting that lexical grounding under constraint is an open challenge for current language models.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-110](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
