# 🔐 大模型安全相关研究 | 2026年04月30日

> 本类共 **9** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Semantic Denial of Service in LLM-controlled robots](https://arxiv.org/abs/2604.24790)

**<font color=#1a73e8>作者：</font>** Jonathan Steinberg, Oren Gal  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety-oriented instruction-following is supposed to keep LLM-controlled robots safe. We show it also creates an availability attack surface. By injecting short safety-plausible phrases (1-5 tokens) into a robots audio channel, an adversary can trigger the models safety reasoning to halt or disrupt execution without jailbreaking the model or overriding its policy. In the embodied setting, this is a semantic denial-of-service attack: the agent stops because the injected signal looks like a legitimate alert. Across four vision-language models, seven prompt-level defenses, three deployment modes, and single- and multi-injection settings, we find that prompt-only defenses trade off attack suppression against genuine hazard response. The strongest defenses reduce hard-stop attack success on some models, but defenses change the form of disruption, not its fact: suppressed hard stops re-emerge as acknowledge loops and false alerts, which we measure with Disruption Success Rate (DSR). We further find that injection variety is consistently more effective than repeating the same phrase, suggesting that models treat diverse safety cues as corroborating evidence. The practical implication is architectural rather than prompt-level: systems that route unauthenticated audio text directly into the LLM create an avoidable security dependency between safety monitoring and action selection.

---


### 2. [SUDP: Secret-Use Delegation Protocol for Agentic Systems](https://arxiv.org/abs/2604.24920)

**<font color=#1a73e8>作者：</font>** Xiaohang Yu, Hejia Geng, William Knottenbelt  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic systems increasingly act with user secrets for APIs, messaging platforms, and cloud services. Today's bearer-secret interfaces implement authorization by exposure: enabling action often means placing a reusable secret, or a reusable artifact derived from it, within a model-steerable boundary, so a transient prompt-injection or tool-side compromise becomes durable account compromise. Existing defenses cover adjacent pieces such as secret storage, scoped delegation, sender-constrained tokens, and runtime monitoring, but leave the combined agentic obligation without a common specification: an untrusted autonomous requester should be able to cause a user-authorized secret-backed operation without exposing reusable authority to the requester. We formalize this problem as Agent Secret Use (ASU). From ASU we derive a security-property taxonomy that separates the problem's structural obligations from the realization-level robustness conditions any concrete construction must establish, enabling principled comparison of existing agentic-secret defenses against a problem-grounded specification. We propose the Secret-Use Delegation Protocol (SUDP), a three-role protocol realizing ASU: a requester proposes a canonical operation; the user authorizes it with a fresh authenticator-backed grant; and a custodian redeems the grant once to perform the bounded use, so reusable authority never crosses the requester boundary. We specialize SUDP for agentic deployments: agents propose operations; they do not retrieve secrets. Under explicit assumptions, we show that SUDP satisfies the ASU requirements: authorization is verifiable, operation-bound, and single-use. SUDP also provides storage confidentiality and wrapping-epoch key isolation under stated sealing and erasure assumptions; plaintext-level forward secrecy of the underlying secret additionally requires the environment to rotate and revoke it.

---


### 3. [R-CoT: A Reasoning-Layer Watermark via Redundant Chain-of-Thought in Large Language Models](https://arxiv.org/abs/2604.25247)

**<font color=#1a73e8>作者：</font>** Ziming Zhang, Li Li, Guorui Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely deployed in multiple scenarios due to reasoning capabilities. In order to prevent the models from being misused, watermarking is generally employed to ensure ownership. However, most existing watermarking methods rely on superficial modifications to the model's output distribution, rendering the watermark vulnerable to perturbation and removal. To overcome this challenge, this paper introduces a reasoning-layer framework termed Redundant Chain-of-Thought (R-CoT), which embeds watermarks into the reasoning path. A dual-trajectory optimization mechanism based on GRPO enables the native and the watermark reasoning path to coexist within a shared parameter space, internalizing the watermark as a distinct reasoning policy. Therefore, the watermark is embedded into the model's stable reasoning path, avoiding the watermark failure caused by output-level perturbations. Experimental results show that, compared with existing methods, R-CoT achieves high watermark effectiveness and strong robustness. Under fine-tuning and other post-training operations, the true positive rate (TPR) consistently remains above 95%, exhibiting only marginal degradation.

---


### 4. [MARD: A Multi-Agent Framework for Robust Android Malware Detection](https://arxiv.org/abs/2604.25264)

**<font color=#1a73e8>作者：</font>** Xueying Zeng, Youquan Xian, Sihao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the rapid evolution of Android applications, traditional machine learning-based detection models suffer from concept drift. Additionally, they are constrained by shallow features, lacking deep semantic understanding and interpretability of decisions. Although Large Language Models (LLMs) demonstrate remarkable semantic reasoning capabilities, directly processing massive raw code incurs prohibitive token overhead. Moreover, this approach fails to fully unleash the deep logical reasoning potential of LLMs within complex contexts. To address these limitations, we propose MARD, a multi-agent framework for robust Android malware detection. This framework effectively bridges the gap between the semantic understanding of LLMs and traditional static analysis. It treats underlying deterministic analysis engines as on-demand execution tools, while utilizing the LLM to orchestrate the entire decision-making process. By designing an autonomous multi-agent interaction mechanism based on the ReAct paradigm, MARD constructs a highly interpretable evidentiary chain for conviction. Furthermore, we radically reduce the total cost of conducting a deep analysis of a single complex APK to under $0.10. Evaluations demonstrate that, without any domain-specific fine-tuning, MARD achieves an F1 score of 93.46%. It not only outperforms continual learning baselines but also exhibits robustness against concept drift and strong cross-domain generalization capabilities in evaluations spanning up to five years.

---


### 5. [Medoid Prototype Alignment for Cross-Plant Unknown Attack Detection in Industrial Control Systems](https://arxiv.org/abs/2604.25544)

**<font color=#1a73e8>作者：</font>** Luyao Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deploying an intrusion detector trained in one industrial plant to another remains difficult because Industrial Control System (ICS) traffic is highly site-dependent, labels are scarce, and unseen attacks often appear after deployment. To address this challenge, this paper introduces a medoid prototype alignment framework for cross-plant unknown attack detection. Instead of aligning all source and target samples directly, the method first compresses heterogeneous traffic into a comparable representation space and then extracts robust medoid prototypes that summarize local operational structure in each domain. A prototype-calibrated transfer objective is further designed to align target prototypes with source prototypes while preserving source-domain discrimination and encouraging confident target predictions. This strategy reduces noisy cross-domain matching and improves transfer stability under heterogeneous industrial conditions. Experiments conducted on natural gas and water storage control systems show that the proposed method achieves the best average performance among all compared models, reaching an average accuracy of 0.843 and an average F1-score of 0.838 across four unknown-attack transfer tasks. The analysis also shows clear transfer asymmetry between source-target directions and confirms that prototype guidance is especially helpful on challenging reverse-transfer settings. These findings suggest that medoid prototype alignment is a practical solution for robust industrial intrusion detection under domain shift.

---


### 6. [From CRUD to Autonomous Agents: Formal Validation and Zero-Trust Security for Semantic Gateways in AI-Native Enterprise Systems](https://arxiv.org/abs/2604.25555)

**<font color=#1a73e8>作者：</font>** Ignacio Peyrano  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Enterprise software engineering is shifting away from deterministic CRUD/REST architectures toward AI-native systems where large language models act as cognitive orchestrators. This transition introduces a critical security tension: probabilistic LLMs weaken classical mechanisms for validation, access control, and formal testing.
This paper proposes the design, formal validation, and empirical evaluation of a Semantic Gateway governed by the Model Context Protocol (MCP). The gateway reframes the enterprise API as a semantic surface where tools are dynamically discovered, authorized, and executed based on intent and policy enforcement. The central contribution rests on a paradigm shift: autonomous agents must not be validated as traditional software nor as simple API consumers, but as stochastic state-transition systems whose behavior must be abstracted, fuzzed, and audited through enabled-tool graphs.
The architecture introduces a three-layer Zero-Trust security model comprising a pre-inference Semantic Firewall, deterministic Tool-Level RBAC, and out-of-band Cryptographic Human-in-the-Loop approval. Enabledness-Preserving Abstractions (EPAs) and greybox semantic fuzzing--originally developed for blockchain smart contract verification--are adapted to audit agent behavior in enterprise environments. Results demonstrate an 84.2% reduction in incidental code. Across 500,000 multi-turn fuzzing sequences, the methodology achieved a 100% discovery rate of hidden unauthorized state transitions, proving that dynamic formal verification is strictly necessary for secure agentic deployment.

---


### 7. [SnapGuard: Lightweight Prompt Injection Detection for Screenshot-Based Web Agents](https://arxiv.org/abs/2604.25562)

**<font color=#1a73e8>作者：</font>** Mengyao Du, Han Fang, Haokai Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Web agents have emerged as an effective paradigm for automating interactions with complex web environments, yet remain vulnerable to prompt injection attacks that embed malicious instructions into webpage content to induce unintended actions. This threat is further amplified for screenshot-based web agents, which operate on rendered visual webpages rather than structured textual representations, making predominant text-centric defenses ineffective. Although multimodal detection methods have been explored, they often rely on large vision-language models (VLMs), incurring significant computational overhead. The bottleneck lies in the complexity of modern webpages: VLMs must comprehend the global semantics of an entire page, resulting in substantial inference time and GPU memory usage. This raises a critical question: can we detect prompt injection attacks from screenshots in a lightweight manner? In this paper, we observe that injected webpages exhibit distinct characteristics compared to benign ones from both visual and textual perspectives. Building on this insight, we propose SnapGuard, a lightweight yet accurate method that reformulates prompt injection detection as multimodal representation analysis over webpage screenshots. SnapGuard leverages two complementary signals: a visual stability indicator that identifies abnormally smooth gradient distributions induced by malicious content, and action-oriented textual signals recovered via contrast-polarity reversal. Extensive evaluations across eight attacks and two benign settings demonstrate that SnapGuard achieves an F1 score of 0.75, outperforming GPT-4o-prompt while being 8x faster (1.81s vs. 14.50s) and introducing no additional memory overhead.

---


### 8. [The Surprising Universality of LLM Outputs: A Real-Time Verification Primitive](https://arxiv.org/abs/2604.25634)

**<font color=#1a73e8>作者：</font>** Alex Bogdan, Adrian de Valois-Franklin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We report a striking statistical regularity in frontier LLM outputs that enables a CPU-only scoring primitive running
at 2.6 microseconds per token, with estimated latency up to 100,000$\times$ (five orders of magnitude) below existing
sampling-based detectors. Across six contemporary models from five independent vendors, two generation sizes, and five
held-out domains, token rank-frequency distributions converge to the same two-parameter Mandelbrot ranking
distribution, with 34 of 36 model-by-domain fits exceeding $R^{2} = 0.94$ and 35 of 36 favoring Mandelbrot over Zipf
by AIC. The shared family does not collapse the models into statistical duplicates. Fitted Mandelbrot parameters
remain cleanly separable between models: the cross-model spread in $q$ (1.63 to 3.69) exceeds its per-model bootstrap
standard deviation (0.03 to 0.10) by more than an order of magnitude, yielding tens of standard deviations of
separation per few thousand output tokens. Two capabilities follow. First, statistical model fingerprinting: text from
a vendor-delivered LLM can be tested against its claimed model family without cryptographic watermarks or access to
model internals, supporting provenance verification and silent-substitution audits. Second, a model-agnostic reference
distribution for black-box output assessment, from which we derive a single-pass scoring primitive that composes with
model log probabilities when available and degrades to a rank-only mode usable on closed APIs. Pilot results on
FRANK, TruthfulQA, and HaluEval map where the primitive helps (lexical anomalies, unsupported entities) and where it
structurally cannot (reasoning errors in domain-appropriate vocabulary). We position the primitive as a first-pass
triage layer in compound evaluation stacks, not as a replacement for sampling-based or source-conditioned verifiers.

---


### 9. [Towards Agentic Investigation of Security Alerts](https://arxiv.org/abs/2604.25846)

**<font color=#1a73e8>作者：</font>** Even Eilertsen, Vasileios Mavroeidis, Gudmund Grov  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security analysts are overwhelmed by the volume of alerts and the low context provided by many detection systems. Early-stage investigations typically require manual correlation across multiple log sources, a task that is usually time-consuming. In this paper, we present an experimental, agentic workflow that leverages large language models (LLMs) augmented with predefined queries and constrained tool access (structured SQL over Suricata logs and grep-based text search) to automate the first stages of alert investigation. The proposed workflow integrates queries to provide an overview of the available data, and LLM components that selects which queries to use based on the overview results, extracts raw evidence from the query results, and delivers a final verdict of the alert. Our results demonstrate that the LLM-powered workflow can investigate log sources, plan an investigation, and produce a final verdict that has a significantly higher accuracy than a verdict produced by the same LLM without the proposed workflow. By recognizing the inherent limitations of directly applying LLMs to high-volume and unstructured data, we propose combining existing investigation practices of real-world analysts with a structured approach to leverage LLMs as virtual security analysts, thereby assisting and reducing the manual workload.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
